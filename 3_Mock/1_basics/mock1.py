from unittest.mock import Mock
import random

first_mock = Mock(name = 'First mock')
print(first_mock)

techs = ['python', 'sql', 'java', 'aws', 'c++']

random.choice = Mock(return_value='aws')
print(random.choice())