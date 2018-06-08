"""Number of bit changes to convert one integer to another."""


def bits_to_convert(a, b):
    c = a ^ b
    k = c.bit_length()
    count = 0
    while k > 0:
        if c & 1 == 1:
            count += 1
        c = c >> 1
        k -= 1
        
    return count


import unittest


class Test(unittest.TestCase):

    def test_bits_to_convert(self):
        self.assertEqual(bits_to_convert(0,0), 0)       
        self.assertEqual(bits_to_convert(1,1), 0)
        self.assertEqual(bits_to_convert(100,100), 0)
        self.assertEqual(bits_to_convert(1,0), 1)
        self.assertEqual(bits_to_convert(0,1), 1)
        self.assertEqual(bits_to_convert(3,1), 1)
        self.assertEqual(bits_to_convert(1,3), 1)
        self.assertEqual(bits_to_convert(2,1), 2)
        self.assertEqual(bits_to_convert(1,2), 2)
        self.assertEqual(bits_to_convert(-1,0), 1)
        self.assertEqual(bits_to_convert(-1,1), 1)
        self.assertEqual(bits_to_convert(-1,-2), 1)
        self.assertEqual(bits_to_convert(-1,2), 1)
        self.assertEqual(bits_to_convert(1234, 1234 ^ 32), 1)


if __name__ == '__main__':
    unittest.main()
