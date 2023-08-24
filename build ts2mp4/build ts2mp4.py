import os
import sys
import subprocess




# 创建一个临时的Python脚本，将批处理脚本内容写入
temp_python_script = """
# -*- coding: gbk -*-
import os
import subprocess
import sys
import msvcrt

def process_files(file_paths):
    ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")  # 获取当前可执行文件所在目录的路径
    if not os.path.exists(ffmpeg_path):
        print("ffmpeg.exe not found.")
        return

    for fullpath in file_paths:
        filename, extension = os.path.splitext(os.path.basename(fullpath))
        filedir = os.path.dirname(fullpath)

        output_file = os.path.join(filedir, f"{filename}.mp4")

        # 使用 subprocess 调用 ffmpeg
        ffmpeg_command = f'"{ffmpeg_path}" -i "{fullpath}" -f mp4 -codec copy "{output_file}"'
        subprocess.run(ffmpeg_command, shell=True)

if __name__ == "__main__":
    file_paths = sys.argv[1:]

    if not file_paths:
        print("No input files provided.")
    else:
        process_files(file_paths)

    print("Press any key to continue...")
    msvcrt.getch()

"""

# 将临时Python脚本编码为GBK并写入文件
with open("ts2mp4.py", "w", encoding="gbk") as temp_file:
    temp_file.write(temp_python_script)

# 使用PyInstaller编译临时Python脚本
subprocess.run(["pyinstaller", "--onefile","--add-data","ffmpeg.exe;.","--icon=ts2mp4.ico","--clean","ts2mp4.py"])



# 清理临时文件
os.remove("ts2mp4.py")
