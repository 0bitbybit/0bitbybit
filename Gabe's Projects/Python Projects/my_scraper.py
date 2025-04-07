#Gabe Jasso
"""This program is a basic web scraper using Beautiful Soup v.4 library (parses HTML/XML). Web scraping is downloading then
processing content from the web. This program can also scrape downloaded files offline """

import requests #library to get and send data to webpages (servers) or APIs
from bs4 import BeautifulSoup #scraping tool for parsing HTML and XML
#from itertools import chain

url = "https://github.com/trending"

def request_github_trending(url): #enter https://github.com/trending
    global page
    page = requests.get(url)
    return requests.get(url)
    return page

def extract(page):

   # global data
    header = "h1"
    
    if "github" in url: #checks if substring is in a given string
        header = "h2"
        print("Yes! Github in the string")
    
    soup = BeautifulSoup(page.text, 'html.parser')
    #data = soup.findAll("article")

    r = soup.findAll(header, attrs={"class":"h3 lh-condensed"}, limit=25) #notice we put h1 with was used in older html
    s = soup.findAll("span", attrs={"class":"d-inline-block float-sm-right"}, limit=25)
    
    #data = repo_link + stars_link
    #print(len(data))
    #return list(chain(repo_link, stars_link))
    #dev_link = soup.findAll("span", attrs={"class": "text-normal"})
    #print(len(list(zip(r,s)))
    return list(zip(r,s))

def transform(data):

    array_of_dict = []
    #print(x)
    #print(len(repo_link))
    #print(len(stars_link))

    for i in data:
        
        d = i[0].getText().strip().split()
        s = i[1].getText().strip().split()
        
        #del z[1:] #removes xtra text from stars
        #del r[1:2]  #removes xtra text from repo_link, 1:2
        #k = ' '.join(z)
         # make a dictionary
        #array_of_dict.append(p)  #my_list append each iteration
        array_of_dict.append({"developer":d[0], "repository_name":d[2], "nbr_stars":s[0]})
    #return(array_of_dict)
        #print(array_of_dict)
    return array_of_dict
    #print(array_of_dict)
    #, sep='\n'
    

def format(array_of_dict):
    
    list_of_dicts = array_of_dict

    # Method 1: Using a Loop
    result_string = ''
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            result_string += f"{key}: {value}, "
    result_string = result_string.rstrip(', ')
 
    #print(result_string)
    return result_string
    
request_github_trending(url)
data = extract(page)
#print(data)
array_of_dict = transform(data)
print(array_of_dict)
