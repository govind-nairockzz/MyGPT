# list_models.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env or set it directly
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models accessible with your API key
def list_models():
    models = genai.list_models()
    for model in models:
        print(f"{model.name} -> {model.supported_generation_methods}")

list_models()
