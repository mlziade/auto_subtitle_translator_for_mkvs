# Auto Subtitle Translator for MKVs

## Objective
The objective of this project is to automatically translate subtitles for videos using locally running Large Language Models (LLMs).

## Workflow
1. **Extract Subtitles**: Use FFmpeg to extract the current subtitles from the .mkv file.
2. **Translate Subtitles**: Pass the extracted text through a prompt on a local LLM running on Ollama as a server.
3. **Import Translated Subtitles**: Import the translated subtitles back into the original .mkv file.

## Technologies Used
- [Ollama](https://github.com/ollama/ollama)
- [FFmpeg](https://www.ffmpeg.org/)

## Installation

### Python
1. Install [Python](https://www.python.org/downloads/)
2. Install [python-dotenv](https://pypi.org/project/python-dotenv/)

### FFmpeg
1. Install [FFmpeg](https://www.ffmpeg.org/download.html)

### Ollama
1. Install [Ollama](https://ollama.com/download)
2. Download and install a [model](https://ollama.com/search) you want to use:
    ```sh
    ollama run llama3.3
    ```
3. Run Ollama as a server on port 11434:
    ```sh
    ollama serve
    ```

### Project Setup
1. Update the `.env` file with the necessary configurations.
2. Run the project:
    ```sh
    python main.py
    ```
