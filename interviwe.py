# list1=[1,8,6,4,3,9,7,5,1,9]
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i]<list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)


# list1=[1,8,6,4,3,9,7,5,1,9]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list1):
#         if list1[i]<list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
#         j+=1
#     i+=1
# print(list1)


# str= "45My 45Name 56Is 87Priyanka 78Dangwal"
# output should be =
# List=["My", "Name","Priyanka","Dangwal"]


# s= "45My 45Name 56Is 87Priyanka 78Dangwal"
# i=0
# k=""
# while i<len(s):
#     if s[i]!='4'and s[i]!='5' and s[i]!='6' and  s[i]!='7' and s[i]!='8' :
#         print(s[i],end="")           
#     i+=1

    

# b= "45My 45Name 56Is 87Priyanka 78Dangwal"
# s=b.split()
# p=[]
# for i in range(len(s)):
#     s[i]=str(s[i])
#     for j in range(len(s[i])):
#         p.append(s[i][2: ])
#     k=0
#     list1=[]
#     while k<len(p):
#         if p[k] not in list1:
#             list1.append(p[k])
#         k+=1
# print(list1)


# di={'a':1,'b':2,'c':{9:'a','b':21},'d':{'a':11}}
# p=(di['c']['b'])
# p1=di['d']['a']
# print(p,p1)
# for i in di['c']:
#     print(di['c'][i])
# b=di['a']
# b1=di['d']['a']
# print(b,b1)


# a=['mom','123','dad','nunu']
# i=0
# c=0
# while i<len(a):
#     j=0
#     s=''
#     d=''
#     while j<len(a[i]):
#         s+=a[i][j]
#         j+=1
#     g=1
#     while g<=len(a[i]):
#         d+=a[i][-g]
#         g+=1
#     if s==d:
#         print(s)
#         c+=1
#     i+=1
# print(c)


# c='tanuja khose'
# b=c.upper()
# print(b)

# c='tanuja khose'
# a=c[0].upper()
# a1=c[7].upper()
# p=c[1:7]
# p1=c[8: ]
# print(a+p+a1+p1)

# c="tanuja khose"
# print([c])

