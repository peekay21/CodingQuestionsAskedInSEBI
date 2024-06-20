# dec2hexadec is function which convert the decimal number to hexadecimal number. 
def dec2hexadec(n):
  hex = '' # string
  while n > 0: 
    hex += str(n % 16) # append the remainder of 16 to the string
    n //= 16 # divide the number by 16

  return hex 

n = int(input('enter a number - ')) #take input from user
print(str(n) + ' in hexadecimal is ' + dec2hexadec(n))  # display the hexadecimal number.
