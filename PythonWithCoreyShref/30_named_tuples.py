from collections import namedtuple

# named tuple is light weight object works like regular tuple.
Color = namedtuple('Color',['Red','Green','Blue'])
color = Color(55, 155, 255)
print(color.Red)