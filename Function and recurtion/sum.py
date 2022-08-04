# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

a=int(input("Enter a number to make sum: "))
if a<0:
    print("Enter a positive number.")
else:
    print(f"Sum value of number 1 to {a} is" ,recur_sum(a))