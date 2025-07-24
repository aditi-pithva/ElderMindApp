from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

MODEL_DIR = "./models"
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if not data or 'answers' not in data:
        return jsonify({"error": "JSON must include an 'answers' field."}), 400

    answers = data['answers']

    for k, v in answers.items():
        if not isinstance(v, (int, float)):
            return jsonify({"error": f"Invalid value for '{k}': must be numeric"}), 400

    prompt = "Patient data: " + ", ".join(f"{k}={v}" for k, v in answers.items())
    prompt += "\nPredict if the patient shows early signs of Alzheimer's disease."

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs['input_ids'],
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({
        "response": response_text,
        "input_prompt": prompt
    })

if __name__ == '__main__':
    app.run(debug=True)