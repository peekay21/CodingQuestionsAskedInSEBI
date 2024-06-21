# Problem5: Write a program to find the difference between two diagonal matrix.


# function to find the difference between two diagonal matrix
def diff_in_diagonal_matrix(a,b):
  arow = len(a)
  acol = len(a[0])
  brow = len(b)
  bcol = len(b[0])
  diff = 0
  if arow == brow and acol == bcol:
    diff = [[0 for _ in range(acol)] for _ in range(arow)]

    for i in range(len(a)):
      for j in range(len(a)):
        if i == j:
          diff[i][j] += a[i][j] - b[i][j]


  return 0 if diff==0 else diff

# driver function
if __name__ == "__main__":
  # a and b are the two matrix
  a = [[5, 0, 0], [0, 4,0], [0,0,1]]
  
  b = [[8, 0, 0], [0, 6,0], [0,0,9]]

  #output of the both function
  print(diff_in_diagonal_matrix(a,b))
