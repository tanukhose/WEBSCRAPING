"""        -:TASK NUMBEWR 2:-       """
import json

with open("Top_movie_task1.json")as g:
    data=json.load(g)
def group_by_year(movies):
    year=[]
    dic={}
    for i in movies:
        list2=[]
        y=(i['year_of_release'])
        # print(y)
        if y not in year:
            year.append(y)

        year.sort()

        for movie1 in movies:
            if movie1["year_of_release"]==y:
                list2.append(movie1)
            else:
                pass
                dic[y]=list2
    return dic
    
movie_2=group_by_year(data)   
with open("group_by_year_task2.json","w")as f:
    json.dump(movie_2,f,indent=4)







# import json

# with open("Top_movie1.json")as g:
#     data=json.load(g)
# def group_by_year(movies):
#     year=[]
#     for i in movies:
#         year.append(i['year_of_release'])
#         # print(i['year_of_release'])
#         for j in range(len(year)):
#             for g in range(len(year)):
#                 if year[j]<year[g]:
#                     year[g],year[j]=year[j],year[g]
#     # print(year)
#     list1=[]
#     for k in range(len(year)):
#             # print(k)
#             for n in range(len(movies)):
#                 # print(n)
#                 if year[k]==movies[n]['year_of_release']:
#                     s=movies[n]
#                     list1.append(s)
#     with open("group_by_year2.json","w")as f:
#         json.dump(list1,f,indent=4)
# group_by_year(data)