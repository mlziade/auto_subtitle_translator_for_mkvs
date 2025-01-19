import os
import requests
from dotenv import load_dotenv

# Ollama 
# You can add more models here if needed
models = {
    "llama3.3",
    "phi4",
    "llama3.2",
    "llama3.1",
    "llama3.2:1b",
    "mistral:latest",
}

# Supported languages, with their respective codes
# You can add more languages here if needed
languages = {
    "en": "ENGLISH",
    "pt-br": "BRAZILLIAN PORTUGUESE",
    "es": "SPANISH",
    "fr": "FRENCH",
}

class Ollama:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('OLLAMA_URL')
        if not self.base_url:
            raise ValueError("OLLAMA_URL is not defined")

    def generate(self, prompt: str, model: str) -> str:
        """
        Generates text using the given prompt and model.

        Args:
            prompt (str): The input prompt for text generation.
            model (str): The model to use for text generation.

        Returns:
            str: The generated text.
        """
        
        if model not in models:
            raise ValueError("Invalid model name")
        
        final_url = f"{self.base_url}/api/generate"
        body = {
            "model": model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(final_url, json=body)
            response.raise_for_status()
            return response.json().get("response")
        except requests.exceptions.RequestException as error:
            print(f"🚀 ~ Ollama ~ generate ~ error: {error}")
            raise RuntimeError("Error in OllamaService") from error

    def translates_subtitles(self, input_file_path: str, output_file_path: str, model: str, input_language: str, output_language: str):
        """
        Translates subtitles using Ollama.

        Args:
            input_file_path (str): Path to the input subtitle file.
            output_file_path (str): Path to save the translated subtitle file.
            model (str): The model to use for translation.
        """
        
        try:
            with open('prompt.txt', "r") as file:
                prompt = file.read()
        except FileNotFoundError:
            print("Prompt file not found.")
            return
        
        try:
            with open(input_file_path, "r") as file:
                input_text = file.read()
                # Replace placeholders in the prompt
                final_prompt = prompt.replace("[[[INPUT TEXT]]]", input_text)
                final_prompt = final_prompt.replace("[[[INPUT LANGUAGE]]]", input_language)
                final_prompt = final_prompt.replace("[[[OUTPUT LANGUAGE]]]", output_language)
                # Generate translated text                    
                translated_text: str = self.generate(final_prompt, model)
                with open(output_file_path, "w") as output_file:
                    output_file.write(translated_text)
        except FileNotFoundError:
            print("Input file not found.")
        except Exception as e:
            print(f"Error occurred: {e}")
            
if __name__ == "__main__":
    pass    