import google.generativeai as genai
import os
import markdown

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Choose your best available model (from your list)
model = genai.GenerativeModel('models/gemini-1.5-pro')

def get_genai_response(prompt):
    try:
        response = model.generate_content(prompt)
        text = response.text

        # Convert Markdown to HTML
        formatted = markdown.markdown(text)
        return formatted
    except Exception as e:
        return f"<p style='color:red;'>Error: {e}</p>"
