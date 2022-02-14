import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
    url= 'https://www.linkedin.com/jobs/search/?keywords=software%20engineer&position=1&pageNum=0'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div',class_ = 'base-search-card__info')
    for item in divs:
        title = item.find('h3').text.strip()
        company = item.find('a', class_ ='hidden-nested-link').text.strip()
        location = item.find('span', class_='job-search-card__location').text.strip()

        job = {
            'title': title,
            'company': company,
            'location': location,
        }
        joblist.append(job)
    return

joblist = []

for i in range(0,30,10):
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')