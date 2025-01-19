import os
import ollama
import ffmpeg
from dotenv import load_dotenv

def translate_episodes(input_files_folder_path: str, originals_subs_folder_path: str, translated_subs_folder_path: str):
    """
    Translates subtitles from MKV files and adds the translated subtitles back to the MKV files.
    
    :param input_files_folder_path: Path to the folder containing the input MKV files.
    :param originals_subs_folder_path: Path to the folder where the original subtitles will be saved.
    :param translated_subs_folder_path: Path to the folder where the translated subtitles will be saved.
    :param final_files_folder_path: Path to the folder where the final MKV files with translated subtitles will be saved.
    """
    ollama_service = ollama.Ollama()
    ffmpeg_service = ffmpeg.FFmpeg()

    for file_name in os.listdir(input_files_folder_path):
        # Check if the file is an MKV file
        if file_name.endswith(".mkv"):
            mkv_file_path = os.path.join(input_files_folder_path, file_name)
            original_subs_path = os.path.join(originals_subs_folder_path, f"{file_name}.srt")
            
            # Extract subtitles from the MKV file
            ffmpeg_service.extract_subtitles_from_mkv(
                mkv_file_path = mkv_file_path,
                output_file_path = original_subs_path,
                subtitle_stream_index = "s:0"
            )
            
            # Translate the subtitles
            translated_subs_path = os.path.join(translated_subs_folder_path, f"{file_name}.srt")
            ollama_service.translates_subtitles(
                input_file_path = original_subs_path, 
                output_file_path = translated_subs_path, 
                model = "mistral:latest", 
                input_language = "es", 
                output_language = "pt-br"
            )
            
            output_file_path = os.path.join(translated_subs_folder_path, f"{file_name}.srt")
            # Add the translated subtitles to the MKV file
            ffmpeg_service.add_subtitle_to_mkv(
                input_mkv_file_path = mkv_file_path,
                subtitle_file_path = translated_subs_path,
            )
            

def main():
    # Specify the path to your .env file
    dotenv_path = '.env'
    load_dotenv(dotenv_path = dotenv_path)

    # Get the paths from the environment variables
    input_files_folder_path =  os.getenv("FILES_FOLDER_COMPLETE_PATH")
    originals_subs_folder_path = os.getenv("ORIGINAL_SUBS_FOLDER_COMPLETE_PATH")
    translated_subs_folder_path = os.getenv("TRANSLATED_SUBS_FOLDER_COMPLETE_PATH")
    
    # Translate the episodes
    translate_episodes(
        input_files_folder_path, 
        originals_subs_folder_path, 
        translated_subs_folder_path,
    )
    
if __name__ == "__main__":
    main()