def check_age():

  age = int(input("Enter your age: "))

  if age < 0:
    print("Invalid age. Age cannot be negative.")
  elif age < 13:
    print("You are a minor.")
    if age < 18:
      print("You are a child.")
    else:
      print("You are a teenager.")
  elif age < 65:
    print("You are an adult.")
  else:
    print("You are a senior citizen.")
check_age()