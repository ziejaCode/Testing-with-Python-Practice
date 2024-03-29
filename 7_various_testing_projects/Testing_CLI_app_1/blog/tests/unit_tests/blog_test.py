from unittest import TestCase
from blog import Blog
#from post import Post


class BlogUnitTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertEqual(0, len(b.posts))
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test author')

        self.assertEqual(b.__repr__(), 'Test by Test author (0 posts)')

    def test_json_no_posts(self):
        b = Blog('Test', 'Test author')

        self.assertDictEqual(b.json(), {
            'title': b.title,
            'author': b.author,
            'posts': [],
        })
