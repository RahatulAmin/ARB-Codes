temp=open("work.txt","r")
#print temp.read()
t=temp.read().split("\n")
s = " "
y = 0
for y in range(len(t)):
	lo=t[y].split(" ")
	for h in range(len(lo)):
		s = s +" "+ lo[h]

#k=[]
#for i in s:
    #j = i.replace(' ','')
    #k.append(j)
#s=[m.strip(' ') for x in s]
#z = s.split(" ")

#for a in range(len(z)):
	#print z[a]
#print z[5]
	#hello = [x.strip(' ') for x in hello]
new_list = [elem for elem in s if not elem.isspace()]
print s
for e in new_list:
    print e
print new_list
    #[elem for elem in mylist if not elem.isspace()]
	
