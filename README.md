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
usage: Qiyana.py [-h] [-u URL] [-w WORDLIST] [-m METHOD] [-d DATA] [-f FOLLOW] [-x TIMEOUT] [-t THREADS] [-H HEADER] [-F FILTER] [-o OUTPUT] [-p PROXIES] [-pp PROXIES_TYPE] [-s STATUS_CODES]

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
  -x TIMEOUT, --timeout TIMEOUT
                        this is asking for request timeout (default=10)
  -t THREADS, --threads THREADS
                        enter count of threads per second (default=20)
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
