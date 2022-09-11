from datetime import datetime
from bs4 import BeautifulSoup
import requests
import mysql.connector
from Scraper import Scraper
from ScraperBDD import ScraperBdd

# récupération des recherches dans le fichier link.csv
with open("link.csv", "r") as link:
    search = link.read().split(";")
    print(search)

headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0','connection': 'keep-alive'}


# récupération de la date actuelle
enrgDate = datetime.now()
dateNow = enrgDate.date().isoformat()

# récupération de la dernière date d'utilisation
fileDate = open("lastDate.txt", "r")
lastDate = fileDate.read().split('-')
fileDate.close()

"""# écriture de la date actuelle dans le fichier lors de l'activation du script
fileDate = open("lastDate.txt", "w")
fileDate.write(dateNow)
fileDate.close()"""

print(dateNow.split("-"))
print(lastDate)


"""host = input("host : ")
user = input("user : ")
password = input("password : ")
database = input("database : ")"""

"""connection_params = {
    'host': host,
    'user': user,
    'password': password,
    'database': database,
}"""

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "",
}
cnx = mysql.connector.connect(**connection_params)
cursor = cnx.cursor()

test = ScraperBdd(cnx)

d = {}

# récupération de la recherche et son id en bdd pour voir si la recherche n'est pas deja faite
for line in search:
    print(line)
    valSearch = line.replace("\n", "")
    try:
        res = test.SelectDb(valSearch)
        for j in res:
            d[valSearch] = j
    except:
        res = test.InsertDb(valSearch)
        for j in res:
            d[valSearch] = j

    searchObject = Scraper(valSearch, d.get(valSearch), )
    searchObject.SearchPage(valSearch, lastDate, dateNow, headers)
    print(searchObject.getListSearch())

print(d)





