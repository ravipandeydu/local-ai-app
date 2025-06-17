# Local AI Writer App

A web application that generates creative content using a local Large Language Model (LLM) running entirely on your machine without relying on external APIs.

## App Type

**AI Writer** - Generate creative content like blog intros, tweets, or stories based on user prompts.

## Features

- Prompt input box for describing what content you want to generate
- Temperature slider to control creativity level
- Loading UI during content generation
- Output display for generated content
- Local logging of all generated content

## Requirements

- Python 3.8 or higher
- At least 8GB of RAM (16GB recommended)
- Approximately 5GB of free disk space for the model

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd local-ai-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

#### Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the LLM model

Create a `models` directory in the project root:

```bash
mkdir models
```

Download the Llama 3 8B Instruct model from Hugging Face:

1. Visit [TheBloke/Llama-3-8B-Instruct-GGUF](https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF)
2. Download the `llama-3-8b-instruct.Q4_K_M.gguf` file (approximately 4.7GB)
3. Place the downloaded file in the `models` directory

Alternatively, you can use other GGUF models like Mistral or Phi-2, but you'll need to update the model path and type in `app.py`.

### 5. Run the application

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Use

1. Enter a topic or specific instructions in the prompt box (e.g., "Write a blog intro about sustainable living")
2. Adjust the creativity level using the temperature slider:
   - Lower values (0.1-0.3): More focused, deterministic outputs
   - Medium values (0.4-0.7): Balanced creativity
   - Higher values (0.8-1.0): More creative, diverse outputs
3. Click "Generate Content" and wait for the local model to process your request
4. View the generated content in the output section

## Model Information

This app uses **Llama 3 8B Instruct** (Q4_K_M quantized version) by default. This is a smaller, more efficient version of Meta's Llama 3 model that can run on consumer hardware while still providing good quality outputs.

## Logs

All generated content is logged in the `logs` directory with timestamps for future reference.

## Customization

You can modify the prompt template in `app.py` to customize how the AI responds to different types of content requests.

## Troubleshooting

- **Model loading errors**: Ensure you've downloaded the correct model file and placed it in the `models` directory
- **Memory issues**: Try using a smaller quantized model if you're experiencing out-of-memory errors
- **Slow generation**: Generation speed depends on your hardware. CPU inference will be significantly slower than GPU inference