from day4.passport import Passport


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        passports_data = [line.strip() for line in content]
        passport_data = []
        passports = []
        valid_passport_count = 0

        for line in passports_data:
            if line == '':
                passport = Passport(passport_data)
                passports.append(passport)
                passport_data = []
            else:
                for field in line.split(' '):
                    passport_data.append(field)
        passport = Passport(passport_data)
        passports.append(passport)

        for passport in passports:
            if Passport.validate_proper(passport):
                valid_passport_count += 1

        print(valid_passport_count)


if __name__ == "__main__":
    main()

