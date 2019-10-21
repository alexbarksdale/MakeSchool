class Person(object):
    # setup function (tell python to run first)
    def __init__(self, person_name):
        self.name = person_name

    def say_hello(self):
        print(f'Sup yo {self.name}')


John = Person('greg')
John.say_hello()
