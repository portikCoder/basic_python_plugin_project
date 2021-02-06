#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.

import unittest

from mainmodulename.__main__ import main


class MyTestCase(unittest.TestCase):
    def test_e2e(self):
        raised_e: Exception = None
        try:
            main()
        except Exception as e:
            raised_e = e

        self.assertIsNone(raised_e, f"Exception raised: {raised_e}")


if __name__ == '__main__':
    unittest.main()
