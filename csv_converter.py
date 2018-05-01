import csv
import json
from ast import literal_eval
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from ast import literal_eval


def production_to_dict(filename):
    datafile = open(filename, newline='', encoding = 'utf8')
    my_reader = csv.DictReader(datafile)
    list_of_productions = []
    for row in my_reader:
        list_of_productions.append( dict(row) )
    datafile.close()
    return list_of_productions

def get_company_ratings(list_of_dicts):
    production_list = []
    company_list = []
    counter = 0
    num = 1
    for data in list_of_dicts:
        movieTitle = data['Title'].replace(" ","_")
        production_names = literal_eval(data['Production'])
        for production in production_names:
            if production not in production_list:
                production_list.append(production)
    for company in production_list:
        imdb_list = []
        appearances = 0
        rotten_tomatoes_list = []
        metacritic_list = []
        imdb_score = 0
        rotten_tomatoes_score = 0
        metacritic_score = 0
        for data in list_of_dicts:
            for production in literal_eval(data['Production']):
                if company == production:
                    appearances += 1
                    try:
                        ratings = data['Ratings']
                        ratings_clean = literal_eval(ratings)
                        for rating in ratings_clean:
                            if rating['Source'] == 'Internet Movie Database':
                                imdb_list.append (float(rating['Value'].strip('/10')))
                            elif rating['Source'] == 'Rotten Tomatoes':
                                rotten_tomatoes_list.append( int(rating['Value'].strip('%')))
                            elif rating['Source'] == 'Metacritic':
                                try:
                                    metacritic_list.append(int(rating['Value'].strip('/100')))
                                except ValueError:
                                    pass
                    except SyntaxError:
                        pass
                    except ValueError:
                        pass
        for score in imdb_list:
            imdb_score += score
        for score in rotten_tomatoes_list:
            rotten_tomatoes_score += score
        for score in metacritic_list:
            metacritic_score += score
        if len(imdb_list) != 0:
            imdb_avg = (imdb_score/len(imdb_list))
            imdb_avg = round(imdb_avg, 1)

        else:
            imdb_avg = 'N/A'
        if len(rotten_tomatoes_list) != 0:
            rotten_tomatoes_avg = (rotten_tomatoes_score/len(rotten_tomatoes_list))
            rotten_tomatoes_avg = round(rotten_tomatoes_avg)
        else:
            rotten_tomatoes_avg = 'N/A'
        if len(metacritic_list) != 0:
            metacritic_avg = (metacritic_score/len(metacritic_list))
            metacritic_avg = round(metacritic_avg)
        else:
            metacritic_avg = "N/A"
        with open('production_company_data.csv','a', newline='', encoding='utf8') as csvfile:
            productionWriter = csv.writer(csvfile)
            if counter == 0:
                productionWriter.writerow(['ID',"Company Name","IMDB Average", "Rotten Tomatoes Average", "Metacritic Average", "Number of Movies"])
            productionWriter.writerow([num,company,str(imdb_avg)+"/10",str(rotten_tomatoes_avg)+"%",str(metacritic_avg)+'/100',appearances])
            counter += 1
            num += 1
    return company_list

def director_to_dict(filename):
    datafile = open(filename, newline='', encoding = 'utf8')
    my_reader = csv.DictReader(datafile)
    list_of_directors = []
    for row in my_reader:
        list_of_directors.append( dict(row) )
    datafile.close()
    return list_of_directors

def get_director_ratings (list_of_dicts):
    director_list = []
    counter = 0
    num = 1
    for data in list_of_dicts:
        director = data['Director']
        try:
            director_coop = director.split(',')
            for director in director_coop:
                if "(co-director)" in director:
                    director = director.strip('(co-director)')
                if director not in director_list:
                    director_list.append(director)
        except AttributeError:
            pass

    if director not in director_list and direcor != "N/A":
            director_list.append(director)
    for director in director_list:
        appearances = 0
        imdb_list = []
        rotten_tomatoes_list = []
        metacritic_list = []
        imdb_score = 0
        rotten_tomatoes_score = 0
        metacritic_score = 0
        for data in list_of_dicts:
            if director in data['Director']:
                appearances += 1
                try:
                    ratings = data['Ratings']
                    ratings_clean = literal_eval(ratings)
                    for rating in ratings_clean:
                        if rating['Source'] == 'Internet Movie Database':
                            imdb_list.append (float(rating['Value'].strip('/10')))
                        elif rating['Source'] == 'Rotten Tomatoes':
                            rotten_tomatoes_list.append( int(rating['Value'].strip('%')))
                        elif rating['Source'] == 'Metacritic':
                            try:
                                metacritic_list.append(int(rating['Value'].strip('/100')))
                            except ValueError:
                                pass
                except SyntaxError:
                    pass
                except ValueError:
                    pass
        for score in imdb_list:
            imdb_score += score
        for score in rotten_tomatoes_list:
            rotten_tomatoes_score += score
        for score in metacritic_list:
            metacritic_score += score
        if len(imdb_list) != 0:
            imdb_avg = (imdb_score/len(imdb_list))
            imdb_avg = round(imdb_avg, 1)
        else:
            imdb_avg = 'N/A'
        if len(rotten_tomatoes_list) != 0:
            rotten_tomatoes_avg = (rotten_tomatoes_score/len(rotten_tomatoes_list))
            rotten_tomatoes_avg = round(rotten_tomatoes_avg)
        else:
            rotten_tomatoes_avg = 'N/A'
        if len(metacritic_list) != 0:
            metacritic_avg = (metacritic_score/len(metacritic_list))
            metacritic_avg = round(metacritic_avg)
        else:
            metacritic_avg = "N/A"
        with open('director_data.csv','a', newline='', encoding='utf8') as csvfile:
            directorWriter = csv.writer(csvfile)
            if counter == 0:
                directorWriter.writerow(["ID","Director Name","IMDB Average", "Rotten Tomatoes Average", "Metacritic Average", "Number of Movies"])
            directorWriter.writerow([num,director,str(imdb_avg)+"/10",str(rotten_tomatoes_avg)+"%",str(metacritic_avg)+'/100',appearances])
            counter += 1
            num += 1

    return director_list

director_info_list = (director_to_dict("movie_data.csv"))
production_info_list = (production_to_dict("production_companies.csv"))
company_list = get_company_ratings(production_info_list)
director_list = get_director_ratings(director_info_list)
print(company_list)
print(director_list)
