import os
from modules.logo import print_logo
print_logo()





while True:
    print("\nTo Ckack Error-Based SQL Injection : 1 ")
    print("To Ckack Union-Based SQL Injection : 2")
    print("Authentication Bypass : 3")
    print("To Ckack Boolean Based : 4 ")
    print("To Ckack Time-Based : 5")
    print("To Ckack multiple url : 6")
    print("End: 7")

    choice = input("Enter Your Choice:")
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Please try again.\n")
        continue

    url = None
    if choice in ["1", "2", "3", "4", "5"]:
        url = input("Enter the URL to test for SQL injection: ")
        if not url.startswith("http://") and not url.startswith("https://"):
            print("Please enter a valid URL starting with http:// or https://")
            continue
        print(f"You have selected option {choice}.")
        print(f"Testing {url} for SQL injection vulnerabilities...")
    if choice == "1":
        from modules.error_based import error_based_sql_injection
        error_based_sql_injection(url)
    elif choice == "2":
        from modules.union_based import union_based_sql_injection
        union_based_sql_injection(url)
    elif choice == "3":
        from modules.authentication_bypass import authentication_bypass
        authentication_bypass(url)
    elif choice == "4":
        from modules.boolean_based import boolean_based_sql_injection
        boolean_based_sql_injection(url)
    elif choice == "5":
        from modules.time_based import time_based_sql_injection
        time_based_sql_injection(url)
    elif choice == "6":
        from modules.multiple_urls import multiple_urls_sql_injection
        print("Enter File path for Multiple URLs txt file:")
        file_path = input("File path: ")
        if not os.path.isfile(file_path):
            print("File does not exist. Please check the path.")
            continue
        else:
            multiple_urls_sql_injection(file_path)
    elif choice == "7":
        print("You have selected to exit the program.")
        print("Exiting the program.")
        break