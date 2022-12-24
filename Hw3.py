import tkinter as tk
import json
import pandas as pd
with open('weather.json,','r') as d:
    weather=json.load()
    temp=wether["fact"]["temp"]
    condition = wether["fact"]["condition"]

    window = tk.Tk()
    window.geonetry("300x150")
33
temp_tk= tk.Label(window ,text="Температура"+str(temp))
temp_tk.grid(column=0,row=0)

temp_image = tk.PhotoImage(file="gradus.png")
temp_image1=tk.Label(image=temp_image)
temp_image1.grid(column=1,row=0)

condition_tk= tk.Label(window ,text="Погода"+str(condition))
condition_tk.grid(column=0,row=1)

overcast_image = tk.PhotoImage(file="oblako.png")
overcast_image1=tk.Label(image=overcast_image)
overcast_image1.grid(column=1,row=1)
window.mainloop()


x=a.to_json(orient="split")
x=json.loads(x)
print(x)
v_name=x["index"]
print(v_name[4])
v_data=x["data"]
print(int(v_data[4][0]))

import tkinter as tk
window=tk.Tk()
window.geometry("300x150")

def onclick():
    print(1)
voltage_tk=tk.Label(window,text=(v_name[0])+str("  ")+str(v_date[0][0]),front=("Arial",15))
voltage_tk.grid(column=0,row=0)
voltage_tk=tk.Label(window,text=(v_name[1])+str("  ")+str(v_date[1][0]),front=("Arial",15))
voltage_tk.grid(column=0,row=1)
voltage_tk=tk.Label(window,text=(v_name[2])+str("  ")+str(v_date[2][0]),front=("Arial",15))
voltage_tk.grid(column=0,row=2)