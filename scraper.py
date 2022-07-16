import requests
import pandas as pd
import time 
import bs4
from bs4 import BeautifulSoup
from helper import *

# limit per city
max_results_per_city = 100

# Full set of cities
full_city_set = ['New+York', 'Chicago', 'San+Francisco', 'Austin', 'Seattle', 
        'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 
        'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington%2C+DC', 
        'Baltimore', 'El+Paso', 'Boston','Bethesda%2C+MD','Morrisville%2C+NC',
        'Palo+Alto%2C+CA','Redmond%2C+WA','Mountain+View%2C+CA','El+Segundo%2C+CA',
        'Herndon%2C+VA','Menlo+Park%2C+CA', 'Collegeville%2C+PA','Roseland%2C+NJ',
        'Princeton%2C+NJ','St.+Louis%2C+MO', 'Tampa%2C+FL','Cambridge%2C+MA',
        'Stamford%2C+CT','Santa+Clara%2C+CA','Detroit', 'Ann+Arbor%2C+MI', 
        'Des+Moines%2C+IA', 'Minneapolis%2C+MN','New+Orleans']

# db of city 
city_set = ['Chicago']

# job roles
job_set = ['software+engineer', 'data+scientist']

# file num
file = 1

print("Started scraping...")
# loop on all cities
for city in city_set:
    for job_qry in job_set:
        cnt = 0
        startTime = time.time()

        df = pd.DataFrame(columns = ['City', 'Job Query','Job Title', 'Company', 'Summary', 'Salary', 'URL Link', 'Job Description'])

        for start in range(0, max_results_per_city, 10):
            page = requests.get('http://www.indeed.com/jobs?q=' + job_qry +'&l=' + str(city) + '&start=' + str(start))
            time.sleep(1)  

            soup = get_soup(page.text)
            divs = soup.find_all(name="div", attrs={"class":"row"})
            
            if(len(divs) == 0):
                print("Could not get any source code for the query...")
                break
            # for all jobs on a page
            for div in divs: 
                num = (len(df) + 1) 
                cnt = cnt + 1

                job_post = [] 

                job_post.append(city)
                job_post.append(job_qry)
                job_post.append(extract_job_title(div))
                job_post.append(extract_company(div))
                job_post.append(extract_summary(div))
                job_post.append(extract_salary(div))
                link = extract_link(div)
                job_post.append('http://www.indeed.com' + link)
                job_post.append(extract_fulltext(link))

                df.loc[num] = job_post
                
                # write_logs(('Completed =>') + '\t' + city  + '\t' + job_qry + '\t' + str(cnt) + '\t' + str(start) + '\t' + str(time.time() - startTime) + '\t' + ('file_' + str(file)))

            #saving df as a local csv file 
            df.to_csv(str(city) + '_jobs_' + str(file) + '.csv', encoding='utf-8')
        
        # else:
        #     write_logs(('Skipped =>') + '\t' + city  + '\t' + job_qry + '\t' + str(-1) + '\t' + str(-1) + '\t' + str(time.time() - startTime) + '\t' + ('file_' + str(file)))
        
        # increment file
        file = file + 1
print("DONE")
