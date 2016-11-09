door=[]
print ('The following doors are open:')
#set up the range for 100doors
for x in range(100):
    door.append(0)
for i in range(100):
    for x in range(i, 100, i+1):
        #setting up the doors
        #if door(x) is equal to 1, door is open
        #if door(x) is equal to 0, it means door is closed
        if door[x] == 0:
            door[x]=1
        else:
            door[x]=0
    if door[i] == 1:
        print (i+1, end=', ') 
