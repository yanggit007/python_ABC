
print(dir(__builtins__))
print('\n')

x = 1
copyright = 'This is the global copyright.'

print(x)
print(copyright)
print(globals())
print(locals())
print('\n')


class Student:

    x = 2
    copyright = 'This is the class copyright.'

    print(x)
    print(copyright)
    print(globals())
    print(locals())
    print('\n')

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # global x, copyright
        x = 3
        copyright = 'This is the init copyright.'

        print('Student(name={}, age={})'.format(self.name, self.age))
        print(x)
        print(copyright)
        print(globals())
        print(locals())
        print('\n')

    def say(self):

        x = 4
        copyright = 'This is the self copyright.'

        print(x)
        print(copyright)
        print(globals())
        print(locals())
        print('\n')


s1 = Student('Jack', 20)
s1.say()

print(x)
print(copyright)
print(globals())
print(locals())
print('\n')
