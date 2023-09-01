# -*- coding: gbk -*-
import os
import sys
import msvcrt
import subprocess
import ffmpeg

def process_files(file_paths):
    rec_files = []

    for path in file_paths:
        if os.path.isfile(path):
            filename, extension = os.path.splitext(os.path.basename(path))
            if extension.lower() == '.ts':
                output_file = os.path.join(os.path.dirname(path), f"{filename}.mp4")
                (
                    ffmpeg.input(path)
                    .output(output_file, codec='copy')
                    .run(overwrite_output=True)
                )
                rec_files.append(output_file)
            elif extension.lower() == '.mp4':
                rec_files.append(path)
        elif os.path.isdir(path):
            ts_files = [file for file in os.listdir(path) if file.lower().endswith('.ts')]
            ts_files = [os.path.join(path, file) for file in ts_files]
            rec_files.extend(process_files(ts_files))

    return rec_files

if __name__ == "__main__":
    file_paths = sys.argv[1:]

    if not file_paths:
        print("No input files provided.")
    else:
        rec_path = os.path.join(os.path.dirname(sys.executable), "REC.exe")
        print("Input files:", file_paths)  # Add this line to check input files
        transcoded_files = process_files(file_paths)
        
        rec_option = input("Do you want to perform transcoding and run REC.exe? (y/n): ")
        if rec_option.lower() == "y":
            if not os.path.exists(rec_path):
                print("REC.exe not found.")
                print("Press any key to exit...")
                msvcrt.getch()
                sys.exit(1)
            else:
                subprocess.run([rec_path] + transcoded_files)  # Pass all transcoded files as arguments
        else:
            sys.exit(1)

    print("Press any key to exit...")
    msvcrt.getch()
