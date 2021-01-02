from day8.console import Console

def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        program = [line.strip().split(' ') for line in content]

        console = Console(program)

        # alter program
        for line in program:
            if line[0] == 'jmp':
                line[0] = 'nop'
                console = Console(program)
                console.run()
                if console.corrupted:
                    line[0] = 'jmp'
                else:
                    print(console.accumulator)
            elif line[0] == 'nop':
                line[0] = 'jmp'
                console = Console(program)
                console.run()
                if console.corrupted:
                    line[0] = 'nop'
                else:
                    print(console.accumulator)
            else:
                continue


if __name__ == "__main__":
    main()
