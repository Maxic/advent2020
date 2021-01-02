from day8.console import Console

def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        program = [line.strip().split(' ') for line in content]

        console = Console(program)
        console.run()
        print(console.pointer_passed)
        print(console.accumulator)


if __name__ == "__main__":
    main()
