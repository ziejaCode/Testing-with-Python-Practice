import unittest
import Widget as w

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = w.Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))te