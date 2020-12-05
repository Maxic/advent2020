def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        rows = 128
        columns = 8
        seat_ids = []

        bsp_list = [line.strip() for line in content]

        for bsp in bsp_list:

            # Calculate row
            upper_limit = rows
            lower_limit = 0
            front_back = bsp[:7]
            for letter in front_back:
                if letter == 'F':
                    upper_limit = lower_limit + int((upper_limit - lower_limit) / 2)
                if letter == 'B':
                    lower_limit = lower_limit + int((upper_limit - lower_limit) / 2)
            row = lower_limit

            # calculate column
            upper_limit = columns
            lower_limit = 0
            left_right = bsp[-3:]
            for letter in left_right:
                if letter == 'L':
                    upper_limit = lower_limit + int((upper_limit - lower_limit) / 2)
                if letter == 'R':
                    lower_limit = lower_limit + int((upper_limit - lower_limit) / 2)
            column = lower_limit

            # calculate seat id
            seat_id = (row * 8 ) + column

            seat_ids.append(seat_id)

        # Find missing seat
        seat_ids.sort()
        i = 0
        for seat_id in seat_ids:
            if (i+46) != seat_id:
                print(i+46)
                break
            i += 1


if __name__ == "__main__":
    main()
