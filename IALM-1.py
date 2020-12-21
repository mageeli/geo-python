from datetime import date
import sys


def print_message(message):
    print(message)


def main():
    message = "HI DS 540 Course"

    print_message(message)
    print("Today's date: {}".format(date.today()))
    print("Python version: {}".format(sys.version))


if __name__ == '__main__':
    main()


print('Enter your first name:')
first_name = input()
print('Hello, ' + first_name + ", from Python input() function")

mousa =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for m in mousa:
    print(m)


for letter in "Programming":
  if letter == "m":
    break
  print("Current Letter: ", letter)