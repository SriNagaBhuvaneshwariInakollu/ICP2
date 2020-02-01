#count=0
#a= input("enter the file name")
#b=a.readLine()
#while line !="":
a= open("fileexample.txt", 'r')
cnt= dict()
for line in a:
 line=line.strip()
 word=line.split(" ")
 for w in word:
  if w in cnt:
   cnt[w] = cnt[w] + 1
  else:
   cnt[w] = 1

print(cnt)




