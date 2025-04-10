import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import markdown
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def format_response_markdown(text):
    html = markdown.markdown(text)
    return html

def get_suggestions(prompt):
    prompt_lower = prompt.lower()
    if "python" in prompt_lower:
        return [
            "What is Python used for?",
            "What are Python's key advantages?",
            "How is Python different from Java?"
        ]
    elif "infosys" in prompt_lower:
        return [
            "What are Infosys' core values?",
            "How can I prepare for Infosys interviews?",
            "What is Infosys known for?"
        ]
    else:
        return [
            "Explain AI in simple terms",
            "Give me a fun fact about technology",
            "What is the difference between AI and ML?"
        ]

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Prompt is missing"}), 400

        try:
            response = model.generate_content(prompt)
            markdown_text = response.text.strip()
            html_response = format_response_markdown(markdown_text)
            return jsonify({
                "response": html_response,
                "suggestions": get_suggestions(prompt)
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")
