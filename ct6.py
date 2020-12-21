import numpy as np

my_strings = np.array(['M', 'u', 's', 'a', 'a', 'g', 'l', 'i', 'u'])


def main(string):
  #will join
  string_join = ''.join(string)
  print(string_join)
  #after the joining the string will return them
  string_split = string_join.split()

  print(string_split)
  # main function
if __name__ == '__main__':
    main(my_strings)








