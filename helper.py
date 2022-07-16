import requests
from bs4 import BeautifulSoup
# Based on this: https://github.com/tarunsinghal92/indeedscrapperlatest

# get soup object
def get_soup(text):
    return BeautifulSoup(text, "lxml", from_encoding="utf-8")


# extract company
def extract_company(div): 
    company = div.find_all(name="span", attrs={"class":"company"})
    if len(company) > 0:
        for b in company:
            return (b.text.strip())
    else:
        sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
        for span in sec_try:
            return (span.text.strip())
    return 'NOT_FOUND'


# extract job salary
def extract_salary(div): 
    try:
        div_two = div.find(name='div', attrs={'class':'salarySnippet holisticSalary'})
        div_three = div_two.find('span', {'class':'salaryText'})
        return div_three.text.strip()
    except:
        return ('NOT_FOUND')
    return 'NOT_FOUND'


# extract job location
def extract_location(div):
    for divs in div.findAll('div', attrs={'class': 'location accessible-contrast-color-location'}):
        return (divs.text)
    return 'NOT_FOUND'


# extract job title
def extract_job_title(div):
    for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
        return (a['title'])
    return 'NOT_FOUND'


# extract jd summary
def extract_summary(div): 
    divs = div.findAll('div', attrs={'class': 'summary'})
    for div_1 in divs:
        return (div_1.text.strip())
    return 'NOT_FOUND'
 

# extract link of job description 
def extract_link(div): 
    for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
        return (a['href'])
    return 'NOT_FOUND'


# # extract date of job when it was posted
# def extract_date(div):
#     try:
#         spans = div.findAll('span', attrs={'class': 'date'})
#         for span in spans:
#             return (span.text.strip())
#     except:
#         return 'NOT_FOUND'
#     return 'NOT_FOUND'

# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get('http://www.indeed.com' + url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
        divs = soup.findAll('div', attrs={'class': 'jobsearch-jobDescriptionText'})
        for div in divs:
            return (div.text.strip())
    except:
        return 'NOT_FOUND'
    return 'NOT_FOUND'

# # write logs to file
# def write_logs(text):
#     # print(text + '\n')
#     f = open('log.txt','a')
#     f.truncate(0)
#     f.write(text + '\n')  
#     f.close()