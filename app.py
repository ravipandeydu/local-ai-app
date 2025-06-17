from flask import Flask, request, jsonify, render_template
import os
import json
import datetime
from pathlib import Path

# Import local LLM library
import ctransformers as ct

app = Flask(__name__)

# Configure the model path - user will need to download this model
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "llama-3-8b-instruct.Q4_K_M.gguf")

# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
Path(LOGS_DIR).mkdir(exist_ok=True)

# Initialize the model
def get_llm():
    try:
        # Load the model with ctransformers
        llm = ct.LLM(MODEL_PATH, model_type="llama")
        return llm
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Log the output to a file
def log_output(prompt, output, temperature):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOGS_DIR, f"ai_writer_log_{timestamp}.json")
    
    log_data = {
        "timestamp": timestamp,
        "prompt": prompt,
        "temperature": temperature,
        "output": output
    }
    
    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    temperature = float(data.get('temperature', 0.7))
    
    # Validate input
    if not prompt:
        return jsonify({"error": "Prompt cannot be empty"}), 400
    
    # Load the model
    llm = get_llm()
    if not llm:
        return jsonify({"error": "Failed to load the model. Make sure the model file exists."}), 500
    
    try:
        # Create AI Writer prompt template
        full_prompt = f"""You are an AI Writer assistant. Create content based on the following topic or instructions. Be creative, engaging, and follow the user's instructions carefully.

Topic or instructions: {prompt}

Response:"""
        
        # Generate text with the model
        output = llm(full_prompt, max_new_tokens=512, temperature=temperature)
        
        # Log the output
        log_output(prompt, output, temperature)
        
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Check if model exists
    if not os.path.exists(MODEL_PATH):
        print(f"\nWARNING: Model file not found at {MODEL_PATH}")
        print("Please download the model and place it in the 'models' directory.")
        print("You can download Llama 3 8B Instruct from: https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF")
        # Create models directory if it doesn't exist
        Path(os.path.dirname(MODEL_PATH)).mkdir(exist_ok=True)
    
    app.run(debug=True)