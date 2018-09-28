import datetime
import xlrd


def dt():
    today = datetime.datetime.now()
    return datetime.datetime.strftime(today, "%d.%m.%Y")


def pechat(dmy: object) -> object:
    def transform_num(num):                                                # transform string num to one picture of line
        zero = ("  000  ", " 0   0 ", "0     0", "0     0", "0     0", " 0   0 ", "  000  ")
        one = ("  1  ", " 11  ", "1 1  ", "  1  ", "  1  ", "  1  ", "11111")
        two = (" 222 ", "2   2", "    2", "   2 ", "  2  ", " 2   ", "22222")
        three = (" 333 ", "3   3", "    3", "  33 ", "    3", "3   3", " 333 ")
        four = ("   4 ", "  44 ", " 4 4 ", "4  4 ", "44444", "   4 ", "   4 ")
        five = ("55555", "5    ", "5555 ", "    5", "    5", "    5", "5555 ")
        six = (" 666 ", "6    ", "6    ", "6666 ", "6   6", "6   6", " 666 ")
        seven = ("77777", "    7", "   7 ", "  7  ", " 7   ", "7    ", "7    ")
        eight = (" 888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", " 888 ")
        nine = (" 9999", "9   9", "9   9", " 9999", "    9", "   9 ", "  9  ")
        point = ("      ", "      ", "      ", "      ", "      ", "  **  ", "  **  ")
        numerals = (zero, one, two, three, four, five, six, seven, eight, nine)

        if num == ".":
            return list(point)
        if len(num) < 2 or num[0] == "0":
            lst = list(zero)
        else:
            lst = [""] * 7
        num = int(num)
        length = len(str(num))
        numerals_of_number = []

        for i in range(1, length+1):
            numeral = num // (10 ** (length-i))
            num -= 10 ** (length-i) * numeral
            numerals_of_number.append(numeral)

        for j in range(7):
            ln = ""                                                     # ln because line. one line of picture
            for k in range(length):
                ln += numerals[numerals_of_number[k]][j] + "  "
            lst[j] += ln
        return lst

    def transform(strng):                                               # strng because string. join nums to one picture

        lst = strng.split(".")                                          # lst because list. to apply transform_num
        yr = []
        # yr because year. join picture of num together
        for num in lst:
            yr.append(transform_num(num))
            yr.append(transform_num("."))

        yr.pop()
        lines = [""] * 7

        for picture in yr:
            for i in range(7):
                lines[i] += picture[i]

        return lines

    result = []
    print("")
    for line in transform(dmy):
        print(line)
        result.append(line)
    print("")
    return result


def exl(name: object) -> object:

    fl_exel = xlrd.open_workbook(name)
    sheet = fl_exel.sheet_by_index(0)
    points_x, points_y = [], []

    for num_line in range(sheet.nrows):
        points_x.append(sheet.row_values(num_line)[0])
        points_y.append(sheet.row_values(num_line)[1])

    return points_x, points_y


if __name__ == '__main__':
    exl("Points.xlsx")
    print("Today : {}".format(dt()))
    pechat(dt())
    while True:
        ymd = input("Enter your date, format dd.mm.yyyy: ")
        try:
            datetime.datetime.strptime(ymd, "%d.%m.%Y")
            break
        except ValueError:
            print("You don't enter dd.mm.yyyy date!")
            continue

    pechat(ymd)
