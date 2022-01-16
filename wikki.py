#Made by Ja'Crispy4939, feel free to use this code but please dont just rename it as yours. E

import bs4
import bs4 as BeautifulSoup
import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import time
import os
import time
import lxml
import os
import lxml.html

def main():
    import lxml
    Article = input("What article do you want to find: ")

    s = requests.session()
    page = s.get("https://en.wikipedia.org/wiki/" + Article + "")
    lxml = lxml.html.fromstring(page.content)
    if page is not None:
        page = bs4.BeautifulSoup(page.text, 'html.parser')

        firstpara = lxml.xpath("""/html/body/div[3]/div[3]/div[5]/div[1]/p[3]/text()""")
        paragraphs = page.select("p")

        print(".")
        time.sleep(.5)
        print("..")
        time.sleep(.5)
        print("...")
        time.sleep(.5)
        os.system('cls')
        
        print(firstpara)
        intro = '\n'.join([firstpara.text for firstpara in paragraphs[0:5]])
        print (intro)

        if firstpara == []:
            firstpara = "Couldnt find a wikki page"
            print(firstpara)
            time.sleep(5)
            again()
        again()

def again():
    another = input("Would you like to search another topic(y/n): ")
    if another == "y":
        os.system('cls')
        main()
    if another == "n":
        print("Goodbye")
        time.sleep(3)
        exit()
    else:
        print("Please say y or n")
        time.sleep(4)
        os.system('cls')
        again()


main()