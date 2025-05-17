#Task 1: Create a Dictionary of Student Marks
'''
1.    Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
d={"raja":45,"alice":86,"bob":78}
user=input("Enter the Student name:   ")
if user in d.keys():
    print(user,"'s mark is ",d[user])
else:
    print(f"{user } not Found")
