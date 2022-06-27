

import json
import requests
url=requests.get("https://api.merakilearn.org/courses").json()
# a=url.json() 
with open("courses.json","w") as file:
    json.dump(url , file , indent=4)
r = open("courses.json","r").read()
data = json.loads(r)
print() 
print("<<<<< Welcome to Navgurukul and learn basic promming language >>>>>")
print()
i = 0
while i < len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i+=1
user=int(input("<<<< enter the program number  >>>>:"))
print(data[user-1]["name"],data[user-1]["id"])
print()
data_file=data[user-1]["name"]+"_ "+data[user-1]["id"]+".json" 
url_file="http://api.merakilearn.org/courses/"+data[user-1]["id"]+"/exercises"
new_url=requests.get(url_file).json()
with open(data_file,"w") as f:  
    json.dump(new_url,f,indent=4)
read_file= open(data_file,"r").read()
deta = json.loads(read_file)



i = 0
while i < len(deta["course"]["exercises"]):
    print(str(i+1)+".",deta["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("enter the topic no:- "))
topic = topic-1
i = 0
while i < len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic <= len(deta["course"]["exercises"]):

   
    a = input("previous or next(p&n):")
    if a == "p" and a!= "n":
        topic-=1
        if a == "p" and topic >1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else :
            i = 0
            while i < len(deta):
                print(str(i+1),deta["course"]["exercises"][i]["name"])
                i+=1
    elif a == "n" and a!="p":
        topic+=1
        if a == "n" and topic < len(deta["course"]["exercises"]):
                print(deta["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(deta["course"]["exercises"][topic]["content"]):
                    print(deta["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(deta["course"]["exercises"]):
            print("topic is completed.")
            break
    else:
        print("wrong user_input ")
        break



# a="AAABCDEFE"
# user=input("enter")
# i=0
# while i<len(a):
#     j=1
#     if a[i]==a[j]:
#         j+=j
#         print(i+i,a[i])
#     else:
#         print(a[i],j)
#     i+=1
# print(i)



 
# def dev(a,b,c):
#         if a%2==0 and b%2==0 and c%2==0:
#             print ("Ture")
#         else:
#             print("FAlse")
# dev(12,4,-14)



# List1 = [1,5,10,12,16,20]
# List2 = [1,2,10,13,16]

# # Output=[1,2,5,10,12,13,16,20]
# List1.extend(List2)
# L=[]
# for i in List1:
#     if i  not in L:
#             L.append(i)
# print(sorted(L)) 



# list=["a","n","t","a","a","t","n","a","x","u","g","a","x","a"]
# L= []
# for I in list :
#     C=0
#     for j in list :
#         if I==j: 
#             C+=1
#         if I not in L:
#             L. append(I) 
#     print([I, C],end="") 
# output=(['a',5]['n',3]['t',2]['x',2]['u',1]['g',1])


# List1 = ['1','2','3','4','5','6','7']
# List2 =[]
# Sum=""
# for I in List1 :
#     Sum+=I
# List2. append(int(Sum)) 
# print(List2)


# a = {"4":5,"6":7,"1":3,"2":4}
# S =sorted (a.items())
# d ={}
# for i in S:
#       d[i[0]]=i[1]
# print(d) 


# a=["red","maroom","yellow","olive"]
# L=[]
# for i in a:
#     b=list(i)
#     L.append(b)
# print (L) 
# Output=[['R','e,'d'],['M','a','r','o','o','n'],['Y','e','l','l','o','w'],['O','l','l','v','e']]

# List= [1,1,2,3,4,5,2]
# A=int(input ("enter the number"))
# i= 0
# while i<len(List):
#         if A in List:
#             List.remove(A)
#         i+=1
# print (List)  
# dic={"A":[3,9,0,7],"B":[6,2,4,5]}
# my_dict1={}
# for x,y in dic.items():
#     s=[]
#     a=' '
#     if type(y)==list:
#         a=x
#         i=1
#         while i<len(y)+1:
#             s.append(y[-i])
#             i+=1
#             my_dict1.update({a:s})
# print(my_dict1) 
# dic={}
# n=15
# i=1
# while i<=n:
#     c=i*i
#     dic[i]=c
#     i=i+1
# print(dic) 
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in d:
#     d[i].clear()
# print(d)


# # data################################
# import requests
# from bs4 import BeautifulSoup
# req=requests.get("https://www.youtube.com/watch?v=O6nnVHPjcJU&ab_channel=GeeksforGeeks") 
# soup=BeautifulSoup(req.content,"html.parser")
# print(soup.prettify)

# #text#############################
# import requests
# from bs4 import BeautifulSoup
# req=requests.get("https://pypi.org/project/beautifulsoup4/") 
# soup=BeautifulSoup(req.content,"html.parser")
# print(soup.get_text) 

# #title##############################
# import requests
# from bs4 import BeautifulSoup
# req=requests.get("https://pypi.org/project/beautifulsoup4/") 
# soup=BeautifulSoup(req.content,"html.parser")
# res=soup.title
# # print(soup.get_text()) 
# print(res.prettify())


# import requests
# from bs4 import BeautifulSoup
# url="https://codewithharry.com/"
# r=requests.get(url)
# htmlContent=r.content
# # print(htmlContent)

# soup=BeautifulSoup(htmlContent, "html.parser")
# print(soup) 