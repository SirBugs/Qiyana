#!/usr/bin/python3/
#! Written in Python3
#! Written by @SirBugs

#! Importing Modules
#! ------------------

import os
import re
import sys
import time
import random
import requests
import argparse
import colorama
from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime
from colorama import Fore, Back, Style
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#! Arguments Assigning
#! ----------------------
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="the URL of the pentesterlab without addons")
parser.add_argument("-w", "--wordlist", help="cookies of your pentesterlab account")
parser.add_argument("-m", "--method", help="this selects the request method")
parser.add_argument("-d", "--data", help="use this if you send data with your request")
parser.add_argument("-f", "--follow", help="asking if you wanna follow redirects or not [y/n]")
parser.add_argument("-x", "--timeout", help="this is asking for request timeout (default=10)")
parser.add_argument("-t", "--threads", help="enter count of threads per second (default=20)")
parser.add_argument("-H", "--header", help=".txt file, if you wanna enter specific header into the request")
parser.add_argument("-F", "--filter", help="this filter is checking your conditions [length:300/lines:50/word:success")
parser.add_argument("-o", "--output", help="saving the output of the fuzzed paths/params")
parser.add_argument("-p", "--proxies", help=".txt file, this if you wanna use proxies, Enter proxies file")
parser.add_argument("-pp", "--proxies_type", help="this is the proxies type [http/socks4/socks5] ** HAVE TO BE SENT WITH PROXIES")
parser.add_argument("-s", "--status_codes", help="if you wanna get more status codes send it (default=200,204,301,302,307,401,403,405,500)")
args = parser.parse_args()


#! Print Logo
#! ------------
def LOGO():
	print(Fore.CYAN+"\n\n\t\t $$$$$$\  $$\                                         "); time.sleep(0.1)
	print(Fore.WHITE+"\t\t$$  __$$\ \__|                                        "); time.sleep(0.1)
	print(Fore.CYAN+"\t\t$$ /  $$ |$$\ $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\  "); time.sleep(0.1)
	print(Fore.WHITE	+"\t\t$$ |  $$ |$$ |$$ |  $$ | \____$$\ $$  __$$\  \____$$\ "); time.sleep(0.1)
	print(Fore.CYAN+"\t\t$$ |  $$ |$$ |$$ |  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |"); time.sleep(0.1)
	print(Fore.WHITE+"\t\t$$ $$\$$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$ |"); time.sleep(0.1)
	print(Fore.CYAN+"\t\t\$$$$$$ / $$ |\$$$$$$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |"); time.sleep(0.1)
	print(Fore.WHITE+"\t\t \___$$$\ \__| \____$$ | \_______|\__|  \__| \_______|"); time.sleep(0.1)
	print(Fore.CYAN+"\t\t     \___|    $$\   $$ |                              "); time.sleep(0.1)
	print(Fore.WHITE+"\t\t              \$$$$$$  |                              "); time.sleep(0.1)
	print(Fore.CYAN+"\t\t               \______/                               ")
	print(Fore.CYAN+"\t\t V 0.0.1\n"); time.sleep(1)
def OPTIONS():
	global _REQUEST
	global _URI
	global _WORDLIST
	global _FOLLOW_REDIRECTS
	global _TIMEOUT
	global _THREADS
	global _SCODES
	global _DATA
	global _PROXY
	global _OUTPUT
	global _HEADER
	print(Fore.WHITE+"\t " + "="*100 + "\r\n"); time.sleep(0.1)
	print("\t "+Fore.CYAN+"[ ! ] \tQ_Method\t : "+_REQUEST); time.sleep(0.1)
	print("\t "+Fore.WHITE+"[ ! ] \tQ_URL\t\t : "+_URI); time.sleep(0.1)
	print("\t "+Fore.CYAN+"[ ! ] \tQ_Worlist\t : "+_WORDLIST+Fore.RED+" [ "+str(len(open(_WORDLIST, "r").read().split("\n")))+" ]"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"[ ! ] \tQ_Timeout\t : "+str(_TIMEOUT)); time.sleep(0.1)
	print("\t "+Fore.CYAN+"[ ! ] \tQ_Threads\t : "+str(_THREADS)); time.sleep(0.1)
	print("\t "+Fore.WHITE+"[ ! ] \tQ_Output\t : "+str(_OUTPUT)); time.sleep(0.1)
	if str(_HEADER) == "None": print("\t "+Fore.CYAN+"[ ! ] \tQ_Header\t : NoHeadersSubmitted")
	else: print("\t "+Fore.CYAN+"[ ! ] \tQ_Header\t : HeadersApplied")
	print("\t "+Fore.WHITE+"[ ! ] \tQ_Targets\t : "+str(_SCODES)); time.sleep(0.1)
	print("\t "+Fore.CYAN+"[ ! ] \tQ_REDIRECTION\t : "+_FOLLOW_REDIRECTS+"\n"); time.sleep(0.1)
	print(Fore.WHITE+"\t " + "="*100 + "\r\n"); time.sleep(0.3)
	print("\t "+Fore.WHITE+"["+Fore.RED+"WAR"+Fore.WHITE+"] "+Fore.CYAN+"This tool is for hunters and pentesters, Don't use it for anything else."); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.RED+"WAR"+Fore.WHITE+"] "+Fore.WHITE+"Today's Advice: Never ask your gf/bestfiriend for nudes bro"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.RED+"WAR"+Fore.WHITE+"] "+Fore.CYAN+"This is the first version of the tool and you may find problems or errors, contact me at @SirBagoza"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.MAGENTA+"DOT"+Fore.WHITE+"] "+Fore.WHITE+"Once you run this tool, it's gonna start fuzzing the the directories in your wordlist path"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.MAGENTA+"DOT"+Fore.WHITE+"] "+Fore.CYAN+"Check if you wanna save the output in a .txt file by adding (-o [file.txt)"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.MAGENTA+"DOT"+Fore.WHITE+"] "+Fore.WHITE+"If you wanna use proxies, Make sure you are using (-p) and (-pp) together"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.MAGENTA+"DOT"+Fore.WHITE+"] "+Fore.CYAN+"For submitting headers, Enter them in .txt file separated by new line\\n\n"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.BLUE+"INF"+Fore.WHITE+"] "+Fore.WHITE+"We all love the president @AbdelfattahElsisi cuz we are egyptians"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.BLUE+"INF"+Fore.WHITE+"] "+Fore.CYAN+"Go find more projects/tools on GITHUB@SirBugs"); time.sleep(0.1)
	print("\t "+Fore.WHITE+"["+Fore.BLUE+"INF"+Fore.WHITE+"] "+Fore.WHITE+"Visit my TWITTER@SirBagoza HackerOne/BugCrowd@bugsv2 \n"); time.sleep(0.5)

	print(Fore.WHITE+"\t " + "="*100 + "\r\n")

#! Strating Coding
#! -----------------

if str(args.method) == "None": _REQUEST = "GET"
else: _REQUEST = str(args.method)

if str(args.url) == "None":
	print("Please read the help docs by running:\n\t\t  Qiyana.py -h / Qiyana.py --help\n\t\tRun as: Qiyana.py -u <URL> -w <WORDLIST>")
	quit()
else: _URI = str(args.url)

if str(args.wordlist) == "None":
	print("Please read the help docs by running:\n\t\t  Qiyana.py -h / Qiyana.py --help\n\t\tRun as: Qiyana.py -u <URL> -w <WORDLIST>")
	quit()
else: _WORDLIST = str(args.wordlist)

if str(args.timeout) == "None": _TIMEOUT = 10
else: _TIMEOUT = int(str(args.timeout))

if str(args.threads) == "None": _THREADS = 20
else: _THREADS = int(str(args.threads))

_SCODES = ["200","204","301","302","307","401","403","405","500"]
if str(args.status_codes) == "None":
	pass
else:
	if "," in str(args.status_codes):
		for Status_Code in str(args.status_codes).split(","):
			if Status_Code in _SCODES: pass
			else: _SCODES.append(Status_Code)
	else:
		if str(args.status_codes) in _SCODES: pass
		else: _SCODES.append(str(args.status_codes))

if str(args.follow) == "None": _FOLLOW_REDIRECTS = "False"
else:
	if str(args.follow) == "y": _FOLLOW_REDIRECTS = "True"
	else: _FOLLOW_REDIRECTS = "False"

_FILTER = str(args.filter)

_OUTPUT = str(args.output)

_HEADER = str(args.header)

_DATA = str(args.data)

_PROXY = str(args.proxies)
if str(args.proxies) == "None" and str(args.proxies_type) == "None": _PROXY = str(args.proxies) # proxies_type
elif str(args.proxies_type) == "None" and _PROXY != "None": pass
elif str(args.proxies_type) != "None" and _PROXY == "None": pass
else: _PROXY = open(str(args.proxies), "r").read().split("\n")

LOGO()
OPTIONS()

#! -----------------------------------------------------------------------------------------------------------------

#! Fuzzing URL Main Function
def FUZZ_URL_DIRECTORY(_KEY):
	global _REQUEST
	global _URI
	global _WORDLIST
	global _FOLLOW_REDIRECTS
	global _TIMEOUT
	global _THREADS
	global _SCODES
	global _DATA
	global _PROXY
	global _OUTPUT
	global _HEADER
	# SETUP FINAL URL
	if _KEY == "":
		pass
	else:
		if _URI[-1] == "/": _URI = _URI[: -1]
		if _KEY[0] == "/": _KEY = _KEY[1:]
		_URL_ = _URI + "/" + _KEY
		# REQUEST DETAILS
		if _HEADER == "None":
			headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0"}
		else:
			headers = {}
			A = open(_HEADER, "r").read().split("\n")
			for aheader in A:
				if aheader == "": pass
				else:
					H_Name, H_Value = aheader.split(": ")
					headers[H_Name] = H_Value
		while 1:
			try:
				#! REQUEST IF FUNCTION
				REQ = requests.Session()
				REQ.headers = headers
				REQ.verify  = False
				REQ.timeout = _TIMEOUT
				rand_proxy = ""
				if _FOLLOW_REDIRECTS == "None": REQ.allow_redirects = False
				else:
					if _FOLLOW_REDIRECTS == "y": REQ.allow_redirects = True
					else: REQ.allow_redirects = False
				if _DATA == "None": pass
				else: REQ.data = str(args.data)
				if _PROXY == "None": pass
				else:
					rand_proxy = random.choice(_PROXY)
					if str(args.proxies_type) == "http" or str(args.proxies_type) == "HTTP": REQ.proxies = {'http': rand_proxy, 'https': str(args.proxies_type)+'://'+rand_proxy}
					else: REQ.proxies = {'http': rand_proxy, 'https': str(args.proxies_type)+'://'+rand_proxy}

				if str(args.method) == "None" or str(args.method) == "GET": r = REQ.get(_URL_)
				elif str(args.method) == "POST": r = REQ.post(_URL_)
				elif str(args.method) == "PUT": r = REQ.put(_URL_)
				elif str(args.method) == "DELETE": r = REQ.delete(_URL_)
				elif str(args.method) == "OPTIONS": r = REQ.options(_URL_)
				elif str(args.method) == "PATCH": r = REQ.patch(_URL_)
				else: r = REQ.get(_URL_)

				if str(r.status_code) in _SCODES:
					if _FILTER == "None":
						print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ]")
						if _OUTPUT == "None": pass
						else:
							file = open(_OUTPUT, "a+")
							file.write(str(r.status_code) + " : " + _URL_ + "\n")
							file.close()
					else:
						if "length:" in _FILTER:
							wanted_length = _FILTER.split("length:")[1]
							if len(r.content) > int(wanted_length):
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Length] : "+Fore.RED+str(len(r.content))+Fore.YELLOW+" ]")
								pass
							else:
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Length] : "+Fore.GREEN+str(len(r.content))+Fore.YELLOW+" ]")
								if _OUTPUT == "None": pass
								else:
									file = open(_OUTPUT, "a+")
									file.write(str(r.status_code) + " : " + _URL_ + "\n")
									file.close()
						elif "lines:" in _FILTER:
							wanted_lines = _FILTER.split("lines:")[1]
							if len(str(r.content).split("\\r\\n")) > int(wanted_lines):
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Lines] : "+Fore.RED+str(len(str(r.content).split("\\r\\n")))+Fore.YELLOW+" ]")
								pass
							else:
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Lines] : "+Fore.GREEN+str(len(str(r.content).split("\\r\\n")))+Fore.YELLOW+" ]")
								if _OUTPUT == "None": pass
								else:
									file = open(_OUTPUT, "a+")
									file.write(str(r.status_code) + " : " + _URL_ + "\n")
									file.close()
						elif "word:" in _FILTER:
							wanted_word = _FILTER.split("word:")[1]
							if wanted_word in r.content:
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Word] : "+Fore.GREEN+wanted_word+Fore.YELLOW+" ]")
								if _OUTPUT == "None": pass
								else:
									file = open(_OUTPUT, "a+")
									file.write(str(r.status_code) + " : " + _URL_ + "\n")
									file.close()
							else:
								print("\t "+Fore.YELLOW+"[ "+Fore.GREEN+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(r.content))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]"+Fore.YELLOW+"\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ] [ Filter[Word] : "+Fore.GREEN+wanted_word+Fore.YELLOW+" ]")
						else:
							print("?")
							quit()
				else:
					print("\t "+Fore.YELLOW+"[ "+Fore.RED+str(r.status_code)+Fore.YELLOW+" ] "+Fore.CYAN+" \t Length: "+Fore.YELLOW+str(len(_URL_))+Fore.CYAN+", Line: "+Fore.YELLOW+str(len(str(r.content).split("\\r\\n")))+"\t [ "+Fore.CYAN+_URL_+Fore.YELLOW+" ]\t [ "+Fore.CYAN+rand_proxy+Fore.YELLOW+" ]")
				break
			except:
				pass

#! -----------------------------------------------------------------------------------------------------------------

#! Final Running Process
#! -----------------------

#for _Q in open(str(args.wordlist), "r").read().split("\n"):
#	if _Q == "": pass
#	else: FUZZ_URL_DIRECTORY(_Q)

_STARTER = open(str(args.wordlist), "r").read().split("\n")

def main():
	pool = ThreadPool(_THREADS)
	try:
		results = pool.map(FUZZ_URL_DIRECTORY , _STARTER)
		pool.close()
		pool.join()
	except KeyboardInterrupt:
		print("Exiting...")
		sys.exit(0)

main()

print("\n\n")


