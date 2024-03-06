def create_integer_set():
    input_str = input("Enter integers separated by spaces: ")
    integers = map(int, input_str.split())
    return set(integers)

def main():
    print("Enter integers for the first set:")
    set1 = create_integer_set()

    print("Enter integers for the second set:")
    set2 = create_integer_set()

    common_elements = set1.intersection(set2)
    
    print("Common elements in both sets:", common_elements)

if __name__ == "__main__":
    main()
