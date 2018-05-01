from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import csv

#this opens the csv file written by the movie_data.py file, and converts it into a list
linkList = []
openUrl = open('page_links.txt','r')
readUrl = openUrl.readlines()
for line in readUrl:
    line = line.strip('\n')
    linkList.append(line)


def get_movie_titles(linkList):
    gross_list = []
    movie_list = []
    for link in linkList:
        html = urlopen(link)
        bsObj = BeautifulSoup(html, "html.parser")
        table_list = bsObj.findAll('table')
        movie_table = table_list[6].findAll('tr')
        del movie_table[0:2]
        movie_table = movie_table[:-4]
        for tr in movie_table:
            td_list = tr.findAll("td")
            gross = td_list[3].get_text().strip('$').replace(',', '')
            gross = int(gross)
            #this if statement filters out movies that have made less that $1,000,000
            if gross >= 1000000:
                movie_link = tr.find('a').get_text()
                if movie_link not in movie_list:
                    movie_list.append(movie_link)
            else:
                break
    #this writes all 4,000+ movies into a txt file: movies.txt
    for movie in movie_list:
        addMovie = open('movies.txt','a')
        addMovie.write(movie + "\n")
    addMovie.close()
    return movie_list

movies = get_movie_titles(linkList)
print(movies)
