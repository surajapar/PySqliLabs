import re
from urllib.parse import urlparse
import argparse

from modules.error_based import error_based_sql_injection
from modules.union_based import union_based_sql_injection
from modules.authentication_bypass import authentication_bypass
from modules.boolean_based import boolean_based_sql_injection
from modules.time_based import time_based_sql_injection

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc

def multiple_urls_sql_injection(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
        
        if not urls:
            print("No URLs found in the file.")
            return

        print(f"Found {len(urls)} URLs in the file.")
        vulnerable_urls = []

        for index, url in enumerate(urls, start=1):
            print(f"[{index}/{len(urls)}] Testing URL: {url}")

            if not is_valid_url(url):
                print(f"Skipping invalid URL: {url}")
                continue

            try:
                if error_based_sql_injection(url):
                    vulnerable_urls.append((url, 'error_based'))

                if union_based_sql_injection(url):
                    vulnerable_urls.append((url, 'union_based'))

                if authentication_bypass(url):
                    vulnerable_urls.append((url, 'authentication_bypass'))

                if boolean_based_sql_injection(url):
                    vulnerable_urls.append((url, 'boolean_based'))

                if time_based_sql_injection(url):
                    vulnerable_urls.append((url, 'time_based'))

            except Exception as e:
                print(f"Error testing {url}: {e}")

        if vulnerable_urls:
            print("\n=== Vulnerable URLs Detected ===")
            for url, method in vulnerable_urls:
                print(f"{url} - {method}")
        else:
            print("\nNo SQL injection vulnerabilities detected in the given URLs.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SQL Injection Scanner for Multiple URLs")
    parser.add_argument("file_path", help="Path to the file containing URLs")
    args = parser.parse_args()

    multiple_urls_sql_injection(args.file_path)
