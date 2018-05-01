from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import csv

target_year_list = [2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]
link_list= []
def get_all_links(foobar):
    number_list = [1,2,3,4,5,6,7,8,9,10]
    for year in target_year_list:
        for number in number_list:
            link = "http://www.boxofficemojo.com/yearly/chart/?page="+ str(number) + "&view=releasedate&view2=domestic&yr="+ str(year)+ "&p=.htm"
            html = urlopen(link)
            bsObj = BeautifulSoup(html, "html.parser")
            try:
                table_list = bsObj.findAll('table')
                movie_table = table_list[6].findAll('tr')
                link_list.append(link)
            except IndexError:
                break
    return link_list


print(get_all_links("foobar"))
