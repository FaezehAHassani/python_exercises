print(True and True) # True
print(False and True) # False
print(1 == 1 and 2 == 1) # False
print("test" == "test") # True
print('\n')
print(True and 1 == 1) # True
print(False and 0 != 0) # False
print(True or 1 == 1) # True
print("test" == "testing") # False
print('\n')
print(1 != 0 and 2 == 1) # False
print("test" != "testing") # True
print("test" == 1) # False
print(not (True and False)) # True
print('\n')
print(not ( 1 == 1 and 0 != 1)) # False
print(not (10 == 1 or 1000 == 1000)) # False
print(not (1 != 10 or 3 == 4)) # False
print('\n')
print(not ("testing" == "testing" and "Zed" == "Cool Guy")) # True
print(1 == 1 and (not ("testing" == 1 or 1 == 0))) # True
print("chunky" == "bacon" and not (3 == 4 or 3 == 3)) # False
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # False
print('\n')
print(False and 1) # return False => DIFFERENT CASE
print(True and 1) # returen  1 => DIFFERENT CASE
