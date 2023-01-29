from tkinter import *
from tkinter import messagebox
import csv
import random
import pickle

file = open(r"Python\ML\Smoke Detection\smoke_detection_iot.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
count = 0
for row in csvreader:
    rows.append(row)
    count += 1
    if count == 10000:
        break
file.close()


# Predictors
def predictors(t, hum, tv, ec, h, eth, pres, p1, p2, n0, n1, n2):

    load = pickle.load(
        open(
            r"E:\Development\Python\ML\Smoke Detection\Final.pkl",
            "rb",
        ))
    pred = load.predict([[t, hum, tv, ec, h, eth, pres, p1, p2, n0, n1, n2]])

    if pred[0] == 0:
        messagebox.showinfo("Result", "You will be safe !!!")
    else:
        messagebox.showwarning("Result", "Fire Alert")


# Auto Prediction Function
def pred_fn_auto():
    fields = [
        "t", "hum", "tv", "ec", "h", "eth", "pres", "p1", "p2", "n0", "n1",
        "n2"
    ]
    fields1 = [
        temp, humidity, tvoc, eco2, h2, ethanol, pressure, pm1, pm2, nc, nc1,
        nc2
    ]

    x = random.choice(rows)
    for i in range(12):
        fields[i] = x[i + 2]
        fields1[i].delete(0, END)
        fields1[i].insert(0, fields[i])

    for i in range(0, len(fields)):
        fields[i] = float(fields[i])

    predictors(fields[0], fields[1], fields[2], fields[3], fields[4],
               fields[5], fields[6], fields[7], fields[8], fields[9],
               fields[10], fields[11])


# Prediction Function


def pred_fn():
    t = temp.get()
    hum = humidity.get()
    tv = tvoc.get()
    ec = eco2.get()
    h = h2.get()
    eth = ethanol.get()
    pres = pressure.get()
    p1 = pm1.get()
    p2 = pm2.get()
    n0 = nc.get()
    n1 = nc1.get()
    n2 = nc2.get()

    if t != "" and hum != "" and tv != "" and ec != "" and h != "" and eth != "" and pres != "" and p1 != "" and p2 != "" and n0 != "" and n1 != "" and n2 != "":
        if (t.lstrip('-').isdigit() and hum.lstrip('-').isdigit()
                and tv.lstrip('-').isdigit() and ec.lstrip('-').isdigit()
                and h.lstrip('-').isdigit() and eth.lstrip('-').isdigit()
                and pres.lstrip('-').isdigit() and p1.lstrip('-').isdigit()
                and p2.lstrip('-').isdigit() and n0.lstrip('-').isdigit()
                and n1.lstrip('-').isdigit()
                and n2.lstrip('-').isdigit()) == True:

            if float(tv) < 0 or float(p1) < 0 or float(p2) < 0 or float(
                    n0) < 0 or float(n1) < 0 or float(n2) < 0:
                messagebox.showwarning("Warning", "Values cant be negative")

            else:
                predictors(float(t), float(hum), float(tv), float(ec),
                           float(h), float(eth), float(pres), float(p1),
                           float(p2), float(n0), float(n1), float(n2))

        else:
            messagebox.showwarning("Warning", "Invalid Values")
    else:
        messagebox.showwarning("Warning", "Fields can't be NULL")


# Layout
pred_layout = Tk()

# Window Position
window_width = 800
window_height = 600
screen_width = pred_layout.winfo_screenwidth()
screen_height = pred_layout.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
pred_layout.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Configure
pred_layout.configure(bg="White")
pred_layout.title("Early Fire Alert System By Smoke Prediction")
pred_layout.resizable(False, False)

# Heading
Label(
    pred_layout,
    text="Early Fire Alert System By Smoke Prediction",
    font=("Bell MT", 17, "bold", "underline"),
    bg="White",
).pack(pady=5, side=TOP)

# Team Name
Label(
    pred_layout,
    text="~ Team No. 407",
    font=("Bell MT", 8, "bold", "underline"),
    bg="White",
).place(x=558, y=37)

# Temp
temp_lab = Label(pred_layout,
                 text="Temperature [C] :",
                 font=("Bell MT", 15),
                 bg="White")
temp = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# Humidity
hum_lab = Label(pred_layout,
                text="Humidity [%]  :",
                font=("Bell MT", 15),
                bg="White")
humidity = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# TVOC
tvoc_lab = Label(pred_layout,
                 text="TVOC [ppb]  :",
                 font=("Bell MT", 15),
                 bg="White")
tvoc = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# eco2
eco2_lab = Label(pred_layout,
                 text="eCO2 [ppm]  :",
                 font=("Bell MT", 15),
                 bg="White")
eco2 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# h2
h2_lab = Label(pred_layout, text="Raw H2 :", font=("Bell MT", 15), bg="White")
h2 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# Ethanol
eth_lab = Label(pred_layout,
                text="Raw Ethanol :",
                font=("Bell MT", 15),
                bg="White")
ethanol = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# pressure
pres_lab = Label(pred_layout,
                 text="Pressure [hPa] :",
                 font=("Bell MT", 15),
                 bg="White")
pressure = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# pm1
pm1_lab = Label(pred_layout, text="PM1.0 :", font=("Bell MT", 15), bg="White")
pm1 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# pm2
pm2_lab = Label(pred_layout, text="PM2.5 :", font=("Bell MT", 15), bg="White")
pm2 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# nc
nc_lab = Label(pred_layout, text="NC0.5 :", font=("Bell MT", 15), bg="White")
nc = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# nc1
nc1_lab = Label(pred_layout, text="NC1.0 :", font=("Bell MT", 15), bg="White")
nc1 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

# nc2
nc2_lab = Label(pred_layout, text="NC2.5 :", font=("Bell MT", 15), bg="White")
nc2 = Entry(pred_layout, width=10, font=("Times New Roman", 15))

X1 = 90
X2 = 275
Y = 100
for i in range(12):
    fields2 = [
        temp_lab, hum_lab, tvoc_lab, eco2_lab, h2_lab, eth_lab, pres_lab,
        pm1_lab, pm2_lab, nc_lab, nc1_lab, nc2_lab
    ]
    fields3 = [
        temp, humidity, tvoc, eco2, h2, ethanol, pressure, pm1, pm2, nc, nc1,
        nc2
    ]
    if i == 6:
        X1 = 475
        X2 = 625
        Y = 100
    fields2[i].place(x=X1, y=Y)
    fields3[i].place(x=X2, y=Y)
    Y += 60

predict = Button(
    pred_layout,
    text="Predict",
    font=("Calibri", 15, "bold"),
    width=17,
    bg="Gray",
    fg="White",
    command=pred_fn,
)
predict.place(x=210, y=500)

# Output Button (Automated)
predict_auto = Button(
    pred_layout,
    text="Auto Predict",
    font=("Calibri", 15, "bold"),
    width=17,
    bg="Gray",
    fg="White",
    command=pred_fn_auto,
)
predict_auto.place(x=475, y=500)

pred_layout.mainloop()
