from unittest import TestCase
from blog import Blog
from post import Post


class BlogIntegrationTest(TestCase):

    def test_create_post(self):
        b = Blog('Test', 'Test author')
        p = Post('Music', 'the doors')
        b.create_post(p.title, p.content)

        self.assertEqual('Music : the doors', b.posts[0].__repr__())


