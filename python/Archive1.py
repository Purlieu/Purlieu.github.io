from functools import reduce

def main():
    numberlist = []
    output = ''
    for x in range(0, 1000):
        if x % 3 == 0 or x % 5 == 0:
            numberlist.append(x)
    output = reduce(lambda x, y: x + y, numberlist)
    print(output)

if __name__== "__main__":
    main()