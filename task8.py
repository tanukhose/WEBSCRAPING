# from task1 import movies
# from task4 import m
# import json
# import os

# url=movies[1]["link"]
# # print(ur)

# def movie_details(movie_detail):
#     movie_id=""
#     data=[]
#     for id in movie_detail[27:-1]:
#         movie_id+=id
#         # print(movie_id)
#     filename=movie_id+'.json'
#     text=os.path.exists(filename)
#     if text==True:
#         with open(filename)as f:
#             a=json.load(f)    
#         print(a)   
#     else:
#         data.append(m)
#         with open(filename,"w") as f:
#             json.dump(data,f,indent=6)
#         print(data)  
          
# movie_details(url)


# def cal(a,b,o):
#     if o=='+':
#         print(a+b)
#     elif o=='-':
#         print(a-b)
#     elif o=='*':
#         print(a*b)
#     elif o=='/':
#         print(a/b)
# a=int(input('enter the number:-'))
# b=int(input('enter the number:- '))
# o=input('enter the operator:-')
# cal(a,b,o)

# def fact(a):
#     if a==1:
#         return 1
#     return a*fact(a-1)
# print(fact(5))


a=int(input("enter the number"))
l=len(str(a))
l=int(a)
# print(type(a))
sum=0
n=a
while a>0:
    sum+=(a%10)**l
    print(sum)
    a//=10
if n==sum:
    print("amstrong")
else:
    print("Not")