# tutedudeassignment5
Module 6: Data Structures and Strings in Python
#Task1
d={"raja":45,"alice":86,"bob":78}
user=input("Enter the Student name:   ")
if user in d.keys():
    print(user,"'s mark is ",d[user])
else:
    print(f"{user } not Found")


Task 2: Demonstrate List Slicing
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print("Extracted First five element",l[:5])
print("Revesed extracted element",(l[:5])[::-1])


