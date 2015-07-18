import urllib2
import time
from collections import defaultdict
import json
from bs4 import BeautifulSoup
import csv
import pickle
import os.path

def write_to_file(mydict):
    print mydict
    f = open('dict3.csv','wb')
    mystr = ""
    for key in mydict.keys() :
        mystr += key + "," +mydict[key] + "\n"

    f.write(mystr)
    f.close()

if __name__ == "__main__":
    profile_urls = ["https://www.linkedin.com/pub/max-scheiber/42/603/506?trk=pub-pbmap","http://www.linkedin.com/pub/stuart-wagner/5/202/482", "https://au.linkedin.com/in/yashdv", "https://in.linkedin.com/in/deepaksharma1310", "https://www.linkedin.com/in/kunalbhalla","https://in.linkedin.com/in/kirthiga","https://es.linkedin.com/in/swarandeepsingh","https://www.linkedin.com/pub/anisha-arora/31/a15/470?trk=pub-pbmap","https://www.linkedin.com/in/anishaarora2009","https://www.linkedin.com/pub/ekta-patel/10/324/907?trk=pub-pbmap","https://www.linkedin.com/pub/gauri-pendse/0/a47/106?trk=pub-pbmap","https://in.linkedin.com/in/praveengoogle","https://in.linkedin.com/in/renusd","https://in.linkedin.com/in/rinkysharma5","https://in.linkedin.com/in/govindpebbety","https://www.linkedin.com/in/deepaksharma","https://www.linkedin.com/pub/daniel-delos/92/377/6b0","https://www.linkedin.com/in/dalaplante","https://www.linkedin.com/in/davidlaplante","https://www.linkedin.com/in/rachelhocevar", "https://www.linkedin.com/in/kellygiusti","https://www.linkedin.com/pub/cat-nunnery/42/819/79b?trk=pub-pbmap", "https://www.linkedin.com/in/kristengorbell", "https://www.linkedin.com/pub/caitlin-smith/46/aaa/29b?trk=pub-pbmap","https://www.linkedin.com/in/kellyconnery", "https://www.linkedin.com/pub/prasoon-mishra/a/a92/823", "https://www.linkedin.com/in/jasmeet13n","https://in.linkedin.com/pub/kalpana-behara/6/1ab/72a", "https://in.linkedin.com/in/anshumansingh26", "https://uk.linkedin.com/pub/tarang-shrivastava/2b/714/34", "https://www.linkedin.com/in/abhishekkona", "https://in.linkedin.com/pub/inderjeet-kaur/11/b11/6a0", "https://in.linkedin.com/pub/kanchan-verma/4/368/103","https://in.linkedin.com/in/payalgpt", "https://in.linkedin.com/pub/ashudeep-sharma/7/93b/a78"]

    url_to_image = defaultdict()
    idx = 0
    while True:
        url = profile_urls[0]
        time.sleep(1)
        print "completed iteration:", idx, len(url_to_image), url
        response = urllib2.urlopen(url)
        page_source = response.read()
        soup = BeautifulSoup(page_source, 'html.parser')
        try:
            div = soup.find("div", class_="profile-picture")
            if div.find('a').find('img')['height'] > 180 and div.find('a').find('img')['width'] > 180:
                url_to_image[url] = div.find('a').find('img')['src']
        except:
            print "Caught other error"

        if len(url_to_image) > 200:
            pickle.dump(url_to_image, open('url_to_image.p', 'wb'))
            pickle.dump(profile_urls, open('profile_urls.p', 'wb'))
            write_to_file(url_to_image)
            exit(0)

        #insights = soup.find("div", class_="insights-browse-map")

        for div_tree in soup.find_all("div", class_="insights-browse-map"):
            try:
                if div_tree.find("h3").text == "People Also Viewed":
                    for person in div_tree.find("ul").find_all('li'):
                        link_to_person = person.find('a', class_='browse-map-photo')['href']
                        if link_to_person not in url_to_image:
                            profile_urls.append(link_to_person)
            except:
                print "Caught: moving on"
        idx += 1
        profile_urls = profile_urls[1:]

        '''
        if insights:
            insights.find('ul').prettify()
        #print div['div'], "working?"
        '''

