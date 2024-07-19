import sys

def main():
    args = sys.argv

    if len(args[1:]) <  1:
        print("Usage: goExe <name> [name2] [name3] ...")
        return 1

    print("Hello", end=" ")
    for arg in args[1:]:
        print(arg, end=" ")
    print("!")

    return 0

if __name__ == "__main__":
    sys.exit(main())


