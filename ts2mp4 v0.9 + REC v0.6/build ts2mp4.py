import os
import sys
import subprocess


# 将临时Python脚本编码为GBK并写入文件
#with open("temp.py", "w", encoding="gbk") as temp_file:
#    temp_file.write(temp_python_script)

# 使用PyInstaller编译临时Python脚本
#subprocess.run(["pyinstaller", "--onefile","--add-data","ffmpeg.exe;.","--icon=ts2mp4.ico","--clean","ts2mp4_v0.6.py"])
subprocess.run(["pyinstaller", "--onefile","--icon=T2M.ico","--clean","ts2mp4_v0.9.py"])