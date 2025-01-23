from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.arsenal.com/results"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    
    scores= soup.find_all( class_ = "scores__score")
    

    arsenal = int(scores[0].text)
    oponent = int(scores[1].text)

    if arsenal == oponent:
        print("Učitel má špatnou náladu")
    class_home = scores[0].get("class")
    print(class_home)
if __name__ == "__main__":
    main()

