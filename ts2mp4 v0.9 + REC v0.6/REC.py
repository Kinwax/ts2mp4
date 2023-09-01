import os
import sys
import ffmpeg
import msvcrt

def get_video_info(file_path):
    try:
        probe = ffmpeg.probe(file_path, v="error")
        video_stream = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
        width = int(video_stream['width'])
        height = int(video_stream['height'])
        resolution = f"{width}x{height}"
        display_aspect_ratio = video_stream.get('display_aspect_ratio', 'N/A')
        bitrate = float(video_stream['bit_rate']) / 1000000  # Convert to Mbps
        return width, height, resolution, display_aspect_ratio, bitrate
    except Exception as e:
        print("Error:", e)
        return None, None, None, None, None

def reencode_video(input_path, output_path, width, height, bitrate):
    try:
        ffmpeg.input(input_path).output(output_path, vcodec='h264_nvenc', s=f"{width}x{height}", b=f"{bitrate:.2f}M").run(overwrite_output=True)
    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) < 2:
        print("Usage: drag and drop media files onto this executable.")
        return
    
    videos_info = []
    for input_file in sys.argv[1:]:
        input_dir, input_name = os.path.split(input_file)
        width, height, resolution, display_aspect_ratio, bitrate = get_video_info(input_file)
        
        input_name_without_extension = os.path.splitext(input_name)[0]
        videos_info.append({
            "file_name": input_name_without_extension,
            "width": width,
            "height": height,
            "resolution": resolution,
            "display_aspect_ratio": display_aspect_ratio,
            "bitrate": bitrate
        })
    
    video_groups = {}
    for video_info in videos_info:
        aspect_ratio = video_info['width'] / video_info['height']
        if aspect_ratio not in video_groups:
            video_groups[aspect_ratio] = []
        video_groups[aspect_ratio].append(video_info)
    
    print("Detected videos:")
    for aspect_ratio, group_videos in video_groups.items():
        print(f"Aspect Ratio: {aspect_ratio:.2f}")
        for video_info in group_videos:
            print(f"File: {video_info['file_name']}")
            print(f"Resolution: {video_info['resolution']}")
            print(f"Display Aspect Ratio: {video_info['display_aspect_ratio']}")
            print(f"Bitrate: {video_info['bitrate']:.2f} Mbps")
        print()
    
    bitrate_input_dict = {}
    resolution_input_dict = {}
    for aspect_ratio in video_groups:
        bitrate_input = input(f"Enter a new bitrate in Mbps for group with aspect ratio {aspect_ratio:.2f}: ")
        bitrate_input_dict[aspect_ratio] = float(bitrate_input)
        resolution_height_input = input(f"Enter a new resolution height for group with aspect ratio {aspect_ratio:.2f} (leave empty to use source resolution): ")
        if resolution_height_input:
            resolution_input_dict[aspect_ratio] = int(resolution_height_input)
    
    for aspect_ratio, group_videos in video_groups.items():
        new_bitrate = bitrate_input_dict[aspect_ratio]
        new_resolution_height = resolution_input_dict.get(aspect_ratio)
        
        for video_info in group_videos:
            input_file = os.path.join(input_dir, f"{video_info['file_name']}.mp4")
            if new_resolution_height:
                new_resolution_width = int(new_resolution_height * video_info['width'] / video_info['height'])
            else:
                new_resolution_width = video_info['width']
                new_resolution_height = video_info['height']
            output_file = os.path.join(input_dir, f"{video_info['file_name']}_{new_resolution_width}x{new_resolution_height}_{new_bitrate:.2f}Mbps.mp4")
            reencode_video(input_file, output_file, new_resolution_width, new_resolution_height, new_bitrate)
            print(f"Reencoded video {video_info['file_name']} saved as {output_file}\n")
    
    print("All videos processed.")
    print("Press any key to exit...")
    msvcrt.getch()
    sys.exit(1)

if __name__ == "__main__":
    main()
