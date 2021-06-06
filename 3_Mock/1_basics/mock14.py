from unittest import main, TestCase
from unittest.mock import Mock


def can_cancel_order(order_id, shipping_system):
    status = shipping_system.get_status(order_id)
    if status in ('SENT', 'DELIVERED'):
        return False
    return True


class CanCancelOrderTest(TestCase):
    def test_can_cancel_order_with_status_sent_false(self):
        self.assertFalse(can_cancel_order(1, Mock(get_status=Mock(return_value='SENT'))))

    def test_can_cancel_order_with_status_sent_true(self):
        self.assertTrue(can_cancel_order(1, Mock(get_status=Mock(return_value=''))))



if __name__ == '__main__': main()