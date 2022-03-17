import os

path = input("enter your path: ")
SZE = int(input("enter the size you want to separet: "))
file = open('fileDigger.txt','w')
file.write("")

filelist = []
cnt = 0
char = ".  "

def wrt(text):
    file = open("fileDigger.txt", "a") 
    file.write(text + '\n') 
    file.close() 

for root, dirs, files in os.walk(path):
	for file in files:
                
		filelist.append(os.path.join(root,file))

for name in filelist:
    size = os.path.getsize(name)
    size = size/1000000
    if size >= SZE:
        cnt += 1
        name = str(cnt)+char+name
        size = "---"+str(int(size))+" mb"

        wrt(name)
        wrt(str(size))
        print(name)
