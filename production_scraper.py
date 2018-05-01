from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import csv


def convert_to_dict(filename):
    datafile = open(filename, newline='', encoding = 'utf8')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = []
    studio_list = []
    fail_list = []
    for row in my_reader:
        list_of_dicts.append( dict(row) )
    datafile.close()
    counter = 0
    for data in list_of_dicts:
        movieTitle = data['Title'].replace(" ","_")
        row_list = []
        company_list_clean = []
        try:
            html = urlopen("https://en.wikipedia.org/wiki/"+ movieTitle)
            bsObj = BeautifulSoup(html, "html.parser")
            table = bsObj.find('table', {'class':'infobox vevent'})
            tr_list = table.findAll('tr')
        except (AttributeError, HTTPError, UnicodeEncodeError):
            try:
                html = urlopen("https://en.wikipedia.org/wiki/"+ movieTitle + "_(film)")
                bsObj = BeautifulSoup(html, "html.parser")
                table = bsObj.find('table', {'class':'infobox vevent'})
                tr_list = table.findAll('tr')
            except (AttributeError, HTTPError, UnicodeEncodeError):
                try:
                    html = urlopen("https://en.wikipedia.org/wiki/"+ movieTitle + "_(" + str(data['Year']) + "_film)")
                    bsObj = BeautifulSoup(html, "html.parser")
                    table = bsObj.find('table', {'class':'infobox vevent'})
                    tr_list = table.findAll('tr')
                except (AttributeError, HTTPError, UnicodeEncodeError):
                    tr_list = False
                    fail_list.append(data["Title"])
        if tr_list != False:
            try:
                for tr in tr_list:
                    row_list.append(str(tr))
                for tr in row_list:
                    if "Production<br/>" in tr:
                        production_row = tr
                        break
                x = row_list.index(production_row)
                studio = tr_list[x]
                company = studio.find('td')
                company_list = company.findAll('li')
                if len(company_list) == 0:
                    company = company.find('div').get_text(strip=True, separator='","')
                    if '[1]' in company:
                        company = company.replace('[1]','')
                    if '[2]' in company:
                        company = company.replace('[2]','')
                    if '[3]' in company:
                        company = company.replace('[3]','')
                    if '[4]' in company:
                        company = company.replace('[4]','')
                    company_list_clean.append(company)
                else:
                    for company in company_list:
                        company = company.get_text()
                        if '[1]' in company:
                            company = company.replace('[1]','')
                        if '[2]' in company:
                            company = company.replace('[2]','')
                        if '[3]' in company:
                            company = company.replace('[3]','')
                        if '[4]' in company:
                            company = company.replace('[4]','')
                        company_list_clean.append(company)
                with open('production_companies.csv',"a", newline = '', encoding = 'utf8') as csvfile:
                    productionWriter = csv.writer(csvfile)
                    if counter == 0:                    productionWriter.writerow(["Title","Ratings","Production"])
                    productionWriter.writerow([data["Title"],data["Ratings"],company_list_clean])
                    counter += 1

            except (ValueError, UnboundLocalError, AttributeError):
                fail_list.append(data["Title"])
                continue
        else:
            continue




    return fail_list



print (convert_to_dict('movie_data.csv'))
