# Welcome to My First Scraper
***

## Task
We want to scrape a webpage, or even the html file of a downloaded page. The challenge is to find only the 
html elements of interest, use Beautiful soup html parsing library and code to output the scraped data to a readable
string such as a CSV string.  

## Description
First, researched the topic using a python book "automate boring stuff" and a youtube lesson to figure out how to scrape
and then several instructionals to learn to parse the output.  My program uses 4 functions: Request- downloads web pages'
html, Extract-returns items of interest from a given page, e.g. hyperlinks, Transform - returns formats data into a list of 
key:values, Format - returns a long string of readable plain text which can then be used many ways.    

## Installation
This progam can be run in an IDE or from a command line. It can be run using function calls, or without functions, in which
case the code needs a slight modification.

## Usage
Supply a url, requests.get means ping the webage for its html, extract has specific html
locations to grab the parts of the page we want and then it stores these in a list using zip and
list to limit the return list to 25 items only, storing it in pairs. Data makes the list of data 
pretty i.e. "developer" etc, format gets the data into a readable string.  
```
run it in the terminal by using python my_first_scraper.py 
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
