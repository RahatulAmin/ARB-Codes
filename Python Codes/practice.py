temp=open("work.txt","r")
#print temp.read()
t=temp.read().split("\n")
s = " "
y = 0
for y in range(len(t)):
	lo=t[y].split(" ")
	for h in range(len(lo)):
		s = s +" "+ lo[h]	
	#s = s + t[y].split(" ")
#x = 0
#for x in range(len(s)):
	#print (s[x])
#print s[0]
#print s[1]
#print s[6]
	#print t[y]
z = s.split(" ")
print s
for a in range(len(z)):
	print z[a]
print z[5]
