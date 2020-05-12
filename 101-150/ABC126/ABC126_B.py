def main():
    S = input()
    a = S[0:2]
    b = S[2:4]

    if 1 <= int(a) <= 12:
        if 1 <= int(b) <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= int(b) <= 12:
            print("YYMM")
        else:
            print("NA")


if __name__ == "__main__":
    main()
