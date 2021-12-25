# Write a Python program to multiplies all the items in a list.

# ---------- by function ---------

def multiplication(byList):
    answer = 1
    for a in byList:
        answer = answer * a
    return answer

data = [1,2,3]
print("The multiplication answer is " ,multiplication(data))

# -------prod function-----
import math

print("The answer is ", math.prod(data))
 