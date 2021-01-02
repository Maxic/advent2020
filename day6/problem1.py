def count_unique_chars(group):
    # first create a single string
    group = ''.join(group)
    group_set = set()

    # then count unique character by using a set
    for char in group:
        group_set.add(char)

    return group_set.__len__()


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        content = [line.strip() for line in content]
        groups = []
        group = []
        count_sum = 0

        for line in content:
            if line == '':
                groups.append(group)
                group = []
            else:
                group.append(line)
        groups.append(group)

        for group in groups:
            count_sum += count_unique_chars(group)

        print(count_sum)


if __name__ == "__main__":
    main()
