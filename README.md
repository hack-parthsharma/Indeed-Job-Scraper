# Indeed Job Scraper

Majority of the code credited to this repo: https://github.com/tarunsinghal92/indeedscrapperlatest

Simple and updated python script that gets job data for cities and job titles.

You may not have all the dependencies that are needed for the scripts to work so make sure to run the following command as the necessary ones are mentioned in the requirements.txt. Make sure that you are running on Python3.
```
pip3 install -r requirements.txt
```

This repo isn't configurable with another file so queries, cities, and number of jobs to be scraped should be modified in the scraper.py source code.

To change results per city modify the following:
```
max_results_per_city = 100
```

To add jobs or change the existing set, modify the following:
```
job_set = ['software+engineer']
```
NOTE: make sure to add the '+' between separate words.

To add cities or change the existing set, modify the following:
```
city_set = ['Chicago']
```
NOTE: there is a full_city_set which has a bunch of major cities and the proper formatting required.

To run the main logic of the scraper:
```
python3 scraper.py
```

The result should be in a properly named CSV file.