def main():
    N = input()
    n = len(N) - 1
    if N[n] == "2" or N[n] == "4" or N[n] == "5" or N[n] == "7" or N[n] == "9":
        print("hon")
    elif N[n] == "3":
        print("bon")
    else:
        print("pon")


if __name__ == "__main__":
    main()
