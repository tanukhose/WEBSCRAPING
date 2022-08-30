from task1 import movies
import requests
import json
from bs4 import BeautifulSoup

def t5():
  m=[]
  for i in range(0,21):
      a=movies[i]["link"]
      print(a)
      page=requests.get(a)
      soup=BeautifulSoup(page.text,'html.parser')
      s=soup.find('section',class_="ipc-page-background ipc-page-background--baseAlt sc-2a827f80-0 cpecwB")
      # print(s)
      movie1={}
      movie1["movie_name"]=movies[i]['movie_name']
      # print(s)

    #   movie_name=s.find("div",class_="sc-b73cd867-0 eKrKux").get_text()
    #   movie1["movie_name"]=movie_name

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

  with open("task5.json","w")as f:
      json.dump(m,f,indent=4)
  return m
t5()




# # a=['cat','camel','dog','red']
# # i=0
# # while i<len(a):
# #     b=len(a[i])
# #     j=1
# #     while j<=b:
# #         g=1
# #         f=1
# #         while g<j:
# #             print(f,'*')
# #             f+=1
# #             g+=1
# #         j+=1

# #     # print(b)
# #     i+=1




# with open("task5.json","r") as file:
#     data=json.load(file)
# def movie_language(movie_list):
#     language_list=[]
#     list=[]
#     for i in range(len(movie_list)):
#         for j in range(len(movie_list[i]["language"])):
#             if movie_list[i]["language"][j] not in language_list:
#                 language_list.append(movie_list[i]["language"][j])
#             list.append(movie_list[i]["language"][j])
#     language_dict={i:""for i in language_list}
#     for x,y in language_dict.items():
#         count=0
#         for i in range(len(list)):
#             if x==list[i]:
#                 count+=1
#                 language_dict[x]=count
#     print(language_dict)
#     # print(language_list)
#     # print(list)
#     with open("task6_movie_language.json","w") as file:
#         json.dump(language_dict,file,indent=4)
# movie_language(data)