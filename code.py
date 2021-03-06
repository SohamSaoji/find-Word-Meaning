import subprocess
import sys
import requests
from bs4 import BeautifulSoup as B


word = input("Enter your word: ").strip().lower() or "great"
print(word)

url = "https://www.lexico.com/definition/"

# joining the url and word
links = "".join([url, word])

try:
    page = requests.get(links)
    
    # parsing the html information
    soup = B(page.content, "html.parser")

    # finding the information in span tag
    word_info = soup.find("span", class_="ind")
    
    # extracting the word information
    word_extr = word_info.get_text()
    
    hyp = "-"
    
    word_mean = " ".join([f"{word.title()}", hyp, word_extr])
    print(word_mean)

    # heading of example
    eg_head = soup.find_all("div", class_="ex")[0]
    # extracting the example information
    eg_extr = eg_head.get_text()
    eg = "\nEg -"
    
    eg_info = " ".join([eg, eg_extr])
    print(eg_info)
except:
    print("\nWord or example not found. Error 404")