print("Enter a marks Of Student out of 100 : ")
phy=int(input("Pysics : "))
chem=int(input("Chemestry : "))
maths=int(input("Maths : "))

pers=((phy+chem+maths) / 300)*100
print("The Total is :",pers)

if(pers>=90):
  print("Grade = AA")
elif(pers>=80 and pers<90):
  print("Grade = AB")
elif(pers>=70 and pers<80):
  print("Grade = BB")
elif(pers<70):
  print("Grade = CC")
else:
  print("Grade = Fail")
