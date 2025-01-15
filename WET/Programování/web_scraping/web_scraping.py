from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.trebesin.cz"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    paragraph = soup.p
    
    print(f"První odstavec na stránce je :{paragraph}")
if __name__ == "__main__":
    main()
