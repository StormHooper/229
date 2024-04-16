import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
  """
  translates the complex numbers of set S by z0
  :param S: set type; a set of complex numbers
  :param z0: complex type; a complex number
  :return: set type; a set consisting of points in S translated by z0
  """
  # FIXME: Implement this function
  translate_set = set()
  for i in S:
    translate_set.add(i + z0)
  # FIXME: Return correct output
  return translate_set


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
  """
  scales the complex numbers of set S by k.  
  :param S: set type; a set of complex numbers
  :param k: float type; positive real number
  :return: set type; a set consisting of points in S scaled by k
  :raise: raises ValueError if k <= 0       
  """
  # FIXME: Implement this function.
  if k <= 0:
    raise ValueError("k must be a positive real number")
  scaled_set = set()
  for i in S:
    scaled_set.add(i * k)
  # FIXME: Return correct output
  return scaled_set


""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
  """
    rotates the complex numbers of set S by tau radians.  
    :param S: set type; - set of complex numbers
    :param tau: float type; radian measure of the rotation value. 
                If negative, the rotation is clockwise.  
                If positive the rotation is counterclockwise. 
                If zero, no rotation.
    :returns: set type; a set consisting of points in S rotated by tau radians
  """
  # FIXME: Implement this function.
  rotated_set = set()
  cos_tau = math.cos(tau)
  sin_tau = math.sin(tau)
  for z in S:
    rotated_z = complex(z.real * cos_tau - z.imag * sin_tau, z.real * sin_tau + z.imag * cos_tau)
    rotated_set.add(rotated_z)
  # FIXME: Return correct output
  return rotated_set


""" ----------------- PROBLEM 4 ----------------- """
class Vec:
  def __init__(self, contents = []):
      """
      Constructor defaults to empty vector
      INPUT: list of elements to initialize a vector object, defaults to empty list
      """
      self.elements = contents
      return

  def __abs__(self):
      """
      Overloads the built-in function abs(v)
      :returns: float type; the Euclidean norm of vector v
      """
      # FIXME: Implement this method
      # FIXME: Return correct output
      return math.sqrt(sum(x**2 for x in self.elements))

  def __add__(self, other):
    """
      overloads the + operator to support Vec + Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the sum vector of this Vec and 'other' Vec
    """
      # FIXME: Finish the implementation
    if len(self.elements) != len(other.elements):
      raise ValueError("Vectors must have the same length")
      # FIXME: Return correct output
    return Vec([a + b for a, b in zip(self.elements, other.elements)])

  def __sub__(self, other):
    """
      overloads the - operator to support Vec - Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the difference vector of this Vec and 'other' Vec
    """
      # FIXME: Finish the implementation
    if len(self.elements) != len(other.elements):
      raise ValueError("Vectors must have the same length")
      # FIXME: Return correct output
    return Vec([a - b for a, b in zip(self.elements, other.elements)])



  def __mul__(self, other):
      """
      Overloads the * operator to support 
          - Vec * Vec (dot product) raises ValueError if vectors are not 
            same length in the case of dot product; returns scalar
          - Vec * float (component-wise product); returns Vec object
          - Vec * int (component-wise product); returns Vec object

      """
      if type(other) == Vec: #define dot product
          # FIXME: Complete the implementation
        if len(self.elements) != len(other.elements):
          raise ValueError("Vectors must have the same length")
          # FIXME: Return the correct output
        return sum(a * b for a, b in zip(self.elements, other.elements))

      elif type(other) == float or type(other) == int: #scalar-vector multiplication
          # FIXME: Complete the implementation
          # FIXME: Return the correct output
          return Vec([x * other for x in self.elements])


  def __rmul__(self, other):
      """
      Overloads the * operation to support 
          - float * Vec; returns Vec object
          - int * Vec; returns Vec object
      """
      # FIXME: Complete the implementation
      # FIXME: Return the correct output
      return self.__mul__(other)



  def __str__(self):
      """returns string representation of this Vec object"""
      return str(self.elements) # does NOT need further implementation