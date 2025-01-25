# Your code below:
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]
prices = [
  2,
  6,
  1,
  3,
  2,
  7,
  2
]
num_two_dollar_slices = prices.count(2)
num_pizza = len(toppings)
pizza_and_prices = [
  [2	,"pepperoni"],
  [6	,"pineapple"],
  [1	,"cheese"],
  [3	,"sausage"],
  [2	,"olives"],
  [7	,"anchovies"],
  [2	,"mushrooms"]
]
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1:]
pizza_and_prices.pop()
pizza_and_prices.insert(4, (2.5, "peppers"))
three_cheapest = pizza_and_prices[:3]
print(priciest_pizza )
print(cheapest_pizza)
print(pizza_and_prices)
print(num_two_dollar_slices)
print("We sell "+ str(num_pizza) +" different kinds of pizza!")
print(f"We sell {num_pizza} different kinds of pizza!")
print(three_cheapest)