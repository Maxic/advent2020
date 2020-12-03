def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        forest = [row.strip() for row in content]
        width = forest[0].__len__()

        x_pos = 0
        y_pos = 0
        tree_count = 0

        trees_slope_1 = count_trees(forest, tree_count, width, x_pos, y_pos, 1, 1)

        trees_slope_2 = count_trees(forest, tree_count, width, x_pos, y_pos, 3, 1)

        trees_slope_3 = count_trees(forest, tree_count, width, x_pos, y_pos, 5, 1)

        trees_slope_4 = count_trees(forest, tree_count, width, x_pos, y_pos, 7, 1)

        trees_slope_5 = count_trees(forest, tree_count, width, x_pos, y_pos, 1, 2)

        print(trees_slope_1 * trees_slope_2 * trees_slope_3 * trees_slope_4 * trees_slope_5)


def count_trees(forest, tree_count, width, x_pos, y_pos, x_move, y_move):
    while y_pos+y_move <= forest.__len__():
        if forest[y_pos][x_pos % width] == '#':
            tree_count += 1
        x_pos += x_move
        y_pos += y_move
    return tree_count


if __name__ == "__main__":
    main()

