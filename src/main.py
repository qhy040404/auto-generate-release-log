import os

changelog_path = os.getenv("CHANGELOG")
template_path = os.getenv("TEMPLATE")
tag_name = os.getenv("TAG")
template_data = os.getenv("TEMPLATE_DATA")
fore_delim = os.getenv("FORE")
back_delim = os.getenv("BACK")

with open(changelog_path, "r", encoding='utf-8') as changelog:
    cl = changelog.read()

try:
    proc_log = cl.split(tag_name + fore_delim)[1].split(back_delim)[0]
    print("Data = " + proc_log)
except IndexError:
    exit(1)

with open(template_path, "r", encoding='utf-8') as template:
    final_data = template.read()

final_data = final_data.replace(template_data, proc_log)

with open(template_path, "w", encoding='utf-8') as release:
    release.write(final_data)

print("Release body overwritten")
