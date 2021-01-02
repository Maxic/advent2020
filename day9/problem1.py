def main():

    preamble_length = 25

    with open("input.txt", "r+") as file:
        content = file.readlines()

        content = [int(line.strip()) for line in content]

        # Start after the preamble
        pointer = preamble_length

        # Loop through all values
        for pointer in range(pointer, content.__len__()):
            if not pair_available(content[pointer], content[pointer-preamble_length:pointer]):
                print(content[pointer])


def pair_available(sum, list):
    for i in range(0, list.__len__()):
        for j in range(i, list.__len__()):
            if list[i] + list[j] == sum:
                return True
    return False


if __name__ == "__main__":
    main()
