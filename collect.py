import requests as r
from bs4 import BeautifulSoup
import os

class tcolor:
    green = '\33[32m'
    red = '\33[31m'

list = open("list.txt", "a+")

def collect():
    print("[+] Started Successfully")
    page = 1
    dork = input(" |  Enter Your Dork: ")
    paged = int(input(" |  Enter Page number: "))

    for k in range(0, paged):
        url = "https://www.bing.com/search?q="+dork+"&first="+str(page)+"&FORM=PORE"
        page += 10

        print(" |  Searching with Your details")

        headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                }

        print(" |  Testing is Search Engine Result Page is Online")

        test = r.get(url, headers=headers)
        soup = BeautifulSoup(test.text, 'html.parser')


        fr = soup.find("ol", {
            "id": "b_results"
            })

        fl = fr.find_all('li', {
            "class": "b_algo"
            })

        print(" |  Finding the Site\'s URL from the source")

        fa = []

        for links in fl:
            h_link = links.find('a').attrs['href']
            fa.append(h_link)

        for domains in fa:
            domains = domains.split('/')
            domains = domains[0]+'//'+domains[2]
            list.write(domains+'\n')
            print("[=>] "+tcolor.red+domains)

def banner():
    os.system("clear")
    print(tcolor.green+"###########################################################")
    print(tcolor.green+"#        Tool: Site Collector                             #")
    print(tcolor.green+"#        Author: Inad Islam                               #")
    print(tcolor.green+"#   A Mass Site Collector Written with PYTHON             #")
    print(tcolor.green+"###########################################################")


def mass():
    banner()
    collect()
    print("[—————–] Script Finished Successfully.Check list.txt")

mass()
