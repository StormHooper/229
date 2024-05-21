from structures import Matrix, Vec
import copy


""" ----------------- PROBLEM 1 ----------------- """


def norm(v : Vec, p: int):
  """
  returns the p-norm of Vec v
  :param v: Vec type; the Vec object for which the norm will be applied
  :param p: int type; the integer determining the norm to be calculated
  :returns: float type; the norm as a float
  """
  return sum((abs(e) ** p for e in v)) ** (1 / p)


""" ----------------- PROBLEM 2 ----------------- """


def _ref(A : Matrix):
  """
    returns the Row Echelon Form of the Matrix A
    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the
            Row-Echelon Form of A
  """
  B = Matrix(copy.deepcopy(A.rows))
  m, n = B.dim()
  k = 1  # initializing the row-index of where to begin searching for the pivot
  for j in range(1, n + 1):
      
      p = _pivot_idx(k, j, B) # gets the index of the pivot at column j
      
      if p is None:
          continue
        
      if p != k: # we must swap row k with row p
          temp = B.get_row(k)
          B.set_row(k, B.get_row(p))
          B.set_row(p, temp)

      pivot = B.get_entry(k, j) # replace with the pivot at column j
      new_row = [elem / pivot for elem in B.get_row(k)] # new_row should be row k divided by the pivot
    
      B.set_row(k, new_row)

      # reducing the rows below row k by a scalar multiple of row k
      for i in range(k + 1, m + 1): 
          scalar = B.get_entry(i, j)
          reduced_row = [elem - scalar * val for elem, val in zip(B.get_row(i), new_row)] # reduced_row should be row i - scalar * row k
        
          B.set_row(i, reduced_row)
      k += 1
  return B


""" ----------------- PROBLEM 3 ----------------- """


def rank(A : Matrix):
  """
  returns the rank of the given Matrix object
  as an integer
  """
  # TODO: implement this function
  pass


""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A : Matrix, b : Vec):
  """
  returns the Row Echelon Form of the Matrix A
  :param A: Matrix type
  :returns: Matrix type; distinct Matrix object that is the
            Row-Echelon Form of A
  """
  new_cols = copy.deepcopy(A.cols)
  new_cols.append(b.elements)

  Ag = Matrix(new_cols).transpose()
  Arank = rank(A)
  Agrank = rank(Ag)
  m, n = A.dim()
  if Arank != Agrank:
      pass # FIXME: Replace with your implementation
  elif Arank < n:
      pass # FIXME: Replace with your implementation
  else:
      pass # FIXME: Replace with your implementation


""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S : set):
  """
  returns the solution to the system Ax = b
  :param A: Matrix type; the matrix of coefficients in the system of equations
  :param b: Vec type; the vector of constants in the system of equations
  :returns:
            - None type if the system does not have a solution
            - int type; if the system has infinitely-many solutions, the number of free
                        variables is returned
            - Vec type; the vector solution of the system if it has a unique solution
  """
  # TODO: Implement this function
  pass



""" HELPER METHOD"""
def _pivot_idx(i: int, j: int, A: Matrix):
    """
    finds the row index >= i of the first non-zero entry
    in column j of the given Matrix.  If no non-zero entry
    exists in column j at or after row i, then None is returned.
    :param i: int type; the row index of where to begin search
    :param j: int type; the column index of where to begin search
    :param A: Matrix type; the matrix of interest
    :return: int type or None type; if int, the row index of the
             first non-zero entry in column j.
    """
    column = A.get_col(j)
    for k in range(i - 1, len(column)):
        if column[k] != 0:
            return k + 1
    return None