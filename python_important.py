num1 = 6
num2 = 3

# Write your if statement here
if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))





# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

if total > budget:
  over_budget = True
else:
  over_budget = False


# Check if the total is greater than the budget and store the result in over_budget


# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))





# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False





# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True






# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False


# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
#should print True
print(divisible_by_ten(25))
#should print False






def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False





# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False





# Write your always_false function here:
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False





