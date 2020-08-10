# Find longest sequence of zeros in binary representation of an integer.

def count_binary_gap():
    num = int(input("Enter an integer "))
    bin_num = bin(num)[2:]

    print(('{} in binary is {}').format(num, bin_num))

    gap = 0
    for n in bin_num.split('1'):
        if n:
            gap += 1
            print(('Gap {}. Length {}').format(gap, len(n)))


if __name__ == '__main__':
    count_binary_gap()
