import csv
import os
path=os.getcwd()
data=open(path+"/when12.txt","r+")
datastr=data.read()
binRep=[]
for x in datastr:
    binRep.append(format(ord(x),"08b"))
doubleBin=[x+y for x,y in zip(binRep[0::2],binRep[1::2])]
doubleInt=[int(x,2) for x in doubleBin]
modData=open(path+"/DoiBin.csv","w")
writefile=csv.writer(modData)
writefile.writerow([str(x) for x in doubleInt])