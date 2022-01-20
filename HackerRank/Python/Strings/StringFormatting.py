def print_formatted(number):
    for i in range(1, number+1):
        print("{}\t{}\t{}\t{}".format(str(i), str(oct(i)[2:]), str(hex(i)[2:]).upper(), str(bin(i)[2:])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
