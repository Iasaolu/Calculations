train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
#CONVERT Fahrenheit TO CELCIUS
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9
  return c_temp
print(f_to_c(100))

#CONVERT CELCIUS TO FAHRENHEIT
def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32
  return f_temp
print(c_to_f(0))

#CALCULATE FORCE
def get_force(mass, acceleration):
  return mass*acceleration
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print("The GE train supplies "+ str(train_force) + " Newtons of force.")

#CALCULATE ENERGY
def get_energy(mass,c=3*10**8):
  return mass* c**2
bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies "+ str(bomb_energy) + " X Joules.")

#CALCULATE WORK
def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration) * distance
  return force
train_work=get_work(train_mass,train_acceleration,train_distance)
print(train_work)

