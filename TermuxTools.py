#-------------------------------импорт библиотек----------------------------------------------------------------------------
import time
import os
#-----------------------------------переменные файлов----------------------------------------------------------------------
file1 = "TermuxTools(eng).txt"
file2 = "TermuxTools(end).txt"
startfile1 = open(file1, mode = 'r', encoding = 'ascii')
startfile2 = open(file2, mode = 'r', encoding = 'ascii')
print (startfile1.read())
#--------------------------переменные запросов-----------------------------------------------------------------------------
c = int(input("choose the command:"))
#--------------------------реакции на переменные запросов---------------------------------------------------------------
if c==1:
	os.system('apt update && apt upgrade -y')
	os.system('pkg update && pkg upgrade -y')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c==2:
	os.system('termux-setup-storage')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c==3:
	os.system('apt install python2 -y')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c==4:
	os.system('cd /storage/emulated/0')
	os.system('ls')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c==5:
	os.system('/data/data/com.termux/files/home && git clone https://github.com/Aizek05/TermuxTools -y')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c==6:
	os.system('pkg install nmap -y')
	time.sleep(3)
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
if c>6:
	print('invalid number!')
	end = input('end?<y/n>')
	if end == 'n':
		print(startfile1.read())
		c = int(input("choose the command:"))
