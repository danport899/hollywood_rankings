# Hollywood Ranker

# Overview
 This project was created to gather data through Python scraping and Flask App development in order to present accurate average ratings of film production companies and directors. This file will provide a step-by-step guide on how the app was accomplished.
 
 # Step 1
 The first necessary step was to gather the data I intended to collect from. I was after every movie which profited over $1,000,000 in the 21st Century
 
 ## Step 1.1
 Using store_page_links.py, I gathered a text file(page_links.txt) over all the necessary links needed from boxofficemojo.com
 ## Step 1.2
  With latest_scraper.py, the previously created text file was opened, then each link was run through a for loop. The for loop gathered the titles of all films fitting my parameters, and inserted them into movies.txt
