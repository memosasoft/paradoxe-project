from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import urllib.parse

from fake_useragent import UserAgent

RELAX_TIME = 0.0000001
memory = []
ua = UserAgent()

def get_url(url):
    
    page = rq.get(current_url, headers={'User-Agent': ua.random},timeout=10)
    status_code = page.status_code
   
    finale_score = 0
    
    if "200" in status_code:
        link_score = link_evaluation(url)
        text = bs.find_all(text=True)

        text = stop_list(text)
        text_score = content_evaluation(text)
        
        spam_score = spam_evalution(text)
        quality_score = quality_evalution(text)
        link_score = link_evaluation(url)
        # content_score = content_evaluation(text)
        
        content_score = 0
        finale_score = finale_verification(spam_score, quality_score, link_score, content_score)
      
    return finale_score

def stop_list(text):
    return text

def spam_evalution(text):
    
    hit = 0

    list = load_list("./spam", list)
    for i in list:
        if text.find(i)>=0:
            hit = hit + 1

    return hit

def quality_evalution(text):
    hit = 0

    list = load_list("./quality", list)
    for i in list:
        if text.find(i)>=0:
            hit = hit + 1

    return hit

def link_evaluation(url):
    hit = 0

    list = load_list("./compromised_domains", list)
    for i in list:
        hit = hit + 1                
    
    list = load_list("./bad_domains", list)
    for i in list:
        hit = hit + 1                
    
    list = load_list("./good_domains", list)
    for i in list:
        hit = hit - 1                

    list = load_list("./top_domains_list_acceptable", list)
    for i in list:
        hit = hit - 1  

    return hit

def content_evaluation(text):
    score = 0
    return score

def finale_verification(spam_score, quality_score, link_score, content_score):
    
    print("Final report")
    print("spam_evalution score: " + spam_score)
    print("quality_evalution score: " + quality_score)
    print("link_evaluation score: " + link_score)
    
    print("Final content: " + spam_score - quality_score)
    if link_score >= 1:
        pass_test = "Failed"
    else:
        pass_test = "Passed"
    
    print("Final report " + pass_test)
    
    
    
    return finale_score


    # url file loading and cleaning process
def load_list(file_name, list):

    print("Starting loading list")
    print("with file name: " + file_name)

    memory = []

    # open file with list of url
    with open(file_name, "r") as file: 
        # reading each line     
        for string in file:    
            # inset in url list object 
            if string not in memory:
                list.append(string)
                memory.append(string)
        file.close()
    memory = []

    return list

url = input("What web site URL do you want to veridy? ")
get_url(url)
