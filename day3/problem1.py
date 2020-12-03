def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        forest = [row.strip() for row in content]
        width = forest[0].__len__()

        x_pos = 0
        y_pos = 0
        tree_count = 0

        while y_pos < forest.__len__():
            if forest[y_pos][x_pos % width] == '#':
                tree_count += 1
            x_pos += 3
            y_pos += 1

        print(tree_count)

if __name__ == "__main__":
    main()

