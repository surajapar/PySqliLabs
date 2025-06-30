import os
from urllib.parse import urlparse
from modules.logo import print_logo
from modules.error_based import error_based_sql_injection
from modules.union_based import union_based_sql_injection
from modules.authentication_bypass import authentication_bypass
from modules.boolean_based import boolean_based_sql_injection
from modules.time_based import time_based_sql_injection
from modules.multiple_urls import multiple_urls_sql_injection
from modules.crawl import crawl,testable_urls

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False

print_logo()

while True:
    print("\nMenu:")
    print("1. Check Error-Based SQL Injection")
    print("2. Check Union-Based SQL Injection")
    print("3. Authentication Bypass")
    print("4. Check Boolean-Based SQL Injection")
    print("5. Check Time-Based SQL Injection")
    print("6. Check Multiple URLs from File")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice not in [str(i) for i in range(1, 8)]:
        print("Invalid choice. Please try again.\n")
        continue

    if choice == "7":
        print("Exiting the program.")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        url = input("Enter the URL to test for SQL injection: ").strip()
        if not is_valid_url(url):
            print("Invalid URL. Please enter a valid URL starting with http:// or https://")
            continue

        print(f"You have selected option {choice}.")
        print(f"Testing {url} for SQL injection vulnerabilities...\n")

        if choice == "1":
            testable_urls.clear()
            crawl(url)
            for u in testable_urls:
                error_based_sql_injection(u)
            
        elif choice == "2":
             testable_urls.clear()
             crawl(url)
             for u in testable_urls:
                union_based_sql_injection(u)
        elif choice == "3":
            testable_urls.clear()
            crawl(url)
            for u in testable_urls:
                authentication_bypass(u)
        elif choice == "4":
            testable_urls.clear()
            crawl(url)
            for u in testable_urls:
                boolean_based_sql_injection(u)
        elif choice == "5":
            testable_urls.clear()
            crawl(url)
            for u in testable_urls:
                time_based_sql_injection(u1)

    elif choice == "6":
        file_path = input("Enter file path for multiple URLs (txt file): ").strip()
        if not os.path.isfile(file_path):
            print("File does not exist. Please check the path.")
            continue
        multiple_urls_sql_injection(file_path)
