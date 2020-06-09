import requests
import re
from termcolor import colored
import argparse

def start():
	print(colored("                  _  ____________ __________ ",'cyan'))
	print(colored("                 | |/ / ___/ ___// ____/ __ \\ ",'cyan'))
	print(colored("                 |   /\\__ \\\__ \\/ __/ / /_/ /",'cyan'))
	print(colored("                /   |___/ /__/ / /___/ _, _/ ",'cyan'))
	print(colored("               /_/|_/____/____/_____/_/ |_|  ",'cyan'))
	print(colored("                                XSS CHECKER  ",'cyan'))
	print("")
	print(colored("#====================================================================#", 'yellow'))
	print(colored("#|||||||||||||||||||||| Develop by MR_VILLAIN |||||||||||||||||||||||#", 'yellow'))
	print(colored("######################## Twitter:@K_m_tanvir #########################", 'yellow'))
	print(colored("#--------------------------------------------------------------------#", 'yellow'))
	print(colored("#                     XSS REFLECTION Checker V.1.0                   #", 'yellow'))
	print(colored("#====================================================================#", 'yellow'))


start()

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target url', dest='url')
parser.add_argument('-urls', help='target urls', dest='url_file')
args = parser.parse_args()

urle = args.url
urls = args.url_file


open("validxss.txt" , 'w').write("all valids xss here.....:" + "\n")
#urle = input("ENTER YOUR TERGET SITE :")
if urle:
	try:
		paramz = urle.split("?")
		refs = []
		withoutvalues = []
		for param in paramz:
		    print(param)
		    if "http://" in param or "https://" in param:
		        print("finding XSS")
		    else:
		        print(param)
		        refs.append(param)
		        cool = re.sub("=.*" , "" , param)
		        print(cool)
		        withoutvalues.append(cool)
		        

		xsses = open("xss.txt" , 'r').read().splitlines()


		for xss in xsses:
		    print(xss)
		    pauz = paramz[0] + "?" + withoutvalues[0] + "=" + xss
		    print(pauz)
		    resp = requests.get(pauz)
		    codz = resp.status_code
		    print(codz)
		    if codz == 200:
		        wow = xss in resp.text
		        print(wow)
		        if wow == False:
		            print("......")
		        else:
		            print(colored("XSS_Found", 'green'))
		            open("validxss.txt" , 'a').write(pauz + "\n")            
		        print(".....")
	except requests.exceptions.ConnectionError:
		pass
		    
if urls:
	file = open(urls, "r")
	for line in file:
		word = line.strip() 
		try:
			paramz = word.split("?")
			refs = []
			withoutvalues = []
			for param in paramz:
			    print(param)
			    if "http://" in param or "https://" in param:
			        print("finding XSS")
			    else:
			        print(param)
			        refs.append(param)
			        cool = re.sub("=.*" , "" , param)
			        print(cool)
			        withoutvalues.append(cool)
			        

			xsses = open("xss.txt" , 'r').read().splitlines()


			for xss in xsses:
			    print(xss)
			    pauz = paramz[0] + "?" + withoutvalues[0] + "=" + xss
			    print(pauz)
			    resp = requests.get(pauz)
			    codz = resp.status_code
			    print(codz)
			    if codz == 200:
			        wow = xss in resp.text
			        print(wow)
			        if wow == False:
			            print("......")
			        else:
			            print(colored("XSS_Found", 'green'))
			            open("validxss.txt" , 'a').write(pauz + "\n")            
			        print(".....")
		except requests.exceptions.ConnectionError:
			pass
