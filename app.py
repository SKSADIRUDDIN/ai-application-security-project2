from flask import Flask, request, jsonify
import requests
 
from validate import validate_input
from output_scanner import scan_output, SYSTEM_PROMPT
 
app = Flask(__name__)
 
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:1b"
 
 
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True)
 
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON request"}), 400
 
    prompt = data.get("prompt", "")
 
    allowed, reason = validate_input(prompt)
 
    if not allowed:
        return jsonify({"error": reason, "blocked": True}), 400
 
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "system": SYSTEM_PROMPT,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )
 
        response.raise_for_status()
 
        answer = response.json().get("response", "")
 
        safe, reason = scan_output(answer)
 
        if not safe:
            return jsonify({
                "error": reason,
                "blocked": True
            }), 400
 
        return jsonify({
            "response": answer,
            "blocked": False
        }), 200
 
    except requests.RequestException:
        return jsonify({
            "error": "Ollama service unavailable"
        }), 503
 
    except (ValueError, TypeError):
        return jsonify({
            "error": "Invalid Ollama response"
        }), 502
 
 
if __name__ == "__main__":
    print("DEFENDED MODE: Three-layer security enabled")
    app.run(host="127.0.0.1", port=5000, debug=False)

