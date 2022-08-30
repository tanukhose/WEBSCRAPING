import requests
import json
from bs4 import BeautifulSoup

url='https://www.imdb.com/title/tt0066763/'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
s=soup.find('section',class_="ipc-page-background ipc-page-background--baseAlt sc-2a827f80-0 cpecwB")
# print(s)
m=[]
movie1={}
movie_name=s.find(class_="sc-b73cd867-0 eKrKux").get_text()
movie1["movie_name"]=movie_name

movie_director=s.find(class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
movie1["movie_director"]=movie_director

u=[]
for ul in soup.find_all('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"):
    u.append(ul.get_text())
    list=["Hindi","English","Tamil","Telugu","Malayalam","Kannada","Bengali"]
    hh=""
    for i in u:
        for j in list:
            if i==j:
                hh=i
movie1['language']=hh


detail=soup.find("section",cel_widget_id="StaticFeature_Details")
s1=detail.find_all("div")

bio=soup.find("div",class_="sc-16ede01-7 hrgVKw").get_text()
movie1["bio"]=[bio]
# print(director)

poster_image=soup.find("div",class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img").img['src']
movie1["poster_image"]=[poster_image]

# print(s1)
y=[]
for j in s1:
    h=j.find_all('ul')
    for li in h:
        o=li.find_all('li')
        for aa in o:
            z=aa.find_all('a')
            details=[details.get_text() for details in z]
            for p in details:
                y.append(p)
# print(y)
movie1["country"]=y[5]
b=y[1].split()
# print(b)
movie1["release_year"]=b[2]
movie1["release_date"]=b[1]+b[0]
m.append(movie1)

# movie_country=s.findovie_country

# print(movie1)
with open("task4.json","w")as f:
    json.dump(m,f,indent=4)
    


















# a=[['harry',37.21],['berry',37.21],['tina',37],['akriti',41],['harsh',39]]
# i=0
# b=0
# l=[]
# while i<len(a):
#     if a[i][1] not in l:
#         l.append(a[i][1])
#     else:
#         b=a[i][1]
#     i+=1
# for i in a:
#     if b in i:
#         print(i[0])





