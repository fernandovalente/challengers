import unittest

'''
An array A consisting of N integers is given. Rotation of the array means that
each element is shifted right by one index, and the last element of the array
is moved to the first place. For example, the rotation of array
A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
'''

def rotate_list(list_num, num_rotation):
    for i in range(num_rotation):
        list_num.insert(0, list_num.pop())
    return list_num


class CyclicTest(unittest.TestCase):
    
    def test_rotate_1(self):
        self.assertEquals(rotate_list([3, 8, 9, 7, 6], 1), [6, 3, 8, 9, 7])

    def test_rotate_2(self):
        self.assertEquals(rotate_list([3, 8, 9, 7, 6], 2), [7, 6, 3, 8, 9])

    def test_rotate_3(self):
        self.assertEquals(rotate_list([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_rotate_4(self):
        self.assertEquals(rotate_list([3, 8, 9, 7, 6], 4), [8, 9, 7, 6, 3])

    def test_rotate_5(self):
        self.assertEquals(rotate_list([3, 8, 9, 7, 6], 5), [3, 8, 9, 7, 6])


if __name__ == '__main__':
    unittest.main()
