favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "u":
    counter = counter + 1
print(counter)


def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False


print(letter_check("strawberry", "a"))

def contains(big_string, little_string):
  return little_string in big_string
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
print(common_letters("banana", "cream")
)
# => True
print(common_letters("blue", "strawberry"))
# => False
message = "Bonjour"
nb_caracteres = len(message)
print(f"Le mot '{message}' contient {nb_caracteres} caractères.")


def username_generator(first_name, last_name):
  if len(first_name) < 3:
    user_name = first_name
  else:
    user_name = first_name[0:3]  # Prend les 3 premiers caractères

  if len(last_name) < 4:
    user_name += last_name
  else:
    user_name += last_name[0:4]  # Prend les 4 premiers caractères

  return user_name


def password_generator(user_name):
  password = ""
  for i in range(len(user_name)):  # Boucle sur tous les indices de la chaîne
    password += user_name[i - 1]  # Décalage circulaire des caractères
  return password


# Appel des fonctions avec affichage des résultats
generated_username = username_generator("david", "jimenez")
print("Generated username:", generated_username)

generated_password = password_generator(generated_username)
print("Generated password:", generated_password)