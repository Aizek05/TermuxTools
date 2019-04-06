import time
import os
#-----------------------------------------------------------------------------------------
file1 = "TermuxTools(eng).txt"
startfile1 = open(file1, mode = 'r', encoding = 'ascii')
print (startfile1.read())
#------------------------------------------------------------------------------------------
c = int(input("choose the command:"))
#------------------------------------------------------------------------------------------
if c==1:
	os.system('apt update && apt upgrade -y')
	os.system('pkg update && pkg upgrade -y')
	time.sleep(3)
if c==2:
	os.system('termux-setup-storage')
	time.sleep(3)
if c==3:
	os.system('apt install python2 -y')
	time.sleep(3)
if c==4:
	os.system('cd /storage/emulated/0')
	os.system('ls')
	time.sleep(3)
if c==5:
	os.system('git clone https://github.com/Aizek05/TermuxTools')
	time.sleep(3)
if c==6:
	os.system('pkg install nmap -y')
	time.sleep(3)
if c>6:
	print('invalid number!')
