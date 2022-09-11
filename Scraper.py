import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, search, id_search):
        self.search = search
        self.id_search = id_search
        self.searchPage = []

    def getListSearch(self):
        return self.searchPage

    # récupération des pages associées à la recherche
    def SearchPage(self, search, lastDate, dateNow, headers):
        page = requests.get("https://www.google.fr/search?q=" + search + "&source=lnt&tbs=cdr%3A1%2Ccd_min%3A" +
                            lastDate[1] + "%2F" + lastDate[2] + "%2F" + lastDate[0] + "%2Ccd_max%3A" +
                            dateNow[1] + "%2F" + dateNow[2] + "%2F" + dateNow[0] + "&tbm=", headers=headers).content
        soup = BeautifulSoup(page, "html.parser")
        for linkPage in soup.find_all("div", attrs={"class": "g"}):
            self.searchPage.append(linkPage.find_next("a").get("href"))

    def ContentPage(self):
        pass