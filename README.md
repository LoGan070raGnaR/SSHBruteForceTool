# SSHBruteForceTool
A Python script for SSH login bruteforcing, allowing security testing by systematically trying passwords from a list against a target host. Features user-friendly prompts and detailed logging for effective security assessments.

# SSH Bruteforce Script Overview

## Features:

- **Logging:** The script uses the `pwn` library for logging, making it easy to understand what's happening.

- **Security Check:** After trying passwords, the script checks and logs the security settings of the SSH connection.

- **User Interaction:** You can input details like the target host IP, username, and the password file's path.

- **Structured Logs:** The script logs attempts, security details, and errors in an organized way.

- **Exception Handling:** Handles errors during SSH attempts and security checks, logging them for reference.

## Constants:

- **TIMEOUT:** A predefined constant regulates the timeout duration for SSH connection attempts.

## Script Execution Overview:

1. **Initialization:**
   - Logging is initiated, signaling the commencement of the SSH bruteforce script.

2. **User Input:**
   - The script prompts the user for crucial information, including the target host IP, username, and the password file's path.

3. **SSH Login Attempt:**
   - The script iterates through passwords, attempting an SSH login using the `ssh()` function from the `pwn` module.

4. **Security Settings Check:**
   - Upon successful login, the script thoroughly inspects and logs the security settings of the SSH connection.

5. **Exception Handling:**
   - Robust exception handling captures and logs errors during both SSH connection attempts and the security settings check.

6. **Cleanup:**
   - The script gracefully concludes the SSH connection and loops for subsequent iterations.

7. **Script Completion:**
   - A conclusive log message signifies the successful completion of the SSH bruteforce script.

---
## SSH Bruteforce Script Overview

### Libraries and Modules

#### pwn Library

- **Purpose:** A powerful library for exploitation and binary manipulation.
- **Usage:** Used for logging and handling interactions in an organized way.
- **Functions:**
  - `log.info()`: Logs informational messages.
  - `log.success()`: Logs success messages.
  - `log.failure()`: Logs failure messages.

#### paramiko Library

- **Purpose:** A Python implementation of the SSH protocol, providing support for secure connections.
- **Usage:** Used for SSH connection attempts and security settings inspection.
- **Classes:**
  - `Transport`: Represents an SSH transport, allowing for connection and security checks.
  - `Transport.get_security_options()`: Retrieves security options (ciphers, digests, etc.) from the established transport.
  - **`SecurityOptions` Class:**
    - **Purpose:** Simple object containing the security preferences of an SSH transport.
    - **Usage:** Preferences include acceptable ciphers, digests, key types, key exchange algorithms, and compression algorithms.
    - **Methods:**
      - `__init__(transport)`: Initializes the object with a given transport.
      - `__repr__()`: Returns a string representation of the object for debugging.
    - **Properties:**
      - `ciphers`: Symmetric encryption ciphers.
      - `digests`: Digest (one-way hash) algorithms.
      - `key_types`: Public-key algorithms.
      - `kex`: Key exchange algorithms.
      - `compression`: Compression algorithms.


### User Input

- **Functions:**
  - `input()`: Takes user input for the target host IP, username, and the path to the password file.
  - **Usage:** Collects information required for SSH bruteforcing.

### SSH Connection Attempt Loop

- **Functions:**
  - `with open(password_file, "r") as password_list:`: Opens the password file for reading.
  - `for password in password_list:`: Iterates through the password list.
  - `ssh()`: Initiates an SSH connection attempt using the provided credentials.

### Exception Handling

- **Purpose:** Captures and logs errors during SSH connection attempts and security settings checks.
- **Functions:**
  - `paramiko.ssh_exception.AuthenticationException`: Handles authentication errors during SSH login attempts.
  - `Exception`: Catches and logs general exceptions.

### Security Settings Inspection

- **Purpose:** Checks and logs the security settings of the established SSH connection.
- **Functions:**
  - `Transport.get_security_options()`: Retrieves and logs security options.

### Cleanup and Finalization

- **Functions:**
  - `transport.close()`: Closes the SSH connection.
  - `log.info("SSH bruteforce script completed")`: Logs a completion message for the script.

In summary, the script utilizes the `pwn` library for logging and interaction, the `paramiko` library for SSH connection attempts and security settings inspection, along with constants and user input to perform a bruteforce attack on an SSH login. Exception handling ensures robust error logging, and the script concludes by closing the SSH connection and logging the completion message.

## For more information:

### pwntools:

- Source Code: [pwntools](https://github.com/Gallopsled/pwntools)
- Docs: [Docs](https://docs.pwntools.com/en/stable/)

### Paramiko:

- Official Website: [Paramiko](https://www.paramiko.org/)
- API Docs: [Docs](https://docs.paramiko.org/en/latest/)
- Transport Class: [Transport](https://docs.paramiko.org/en/latest/api/transport.html)

------------
## Troubleshooting Steps for SSH Bruteforce Script

### Error: Unable to Connect to Port 22 on 127.0.0.1

1. **Check SSH Server Status:**
   ```bash
   sudo service ssh start
   ```
   Ensure that the SSH server is running. If not, install the SSH server:
   ```bash
   sudo apt update
   sudo apt install openssh-server
   ```

2. **Verify SSH Port:**
   Confirm that your SSH server is running on port 22. Adjust the port if necessary.

3. **Firewall Check:**
   Make sure your firewall allows incoming connections on port 22.

4. **Inspect SSH Server Logs:**
   Look into the SSH server logs for error messages
   ```bash
   cat /var/log/auth.log
   ```

5. **Verify Localhost Resolution:**
   Ensure that "`localhost`" resolves to `127.0.0.1`:
   ```bash
   ping localhost
   ```
   
### Error: Failed to Start ssh.service: Unit ssh.service not found

1. **Install SSH Server:**
   ```bash
   sudo apt update
   sudo apt install openssh-server
   ```

2. **Start SSH Service:**
   ```bash
   sudo service ssh start
   ```

After addressing these steps, attempt to run your Python script again:

```bash
sudo python3 ssh_bruteforce.py
```

Ensure that the script has the necessary permissions to access the SSH service. If issues persist, review error messages and logs for further troubleshooting.

------------
**Note:** This script is designed for educational purposes and ethical use only. Unauthorized access to systems is illegal and unethical.