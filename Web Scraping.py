import requests
from bs4 import BeautifulSoup

def scrape_wttj_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs = []
    for job_elem in soup.find_all('div', class_='job'):
        title = job_elem.find('h2').text
        company = job_elem.find('div', class_='company').text
        location = job_elem.find('div', class_='location').text
        description = job_elem.find('div', class_='description').text
        jobs.append({'title': title, 'company': company, 'location': location, 'description': description})
    
    return jobs

def scrape_linkedin_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs = []
    for job_elem in soup.find_all('div', class_='job-card'):
        title = job_elem.find('h3').text
        company = job_elem.find('h4').text
        location = job_elem.find('span', class_='job-card__location').text
        description = job_elem.find('p', class_='job-card__snippet').text
        jobs.append({'title': title, 'company': company, 'location': location, 'description': description})
    
    return jobs

# Exemple d'utilisation
wttj_url = 'https://www.welcometothejungle.com/jobs'
linkedin_url = 'https://www.linkedin.com/jobs'
wttj_data = scrape_wttj_data(wttj_url)
linkedin_data = scrape_linkedin_data(linkedin_url)
print(wttj_data)
print(linkedin_data)
