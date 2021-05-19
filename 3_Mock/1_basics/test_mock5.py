from unittest.mock import patch
from mock5 import Programmer


programmer = Programmer().add_tech('python') \
    .add_tech('java') \
    .add_tech('sql') \
    .add_tech('aws') \
    .add_tech('django')



def tech_get_random_tech():
    with patch('random.choice') as mock_random:
        mock_random.return_value = 'sql'
        return programmer.get_random_tech()

print("testing ", tech_get_random_tech())