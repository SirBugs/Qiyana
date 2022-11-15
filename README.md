# Qiyana
Qiyana is a python tool for fuzzing directories,params,etc..
Created with Py3, By TWITTER@SirBagoza

# requirements:
requests

colorama

# Running:
* Viewing Help
```
python3 Qiyana.py -h / --help
```
* Normal Usage
```
python3 Qiyana.py -u <URL> -w <WORDLIST-PATH>
# --url=https://megacorpone.com/ --wordlist=/usr/Users/<USER>/Desktop/wordlist.txt
```
```
usage: Qiyana.py [-h] [-u URL] [-w WORDLIST] [-m METHOD] [-d DATA] [-f FOLLOW] [-U UNIQ] [-x TIMEOUT] [-t THREADS]
                 [-P ISPARAM] [-S ISSUB] [-H HEADER] [-F FILTER] [-o OUTPUT] [-p PROXIES] [-pp PROXIES_TYPE]
                 [-s STATUS_CODES]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     the URL of the pentesterlab without addons
  -w WORDLIST, --wordlist WORDLIST
                        cookies of your pentesterlab account
  -m METHOD, --method METHOD
                        this selects the request method
  -d DATA, --data DATA  use this if you send data with your request
  -f FOLLOW, --follow FOLLOW
                        asking if you wanna follow redirects or not [y/n]
  -U UNIQ, --uniq UNIQ  this switch if you wanna grap uniq content-size (non duplicated) [y/n]
  -x TIMEOUT, --timeout TIMEOUT
                        this is asking for request timeout (default=10)
  -t THREADS, --threads THREADS
                        enter count of threads per second (default=20)
  -P ISPARAM, --isparam ISPARAM
                        turn this on if you wanna fuzz param
  -S ISSUB, --issub ISSUB
                        turn this on if you wanna fuzz subdomains
  -H HEADER, --header HEADER
                        .txt file, if you wanna enter specific header into the request
  -F FILTER, --filter FILTER
                        this filter is checking your conditions [length:300/lines:50/word:success
  -o OUTPUT, --output OUTPUT
                        saving the output of the fuzzed paths/params
  -p PROXIES, --proxies PROXIES
                        .txt file, this if you wanna use proxies, Enter proxies file
  -pp PROXIES_TYPE, --proxies_type PROXIES_TYPE
                        this is the proxies type [http/socks4/socks5] ** HAVE TO BE SENT WITH PROXIES
  -s STATUS_CODES, --status_codes STATUS_CODES
                        if you wanna get more status codes send it (default=200,204,301,302,307,401,403,405,500)
```
# Seeing after running:
```
		 $$$$$$\  $$\                                         
		$$  __$$\ \__|                                        
		$$ /  $$ |$$\ $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\  
		$$ |  $$ |$$ |$$ |  $$ | \____$$\ $$  __$$\  \____$$\ 
		$$ |  $$ |$$ |$$ |  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |
		$$ $$\$$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$  __$$ |
		\$$$$$$ / $$ |\$$$$$$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |
		 \___$$$\ \__| \____$$ | \_______|\__|  \__| \_______|
		     \___|    $$\   $$ |                              
		              \$$$$$$  |                              
		               \______/                               
		 V 0.0.2

	 ====================================================================================================

	 [ ! ] 	Q_Method	 : <REQUEST-METHOD>
	 [ ! ] 	Q_URL		 : <URL>
	 [ ! ] 	Q_Worlist	 : <PATH> [ <LIST-LINES] ]
	 [ ! ] 	Q_Timeout	 : <TIMEOUT>
	 [ ! ] 	Q_Threads	 : <THREADS>
	 [ ! ] 	Q_Output	 : <OUTPUT-FILE>
	 [ ! ] 	Q_Header	 : <HEADERS-FILE>
	 [ ! ] 	Q_Targets	 : ['200', '204', '301', '302', '307', '401', '403', '405', '500']
	 [ ! ] 	Q_REDIRECTION	 : <FOLLOW-REDIRECTS]

	 ====================================================================================================

	 [WAR] This tool is for hunters and pentesters, Don't use it for anything else.
	 [WAR] Today's Advice: Never ask your gf/bestfiriend for nudes bro
	 [WAR] This is the first version of the tool and you may find problems or errors, contact me at @SirBagoza
	 [DOT] Once you run this tool, it's gonna start fuzzing the the directories in your wordlist path
	 [DOT] Check if you wanna save the output in a .txt file by adding (-o [file.txt)
	 [DOT] If you are looking for subdomains fuzzing use -S y
	 [DOT] If you gonna use params fuzzing enter the url like: https://<DOMAIN>/api.php? -P y
	 [DOT] If site keeps replying with 404/home source, Use -U y This grap NonDuplicated length
	 [DOT] To use the filters options run -F length-10 (or) -F lines-10 (or) 0F word-successful
	 [DOT] If you wanna use proxies, Make sure you are using (-p) and (-pp) together
	 [DOT] For submitting headers, Enter them in .txt file separated by new line\n

	 [INF] We all love the president @AbdelfattahElsisi cuz we are egyptians
	 [INF] Go find more projects/tools on GITHUB@SirBugs
	 [INF] Visit my TWITTER@SirBagoza HackerOne/BugCrowd@bugsv2 

	 [UPDATE] **UPDATE: This Version is V 0.0.2 [14/11/2022] 

	 ====================================================================================================
```
# Seutp:
* For manual installation, The tool link is: [Qiyana Github](https://github.com/SirBugs/Qiyana/)

* Installing with clone
```
git clone https://github.com/SirBugs/Qiyana.git
```
* Installing with SSH
```
git@github.com:SirBugs/Qiyana.git
```
* Installing the dependencies in a virtualenv
```
cd Qiyana
pip install -r requirements.txt
```

# Help:
* You can get wordlists from:
* [SecLists](https://github.com/danielmiessler/SecLists)
* [fuzz-](https://github.com/yige666/fuzz-)
* [fuzzing](https://github.com/SooLFaa/fuzzing)

# Version:
* Version 0.0.1 (13/11/2022) : Came Out <3
* Version 0.0.2 (14/11/2022) : Added Time, Parameters Fuzzing(Reflection), Faster, Uniq(NonDuplicated) Content Length <3


# About Me:
Visit My [@Twitter](https://twitter.com/SirBagoza), [@Github](https://github.com/SirBugs), [@Hackerone](https://hackerone.com/bugsv2?type=user)
