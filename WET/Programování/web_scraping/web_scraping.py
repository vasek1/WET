from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.trebesin.cz"
    response = requests.get(url)
    soup = BeautifulSoup(html,"html.parser")