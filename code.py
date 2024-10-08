import turtle


class Vector2:

  ZERO = None
  I_HAT = None
  J_HAT = None
 
  def __init__(self,first,second=None):
    if isinstance(first,(list,tuple,Vector2)):
      self.x = first[0]
      self.y = first[1]
    elif isinstance(first,(int,float)) and isinstance(second,(int,float)):
      self.x = first
      self.y = second
    elif isinstance(first,(complex)):
      self.x = first.real
      self.y = first.imag


  def __str__(self):
    return "<{x}, {y}>".format(x=self.x, y=self.y)


  def __repr__(self):
    return "Vector2({first},{second})".format(first=self.x, second=self.y)


  def __add__(self, other):
    return Vector2(self.x+other.x, self.y+other.y)
  

  def __sub__(self, other):
    return Vector2(self.f-other.f, self.y-other.y)


  def __mul__(self,other):
    if isinstance(other,Vector2):
      return self.x*other.x + self.y*other.y
    else:
      return Vector2(self.x*other, self.y*other)


  def __truediv__(self,other):
    return Vector2(self.x/other, self.y/other)


  def __abs__(self):
    return (self.x**2 + self.y**2)**.5


  def __getitem__(self, index):
    match index:
      case 0: return self.x
      case 1: return self.y
      

  def to_tuple(self):
    return (self.x, self.y)


  def comp(self,axis):
    match axis:
      case "x":
        return self*Vector2.I_HAT
      case "y":
        return self*Vector2.J_HAT


Vector2.ZERO = Vector2(0,0)
Vector2.I_HAT = Vector2(1,0)
Vector2.J_HAT = Vector2(0,1)



#-----------------------------------------------------------





class Monobehaviour:
 
  def __init__(self, name = "", size = 0, mass = 0):
    self.turtle = turtle.Turtle()
    self.name = ''
    self.size = 0
    self.mass = 0


  def __str__(self):
    if self.name:
      return "<Monobehavior named '{name}'>".format(name=self.name)
    else:
      return "<Monobehavior '{id}'>".format(id = id(self))


  def __repr__(self):
    return '''Monobehaviour("{name}")'''.format(name = self.name)

    
  def pos(self):
    return Vector2(self.turtle.pos())
 
 
  def CalcDist(self, other):
    return abs(self.pos()-other.pos())
