# Win: python -m venv xxx | Mac: python3.9 -m venv xxx 命令行创建xxx虚拟环境。
# 进入(xxx)环境：pip install pyinstaller 安装第三方工具pyinstaller
# 在(xxx)环境中：Win: pyinstaller.exe sha256.py -F | Mac: pyinstaller sha256.py 命令行打包python文件
# -F表示：打包成单个exe文件，不要-F打包成一个文件夹包。
# 网站：github.com | github.com/docker/compose | github1s.com/docker/compose 相当于Web版VSCode方便查看
# manim教程：github.com/cai-hust/manim-tutorial-CN

import sys
import hashlib

file_name = sys.argv[1]
with open(file_name, 'rb') as f:
    bytes = f.read()  # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest().upper()
    print(readable_hash)
