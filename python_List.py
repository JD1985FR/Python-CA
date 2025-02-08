# Write your function here
# Define the append_size function
def append_size(input_list):
  # Get the length of the input list
  length=len(input_list)
  # Append the calculated length to the original list
  input_list.append(length)
  # Return the modified list
  return input_list


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))





def append_size(input_list):
  input_list.append(len(input_list))
  return input_list

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))





# Write your function here
# Define the append_sum function
def append_sum(my_list):
  # Calculate the sum of last two elements and append it to the list
  my_list.append(my_list[-1] + my_list[-2])
  # Calculate the sum of last two elements and append it to the list
  my_list.append(my_list[-1] + my_list[-2])
  # Calculate the sum of last two elements and append it to the list
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))





def append_sum(my_list):
  for i in range(3):
    # Get the sum of last two elements of the list and append it to the list
    my_list.append(my_list[-1] + my_list[-2])
  return my_list
# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))





# Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))






# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))





# Write your function here
def combine_sort(my_list1, my_list2):
  # Concatenate input lists
  unsorted = my_list1 + my_list2
  # Sort the concatenated list
  sorted_list = sorted(unsorted)
  return sorted_list


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))