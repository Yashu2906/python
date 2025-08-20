import random
import time

min_oprands = 1
max_oprands = 25
operators = ["+","*","-"]
total_problem = 10

def Problem():
    left = random.randint(min_oprands,max_oprands)
    right = random.randint(min_oprands,max_oprands)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    ans = eval(expr)
    return expr,ans
    
    
wrong = 0
input ("Press Enter to start :")
print("------------------------------")

start_time = time.time()
for i in range(total_problem):
    expr,ans = Problem()
    while True:

        guess = input("  problem #" + str(i+1) + " : " + expr + " = ")
        if guess == str(ans):
            break
        else:
            wrong += 1
end_time = time.time()
total_time = round(end_time - start_time)

print("------------------------------")
print("Great ! You completed math game in ", total_time,"second")
