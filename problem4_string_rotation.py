#Given a string of size n, write a function to perform the following operations on a string.
# 1. Left(Or, anticlockwise) rotate the string by d elements. (d<=n)
# 2. Right(Or, clockwise) rotate the string by d elements. (d<=n)


def array_rot_left(n,d,arr):
  # n = len(arr), d = number of rotation, arr = array is the string.
  arr = list(arr)
  while d>0:
    i = 1
    temp = arr[0]
    while(i<n):
      arr[i-1] = arr[i]
      i +=1
    arr[n-1] = temp

    d -=1
    
  return "".join(arr)
  

def array_rot_right(n,d,arr):
  # n = len(arr), d = number of rotation, arr = array is the string.
  arr = list(arr)
  while d>0:
    i = n-1
    temp = arr[n-1]
    while(i>0):
      arr[i] = arr[i-1]
      i -=1
    arr[0] = temp

    d -=1

  return "".join(arr)

# driver function
if __name__ == "__main__":
  arr = input("Enter the string: ")
  n = len(arr)
  d = int(input("Enter the number of rotation: "))

  opn = int(input("Enter 1 for left rotation and 2 for right rotation: "))
  if opn == 1:
    print(array_rot_left(n,d, arr))
  elif opn == 2:
    print(array_rot_right(n,d, arr))
  else:
    print("Invalid input.")
    
