Now we have token estimation.

File: dabtest/main.py
 Identified issue 1: Hardcoded sensitive data
    Snippet: "PASSWORD = "secret password""
    Line number: 26
    CWE: CWE-287
    Severity: High
    Why: The hardcoded password is a significant security risk as it can be easily extracted from the source code, leading to unauthorized access.
    Mitigation: Use environment variables or secret management systems like HashiCorp Vault for storing sensitive data. Avoid embedding secrets directly in the 
application code.
    Confidence: 1.0

 Identified issue 2: Potential exposure of sensitive information
    Snippet: "do_nasty_things(PASSWORD)"
    Line number: 27
    CWE: CWE-305
    Severity: High
    Why: Passing the hardcoded password directly to a function can lead to accidental logging or display in an insecure manner, exposing it further.
    Mitigation: Ensure that sensitive data is not logged and use secure methods for handling authentication credentials. Avoid passing secrets as arguments unless 
absolutely necessary.
    Confidence: 1.0

Results saved to results/index_20251204_213244.json
> token_usage
Prompt: 1,456, Completion: 281, Embedding: 184, Total: 1,921
Results saved to results/index_20251204_213244.json
>