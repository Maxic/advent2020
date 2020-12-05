import re

class Passport:
    def __init__(self, data):
        self.data = data
        self.byr = ''
        self.iyr = ''
        self.eyr = ''
        self.hgt = ''
        self.hcl = ''
        self.ecl = ''
        self.pid = ''
        self.cid = ''
        self.designate()

    def designate(self):
        for data_point in self.data:
            key = data_point.split(':')[0]
            value = data_point.split(':')[1]

            if key == 'byr':
                self.byr = value
            if key == 'iyr':
                self.iyr = value
            if key == 'eyr':
                self.eyr = value
            if key == 'hgt':
                self.hgt = value
            if key == 'hcl':
                self.hcl = value
            if key == 'ecl':
                self.ecl = value
            if key == 'pid':
                self.pid = value
            if key == 'cid':
                self.cid = value

    def validate(self):

        # Birth year validation
        if self.byr == '':
            return False

        # Issue year validation
        if self.iyr == '':
            return False

        # Expiration Year validation
        if self.eyr == '':
            return False

        # Height validation
        if self.hgt == '':
            return False

        # Hair color validation
        if self.hcl == '':
            return False

        # Eye color validation
        if self.ecl == '':
            return False

        # Passport ID validation
        if self.pid == '':
            return False

        # Country ID validation
        # No check needed for cid
        return True

    def validate_proper(self):

        # Birth year validation
        if not re.search(r'^(?:[0-9]{4})$', self.byr):
            return False
        if int(self.byr) < 1920 or int(self.byr) > 2002:
            return False

        # Issue year validation
        if not re.search(r'^(?:[0-9]{4})$', self.iyr):
            return False
        if int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False

        # Expiration Year validation
        if not re.search(r'^(?:[0-9]{4})$', self.eyr):
            return False
        if int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False

        # Height validation
        if not re.search(r'^(?:[0-9]{3})(?:cm)|(?:[0-9]{2})(?:in)$', self.hgt):
            return False
        else:
            if self.hgt.endswith('cm'):
                if int(self.hgt[:3]) < 150 or int(self.hgt[:3]) > 193:
                    return False
            if self.hgt.endswith('in'):
                if int(self.hgt[:2]) < 59 or int(self.hgt[:2]) > 76:
                    return False

        # Hair color validation
        if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.hcl):
            return False

        # Eye color validation
        if self.ecl == '':
            return False
        if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        # Passport ID validation
        if self.pid == '':
            return False
        if not (self.pid.isdigit() and self.pid.lstrip('0').__len__() <= 9):
            return False

        # Country ID validation
            # No check needed for cid
        return True

