
# 如何使用
先返回根目录
执行`python.exe main.py`

# 如何打包
考虑到pyinstaller打包较大，所以使用虚拟环境！（不用虚拟环境忽略1、2、7步）
1.在cmd中执行`python.exe -m venv .venv`准备虚拟环境
2.执行`.venv\Scripts\activete.bat`
3.执行`pip install pyinstaller`
4.到项目更目录
5.执行`pyinstaller --noconfirm --onefile --windowed  "main.py"`
6.等待打包完成
7.执行`.venv\Scripts\deactivete.bat`

#注意事项！！！
**请准备python环境！！！！！！**
