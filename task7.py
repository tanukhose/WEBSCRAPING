import json

with open("task5.json","r")as f:
    d=json.load(f)

def movie_director():
    list_movie_director=[]
    for i in d:
        # print(i['movie_director'])
        if i not in list_movie_director:
            list_movie_director.append(i['movie_director'])
    dic={}
    for g in list_movie_director:
        count=0
        for j in d:
            if g==j['movie_director']:
                count+=1
            dic[g]=count
    print(dic)
    return dic

m_director=movie_director()
with open("task7.json","w")as f:
    json.dump(m_director,f,indent=4)

    
