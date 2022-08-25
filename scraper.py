import sys
import time
try:
    from googlesearch import search
except ImportError: 
    print(bcolors.FAIL + "No module named 'google' found" + bcolors.ENDC)
from colorama import init
init()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def paradoxlogo():
	print(bcolors.HEADER + """

8888888b.                   888       .d8888b.                                                     
888  "Y88b                  888      d88P  Y88b                                                    
888    888                  888      Y88b.                                                         
888    888  .d88b.  888d888 888  888  "Y888b.    .d8888b 888d888 8888b.  88888b.   .d88b.  888d888 
888    888 d88""88b 888P"   888 .88P     "Y88b. d88P"    888P"      "88b 888 "88b d8P  Y8b 888P"   
888    888 888  888 888     888888K        "888 888      888    .d888888 888  888 88888888 888     
888  .d88P Y88..88P 888     888 "88b Y88b  d88P Y88b.    888    888  888 888 d88P Y8b.     888     
8888888P"   "Y88P"  888     888  888  "Y8888P"   "Y8888P 888    "Y888888 88888P"   "Y8888  888     
                                                                         888                       
                                                                         888                       
                                                                         888    Coded by DrParad0x1999                   
""" + bcolors.OKBLUE + """

For more private methods & tools : https://t.me/DrParad0x1999_Channel | ICQ : DrParad0x1999

""" + bcolors.ENDC)

def PrU(dork,weo_numb,enable_save,filename):

	print (bcolors.UNDERLINE + "Start Collecting Urls Using dork ... \n" + bcolors.ENDC)
	
	pages = 0
	
	try:
		for qwdw in search(dork, tld="com", lang="es", num=weo_numb, start=0, stop=None, pause=2):
			print ("[+] " + bcolors.OKGREEN + qwdw + bcolors.ENDC)
			time.sleep(0.2)
			
			pages += 1
			
			if pages >= weo_numb:
				break
			
			data = (qwdw)
			
			if enable_save == 1:
				file = open(filename, "a")
				file.write(str(data))
				file.write("\n")
				file.close()
				
	except HTTPError:
		if e.code == 429:
		     print (bcolors.FAIL + " Too Many Requests detected !! \n" + bcolors.ENDC)
		     print ("Loading...")


def prmain():
	paradoxlogo()
	enable_save = 0
	filename = ""

	if len(sys.argv) == 1:
		print (bcolors.FAIL + "ERROR: No dork or parameters found" + bcolors.ENDC)
	elif len(sys.argv) == 2:
		arg = sys.argv[1]
		
		if arg == "-h" or arg == "--help" :
			print ("HELP SECTION:\n")
			print ("Usage: \tscraper.py dork number of websites u want \n")
			print ("Example: \tscraper.py inurl:admin 20 -s listname.txt \n")
			print ("-d,--dork \tSpecifies the dork to use in the tool")
			print ("-h,--help \tFor help")
			print ("-v,--version \tShow version")
			print ("-s,--save \tEnable save List of websites in txt file")
		elif arg == "-v" or arg == "--version":
			print ("DorkScraper v1.0 By DrParad0x1999")
		else:
			print (bcolors.FAIL + "ERROR: Incorrect argument or sintaxis" + bcolors.ENDC)
			
	elif len(sys.argv) > 2 and len(sys.argv) <= 6:

		if sys.argv[1] == "-d" or sys.argv[1] == "--dork":
			
			dork = sys.argv[2]
			weo_numb = int(sys.argv[3])
			
			if(len(sys.argv) > 4):
				if sys.argv[4] == "-s" or sys.argv[4] == "--save":
					enable_save = 1
					filename = sys.argv[5]

			PrU(dork,weo_numb,enable_save,filename)
				
prmain()