
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below:
def f_to_c(f_temp):
  return ( f_temp - 32) * 5/9
print(f_to_c(72))
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
def c_to_f(c_temp):
  return (c_temp * (9/5) + 32)
print(c_to_f(0))
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
print(get_force(10, 22))
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies X Newtons of force." + str(train_force))
def get_energy(mass, c):
  return mass*c**2
print(get_energy(bomb_mass, c))
bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies "+ str (bomb_energy) + " Joules.")
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+ str(train_work) +" Joules of work over " +  str(train_distance) +" meters.")
