# Hollywood Ranker

## Overview
 This project was created to gather data through Python scraping and Flask App development in order to present accurate average ratings of film production companies and directors. This file will provide a step-by-step guide on how the app was accomplished.
 
 ## Step 1: The Title Scraper
 The first necessary step was to gather the data I intended to collect from. I was after every movie which profited over $1,000,000 in the 21st Century
 
 ### Step 1.1
 Using **store_page_links.py**, I gathered the text file **page_links.txt** over all the necessary links needed from boxofficemojo.com
 
 ### Step 1.2
  With **latest_movies_scraper.py**, the previously created text file was opened, then each link was run through a for loop. The for loop gathered the titles of all films fitting my parameters, and inserted them into **movies.txt**
 
 ## Step 2: Data Collection
 With the text file containing a list of all the movies, I needed to gather as much information on each title as I could gather. This included ratings, directors, production companies, genres, release years, etc.
  
### Step 2.1
Using **api_to_csv.py**, I accessed the OMDB Database API, which returned json files containing the relevant information. These files were then converted into dictionaries, and appened to the csv file **movie_data.csv**

### Step 2.2
However, while most of the API's data was correct, the production company names were inconsistent. For example, some films were produced by the string "20th Century Fox" whereas other were assigned as "Twentieth Century Fox."  Other companies were just mispelled. This would have severely skewed the data as ratings would be split and averages would be gathered unevenly. As a result, I had to build a scraper, **production_scraper**, to take the titles from **movie_data.csv** and insert them into the scraper, which ran the titles through Wikipedia and gathered consistent production names from each page and insert them into **production_companies.csv**

### Step 2.3
 Now, with all necessary and accurate data on each title, **csv_converter.py** gathered and averaged together the scores,
#### Company Ratings
 Production company ratings were averaged by gathering all scores of movies made by each production company in **production_companies.csv** then dividing by the number of movies with those scores. This data was inserted into **production_company_data.csv**
 
 #### Director Ratings
 The director ratings file was built in a similar way, except data was gathered from **movie_data.csv** and placed into **director_data.csv**
 
 ## Step 3: The Flask App
 
 ### Step 3.1
  The Flask app itself was built in **ranker.py** which loaded the data from all csv files and loaded them through the templates under the templates folder
  
 ##### Search 
   The ability to search was made possible by Flask_wtf, which looped through all the data in the csv files, and gathered the relevant info based on the user's input
