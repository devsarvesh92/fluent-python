from vector.vector import Vector

vec = Vector(10, 20)
print(dir(vec))
print(vec)
print(eval(repr(vec)))
print(vec * 2)
print(vec + Vector(20, 30))
print(vec.__dict__)