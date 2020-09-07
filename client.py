import socket
import threading
import os
from colorama import init
import time
from colorama import Fore, Back, Style

os.system('cls')

init()

serversstatus = Fore.GREEN + "[Online]"

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))
except:
    serversstatus = Fore.RED + "[Offline]"
    client.close()
    time.sleep(1)

version = '11.1'

print(Fore.LIGHTBLUE_EX + f"""


░██████╗██╗░░░██╗░██████╗  ░█████╗░██╗░░██╗░█████╗░████████╗
██╔════╝██║░░░██║██╔════╝  ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
╚█████╗░██║░░░██║╚█████╗░  ██║░░╚═╝███████║███████║░░░██║░░░
░╚═══██╗██║░░░██║░╚═══██╗  ██║░░██╗██╔══██║██╔══██║░░░██║░░░
██████╔╝╚██████╔╝██████╔╝  ╚█████╔╝██║░░██║██║░░██║░░░██║░░░
╚═════╝░░╚═════╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
                    By: ImBugle#8849
                    SocketHoster: ImBugle#8849
                    Version: {version}
                    Servers: {serversstatus}
""")

if serversstatus == Fore.RED + "[Offline]":
    time.sleep(2)
    print(Fore.RED + "[!] " + Fore.YELLOW + "Servers are currently offline!")
    time.sleep(4)
    quit()
else:
    pass


time.sleep(2)
nickname = input(Fore.GREEN + "[Server] " + Fore.WHITE + "Choose a nickname: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print(Fore.RED + "Oops, Somthings not right | Closing connection |")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()