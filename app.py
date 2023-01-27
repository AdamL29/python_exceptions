my_str = "4"
my_num = 3

try:
    print(my_str+my_num)
except TypeError as e:
    print(e)
    print('You cannot do that')