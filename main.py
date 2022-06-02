import random 
char = "123456789abcdefjhijklmnopqrstuvwxyz"
char_list=list(char)
password = input("input password: ")
guess = ''
while(guess != password):
  guess = random.choices(char_list, k=len(password))
  print(guess)
  guess = ''.join(guess)
  print(guess)

print("Your password is: "+ guess)
