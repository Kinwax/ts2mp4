
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

    for path in file_paths:
        if os.path.isfile(path):
            filename, extension = os.path.splitext(os.path.basename(path))
            filedir = os.path.dirname(path)
            output_file = os.path.join(filedir, f"{filename}.mp4")
            ffmpeg_command = f'"{ffmpeg_path}" -i "{path}" -f mp4 -codec copy "{output_file}"'
            subprocess.run(ffmpeg_command, shell=True)
        elif os.path.isdir(path):
            ts_files = [file for file in os.listdir(path) if file.lower().endswith('.ts')]
            ts_files = [os.path.join(path, file) for file in ts_files]
            process_files(ts_files)

if __name__ == "__main__":
    file_paths = sys.argv[1:]

    if not file_paths:
        print("No input files provided.")
    else:
        process_files(file_paths)

    print("Press any key to continue...")
    msvcrt.getch()


