from tkinter import *
import time

root = Tk()
root.title("Clock")


time1 = " "
tmeFrame = Frame(root)
tmeFrame.pack()

scale = Canvas(root, width=1483, height=20, highlightthickness=0)
scale.pack()

oneam = scale.create_text((60*1)+23, 10, text="1 AM")
oneline = scale.create_line((60*1)+23, 15, (60*1)+23, 25)

twoam = scale.create_text((60*2)+23, 10, text="2 AM")
twoline = scale.create_line((60*2)+23, 15, (60*2)+23, 25)

threeam = scale.create_text((60*3)+23, 10, text="3 AM")
threeline = scale.create_line((60*3)+23, 15, (60*3)+23, 25)

fouram = scale.create_text((60*4)+23, 10, text="4 AM")
fourline = scale.create_line((60*4)+23, 15, (60*4)+23, 25)

fiveam = scale.create_text((60*5)+23, 10, text="5 AM")
fiveline = scale.create_line((60*5)+23, 15, (60*5)+23, 25)

sixam = scale.create_text((60*6)+23, 10, text="6 AM")
sixline = scale.create_line((60*6)+23, 15, (60*6)+23, 25)

sevenam = scale.create_text((60*7)+23, 10, text="7 AM")
sevenline = scale.create_line((60*7)+23, 15, (60*7)+23, 25)

eightam = scale.create_text((60*8)+23, 10, text="8 AM")
eightline = scale.create_line((60*8)+23, 15, (60*8)+23, 25)

nineam = scale.create_text((60*9)+23, 10, text="9 AM")
nineline = scale.create_line((60*9)+23, 15, (60*9)+23, 25)

tenam = scale.create_text((60*10)+23, 10, text="10 AM")
tenline = scale.create_line((60*10)+23, 15, (60*10)+23, 25)

elevenam = scale.create_text((60*11)+23, 11, text="11 AM")
elevenline = scale.create_line((60*11)+23, 15, (60*11)+23, 25)

twelvepm = scale.create_text((60*12)+23, 12, text="12 PM")
twelvelinep = scale.create_line((60*12)+23, 15, (60*12)+23, 25)

onepm = scale.create_text((60*13)+23, 10, text="1 PM")
onelinep = scale.create_line((60*13)+23, 15, (60*13)+23, 25)

twopm = scale.create_text((60*14)+23, 10, text="2 PM")
twolinep = scale.create_line((60*14)+23, 15, (60*14)+23, 25)

threepm = scale.create_text((60*15)+23, 10, text="3 PM")
threelinep = scale.create_line((60*15)+23, 15, (60*15)+23, 25)

fourpm = scale.create_text((60*16)+23, 10, text="4 PM")
fourlinep = scale.create_line((60*16)+23, 15, (60*16)+23, 25)

fivepm = scale.create_text((60*17)+23, 10, text="5 PM")
fivelinep = scale.create_line((60*17)+23, 15, (60*17)+23, 25)

sixpm = scale.create_text((60*18)+23, 10, text="6 PM")
sixlinep = scale.create_line((60*18)+23, 15, (60*18)+23, 25)

sevenpm = scale.create_text((60*19)+23, 10, text="7 PM")
sevenlinep = scale.create_line((60*19)+23, 15, (60*19)+23, 25)

eightpm = scale.create_text((60*20)+23, 10, text="8 PM")
eightlinep = scale.create_line((60*20)+23, 15, (60*20)+23, 25)

ninepm = scale.create_text((60*21)+23, 10, text="9 PM")
ninelinep = scale.create_line((60*21)+23, 15, (60*21)+23, 25)

tenpm = scale.create_text((60*22)+23, 10, text="10 PM")
tenlinep = scale.create_line((60*22)+23, 15, (60*22)+23, 25)

elevenpm = scale.create_text((60*23)+23, 10, text="11 PM")
elevenlinep = scale.create_line((60*23)+23, 15, (60*23)+23, 25)

twelveam = scale.create_text((60*0)+23, 10, text="12 AM")
twelveamend = scale.create_text(1440+23, 10, text="12 AM")
twelveline = scale.create_line((60*0)+23, 15, (60*0)+23, 25)
endline = scale.create_line(1440+22, 15, 1440+22, 25)


barcan = Canvas(root, width=(24*60)+3, height=10, highlightthickness=0)
barcan.pack()
bar = barcan.create_rectangle(3, 3, 3, 7, fill='black')
barline = barcan.create_line(3, 3, 3, 7)

startlines = barcan.create_line(3, -5, 3, 25)
onelines = barcan.create_line((60*1)+3, -5, (60*1)+3, 25)
twolines = barcan.create_line((60*2)+3, -5, (60*2)+3, 25)
threelines = barcan.create_line((60*3)+3, -5, (60*3)+3, 25)
fourlines = barcan.create_line((60*4)+3, -5, (60*4)+3, 25)
fivelines = barcan.create_line((60*5)+3, -5, (60*5)+3, 25)
sixlines = barcan.create_line((60*6)+3, -5, (60*6)+3, 25)
sevenlines = barcan.create_line((60*7)+3, -5, (60*7)+3, 25)
eightlines = barcan.create_line((60*8)+3, -5, (60*8)+3, 25)
ninelines = barcan.create_line((60*9)+3, -5, (60*9)+3, 25)
tenlines = barcan.create_line((60*10)+3, -5, (60*10)+3, 25)
elevenlines = barcan.create_line((60*11)+3, -5, (60*11)+3, 25)
twelvelinesp = barcan.create_line((60*12)+3, -5, (60*12)+3, 25)
onelinesp = barcan.create_line((60*13)+3, -5, (60*13)+3, 25)
twolinesp = barcan.create_line((60*14)+3, -5, (60*14)+3, 25)
threelinesp = barcan.create_line((60*15)+3, -5, (60*15)+3, 25)
fourlinesp = barcan.create_line((60*16)+3, -5, (60*16)+3, 25)
fivelinesp = barcan.create_line((60*17)+3, -5, (60*17)+3, 25)
sixlinesp = barcan.create_line((60*18)+3, -5, (60*18)+3, 25)
sevenlinesp = barcan.create_line((60*19)+3, -5, (60*19)+3, 25)
eightlinesp = barcan.create_line((60*20)+3, -5, (60*20)+3, 25)
ninelinesp = barcan.create_line((60*21)+3, -5, (60*21)+3, 25)
tenlinesp = barcan.create_line((60*22)+3, -5, (60*22)+3, 25)
elevenlinesp = barcan.create_line((60*23)+3, -5, (60*23)+3, 25)
endlines = barcan.create_line(1443, -5, 1440, 25)

chart = Canvas(root, height=50, width=1483, highlightthickness=0)
chart.pack()
t = time.localtime()
w = int(time.strftime("%w", t))

if w == 0:
    sunday = chart.create_rectangle((1483 / 2) - 27, 15, (1483 / 2) + 27, 35)
    sundaytxt = chart.create_text(1483 / 2, 25, text="Weekend")
else:
    pass
if w == 1:
    monday1 = chart.create_rectangle(((60*9)+23), 0, ((60*11)+23+40), 50, fill="yellow")
    monday1txt = chart.create_text((((60*9)+23)+((60*11)+23+40))/2, 25, text="Design Principles")
    monday2 = chart.create_rectangle(((60*16)+23+20), 0, ((60*17)+23), 50, fill="cyan")
    monday2txt = chart.create_text((((60*16)+23+20)+((60*17)+23))/2, 25, text=" College \n  Comp")
    monday3 = chart.create_rectangle(((60*19)+23+10), 0, ((60*21)+23), 50, fill="magenta")
    monday3txt = chart.create_text((((60*19)+23+10)+((60*21)+23))/2, 25, text="Calculus 1")
else:
    pass
if w == 2:
    tuesday1 = chart.create_rectangle(((60*11)+23), 0, ((60*11)+23+50), 50, fill="yellow")
    tuesday1txt = chart.create_text((((60*11)+23)+((60*11)+23+50))/2, 25, text="  Intro\n   To\nDesign")
    tuesday2 = chart.create_rectangle(((60 * 14) + 23), 0, ((60 * 16) + 23 + 40), 50, fill="cyan")
    tuesday2txt = chart.create_text((((60 * 14) + 23) + ((60 * 16) + 23 + 40)) / 2, 25, text="  Intro\n    To\nVisCom")
else:
    pass
if w == 3:
    wednesday1 = chart.create_rectangle(((60 * 9) + 23), 0, ((60 * 11) + 23 + 40), 50, fill="yellow")
    wednesday1txt = chart.create_text((((60 * 9) + 23) + ((60 * 11) + 23 + 40)) / 2, 25, text="Design Principles")
    wednesday2 = chart.create_rectangle(((60 * 16) + 23 + 20), 0, ((60 * 17) + 23), 50, fill="cyan")
    wednesday2txt = chart.create_text((((60 * 16) + 23 + 20) + ((60 * 17) + 23)) / 2, 25, text=" College \n  Comp")
    wednesday3 = chart.create_rectangle(((60 * 19) + 23 + 10), 0, ((60 * 21) + 23), 50, fill="magenta")
    wednesday3txt = chart.create_text((((60 * 19) + 23 + 10) + ((60 * 21) + 23)) / 2, 25, text="Calculus 1")
else:
    pass
if w == 4:
    thursday1 = chart.create_rectangle(((60 * 11) + 23), 0, ((60 * 11) + 23 + 50), 50, fill="yellow")
    thursday1txt = chart.create_text((((60 * 11) + 23) + ((60 * 11) + 23 + 50)) / 2, 25, text="  Intro\n   To\nDesign")
else:
    pass
if w == 5:
    friday1 = chart.create_rectangle(((60 * 14) + 23), 0, ((60 * 15) + 23 + 15), 50, fill="cyan")
    friday1txt = chart.create_text((((60 * 14) + 23) + ((60 * 15) + 23 + 15)) / 2, 25, text="  Intro\n    To\nVisCom")
else:
    pass
if w == 6:
    saturday = chart.create_rectangle((1483/2)-27, 15, (1483/2)+27, 35)
    saturdaytxt = chart.create_text(1483 / 2, 25, text="Weekend")

chartmarker = chart.create_line(3+23, -5, 3+23, 60)

clock = Label(tmeFrame)
clock.pack()


def tick():
    global time1
    # get the current local time from the PC
    t = time.localtime()
    time2 = time.strftime("%A, %B %d, %Y \n %I:%M:%S %p \n %Z", t)
    hourday = time.strftime('%H', t)
    minsday = time.strftime('%M', t)
    day = (float(hourday) * 60) + float(minsday)
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    barcan.coords(bar, 3, 3, day+3, 7)
    barcan.coords(barline, day+3, -5, day+3, 25)
    chart.coords(chartmarker, day+23, -5, day+23, 60)
    clock.after(200, tick)




tick()
root.mainloop()