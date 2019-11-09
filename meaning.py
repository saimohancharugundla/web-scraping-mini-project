import requests
from bs4 import BeautifulSoup as bs
from termcolor import colored
i="y"
while i=='y':
	try:
		word=input("Word:")
		headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		url=requests.get("https://dictionary.cambridge.org/dictionary/english/{}".format(word),headers=headers)
		total_content=url.content
		soup=bs(total_content,"html.parser")
		word=soup.find("span",attrs={"class":"hw dhw"}).text
		pos=soup.find("div",attrs={"class":"posgram dpos-g hdib lmr-5"}).text
		phonetic=soup.find("span",attrs={"class":"ipa dipa lpr-2 lpl-1"}).text
		usage=[]
		meaning = soup.find("div",attrs={"class":"def ddef_d db"}).text
		print("\n")
		print(colored("WORD:","white"),word)
		print(colored("PARTS OF SPEECH:","white"),pos)
		print(colored("PHONETIC DESCRIPTION:","white"),phonetic+"\n")
	
		print(colored("Meaning:","white"))
		print(meaning)
		print("\n")
		print(colored('Lets see its usage!!\n\n','blue'))
		
		for j in soup.find_all("div",attrs={"class":"def-body ddef_b"}):
			use=(j.find("div",attrs={"class":"examp dexamp"})).text.replace("\n"," ")
			usage.append(use)
		for k in usage:
			print(k)
		print("\n\n")
		print(colored("NOTE!","red"),"For future reference we have stored this word.")
		f=open("wordlist.txt","a+")
		f.write("word:"+word+"\n"+"meaning:"+meaning+"\n"+"usage:"+"\n")
		for x in usage:
			f.write(x+"\n")
		f.write("\n\n")
		f.close()
	except AttributeError:
		print("Sorry!I dont find the word")
	except requests.exceptions.ConnectionError:
		print("It seems your connection is too bad or no connection!!")
	i=input("Do you want another [y/n]:")	
