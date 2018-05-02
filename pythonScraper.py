#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sihaywar
#
# Created:     11/03/2018
# Copyright:   (c) sihaywar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
from http.cookiejar import CookieJar
import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = input("Please enter your query")# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
#add the directory for your image here
DIR="***YOUR PICTURE DIRECTORY HERE***"
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"
}

soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
'''
req = urllib.request.Request('https://atmedia.imgix.net/abb614aa3b247b859a22d477674b620f6ae0fa46?auto=format&q=45&w=398.0&fit=max&cs=strip')#, headers={'User-Agent' : header})
with urllib.request.urlopen(req) as response:
     response.read()
     '''


for i , (img , Type) in enumerate(ActualImages):
    try:
        req = urllib.request.Request(img)#, headers={'User-Agent' : header})
        raw_img = urllib.request.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print (cntr )
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print ("could not load : "+img)
        print (e)
