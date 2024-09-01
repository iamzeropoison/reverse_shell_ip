#           ---------------->  Special Thanks too Zeropoison  <------------

__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



# Reverse Shell Project
This repository contains a simple implementation of a reverse shell using Python. It includes two main components:

# 1: Server Code (server.py): 
This script should be run on your machine to listen for incoming connections from the target machine. It requires your machine's IP address to be specified in the code so that it can accept connections from the client.

# 2: Client Code (client.py): 
This script is intended to be run on the target machine. When executed, it will establish a connection to the server script running on your machine, effectively giving you control over the target machine.

# How It Works

# 1: Setup Server:
Run server.py on your machine.
Modify the code to include your machine's IP address.
The server will wait for incoming connections from the client script.

# 2: Client Execution:
Distribute client.py to your target.
The target executes the script, which connects back to your server.

# 3: Access:
Once the connection is established, you can execute commands on the target machine remotely.


#                               How we Execute this command
@                 git clone https://github.com/iamzeropoison/reverse_shell_ip.git
$                               cd reverse_shell_ip                

# Important Notes
Usage Warning:
This project is intended for educational purposes to demonstrate the basics of a reverse shell. Unauthorized access to computers or networks is illegal and unethical. Always obtain explicit permission before conducting any security-related activities.

# Dependencies:
This project requires Python 3. Ensure you have Python 3 installed on both server and client machines.

# Binding with Files:
You can bind the client.py script to other file types (e.g., images) to make it less suspicious, but this action is not recommended for any unlawful purposes.

# How to Run
# 1: Server Side:

Edit server.py to specify your IP address.
Run the script using: python3 server.py.

# 2: Client Side:
Distribute client.py to the target.
Once executed by the target, it will initiate a connection to your server.

# Disclaimer
This project is for learning purposes only. Misuse of this tool can lead to serious legal consequences. Always use such tools responsibly and within the bounds of the law.
