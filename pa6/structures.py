import math
from copy import deepcopy


class Vec:
    def __init__(self, contents=[]):
        """
        constructor defaults to empty vector
        accepts list of elements to initialize a vector object with the
        given list
        """
        self.elements = contents
        return

    def __abs__(self):
        """
        overloads the built-in function abs(v)
        :return: float type; the Euclidean norm of vector v
        """
        return math.sqrt(sum([e ** 2 for e in self.elements]))

    def __add__(self, other):
        """
        overloads the + operator to support Vec + Vec
        :raises: ValueError if vectors are not same length
        """
        if len(self.elements) == len(other.elements):
            return Vec([self.elements[i] + other.elements[i] for i in range(len(self.elements))])
        else:
            raise ValueError("ERROR: Vectors must be same length")

    def __mul__(self, other):
        """
        overloads the * operator to support
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
        :raises: ValueError if vectors are not of same length in Vec * Vec operation
        """
        if type(other) == Vec:  # define dot product
            if len(self.elements) == len(other.elements):
                return sum([self.elements[i] * other.elements[i] for i in range(len(self.elements))])
            else:
                raise ValueError("ERROR: Vectors must be same length")
        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            return Vec([other * self.elements[i] for i in range(len(self.elements))])

    def __rmul__(self, other):
        """
        overloads the * operator to support
            - float * Vec
            - int * Vec
        """
        if type(other) == float or type(other) == int:
            return Vec([other * self.elements[i] for i in range(len(self.elements))])
        else:
            raise ValueError("ERROR: Incompatible types.")

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)

    def __sub__(self, other):
        """
        overloads the - operator to support Vec - Vec
        :raises: ValueError if vectors are not same length
        """
        if type(other) == Vec and len(self.elements) == len(other.elements):
            return Vec([self.elements[i] - other.elements[i] for i in range(len(self.elements))])
        elif type(other) == Vec:
            raise ValueError("ERROR: Vectors must be same length")
        else:
            raise ValueError("ERROR: Incompatible types.")

    def __truediv__(self, other):
        if type(other) == float or type(other) == int:
            return Vec([self.elements[i]/other for i in range(len(self.elements))])
        else:
            raise ValueError("ERROR: Incompatible types.")


    def __len__(self):
        """
        overloads the len() function to support len(Vec)
        :return: int type; the number of elements in this Vec object
        """
        return len(self.elements)

    def __eq__(self, other):
        """
        overloads the == operator to support Vec == Vec
        :raises: TypeError if other is not Vec type
        :return: True if the elements of self rounded to four (4) decimal
                  places are the same as the elements of other rounded to
                  four (4) decimal places
        """
        if type(other) != Vec:
            raise TypeError(f"{self} == {other} is not defined")
        rounded_self = [round(x, 4) for x in self.elements]
        rounded_other = [round(x, 4) for x in other.elements]
        return rounded_other == rounded_self

    def __getitem__(self, i: int):
        """
        overloads the slicing operator [] to support Vec object slicing
        :param i: the index of the desired element
        :return: the object at index of i of this Vec object
        """
        return self.elements[i]

    def __iter__(self):
        """
        overloads the list() function so that list(Vec) returns
        the elements of the vector in a Python list
        :return: list type; the elements of the vector
        """
        return iter(self.elements)



class Matrix:
  
  def __init__(self, rows=[]):
    """
    initializes a Matrix with given rows
    :param rows: the list of rows that this Matrix object has
    """
    self.rows = rows
    self.cols = []
    self._construct_cols()
    return
    
  # FIXME: Copy-paste the missing methods from your Matrix class from pa5.py here
  def set_row(self, i, new_row):
    '''
    Changes the i-th row to be the list new_row. 
    If new_row is not the same length as the existing rows, 
    then method raises a ValueError with the message "Incompatible row length."
    '''
    if len(new_row) != len(self.rows[0]):
      raise ValueError("Incompatible row length.")
    self.rows[i-1] = new_row
    self._construct_cols()
    return self

  def set_col(self, j, new_col):
    '''
    Changes the j-th column to the list new_col.
    If new_col is not the same length as the existing columns, 
    then the method raises a ValueError with the message "Incompatible column length."
    '''
    if len(new_col) != len(self.cols[0]):
      raise ValueError("Incompatible column length.")
    self.cols[j-1] = new_col
    self._construct_rows()
    return self

  def set_entry(self, i, j, val):
    '''
    Changes the existing aij entry to val. 
    Raises IndexError if i does not satisfy 1 <= i <= m or j does not satisfy 
    1 <= j <= n, where m = number of rows and n = number of columns.
    '''
    if not (1 <= i <= len(self.rows) and 1 <= j <= len(self.cols)):
      raise IndexError("Index out of range.")
    self.rows[i-1][j-1] = val
    self._construct_cols()

  def get_row(self, i):
    '''
    returns the i-th row as a list. Raises IndexError if i does not satisfy 1 <= i <= m.
    '''
    if not (1 <= i <= len(self.rows)):
      raise IndexError("Index out of range.")
    return self.rows[i-1]

  def get_col(self, j):
    '''
    returns the j-th column as a list. Raises IndexError if j does not satisfy 1 <= j <= n.
    '''
    if not (1 <= j <= len(self.cols)):
      raise IndexError("Index out of range.")
    return self.cols[j-1]

  def get_entry(self, i, j):
    '''
    returns the existing aij entry in the matrix. 
    Raises IndexError if i does not satisfy 1 <= i <= m or j does not satisfy 1 <= j <= n, 
    where m = number of rows and n = number of columns.
    '''
    if not (1 <= i <= len(self.rows) and 1 <= j <= len(self.cols)):
      raise IndexError("Index out of range.")
    return self.rows[i-1][j-1]

  def get_columns(self):
    '''
    return the list of lists that are the columns of the matrix object
    '''
    return self.cols

  def get_rows(self):
    '''
    return the list of lists that are the rows of the matrix object
    '''
    return self.rows

  def get_diag(self, k):
    '''
    returns the k-th diagonal of a matrix where k = 0 returns the main diagonal, 
    k > 0 returns the diagonal beginning at a1(k+1),
    and k < 0 returns the diagonal beginning at a1(-k+1) where m = number of rows.
    '''
    m, n = len(self.rows), len(self.cols)
    if k == 0:
      return [self.rows[i][i] for i in range(min(m, n))]
    elif k > 0:
      return [self.rows[i][i+k] for i in range(min(m, n - k))]
    elif k < 0:
      return [self.rows[i-k][i] for i in range(min(m + k, n))]

  def _construct_cols(self):
      """
      HELPER METHOD: Resets the columns according to the existing rows
      """
      self.cols = []
      for col_i in range(len(self.rows[0])):
        column = [row[col_i] for row in self.rows]
        self.cols.append(column)
      return

  def _construct_rows(self):
      """
      HELPER METHOD: Resets the rows according to the existing columns
      """
      self.rows = []
      for row_i in range(len(self.cols[0])):
        row = [col[row_i] for col in self.cols]
        self.rows.append(row)
      return

  def __add__(self, other):
      """
      overloads the + operator to support Matrix + Matrix
      :param other: the other Matrix object
      :raises: ValueError if the Matrix objects have mismatching dimensions
      :raises: TypeError if other is not of Matrix type
      :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
      """
      if not isinstance(other, Matrix):
        raise TypeError("Unsupported operand types.")
      if self.dim() != other.dim():
        raise ValueError("Incompatible dimensions.")

      rows = []
      for i in range(len(self.rows)):
        new_row = [self.rows[i][j] + other.rows[i][j] for j in range(len(self.rows[0]))]
        rows.append(new_row)
      return Matrix(rows)

  def __sub__(self, other):
      """
      overloads the - operator to support Matrix - Matrix
      :param other:
      :raises: ValueError if the Matrix objects have mismatching dimensions
      :raises: TypeError if other is not of Matrix type
      :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
      """
      if not isinstance(other, Matrix):
        raise TypeError("Unsupported operand types.")
      if self.dim() != other.dim():
        raise ValueError("Incompatible dimensions.")

      rows = []
      for i in range(len(self.rows)):
        new_row = [self.rows[i][j] - other.rows[i][j] for j in range(len(self.rows[0]))]
        rows.append(new_row)
      return Matrix(rows)

  def __mul__(self, other):
      """
      overloads the * operator to support
          - Matrix * Matrix
          - Matrix * Vec
          - Matrix * float
          - Matrix * int
      :param other: the other Matrix object
      :raises: ValueError if the Matrix objects have mismatching dimensions
      :raises: TypeError if other is not of Matrix type
      :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
      """
      matrix_mul = []

      if type(other) == float or type(other) == int:
        for i in range(len(self.rows)):
          matrix_mul.append([j * other for j in self.rows[i]])

      elif type(other) == Matrix:
        if len(self.cols) != len(other.rows):
          raise ValueError("Incompatible dimensions.")
        else:
          for i in range(len(self.rows)):
            listc = self.get_row(i+1)
            listb = []
            for j in range(len(other.cols)):
              temp0 = other.get_col(j+1)
              temp = [listc[k]*temp0[k] for k in range(len(listc))]
              sums = sum(temp)
              listb.append(sums)
            matrix_mul.append(listb)

      elif type(other) == Vec:
        if (len(other) != len(self.cols)):
          raise ValueError("Incompatible dimensions.")
        c = 0
        for i in range(len(self.rows)):
          c = 0
          for j in range(len(self.cols)):
            c += self.get_entry(i+1, j+1) * other[j]
          matrix_mul.append(c)
        return(Vec(matrix_mul))

      else:
        raise TypeError(f"Matrix * {type(other)} is not supported.")
      return Matrix(matrix_mul)

  def __rmul__(self, other):
      """
      overloads the * operator to support
          - float * Matrix
          - int * Matrix
      :param other: the other Matrix object
      :raises: ValueError if the Matrix objects have mismatching dimensions
      :raises: TypeError if other is not of Matrix type
      :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
      """
      matrix_mul = []
      if type(other) == float or type(other) == int:
          for i in range(len(self.rows)):
            matrix_mul.append([j * other for j in self.rows[i]])
      else:
          raise TypeError(f"{type(other)} * Matrix is not supported.")
      return Matrix(matrix_mul)

  '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

  def dim(self):
      """
      gets the dimensions of the mxn matrix
      where m = number of rows, n = number of columns
      :return: tuple type; (m, n)
      """
      m = len(self.rows)
      n = len(self.cols)
      return (m, n)

  def __str__(self):
      """prints the rows and columns in matrix form """
      mat_str = ""
      for row in self.rows:
          mat_str += str(row) + "\n"
      return mat_str

  def __eq__(self, other):
      """
      overloads the == operator to return True if
      two Matrix objects have the same row space and column space
      """
      if type(other) != Matrix:
          return False
      this_rows = [round(x, 3) for x in self.rows]
      other_rows = [round(x, 3) for x in other.rows]
      this_cols = [round(x, 3) for x in self.cols]
      other_cols = [round(x, 3) for x in other.cols]

      return this_rows == other_rows and this_cols == other_cols

  def __req__(self, other):
      """
      overloads the == operator to return True if
      two Matrix objects have the same row space and column space
      """
      if type(other) != Matrix:
          return False
      this_rows = [round(x, 3) for x in self.rows]
      other_rows = [round(x, 3) for x in other.rows]
      this_cols = [round(x, 3) for x in self.cols]
      other_cols = [round(x, 3) for x in other.cols]

      return this_rows == other_rows and this_cols == other_cols
  # FIXME: Copy-paste the missing methods from your Matrix class from pa5.py here
  
  def transpose(self):
    """
    returns the transpose of this matrix
    :return: Matrix type; distinct Matrix object that represents the transpose of this matrix
    """
    rows = deepcopy(self.cols)
    return Matrix(rows)
  