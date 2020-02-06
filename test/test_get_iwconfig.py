import unittest


class TestGetIwconfig(unittest.TestCase):
    def test_message_when_no_such_device(self):
        from iwlib import get_iwconfig

        with self.assertRaises(OSError) as context:
            get_iwconfig('no-such-device')

        self.assertIn("Could not get config for 'no-such-device'",
                      context.exception.strerror)
