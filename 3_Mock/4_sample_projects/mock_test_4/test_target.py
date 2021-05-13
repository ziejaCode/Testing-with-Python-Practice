import target
import unittest
from mock import Mock



class TweetTest(unittest.TestCase):
    def test_example(self):
        mock_target = Mock()
        target.tweet(mock_target, "message")
        #mock_twitter.PostUpdate.assert_called_with("message")

    def test_example2(self):
        mock_twitter = Mock()
        short_tweeter.tweet(mock_twitter, "message!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        mock_twitter.PostUpdate.assert_called_with("message")

if __name__ == '__main__':
    unittest.main()
