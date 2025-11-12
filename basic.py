# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# a = 33
# b = 34
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")#Condition


# thislist = ["apple", "banana", "cherry", "apple", "cherry"]#for loop
# for x in thislist:
  
#   print(x)

# list=["sanket","yogi","modi"]
# for x in list:
#   if x=="sanket":
#     print(x)
def full_pyramid(n):
    for i in range(1, n + 1):
       
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
     
       
        print(spaces + stars)


try:
    num_rows = int(input("Enter the number of rows for the pyramid: "))

    if num_rows > 0:
        full_pyramid(num_rows)
    else:
      
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter an integer.")




num = int(input("Enter the number for the multiplication table: "))


print(f"--- Multiplication Table for {num} ---")


for i in range(1, 11):

  print(f"{num} x {i} = {num * i}")


