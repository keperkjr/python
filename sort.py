def main():

    # Sort, multiple conditions
    arry = [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    # Order by even numbers, then numbers desc
    arry.sort(key=lambda x: (x % 2, -x))

    print(arry)

if __name__ == "__main__":
    main()