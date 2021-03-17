import requests
import re
from pathlib import Path

#might not work on cmd
class fontcolors:
    BLUE = '\x1b[1;34;40m'
    WHITE = '\x1b[1;37;40m'
    GREEN = '\x1b[1;32;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    CYAN = '\x1b[1;36;40m'
    END = '\x1b[0m'

class symbols:
	ONE = f"{fontcolors.YELLOW}[1] {fontcolors.END}"
	TWO = f"{fontcolors.YELLOW}[2] {fontcolors.END}"
	THREE = f"{fontcolors.YELLOW}[3] {fontcolors.END}"
	INFO = f"{fontcolors.YELLOW}[!] {fontcolors.END}"
	QUE = f"{fontcolors.BLUE}[?] {fontcolors.END}"
	FAIL = f"{fontcolors.RED}[-] {fontcolors.END}"
	SUCCESS = f"{fontcolors.GREEN}[+] {fontcolors.END}"
	INPUT = f"{fontcolors.CYAN}[»] {fontcolors.END}"

#online-hash-crack banner	
print(fontcolors.GREEN)
print("""
  ____ _  _ _    _ _  _ ____ 
  |  | |\ | |    | |\ | |___ 
  |__| | \| |___ | | \| |___ 
                           
                    _  _ ____ ____ _  _        
                    |__| |__| [__  |__|        
                    |  | |  | ___] |  |        
          
                               ____ ____ ____ ____ _  _   
                               |    |__/ |__| |    |_/    
                               |___ |  \ |  | |___ | \_   

OnlineHashCrack.com - API                          ~ Sumit             
""")
print(fontcolors.END)

#legend spotted here...hahaha
print(f"{fontcolors.CYAN}*** Usage Instructions ***{fontcolors.END}")
print(f"{fontcolors.CYAN}---------------------------------------------------------{fontcolors.END}")
print(f"{symbols.ONE}{fontcolors.YELLOW}Enter Your Email :{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Email is needed to get the result.{fontcolors.END}")
print(f"\n{symbols.TWO}{fontcolors.YELLOW}Enter File Path :{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Maximum File Size : 200 MB{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Supported Files Are :{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Wifi WPA(2): Network dumps(.cap, .pcap, .pcapng){fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}MS Office: Word, Excel or Powerpoint{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}iTunes Backup: encrypted iTunes Backup Manifest.plist{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Archives: encrypted ZIP / RAR / 7-zip archives{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}PDF: encrypted / password-protected .PDF files{fontcolors.END}")
print(f"\n{symbols.THREE}{fontcolors.YELLOW}Price :{fontcolors.END}")
print(f"{symbols.SUCCESS}{fontcolors.WHITE}Totally free of charge.{fontcolors.END}")
print(f"{fontcolors.CYAN}---------------------------------------------------------{fontcolors.END}")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails : '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 

# check email using regex
def check_email(email):
	if(re.search(regex,email)):
		pass
	else:
		print(f"{symbols.FAIL}Invalid Email !")
		exit()

# check if file exists or not
def check_path(path):
    if Path(path).is_file():
    	pass
    else:
    	print (f"{symbols.FAIL}File Not Found !")
    	exit()

# taking user inputs
email = input(f"\n{symbols.INPUT}{fontcolors.WHITE}Email : {fontcolors.END}")
check_email(email)
path = input(f"\n{symbols.INPUT}{fontcolors.WHITE}File Path : {fontcolors.END}")
check_path(path)

# using curl : curl -X POST -F "email=valid@email.com" -F "file=@/file/path/" https://api.onlinehashcrack.com
files = {
    'email': (None, email),
    'file': (path, open(path, 'rb')),
}

# using requests post to interact with api endpoint
try:
	response = requests.post('https://api.onlinehashcrack.com/', files=files)
	print(response.text)
	if '[-] This file extension is not supported. Please try again or contact us.' in response.text:
		print(f"{symbols.FAIL}Extension is not supported !")
		print(f"{symbols.FAIL}Please try again with another file !")
	elif '[-] File is not valid.' in response.text:
		print(f"{symbols.FAIL}Invalid file !")
		print(f"{symbols.FAIL}Please try again with another file !")
	elif '[+] This file has already been sent!' in response.text:
		print(f"{symbols.SUCCESS}File already exists !")
		print(f"{symbols.SUCCESS}This file is in cracking process !")
		print(f"{symbols.SUCCESS}Check your e-mail...")
	elif '[+] Something went wrong: this file is not password-protected OR the encryption method is not supported.' in response.text:
		print(f"{symbols.FAIL}File is not encrypted !")
		print(f"{symbols.INFO}Please send an encrypted file !")
	elif 'Yours file' and 'enters in the cracking process' in response.text:
		print(f"{symbols.SUCCESS}{fontcolors.GREEN}File Uploaded Successfully...{fontcolors.END}")
		print(f"{symbols.SUCCESS}Started 20M+ wordlist and hybrid bruteforce.")
		print(f"{symbols.SUCCESS}Check your email to see cracking status.")
		print(f"{symbols.INFO}It takes maximum 48 hours to crack a file !")
		print(f"{symbols.INFO}Sit back and relax...")
		print(f"{symbols.INFO}We will send you an email when it's done !")
	else:
		print(f"{symbols.FAIL}{fontcolors.WHITE}Please try again !{fontcolors.END}")
except requests.exceptions.ConnectionError as err:
	print(f"{symbols.FAIL}Something Went Wrong !")
	raise SystemExit(err)
	
## done for now



