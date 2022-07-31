import os

changelog_path = os.getenv("CHANGELOG")
template_path = os.getenv("TEMPLATE")
tag_name = os.getenv("TAG")
template_data = os.getenv("TEMPLATE_DATA")
fore_delim = os.getenv("FORE")
back_delim = os.getenv("BACK")

# Init define
with open(changelog_path, "r") as changelog:
    cl = changelog.read()

try:
    un_proc_log = cl.split(tag_name)[1].split(back_delim)[0]
    proc_log = un_proc_log.lstrip(fore_delim)
except IndexError:
    exit(1)

with open(template_path, "r") as template:
    final_data = template.read()

final_data = final_data.replace(template_data, proc_log)

with open(template_path, "w") as release:
    release.write(final_data)
