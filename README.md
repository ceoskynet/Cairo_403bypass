Cairo - 403 Bypass Tool
Cairo is a Python-based penetration testing tool designed to help security researchers and ethical hackers test and bypass 403 Forbidden HTTP responses. It leverages various payloads, headers, and encoding techniques to identify potential misconfigurations that allow access to restricted resources.

Features
Payload Testing:

Tests common bypass payloads (e.g., /../, /%2e/, etc.).
Dynamically fetches external payload lists from a URL.
Built-in fallback to local payloads.
Header Manipulation:

Adds bypass headers such as X-Forwarded-For, X-Client-IP, Referer, and X-Original-URL.
Custom User-Agent:

Identifies requests using the Cairo tool for debugging or logging purposes.
Lightweight & Simple:

Easy-to-use command-line tool that gives immediate results.
Requirements
Python 3.6+
The following Python libraries:
requests
argparse
Install the dependencies using:

bash
Copy
pip install requests
Installation

Clone the repository:
bash
Copy

git clone https://github.com/<your-username>/Cairo-403-Bypass.git
cd Cairo-403-Bypass
Make the script executable (optional):

bash
Copy
chmod +x cairo.py

Run the tool using Python 3.

Usage
Basic Usage
Run the tool against a target URL:

bash
Copy

python3 cairo.py https://example.com/
Dynamic Payloads from External Source
You can supply an external payload list hosted online using the --payloads-url parameter:

bash
Copy

python3 cairo.py https://example.com/ --payloads-url https://raw.githubusercontent.com/<your-username>/Payloads-403-Bypass/main/payloads.txt
If the --payloads-url parameter is not provided, the tool will fall back to its built-in payload list.

Example Output
Here’s what the tool looks like in action:

███████╗ █████╗ ██╗██████╗  ██████╗ 
██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗
██      ███████║██║██████╔╝██║   ██║
██╔══╝  ██╔══██║██║██╔═══╝ ██║   ██║
███████╗██║  ██║██║██║     ╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝
                Version: 1.1
                Author: shaheeryasirx1@gmail.com

[*] Starting 403 bypass tests on target: https://example.com/

[+] Testing URL: https://example.com/
[-] Blocked: https://example.com/ (Status: 403)
[+] Testing URL: https://example.com/.
[-] Blocked: https://example.com/. (Status: 403)
[+] Testing URL: https://example.com/..;/
[!] Potential bypass: https://example.com/..;/ (Status: 200)
[+] Testing URL: https://example.com/%2e/
[!] Potential bypass: https://example.com/%2e/ (Status: 200)
How It Works
Payload Testing:

Appends different payloads like /../, /%2e/, /index.php, etc., to the target URL to test for bypass scenarios.
Header Testing:

Sends requests with additional headers like X-Forwarded-For and X-Client-IP to check if these headers bypass restrictions.
Dynamic Payloads:

Fetches payloads from an external URL (e.g., GitHub-hosted payload lists) to stay up-to-date with the latest bypass techniques.
Fallback:

If no external payloads are provided or the fetch fails, the tool uses its built-in payload list to ensure functionality.
External Payload List
The tool supports fetching payloads from external sources. To host your own payload list:

Create a text file with one payload per line, like this:

/
/.
/..;/
/%2e/
/%2e%2e/
/%3b/
Host the file online (e.g., on GitHub or your own server).

Provide the URL to the tool using the --payloads-url parameter.

Example Payload List
An example payload list can be found here: PayloadsAllTheThings - Forbidden Bypass

Roadmap
Planned features for future versions:

Multi-threading for faster testing.
Support for custom headers via configuration files.
Logging results to a file for analysis.
Support for proxy servers.
License
This tool is intended for educational purposes and ethical penetration testing only. Use responsibly.

Author
Name: Shaheer Yasir
Contact: shaheeryasirx1@gmail.com
If you encounter any issues or have suggestions, feel free to reach out via email or create an issue in the GitHub repository.
