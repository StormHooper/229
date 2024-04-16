"""PROBLEM 1"""
def hello(subject):
    return f"Hello, {subject}!"

"""PROBLEM 2"""
class Bug:
  def __init__(self, name, position = [0, 0]):
    self.name = name
    self.position = position

  def move_up(self, units):
    self.position[1] += units

  def move_down(self, units):
    self.position[1] -= units

  def move_right(self, units):
    self.position[0] += units

  def move_left(self, units):
    self.position[0] -= units

  def __str__(self):
    return f"Name: {self.name}\nPosition: ({self.position[0]}, {self.position[1]})"
    