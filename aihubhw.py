# -*- coding: utf-8 -*-
"""AIhubhw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OzQgXGqPcVo5kJ9nLwyf0aX102A9GvTE
"""

myList = [1,2,3,4,5,6,7,8]
numb = int(len(myList)/2)

newList = []

for x in range(numb,len(myList)):
  myObj = myList[x]
  newList.append(myObj)

for y in range(0,numb):
  myObj = myList[y]
  newList.append(myObj)

print(newList)