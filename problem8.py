#1

# i=1
# while i<=100:
#   print(i)
#   i+=1
  
#3
  
# n=int(input("Enter The Table No. : "))
# i=1
# while i<=10:
#   print(n*i)
#   i+=1

#4

# list1=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(list1):
#   print(list1[i])
#   i+=1

#5
i=0
tup1=(1,4,9,16,25,36,49,64,81,100)
while i<len(tup1):
  if tup1[i]==64:
    print("found at position :" + str(i))
  i+=1