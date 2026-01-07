class CSSstudent:
  stream = "cse"




  def __init__(self,roll):

    self.roll = roll
  def setAddress(self, adress):
    self.setAddress = adress

  def getAddress(self):
    return self.getAddress
  
add = CSSstudent(101)
add.setAddress("Pune, Maharashtra")
print(add.getAddress())

a = CSSstudent(101)
b = CSSstudent(102)

print(a.stream)
print(b.stream)
print(a.roll)

print(CSSstudent.stream)


