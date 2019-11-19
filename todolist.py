
mylist = ["sleep","hw","read"]

task= input("hello, please imput a task you wish to complete ")
priority= input("how important is this task with 1 being top priority, and 2 as normal ")
if priority == "1":
    mylist[0:0]=[task]
elif priority == "2":
    mylist.append(task)


# print the list
print(mylist[0:3])


        
        