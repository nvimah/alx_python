# get the range of numbers from 0 to 98
number= range(0,99)
#loop around the numbers
for i in range(0,99):
    hex_value= "{0:x}".format(i)
#convert the numbers to hexadecimal
    print(i," = 0*{}" .format(hex_value) )
#print with a string format 