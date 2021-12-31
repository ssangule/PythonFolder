p = "Arya College"
width = 30

print(repr(p))
p1 = p.ljust(width)
print("left just:", repr(p1))
p2 = p.rjust(width, "-")
print("right just: ", repr(p2))
p3 = p.center(width, "-")
print("center: ", repr(p3))
