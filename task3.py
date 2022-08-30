"""        -:TASK NUMBEWR 3:-       """


import json
from task2 import movie_2


def group_by_year():
    movie={}
    l1=[]
    for i in movie_2:
        # print(i)
        i=int(i)
        mode=i%10
        d=i- mode
        # print(d)
        if d not in l1:
            l1.append(d)
    # print(l1)
    l1.sort()
    # print(l1)
    for i in l1:
        movie[i]=[]
    for i in movie:
        d2=i+9
        for x in movie_2:
            x=(x)
            if x<=d2 and x>=i:
                for z in movie_2[x]:
                    movie[i].append(z)
            # print(movie)
    with open("group_by_year_task3.json","w")as f:
        json.dump(movie,f,indent=4)
    return movie
group_by_year()         
    





# with open("Top_movie1.json")as g:
#     data=json.load(g)
# # print(data)
# def decades_by_years(movies):
#     year=[]
#     for i in range(len(movies)):
#         print(movies[i])
#         r=movies[i]['year_of_release']%10
#         de=movies[i]['year_of_release']-r
#         if de not in year:
#             year.append(de)
#         # print(year)
#     year.sort()
#     # print(year)
#     movies_dict={i:[] for i in year}
#     # print(movies_dict)
#     for i in range(len(movies)):
#         for x,y in movies_dict.items():
#             # print(x)
#             if x==1950:
#                 if movies[i]['year_of_release']>=1950 and movies[i]['year_of_release']<=1959:
#                     y.append(movies[i])
#                     break
#                 # print(y)
#             elif x==1960:
#                 if movies[i]['year_of_release']>=1960 and movies[i]['year_of_release']<=1969:
#                     y.append(movies[i])
#                     break
#             elif x==1970:
#                 if movies[i]['year_of_release']>=1970 and movies[i]['year_of_release']<=1979:
#                     y.append(movies[i])
#                     break
#             elif x==1980:
#                 if movies[i]['year_of_release']>=1980 and movies[i]['year_of_release']<=1989:
#                     y.append(movies[i])
#                     break
#             elif x==1990:
#                 if movies[i]['year_of_release']>=1990 and movies[i]['year_of_release']<=1999:
#                     y.append(movies[i])
#                     break
#             elif x==2000:
#                 if movies[i]['year_of_release']>=2000 and movies[i]['year_of_release']<=2009:
#                     y.append(movies[i])
#                     break
#             elif x==2010:
#                 if movies[i]['year_of_release']>=2010 and movies[i]['year_of_release']<=2019:
#                     y.append(movies[i])
#                     break
#             elif x==2020:
#                 if movies[i]['year_of_release']>=2020 and movies[i]['year_of_release']<=2029:
#                     y.append(movies[i])
#                     break
#     # print(movies_dict)
#     with open("decades_by_years3.json","w") as l:
#         json.dump(movies_dict,l,indent=4)
# decades_by_years(data)
