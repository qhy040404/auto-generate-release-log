# auto-generate-release-log

This is a GitHub action to generate Release changelog.

这是一个用于自动创建 Release 更新日志的 GitHub action

## How to use / 如何使用

```yaml
- name: Generate release body
  uses: qhy040404/auto-generate-release-log@v1.1.2
  with:
    changelog: 'Changelog.md'
    template: '.github/RELEASE_TEMPLATE.md'
    tag: ${{ github.ref_name }}
    template-data: 'This is an example'
    fore-delimiter: '\n'
    back-delimiter: '\n'
```