from vector.vector import Vector
from range.range import MyRange
import range.range_with_gen

vec = Vector(10, 20)
# vector test code
# print(dir(vec))
# print(vec)
# print(eval(repr(vec)))
# print(vec * 2)
# print(vec + Vector(20, 30))
# print(vec.__dict__)

custom_range = MyRange(1, 10)
for i in custom_range:
    print(i)

