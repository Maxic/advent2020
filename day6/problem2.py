def count_common_chars(group):

    person_set_list = []

    for person in group:
        person_set = set()
        person_set.update(person)
        person_set_list.append(person_set)

    intersected_set = set.intersection(*person_set_list)

    return intersected_set.__len__()


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
            count_sum += count_common_chars(group)

        print(count_sum)

        
if __name__ == "__main__":
    main()
