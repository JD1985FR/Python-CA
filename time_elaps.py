def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))