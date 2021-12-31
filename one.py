from pprint import pprint
x = 10
def func():
    print(locals())
    print(globals() == locals())
print(globals() == locals())
func()
