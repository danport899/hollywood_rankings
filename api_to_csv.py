import csv
import json
import requests
import time

movieList = []
api = "5cfce222"


openMovie = open('movies.txt','r')
readMovie = openMovie.readlines()
for line in readMovie:
    line = line.strip('\n')
    line = line.replace(" ","+")
    if "-" in line:
        line = line.replace("-",'')
    if ":" in line:
        line = line.replace(':','')
    if "Tyler Perry's" in line:
        line = line.strip("Tyler Perry's")
    movieList.append(line)

infoDictList = []
def get_movie_info(foobar):
    counter = 0
    for movie in movieList:
        year = ''
        if "(2018)" in movie:
            movie = movie.strip('+(2018)')
            year = "&y=2018"
        elif "(2017)" in movie:
            movie = movie.strip('+(2017)')
            year = "&y=2017"
        elif "(2016)" in movie:
            movie = movie.strip('+(2016)')
            year = "&y=2016"
        elif "(2015)" in movie:
            movie = movie.strip('+(2015)')
            year = "&y=2015"
        elif "(2014)" in movie:
            movie = movie.strip('+(2014)')
            year = "&y=2014"
        elif "(2013)" in movie:
            movie = movie.strip('+(2013)')
            year = "&y=2013"
        elif "(2012)" in movie:
            movie = movie.strip('+(2012)')
            year = "&y=2012"
        elif "(2011)" in movie:
            movie = movie.strip('+(2011)')
            year = "&y=2011"
        elif "(2010)" in movie:
            movie = movie.strip('+(2010)')
            year = "&y=2010"
        elif "(2009)" in movie:
            movie = movie.strip('+(2009)')
            year = "&y=2009"
        elif "(2008)" in movie:
            movie = movie.strip('+(2008)')
            year = "&y=2008"
        elif "(2007)" in movie:
            movie = movie.strip('+(2007)')
            year = "&y=2007"
        elif "(2006)" in movie:
            movie = movie.strip('+(2006)')
            year = "&y=2006"
        elif "(2005)" in movie:
            movie = movie.strip('+(2005)')
            year = "&y=2005"
        elif "(2004)" in movie:
            movie = movie.strip('+(2004)')
            year = "&y=2004"
        elif "(2003)" in movie:
            movie = movie.strip('+(2003)')
            year = "&y=2003"
        elif "(2002)" in movie:
            movie = movie.strip('+(2002)')
            year = "&y=2002"
        elif "(2001)" in movie:
            movie = movie.strip('+(2001)')
            year = "&y=2001"
        elif "(2000)" in movie:
            movie = movie.strip('+(2000)')
            year = "&y=2000"
        elif '(IMAX)' in movie:
            movie = movie.strip('(IMAX)')
        response = requests.get("http://www.omdbapi.com/?t=" + movie + "&apikey=" + api + "&type=movie" + year)
        data = response.content
        data_dict = json.loads(data)
        with open('movie_data.csv','a', newline='', encoding='utf8') as csvfile:
            keys = data_dict.keys()
            movieWriter = csv.DictWriter(csvfile,keys)
            if counter == 0:
               movieWriter.writeheader()
               counter += 1
            movieWriter.writerow(data_dict)
        infoDictList.append(data_dict)
    return infoDictList


print(get_movie_info('foobar'))
