# Project 2: Securing a Local AI Application
 
## 1. Project Overview
 
This project demonstrates prompt-injection vulnerabilities in a local AI application and implements a three-layer security system to reduce the risk of malicious inputs and unsafe outputs.
 
The application uses Flask as the backend and Ollama to run the llama3.2:1b language model locally.
 
## 2. Technologies Used
 
- Kali Linux
- Python 3
- Flask
- Ollama (llama3.2:1b)
- Burp Suite
- Requests library
- Git and GitHub
 
## 3. Project Structure
 
- app_baseline.py - Baseline AI application
- app.py - Defended AI application
- validate.py - Input validation
- output_scanner.py - Output security scanning
- test_legitimate.py - Legitimate prompt testing
- requirements.txt - Python dependencies
- attack_comparison.csv - Before-and-after results
- legitimate_results.json - Legitimate test results
- attack1_baseline.txt to attack5_defended.txt - Attack evidence
 
## 4. Three-Layer Security Architecture
 
### Layer 1: Input Validation
 
Validates incoming prompts before forwarding them to the AI model.
 
Includes:
- Prompt-injection pattern detection
- Input type validation
- Empty input rejection
- Maximum input length of 500 characters
 
### Layer 2: System Prompt Protection
 
A security-focused system prompt instructs the model to follow its intended role and resist malicious instructions.
 
### Layer 3: Output Scanning
 
Checks generated responses for potentially unsafe content.
 
Includes:
- Credential pattern detection
- System prompt leakage detection
- Unsolicited external URL detection
 
## 5. Installation
 
Install Python dependencies:
 
```bash
pip install -r requirements.txt
```
 
Install Ollama separately and download the model:
 
```bash
ollama pull llama3.2:1b
```
 
Ensure the Ollama service is running.
 
Start the defended application:
 
```bash
python app.py
```
 
The application runs locally at:
 
http://127.0.0.1:5000
 
## 6. API Endpoint
 
POST /ask
 
Example request:
 
```json
{
  "prompt": "What is cybersecurity?"
}
```
 
Example successful response structure:
 
```json
{
  "blocked": false,
  "response": "Cybersecurity is..."
}
```
 
Blocked requests return an error response.
 
## 7. Security Testing
 
Five adversarial attack cases were tested against both baseline and defended versions.
 
The defended application blocked all five tested attacks with HTTP 400 responses.
 
Baseline observations:
- Attack 1: Apparent system prompt disclosure
- Attack 2: Model refused the request
- Attack 3: Generated a network-information command
- Attack 4: Model refused the request
- Attack 5: Processed an encoded payload
 
Detailed results are available in attack_comparison.csv.
 
## 8. Legitimate Input Testing
 
Ten legitimate prompts were tested.
 
Results:
- Accepted: 10
- Blocked: 0
- Observed false-positive rate: 0%
 
These results apply only to the tested prompts.
 
## 9. Additional Validation Tests
 
The defended application was tested for:
- Malformed JSON
- Missing prompt
- Numeric prompt
- Empty prompt
- HTML/script payload
- Input exceeding 500 characters
 
Burp Suite was used for HTTP request inspection and testing.
 
## 10. Conclusion
 
The project demonstrates how input validation, system prompt protection, and output scanning can be combined to strengthen a local AI application.
 
All five tested adversarial prompts were blocked by the defended application, while the ten legitimate test prompts were accepted.
 
These results demonstrate improved protection for the tested cases, not immunity against every possible prompt-injection technique.
