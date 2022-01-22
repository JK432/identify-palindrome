# Write a program to identify palindromes in the input file 
f=open("first.txt","r")
s=f.read()
x=s.split()
for i in x:
  if (i==i[::-1]):
    if(len(i)!=1):
     print(i)
