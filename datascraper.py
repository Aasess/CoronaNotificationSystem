import requests
from bs4 import BeautifulSoup
#loading the website and parsing using Beautifulsoup and lxml
def datascarpper():
    source = requests.get("https://kathmandupost.com/covid19").text   #sucessfully responded with 200
    soup = BeautifulSoup(source,'lxml')

    table = soup.select('tr')


    result_today = {} #dict
    for row in table:
        column = row.select('td')
        for each_item in column:
            result_today[column[0].text] = {
                "Confirmed" : column[1].text,
                "Death" : column[2].text,
                "Recovered" : column[3].text
            }
    return result_today