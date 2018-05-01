from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import csv
import json
import requests

#this function gathers the links of every page that holds every movie between 2018 and 2000
def get_all_links(foobar):
    #this is inserted into url
    target_year_list = [2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2002,2001,2000]
    link_list= []
    #this is an arbitrary list of numbers meant to be inserted into the pages of each movie. No year has more than 10 pages
    number_list = [1,2,3,4,5,6,7,8,9,10]
    for year in target_year_list:
        for number in number_list:
            link = "http://www.boxofficemojo.com/yearly/chart/?page="+ str(number) + "&view=releasedate&view2=domestic&yr="+ str(year)+ "&p=.htm"
            html = urlopen(link)
            bsObj = BeautifulSoup(html, "html.parser")
            #this try/except assures that the pages which are being tested actually exist, after it fails, it moves on to the next year's pages.
            try:
                table_list = bsObj.findAll('table')
                movie_table = table_list[6].findAll('tr')
                link_list.append(link)
            except IndexError:
                break
        time.sleep(2)
    #this writes all the existing links into a txt file
        for url in link_list:
            addUrl = open('page_links.txt','a')
            addUrl.write(url + "\n")
        addUrl.close()
    return link_list

print(get_all_links('foobar'))
