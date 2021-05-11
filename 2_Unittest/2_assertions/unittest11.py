import unittest


class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))


class TestEmployee(unittest.TestCase):

    def test_email_atribute(self):
        self.assertTrue(hasattr(Employee, 'email'), msg='Employee has no such attribute')

    def test_tax_atribute(self):
        self.assertTrue(hasattr(Employee, 'tax'), msg='Employee has no such attribute')

    def test_fake_atribute(self):
        self.assertTrue(hasattr(Employee, 'apply_bonus'), msg='Employee has no such attribute')

if __name__=='__main__':
    unittest.main()