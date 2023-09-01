# ts2mp4
turn ts files to mp4 by drag

ts2mp4 v0.9 + REC v0.6
· 修复一些ts2mp4调用ffmpeg和REC的问题
· 迭代REC，支持按不同的画幅比例对视频分组，可分别设置不同的码率（方便同时拖入16:9和4:3视频并设置不同码率）
· 迭代REC，支持输入新的像素高度，将按比例计算像素宽度，设置为新的转码分辨率（方便统一像素尺寸）


ts2mp4 v0.8 + REC v0.3
· 因ts2mp4.exe与REC.exe搭配使用，摘除ts2mp4内嵌的ffmpeg，与REC一起引用外挂的ffmpeg.exe
· ts2mp4转文件格式后，可自动调用REC进行转码
· 迭代REC，现在可以先列出拖入视频的码率，以此为参考再去设置转码码率
· REC需要外挂ffprobe.exe


ts2mp4 v0.7 + REC v0.1
· 加入了转码小工具REC.exe(ReCoder)，批量拖入视频，并且设置新的码率进行转码
· REC需要外挂ffmpeg.exe
· 修复了ts2mp4的一些问题

ts2mp4 v0.6
· 加入了可以同时拖入文件/文件夹的功能

ts2mp4 v0.5
· 整体用python重构
· 修复了在run.bat批处理文件形式上，遇到ts文件名带感叹号时，显示找不到文件的问题
· 将ffmpeg.exe进行内嵌
· 加入了程序图标

ts2mp4 v0.2
· 批量选择ts文件，拖动到run.bat上释放，即可批量转换为mp4格式封装的媒体文件

ts2mp4 v0.1 
· 批量选择同目录下的ts文件，拖动到run.bat上释放，即可批量转换为mp4格式封装的媒体文件
