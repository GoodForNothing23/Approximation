from tkinter import *
import Bib


def Approximation(list_x, list_y):
    n = len(list_x)
    sum_x = sum(list_x)
    sum_y = sum(list_y)
    sum_xy = sum([list_x[i] * list_y[i] for i in range(n)])
    sum_x2 = sum([x ** 2 for x in list_x])

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)                        # y = ax + b
    b = (sum_y - a * sum_x) / n

    return a, b


if __name__ == "__main__":

    name_file_points = "Points.xlsx"
    name_file_date = "DATE.txt"

    fil = open(name_file_date, 'a')
    for line in Bib.pechat(Bib.dt()):
        fil.write(line + "\n")
    fil.write("\n")
    fil.close()

    points_x, points_y = Bib.exl(name_file_points)                                             # draw points in the end
    a, b = Approximation(points_x, points_y)
    x1 = 0
    x2 = 990
    y1 = a * x1 + b
    y2 = a * x2 + b
    while (y1 < 0 or y1 > 640) and x1 < 1000:
        x1 += 10
        y1 = a * x1 + b
    while (y2 < 0 or y2 > 640) and x2 >= 0:
        x2 -= 10
        y2 = a * x2 + b

    form = Tk()
    form.title("Approximation")
    form.geometry("1020x720")

    canvas = Canvas(form, width=1020, height=660, bg='#FFF')
    canvas.pack(side="top")

    canvas.create_line(20, 650, 20, 10, width=5, fill="#000", arrow=LAST)
    canvas.create_line(10, 640, 1000, 640, width=5,  fill="#000", arrow=LAST)

    if x1 < 1000 and x2 >= 0:
        # +20, +20 because (0,0) == (-20,-20) in program
        canvas.create_line(x1 + 20, 640 - y1, x2 + 20, 640 - y2, width=5, fill="#00F")

    for i in range(len(points_x)):
        # +20, +20 because (0,0) == (-20,-20) in program and width of rectangle = 4 => +18 and +22. also with y
        canvas.create_rectangle(points_x[i] + 18, 638 - points_y[i], points_x[i] + 22, 642 - points_y[i], fill="#F00")
        canvas.create_text(points_x[i] + 20, 650 - points_y[i],
                           text="({}, {})".format(int(points_x[i]), int(points_y[i])))
    form = mainloop()
