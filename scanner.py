import socket

target = "127.0.0.1"  #localhost
start_p = 1
end_p= 1000
timeout=1

def prescan(): #initialize variables
    global target,start_p,end_p,timeout
    target = input("Enter your victim: ")
    start_p = int(input("Enter an integer for opening port: "))
    end_p = int(input("Enter an integer for ending port: "))
    timeout = int(input("Enter the timeout: "))

prescan()

def portscanner(target, port): #provide the scan for a single port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target, port))
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} closed")
        return False
    
def scanReal(target, startp, endp): #provide iteration for port scanner
    for port in range(startp, endp):
        if portscanner(target, port):
            print(f"Port {port} is open")

scanReal(target, start_p, end_p)
