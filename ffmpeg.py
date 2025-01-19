import subprocess

class FFmpeg:
    def __init__(self):
        pass

    def extract_subtitles_from_mkv(self, mkv_file_path: str, output_file_path: str, subtitle_stream_index: str):
        """
        Extracts subtitles from an MKV file using ffmpeg.

        :param mkv_file_path: Path to the MKV file.
        :param output_file_path: Path to save the extracted subtitle file.
        :param subtitle_stream_index: Subtitle stream index to extract (e.g., 's:0' for the first subtitle stream).
        """
        try:
            command = [
                "ffmpeg",
                "-i", mkv_file_path,
                "-map", f"0:{subtitle_stream_index}",
                output_file_path
            ]
            subprocess.run(command, check=True)
            print(f"Subtitle extracted to {output_file_path}")
        except FileNotFoundError:
            print("ffmpeg not found. Ensure ffmpeg is installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            
    def add_subtitle_to_mkv(self, input_mkv_file_path: str, subtitle_file_path: str, output_mkv_file_path: str):
        """
        Adds subtitles to an MKV file using FFmpeg.

        :param input_mkv_file_path: Path to the input MKV file.
        :param subtitle_file_path: Path to the subtitle file (e.g., SRT).
        :param output_mkv_file_path: Path to the output MKV file.
        """
        try:
            command = [
                "ffmpeg",
                "-i", input_mkv_file_path,
                "-i", subtitle_file_path,
                "-map", "0",
                "-map", "1",
                "-c", "copy",
                "-disposition:s:0", "default",
                output_mkv_file_path
            ]
            
            subprocess.run(command, check=True)
            print(f"Subtitle added successfully to {output_mkv_file_path}")
        except FileNotFoundError:
            print("FFmpeg not found. Make sure it's installed and in your system's PATH.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    pass
