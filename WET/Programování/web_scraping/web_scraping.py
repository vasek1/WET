from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.trebesin.cz"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    paragraph = soup.p
    
    print(f"První odstavec na stránce je :{paragraph.text}")

    #all_p = soup.find_all("p")
    #for p in all_p:
    #    print(p.text)
    gym = soup.find(id = "favimagehover-title4")
    print(f"Název oboru je {gym.text}")
if __name__ == "__main__":
    main()
