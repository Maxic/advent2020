def main():

    invalid_number = 138879426

    with open("input.txt", "r+") as file:
        content = file.readlines()

        content = [int(line.strip()) for line in content]

        # For the invalid number, we should find a contiguous set of which the sum is the invalid number.
        # Step 1, remove all values bigger than invalid_number.
        cleaned_content = content.copy()
        for value in content:
            if value >= invalid_number-min(content):
                cleaned_content.remove(value)
        content = cleaned_content

        # Step 2, loop through all values,
        # starting at that position, create sets from neighbouring numbers.
        # If the sum of a set exceeds invalid_number, stop
        # If the sum of a set equals invalid_number, stop and print result
        for i in range(0, content.__len__()):
            sum_set = set()
            for j in range(i, content.__len__()):
                sum_set.add(content[j])
                if sum(sum_set) == invalid_number:
                    print(sum_set)
                    print(min(sum_set) + max(sum_set))
                    break
                if sum(sum_set) > invalid_number:
                    break


if __name__ == "__main__":
    main()



# Possible solution

