import unittest

'''
Find longest sequence of zeros in binary representation of an integer.
https://app.codility.com/programmers/lessons/1-iterations/
'''

def return_binary_num(num):
    return bin(num)[2:]


def count_binary_gap(binary):
    response, gap = [], 0

    for n in binary.split('1'):
        if n:
            gap += 1
            response.append(('Gap {}. Length {}').format(gap, len(n)))

    return response


class GapCountTest(unittest.TestCase):

    def test_bin_9(self):
        self.assertEqual(return_binary_num(9), '1001')

    def test_bin_10(self):
        self.assertEqual(return_binary_num(10), '1010')

    def test_bin_529(self):
        self.assertEqual(return_binary_num(529), '1000010001')
    
    def test_bin_5000(self):
        self.assertEqual(return_binary_num(5000), '1001110001000')

    def test_gap_bin_9(self):
        num = return_binary_num(9)
        self.assertEqual(count_binary_gap(num), ['Gap 1. Length 2'])

    def test_gap_bin_10(self):
        num = return_binary_num(10)
        self.assertEqual(
            count_binary_gap(num), ['Gap 1. Length 1', 'Gap 2. Length 1']
        )
    
    def test_gap_bin_529(self):
        num = return_binary_num(529)
        self.assertEqual(
            count_binary_gap(num), ['Gap 1. Length 4', 'Gap 2. Length 3']
        )
    
    def test_gap_bin_5000(self):
        num = return_binary_num(5000)
        self.assertEqual(
            count_binary_gap(num), [
                'Gap 1. Length 2',
                'Gap 2. Length 3',
                'Gap 3. Length 3'
            ]
        )


if __name__ == '__main__':
    unittest.main()
