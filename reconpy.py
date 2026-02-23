import socket
import threading
import argparse
import time
start_time = time.time()
# first get the information 
p = argparse.ArgumentParser(description='Multi-threaded Port Scanner')
p.add_argument('i', help='The IP address of the device you want to check',type=str)
p.add_argument('-n','--numeral',help="Number of gates you want to check",type=int)
p.add_argument('-p',"--ports",help="ports thats you detect it ", nargs='+',type=int)
p.add_argument('-o','--save',help='Save file result as file text',type=str)
p.add_argument('-a','--All', action="store_true",help='Show all results of scan')
arg = p.parse_args()


# clors 
G = '\033[92m'  # green
R = '\033[91m'  # red
Y = '\033[93m'  # yellow
C = '\033[96m'  # clue
W = '\033[0m'   # white

BANNER = f"""
{C}#################################################
#                {Y}ReconPy v1.0{C}                   #
#         {W}Multi-threaded Port Scanner{C} 
#              {G}Made by: Fikri{C} 
#################################################{W}
"""


ip_addr =  arg.i
# this is first case when user gives only ip  

result_file = []
file_lock = threading.Lock()
def scan_port(ip , port):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip , port ))
    output = ''
    try:
        portName = socket.getservbyport(port)
    except:
        portName = 'unknown'
    
    if result == 0:
        output = f"{G}[+] PORT {port} / {portName} is OPENED{W}"
    elif arg.All:
         output = f"{R}[-] PORT {port} is CLOSED{W}"
          
    if output:
        print(output)
        with file_lock:
            clean_text = output.replace(G, "").replace(R, "").replace(W, "")
            result_file.append(clean_text + '\n')
    sock.close()

print(BANNER)
print(f"[*][*] Start Scanning {ip_addr}")

print(f"{Y}[*] Target IP: {ip_addr}{W}")
def start_scanning(ip , port):
  print(f"Start scanning {ip} useing threads ... ")
  threads = []
  for p in range(1, port + 1):
        t = threading.Thread(target=scan_port, args=(ip, p))
        threads.append(t)
        t.start()
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []
  for t in threads:
      t.join()

## logic proggram 
if arg.ports:
    for port in arg.ports:
        scan_port(ip_addr, port)
elif arg.numeral:
    start_scanning(ip_addr, arg.numeral)
else:
    start_scanning(ip_addr, 1000)



     
## save in text file 
if arg.save and result_file:
    with open(arg.save , 'w') as f:
       f.writelines(result_file)
    print(f"{C}Result saved to {arg.save} {G}")
print(f'{G}Scan completed successfully!!{W}')
end_time = time.time()
print(f"{Y}Scan finished in {round(end_time - start_time, 2)} seconds{W}")


## reconPy v1.0 Made By  fikri Mohamed 