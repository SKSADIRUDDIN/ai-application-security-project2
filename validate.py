import re
 
MAX_LENGTH = 500
 
INJECTION_PATTERNS = [
    r"ignore\s+(?:all\s+)?previous\s+instructions",
    r"you\s+are\s+now",
    r"pretend\s+you\s+are",
    r"act\s+as\s+if\s+you\s+have\s+no",
    r"reveal\s+your\s+system\s+prompt",
    r"do\s+not\s+summarize",
    r"decode\s+this\s+base64",
    r"follow\s+its\s+instructions",
    r"\b[A-Za-z0-9+/]{40,}={0,2}\b"
]
 
def validate_input(prompt):
    if not isinstance(prompt, str):
        return False, "Input must be a string"
 
    if len(prompt) > MAX_LENGTH:
        return False, "Input exceeds 500 characters"
 
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False, "Prompt injection detected"
 
    return True, "Input accepted"
