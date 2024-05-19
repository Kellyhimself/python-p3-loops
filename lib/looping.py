#!/usr/bin/env python3

def happy_new_year():
  """Counts down from 10 to 1 and prints "Happy New Year!" at the end."""

  # Start at 10
  counter = 10

  # Keep counting down until we reach 1
  while counter >= 1:
    # Print the current counter
    print(counter)

    # Decrement the counter by 1
    counter -= 1

  # Print "Happy New Year!" when we reach 1
  print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    squared_elements = [element * element for element in int_list]
    return squared_elements

def fizzbuzz():
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)


