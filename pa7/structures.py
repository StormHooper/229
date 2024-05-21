import math
from copy import deepcopy


class Vec:
    def __init__(self, contents : list =[]):
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
        elif type(other) == float or type(other) == int or type(other) == complex:  # scalar-vector multiplication

            return Vec([other * self.elements[i] for i in range(len(self.elements))])

    def __rmul__(self, other):
        """
        overloads the * operator to support
            - float * Vec
            - int * Vec
        """
        if type(other) == float or type(other) == int or type(other) == complex:
            return Vec([other * self.elements[i] for i in range(len(self.elements))])
        else:
            raise ValueError("ERROR: Incompatible types.")

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)

    def __rsub__(self, other):
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
        if type(other) == float or type(other) == int or type(other) == complex:
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

    def __hash__(self):
        """
        hash code this 'Vec' object
        :return:
        """
        key = sum([x for x in self.elements])
        d = len(self.elements)
        z = 193759204821
        w = 31
        return z * hash(key) % (2 ** w) >> (w - d)

"""---------------------------- MATRIX CLASS ----------------------------"""
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

    def transpose(self):
        """
        returns the transpose of this Matrix object
        :return: Matrix type; the transpose of this Matrix object
        """
        return Matrix(deepcopy(self.cols))
        
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
        mat_str = ""
        for row in self.rows:
            mat_str += str(row) + "\n"
        return mat_str

    # FIXME: Add the missing methods
