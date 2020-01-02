def main(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

if __name__ == "__main__":
    main(2)
    main(2, [3, 2, 1])
    main(3)