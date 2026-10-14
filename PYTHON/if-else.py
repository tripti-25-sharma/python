age = int(input("Enter your age: "))


# '''Nested if-else'''
# certificate = True

# if age >= 18:
#   if certificate == True:
#     print("You will be hired")
#   else:
#     print("Try another time")
# else:
#   print("You are younger")


# '''if-else'''


  #Shorthand

status = "Adult" if age >= 18 else "Younger"
print(f"Your status is {status}")