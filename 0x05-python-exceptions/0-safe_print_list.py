#!/usr/pin/python3
def safe_print_list(my_list=[], x=0):
	for y in my_list:
        try:
			print("{:d}".format(y), end="")
		except IndexError:
			break
	print()
	return y + 1
