name = input("Введите имя: ")
login = "Dima"
# name = "Yo"
if name == login: # <- False
  # Выражение True
  print("Hello", name)
elif len(name) < 3: # <- True
  print("Такое имя недопустимо")
elif name == "Yo": # <- True
  print("Yo, bro")
else:
  # Выражение False
  print("Hello, user!")

print("The end")