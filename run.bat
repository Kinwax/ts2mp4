@echo off
cls

setlocal enabledelayedexpansion

REM 逐个处理传递给脚本的文件参数
:process_files
if "%~1" == "" goto end_process

REM 提取文件名和扩展名
set "fullpath=%~1"
for %%a in ("!fullpath!") do (
    set "filename=%%~na"
    set "extension=%%~xa"
    set "filedir=%%~dpa"
)

REM 使用 ffmpeg 处理文件
.\ffmpeg -i "!fullpath!" -f mp4 -codec copy "!filedir!!filename!.mp4"

shift
goto process_files

:end_process
pause
