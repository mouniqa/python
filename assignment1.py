studentName=input("Enter name of the student : ")
print("Enter marks of the student "+studentName+" : ")

teluguMarks=int(input("Enter marks for subject Telugu : "))
englishMarks=int(input("Enter marks for subject English : "))
mathsMarks=int(input("Enter marks for subject Maths : "))
scienceMarks=int(input("Enter marks for subject Science : "))
socialMarks=int(input("Enter marks for subject Social : "))

average=teluguMarks+englishMarks+mathsMarks+scienceMarks+socialMarks
result=average/5
print("Average is : ", result)

if(result>=90):
    print("Rating of "+studentName+" is : 5")

elif(result>=75 and result <90):
    print("Rating of "+studentName+" is : 4")

elif(result>=60 and result <75):
    print("Rating of "+studentName+" is : 3")

elif(result>=35 and result <60):
    print("Rating of "+studentName+" is : 2")

else:
    print("Rating of "+studentName+" is : 1")
