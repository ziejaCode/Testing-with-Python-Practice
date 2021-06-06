from unittest import main, TestCase
from unittest.mock import Mock


class FooBar:
    def foo(self, argument: int) -> int:
        return argument ** 2


def function(foobar: FooBar, number: int) -> int:
    return foobar.foo(number * 2)


class FunctionTests(TestCase):
    def test_function_for_10_calls_foobar_with_20(self):
        # use a real instance, just wrap it
        wrapping_mock = Mock(wraps=FooBar())

        result = function(wrapping_mock, 10)
        print('this is', type(result))
        wrapping_mock.foo.assert_called_once_with(20)


if __name__ == '__main__': main()