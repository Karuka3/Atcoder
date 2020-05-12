def main():
    N = int(input())
    book = [input().split() for i in range(N)]
    for i, j in enumerate(book):
        j[1] = int(j[1])
        j.append(i + 1)

    book.sort(key=lambda x: x[1], reverse=True)
    book.sort(key=lambda x: x[0])

    for i in book:
        print(i[2])


if __name__ == "__main__":
    main()
