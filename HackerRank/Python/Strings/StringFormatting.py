def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        d = str(i)
        o = str(oct(i)[2:])
        h = str(hex(i)[2:]).upper()
        b = str(bin(i)[2:])
        print(d.rjust(width), o.rjust(width), h.rjust(width), b.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
