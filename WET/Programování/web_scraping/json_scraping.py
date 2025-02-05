from bs4 import BeautifulSoup
import requests
import json

def main():
    url = "https://www.trebesin.cz"
    response = requests.get(url) # funkce get vezme hodnotu klíče z dictonary 
    soup = BeautifulSoup(response.content,"html.parser")
    list_p = []
    all_p = soup.find_all("p")
    for p in all_p:
       list_p.append(p.text)
    
    with open("trebesin.json", mode="w") as soubor:
     json.dump(list_p,soubor,indent=2)

if __name__ == "__main__":
    main()