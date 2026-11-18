# from helpers import greet
# print(greet("noushad"))
with open("notes.txt",'w')as f:
    f.write("day 02 of learning \n")
    f.write("learned about biltin functions and modules \n"
            "now read write and append files\n")

with open("notes.txt","r")as f:
     content=f.read()
     print(content)

with open("notes.txt","r")as f:
     content=f.read()
     for n in content:
          print(n)

with open("notes.txt","a")as f:
    f.write("im happy that everything makes sense now😭")

with open("notes.txt","r")as f:
    content=f.read()
    for letters in content:
         print(letters)
try:
     with open("read.txt")as r:
          print("exception handling!!")
except FileNotFoundError:
     print("file doesnt exists")
import json
study={"name":"noushad","age":23,"place":["kushalnagar","kodagu"]}
with open("study.json","w")as f:
    json.dump(study,f,indent=2)

with open("study.json")as f:
    content=json.load(f)
    for letter in content:
        print(letter)
    print(content["name"])
    print(content["place"][1])