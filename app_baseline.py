from flask import Flask, request, jsonify
import requests
 
app = Flask(__name__)
 
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:1b"
 
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
 
    # No input validation - intentionally vulnerable baseline
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )
 
    answer = response.json().get("response", "")
 
    return jsonify({"response": answer}), 200
 
 
if __name__ == "__main__":
    print("BASELINE MODE: No validation middleware active")
    app.run(host="127.0.0.1", port=5000, debug=False)

