from django.db import models
from bs4 import BeautifulSoup
import requests

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

def scrape_indeed():
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = 'https://www.indeed.co.uk/jobs?q=Junior+Software+Developer&l=Glasgow%2C+Glasgow'

    response = requests.get(url, headers, timeout=5)

    content = BeautifulSoup(response.content, "html.parser")

    jobArray = []

    for job in content.findAll('a', attrs={"class": 'jobtitle turnstileLink'}):

        link = job.get('href')

        job_url = "https://www.indeed.co.uk" + link

        job_response = requests.get(job_url, headers, timeout=5)

        job_content = BeautifulSoup(job_response.content, "html.parser")

        jobObject = {
            'title': job_content.find('h3', attrs={'class': 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text,
            'company': job_content.find('div', attrs={'class': 'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text,
            'location': job_content.find('span', attrs={'class': 'jobsearch-JobMetadataHeader-iconLabel'}).text,
            'description': job_content.find('div', attrs={'id': 'jobDescriptionText'}).text
        }

        jobArray.append(jobObject)

    return jobArray

def load_data():
    Job.objects.all().delete()
    for listing in scrape_indeed():
        job = Job(title = listing['title'], company=listing['company'], location= listing['location'], description= listing['description'])
        job.save()
