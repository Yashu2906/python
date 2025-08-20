# with open("practice.txt","w") as f:
#   data = f.write("Hi Everyone\nwe learning file I/O\nusing Java\nI like Programming in Java.")
#   f.close()

# with open("practice.txt","r") as f:
#   data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# def word_find():
#   word = "learning"
#   with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) !=-1 ):
#       print("Found")
#     else:
#       print("found")

# word_find()


# word = "learning"
# data = True

# def check_by_line():
#   line_count = 1
#   with open("practice.txt","r") as f:
#     data = f.readline()
#     while data:
#       if word in data:
#         print(line_count)
#       line_count += 1
#       data = f.readline()
#     return -1
# check_by_line()


with open("practice.txt","r") as f:
  data = f.read()
  print(data)

  # num = ""
  # for i in range(len(data)):
  #   if(data[i] == ","):
  #     print(num)
  #     num = ""
  #   else:
  #     num += data[i]
  count = 0
  nums = data.split(",")
  for i in nums:
    if(int(i) % 2 == 0):
      count += 1
  print(count)
