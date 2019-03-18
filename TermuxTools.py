import time
#-----------------------------------------------------------------------------------------
file1 = "TermuxTools(eng).txt"
startfile1 = open(file1, mode = 'r', encoding = 'ascii')
print (startfile1.read())
#------------------------------------------------------------------------------------------
c = int(input("choose the command:"))
#------------------------------------------------------------------------------------------
if c==1:
	print('paste its: apt upgrade')
	time.sleep(3)
if c==2:
	print('paste its: termux-setup-storage')
	time.sleep(3)
if c==3:
	print('paste its: apt install python2')
	time.sleep(3)
if c==4:
	print('paste its: cd /storage/emulated/0')
	time.sleep(3)
if c==5:
	print('paste its: git clone https://github.com/Aizek05/TermuxTools')
	time.sleep(3)
if c==6:
	print('paste its: pkg install nmap -y')
	time.sleep(3)
if c>4:
	print('invalid number!')
