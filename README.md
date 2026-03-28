
# 如何使用
先返回根目录
执行```bash
python.exe main.py
```

# 如何打包
考虑到pyinstaller打包较大，所以使用虚拟环境！（不用虚拟环境忽略1、2、7步）<br>
1.在cmd中执行`python.exe -m venv .venv`准备虚拟环境 <br>
2.执行
`.venv\Scripts\activete.bat` <br>
3.执行`pip install pyinstaller` <br>
4.到项目更目录 <br>
5.执行`pyinstaller --noconfirm --onefile --windowed  "main.py"` <br>
6.等待打包完成 <br>
7.执行`.venv\Scripts\deactivete.bat` <br>

# 注意事项！！！
**请准备python环境！！！！！！** <br>
**如果你不知道要不要用虚拟环境，请使用！** <br>
