#if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")


  a = 200
  b = 33
  if b > a:
      print("b is greater than a")
  elif a == b:
      print("a and b are equal")
  else:
      print("a is greater than b")

      #Short Hand If

if a > b: print("a is greater than b")

# Short Hand If Else

a = 2
b = 330
print("A") if a > b else print("B")

'''
The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.
'''

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


    # while loop

    i = 1
    while i < 6:
        print(i)
        i += 1

    #The break Statement
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

        #continue Statement
        i = 0
        while i < 6:
            i += 1
            if i == 3:
                continue
            print(i)


   #For...loop

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)


