Remote Access Trojan (RAT) - Python Implementation
This Python-based Remote Access Trojan (RAT) provides a wide range of functionalities for remote monitoring and control of a compromised system. It includes features like system information retrieval, remote execution, keylogging, and even taking screenshots. The RAT can operate across both Windows and Linux platforms, adjusting commands and execution accordingly.

Features
1. Socket-based Communication
Establishes a persistent connection to a remote server using TCP sockets. Allows sending and receiving of commands and data from the server.
Usage: This is the core of the communication mechanism between the RAT and the command-and-control server.
2. Remote Command Execution
Allows remote execution of system commands through the RAT, adapting to the platform (Windows/Linux).
Windows: Uses cmd.exe for command execution.
Linux: Executes commands directly via shell.
3. Keylogger
Captures all keystrokes on the victim’s machine and saves them into a log file (keys.txt).
Real-time logging: It logs in real-time, sending captured keystrokes to the server.
4. Screenshot Capture
Captures a screenshot of the victim's desktop and sends the image to the remote server.
Cross-platform support: Utilizes the pyscreenshot library for compatibility across multiple operating systems.
5. System Information
Retrieves detailed information about the victim’s system, including the operating system, processor, and platform details.
Usage: Displays critical system metadata for further exploitation.
6. WinPEAS & LinPEAS Integration
Automates the execution of winPEAS (Windows Privilege Escalation tool) and linPEAS (Linux Privilege Escalation tool) to gather security-related information.
Windows: Downloads and executes the latest winPEAS release.
Linux: Downloads and executes linPEAS through a curl one-liner.
7. Log Handling
Manages logging for various events and errors within the RAT, with options to enable or disable logging.
Real-time: Can send logs to the server upon request.
8. Memory Ripper
Executes a destructive operation called "memory ripper," designed to corrupt memory and files with random symbols.
Usage: Primarily for testing or destructive purposes.
9. Hibernate Mode
Temporarily pauses the RAT for a specified amount of time, "hibernating" the malware and then resuming after the timeout.
Usage: Helps to avoid detection by security software.
10. Connection Status Monitoring
Continuously checks the connection with the server using a "ping/pong" mechanism.
Usage: Re-establishes the connection automatically if it's lost.
11. File Transfer
Sends and receives files between the compromised machine and the remote server.
Supports binary transfers such as screenshots or log files.
12. Process Management
Uses multiprocessing to handle resource-heavy tasks, such as keylogging, without blocking other operations.
Example: Runs the keylogger in a separate process to maintain efficiency.
13. Command Filtering
Interprets and processes various commands sent from the server, including system info, status requests, keylog retrievals, and more.
Command types: Can filter, execute, and respond to a wide range of commands based on server requests.
How to Use
Start the RAT:

The RAT begins by establishing a connection to the remote server using the specified host and port.
It spawns a keylogger process and continuously checks for incoming commands from the server.
Send Commands:

Commands such as screenshot, status, system info, winpeas, or linpeas can be sent to retrieve information or perform specific actions on the target machine.
Retrieve Data:

The RAT sends back requested information, screenshots, keystrokes, and other data to the remote server over the established connection.
