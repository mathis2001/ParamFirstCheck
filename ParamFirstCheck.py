#!/usr/bin/env python3

import sys

class bcolors:
	SQLColor = '\033[92m'
	RCEColor = '\033[93m'
	LFIColor = '\033[91m'
	RESET = '\033[0m'
	OpenRedColor = '\033[94m'

def Search(list, emptylist, line):
	for param in list:
		if param in line:
			emptylist.append(line)
	return emptylist


def main():
	SqlParam = ["id=","page=","dir=","search=","category=","class=","file=","url=","news=","item=","menu=","lang=","name=","ref=","title=","view=","topic=","thread=","type=","data=","form=","join=","main=","nav=","region="] 
	RceParam = ["cmd=", "exec=","command=","execute=","ping=","query=","jump=","code=","reg=","do=","func=","arg=","option=","load=","process=","step=","read=","function=","req=","feature=","exe=","module=","payload=","run=","print="]
	LfiParam = ["cat=", "dir=","action=","board=","date=","detail=","file=","download=","path=","folder=","prefix=","include=","page=","inc=","locate=","show=","doc=","site=","type=","view=","content=","document=","layout=","mod=","conf="]
	OpenParam = ["next=", "url=", "target=","rurl=","dest=","destination=","redir=","redirect_url=","redirect_uri=","redirect=","/redirect/","cgi-bin/redirect","/out/","view=","/login?to=","image_url=","go=","return=","returnTo=","return_to=","checkout_url=","continue=","return_path="]
	sqlist= []
	rcelist = []
	lfilist = []
	openred = []
	
	if len(sys.argv)>5:
		print(bcolors.LFIColor+"[!] "+bcolors.RESET+"too much arguments")
		sys.exit(1)
	elif len(sys.argv)<2:
		print(bcolors.LFIColor+"[!] "+bcolors.RESET+"No argument given")
		sys.exit(1)
	
	for line in sys.stdin:
		sql = Search(SqlParam, sqlist, line)
		rce = Search(RceParam, rcelist, line)
		lfi = Search(LfiParam, lfilist, line)
		open = Search(OpenParam, openred, line)
	

	if '--sql' in sys.argv:
		print(bcolors.SQLColor+"In Top 25 SQL:\n"+bcolors.RESET)
		for url in sql:
			print(url)
	else:
		pass

	print("------------------------------------------")

	if '--rce' in sys.argv:
		print(bcolors.RCEColor+"In Top 25 RCE:\n"+bcolors.RESET)
		for url in rce:
			print(url)
	else:
		pass

	print("------------------------------------------")
	
	if '--lfi' in sys.argv:
		print(bcolors.LFIColor+"In Top 25 LFI:\n"+bcolors.RESET)
		for url in lfi:
			print(url)
	else:
		pass
	print("------------------------------------------")
	
	if '--open-redirect' in sys.argv:
		print(bcolors.OpenRedColor+"In Top Open Redirect:\n"+bcolors.RESET)
		for url in open:
			print(url)
	else:
		pass

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(bcolors.LFIColor+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.OpenRedColor+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
	       	print(bcolors.LFIColor+"[!] "+bcolors.RESET+"Script canceled.")			

