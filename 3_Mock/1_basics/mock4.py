import random
from unittest.mock import Mock


class Programmer:

    def __init__(self):
        self.tech_names = []

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if not name in self.tech_names:
            self.tech_names.append(name)
            return self
        return self

    def get_random_tech(self):
        return random.choice(self.tech_names)


programmer = Programmer().add_tech('python') \
    .add_tech('java') \
    .add_tech('sql') \
    .add_tech('aws') \
    .add_tech('django')
  
random.choice = Mock(return_value='python')

mock = Mock(return_value='python')
programmer = mock
#print(prog.get_random_tech())
print(programmer.get_random_tech())