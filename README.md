# RAT (Remote Access Trojan)

This is a Python-based Remote Access Trojan (RAT) that provides various features for monitoring and controlling a remote system. The RAT includes functionality for capturing screenshots, keylogging, system information extraction, and executing commands on the remote machine.

## Features
> [!WARNING]
> Dont work properly for **Windows** yet.

### 1. **Connection Handling**
   - **Persistent Connection**: The RAT attempts to maintain a persistent connection to the server, reconnecting if the connection is lost.
   - **Socket-based Communication**: Uses a socket connection to communicate between the client and server.

### 2. **Command Execution**
   - **Cross-platform Support**: Executes commands on both Windows and Linux operating systems using the system’s native shell (`cmd.exe` on Windows, Bash on Linux).
   - **Real-time Execution**: Commands can be sent and executed on the remote system in real-time, with the output returned to the server.

### 3. **Screenshot Capture**
   - **Screen Capture**: Captures a screenshot of the remote desktop and sends it to the server.
   - **Cross-platform**: Works on both Windows and Linux systems.

### 4. **Keylogger**
   - **Keylogging**: Logs the keystrokes of the victim's system and sends them to the server.
   - **Optimized with Multithreading**: Uses mulithreading to run the keylogger independently, improving performance.

### 5. **System Information**
   - **Detailed System Info**: Retrieves and sends detailed system information such as OS type, node name, processor, and platform.

### 6. **File Transfer**
   - **Send Files**: Allows sending local files from the victim's machine to the server.
   - **Receive Files**: Files can be downloaded from the server.

### 7. **PEAS Integration**
   - **WinPEAS**: Integrates with WinPEAS to perform privilege escalation checks on Windows systems.
   - **LinPEAS**: Integrates with LinPEAS to perform privilege escalation checks on Linux systems.

### 8. **Log Management**
   - **Event Logging**: Logs all errors and important events during execution.
   - **Enable/Disable Logs**: Logs can be toggled on and off by the server.

### 9. **Memory Ripper**
   - **Memory Corruption Attack**: Executes a function that writes corrupted text repeatedly to memory.

### 10. **Hibernate**
   - **Temporary Pause**: The RAT can hibernate (pause execution) for a specified number of seconds before resuming.

## Commands

The RAT supports the following commands:

- `screenshot`: Captures and sends a screenshot of the victim's desktop.
- `status`: Retrieves the status of the connection and RAT parameters.
- `system info`: Sends detailed system information of the victim's system.
- `logs true/false`: Enables or disables logging on the victim's system.
- `show logs`: Sends the current log to the server.
- `linpeas/linpeas force`: Executes LinPEAS for Linux privilege escalation checks.
- `winpeas/winpeas force`: Executes WinPEAS for Windows privilege escalation checks.
- `memory ripper`: Starts a memory corruption attack.
- `hibernate-X`: Hibernates the RAT for X seconds.
- `get keylogs`: Sends the logged keys to the server and clears the keylog file.

## Usage

1. **Setup**:
   - Ensure you have the required Python packages installed (`pyscreenshot`, `keyboard`, etc.).
   - Modify the `host` and `port` variables to match your server's IP and port.

2. **Running the RAT**:
   - Execute the script on the victim's machine.
   - The script will attempt to connect to the server and await further commands.

3. **Sending Commands**:
   - Use the supported commands to interact with the RAT and the remote system.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on systems where you have explicit permission. Misuse of this software could lead to legal consequences.


