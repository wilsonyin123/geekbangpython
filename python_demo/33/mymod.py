def print_me():
    print('me')


# print_me()

https://www.python.org/dev/peps/pep-0008/



pycharm 安装PEP8
cmd窗口输入：pip install autopep8
Tools→Extends Tools→点击加号

Name：Autopep8（可以随便取）
- Tools settings:
    - Programs：`autopep8` （前提是你已经安装了哦）
    - Parameters:`--in-place --aggressive --aggressive $FilePath$`
    - Working directory:`$ProjectFileDir$`
- 点击Output Filters→添加，在对话框中的：Regular expression to match output中输入：`$FILE_PATH$\:$LINE$\:$COLUMN$\:.*`

