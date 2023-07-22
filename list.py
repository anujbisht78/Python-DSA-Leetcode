# LIST IN PYTHON 

# list=[2,3,4,4,566,7,6]
# print("Creating the First List")
# print("Elements are: ",list)

#ACCESSING THE LIST 
# list=["Anuj","Rahul","Ajay","Mohan","Vijay"]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])

#ACCESSING THE ELEMENTS FROM MULTI-DIMENSIONAL LIST
# list=[["Anuj","Rahul","Ajay"],"Priyanka","Priya",[2,4,6,8]]
# print(list[0][0])
# print(list[3][3])
# print(list[0][2])
# print(list[2])
# print(list[1])

#NEGATIVE INDEXING IN DIMENSIONAL AND MULTI DIMENSIONAL LIST

# DIMEMSIONAL LIST 
# print("Dimensional List")
# list1=[2,4,5,6,"Anuj","Rahul","Mohan"]
# print(list1)
# print("The Elements we accessed:")
# print(list1[-1]) 
# print(list1[-4])
# print(list1[-2])
# print(list1[-6])

#MULTI-DIMENSIONAL LIST
# print("Multi-dimensioanal List:")
# list2=["Apple","Banana",["Anuj","Rohan","Vegetables"],"Hello",[2,4,6,8]]
# print(list2)
# print("The Elements we accessed")
# print(list2[-1][-3])
# print(list2[-3][-3])
# print(list2[-4])
# print(list2[-5])

#TAKING INPUT OF A PYTHON LIST AND DISPLAYING IT
# list=list(map(int,input("Enter the values: ").split()))
# print("Elements are: ",list)

# list=list(map(str,input("Enter the values: ").split()))
# print("Elements are: ",list)

#ADDING THE ELEMENTS TO PYTHON LIST

#append() Method
# list=[2,4,6,8,10,12]
# print(list)
# list.append(34)
# list.append(24)
# list.append(14)
# list.append(44)
#list.append((3,4))
# print("After Appending: ",list)

#ADDING TWO LIST TOGETHER
# list1=[2,4,6,8,10]
# list2=["Anuj","Apple","Banana","Rahul"]
# print("List1: ",list1)
# print("List2: ",list2)

# list1.append(list2)
# print("List2 in List1: ",list1)
# list2.append(list1)
# print("List1 in List2: ",list2)

#ADDING ELEMENTS USING ITERATOR

# list=[1,2,3,4]
# print("Before Appending: ",list)
# for i in range(5,15):
#     list.append(i)
# print("After Appending: ",list)

#TAKING INPUT FROM THE USER AND THEN APPEND THE ELEMENTS
# list=list(map(int,input("Enter the values: ").split()))
# print("Before Appending: ",list)
# list.append("Anuj")
# list.append("Rahul")
# list.append("Ajay")
# list.append("Mohan")
# print("After Appending: ",list)

#insert() Method 
# list=[2,4,6,8,10,12]
# print("Before Inserting: ",list)
# list.insert(1,3)
# list.insert(3,5)
# list.insert(5,7)
# list.insert(7,9)
# list.insert(9,11)
# print("After Inserting: ",list)

#Revere the List

# list=[1,2,3,4,5]
# print("Before Reversing; ",list)

# list.reverse()
# print("After Reversing; ",list)

#TAKE INPUT FROM THE USER AND REVERSE IT
# size=int(input("Enter the size: "))
# list=list(map(int,input("Enter the values: ").split()))
# print("Elements Are: ",list)
# for i in list:
#     list.reverse()
    
# print("After Reversing; ",list)

#TAKE INPUT FROM THE USER AND REVERSE THE ALTERNATE ELEMENTS 
# size=int(input("Enter the size: "))
# list=list(map(int,input("Enter the values: ").split()))
# print("Elements Are: ",list)

# temp=int
# for i in range(0,size-1,2):
#     temp=list[i+1]
#     list[i+1]=list[i]
#     list[i]=temp 
    
# print("After Reversing; ",list)

#REMOVING THE ELEMENT FROM THE LIST
# list=[1,2,3,4,5,"Apple","Anuj"]
# print("Elements Are: ",list)
# list.remove("Apple")
# print("Final List: ",list)

# SLICING OF LIST 
# list=[2,3,4,5,"Apple","Anuj"]
# print(list[2:])
# print(list[2:5])
# print(list[:4])

# COUNT() METHOD 
# list=[2,3,4,5,"Apple","Anuj","Apple","Apple"]
# print(list.count("Apple"))
#LET US SAY THAT WE HAVE TO COUNT EACH ELEMENT AND STORED IN ANOTHER LIST 
list1=[2,3,4,5,"Apple","Anuj","Apple","Apple"]

for i in list1:
    # print(list.count(i))
    newlist=list1.count(i)
    print(list(map(int,newlist)))
# # print(i,newlist)
# # print([[i,list.count(i)]for i in set(list)])

    

    




    

    








    





