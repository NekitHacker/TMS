import time
import random
import os
banner = [
'Loading... \n'
'[*Dragon*]Startin Dragon metasploit',
'[*Dragon*]sTartin Dragon metasploit',
'[*Dragon*]stArtin Dragon metasploit',
'[*Dragon*]staRtin Dragon metasploit',
'[*Dragon*]starTin Dragon metasploit',
'[*Dragon*]startIn Dragon metasploit',
'[*Dragon*]startiN Dragon metasploit',
'[*Dragon*]startin dRagon metasploit',
'[*Dragon*]startin drAgon metasploit',
'[*Dragon*]startin draGon metasploit',
'[*Dragon*]startin drag0n metasploit',
'[*Dragon*]startin dragoN metasploit',
'[*Dragon*]startin dragon Metasploit',
'[*Dragon*]startin dragon mEtasploit',
'[*Dragon*]startin dragon meTasploit',
'[*Dragon*]startin dragon metAsploit',
'[*Dragon*]startin dragon metaSploit',
'[*Dragon*]startin dragon metasPloit',
'[*Dragon*]startin dragon metaspLoit',
'[*Dragon*]startin dragon metaspl0it',
'[*Dragon*]startin dragon metasplo1t',
'[*Dragon*]startin dragon metasploiT',
'[*Dragon*]Startin dragon metasploit',
'[*Dragon*]Dragon Poison loaded',
]
for index in range(len(banner)):
        time.sleep(0.4)
        print(banner[index])
print("By NekitSTRELOK")
while(1==1):
  cmd=input("bpo > ")
  if(cmd=="clear" or cmd=="cls"):
   os.system("clear")
  if(cmd=="owner" or cmd=="cozdatel"):
     print("NekitSTRELOK")
  if(cmd=="exit"):
    exit()
  if(cmd=="launcher"):
    print(" = = = = TMS LAUNCHER = = = = ")
    print(" = = = = CREATED BY NEKITSTRELOK = = = = ")
    print(" 1. MSFCONSOLE ")
    print(" 2. RouterSploit ")
    print(" 3. Websploit ")
    print(" 4. Hammer ")
    f=input("Your answer:")
    if(f=="1"):
      print(" Installer  created run installer to load MSFCONSOLE ")
      b=open("install.sh","w")
      b.write("pkg update && pkg upgrade -y && pkg install wget curl openssh git -y && cd $HOME && wget Auxilus.github.io/metasploit.sh &&  bash metasploit.sh && msfconsole ")
      print("To run installer type: bash install.sh")
      print("By TMS Team : NekitSTRELOK")
    if(f=="2"):
      print(" Installer created run installer to load ROUTERSPLOIT ")
      g=open("install.sh","w")
      g.write("pkg install python &&  pkg upgrade && pkg install autoconf automake bison bzip2 clang cmake \ coreutils diffutils flex gawk git grep gzip libtool make patch perl \ sed silversearcher-ag tar wget pkg-config && pkg install perl && pkg install python-dev clang libcrypt-dev libffi-dev git openssl-dev && export CONFIG_SHELL=$PREFIX/bin/sh && pkg install git && git clone https://github.com/threat9/routersploit && cd routersploit && pip install requests && pip install -r requirements.txt &&  pip install -r requirements-dev.txt 10. termux-fix-shebang rsf.py && python rsf.py")
      print("Run install.sh : bash install.sh")
      prinr("By TMS Team : NekitSTRELOK")
