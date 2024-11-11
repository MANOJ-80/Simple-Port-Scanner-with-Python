# Simple-Port-Scanner-with-Python🐍🔍🔒

## Overview
 
This Python script performs a simple port scan on a target host. It checks whether a specific port on the host is open or closed, providing a basic tool for network exploration and security assessment. The script utilizes Python's built-in socket library to establish connections and determine the status of the targeted port.

## Features

- **Single Port Scan:** The script focuses on scanning a single port at a time, allowing users to specify both the target IP address and the port number they wish to scan.
- **User-friendly Input:** Prompts the user for the target IP address and port number, making it easy to use without modifying the script's source code.
- **Error Handling:** Includes basic error handling to manage exceptions such as invalid inputs or network issues gracefully.

## Getting Started

To run this Python port scanner, ensure you have Python installed on your system. This script has been tested with Python3 versions.

**Installation**

No installation is required. Clone the repository or copy the script to your local machine:

```
git clone https://github.com/MANOJ-80/Simple-Port-Scanner-with-Python.git
```
## Usage

Run the script from the command line and follow the prompts to enter the target IP address and port number:

```
python3 PortScanner.py
```

After entering the IP address and port number, the script will attempt to connect to the specified port on the target host. It will then print a message indicating whether the port is open or closed.

## Contributing

Contributions are welcome! Feel free to submit pull requests for bug fixes, enhancements, or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by the Python Socket Programming Tutorial.
- Additional insights drawn from the Python documentation on socket programming.

