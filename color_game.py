import random
from tkinter import *
from tkinter import messagebox

# ----GLOBALS---------------------------------------------
TIMER = 15  # in seconds
"""
timer = 15 , highscore = 16
timer = 30 , highscore = ?
"""
colors = ["red", "gold", "blue", "cyan", 'green']  # you can add more
qn = random.choice(colors)


# ----END GLOBALS-----------------------------------------

# ---------METHODS-----------------------------------------------------------------------------------------
def update():
    """
    updates timer
    :return: None
    """
    timer.set(timer.get() - 1)  # takes timer variable ad decrement
    if timer.get() == 0:  # timer == 0 => GAME OVER
        if messagebox.showinfo('GAME OVER', f' Your score is : {score.get()}\nThank you for playing!'):
            window.destroy()
    else:
        window.after(1000, update)


def check_change():
    """
    checks if chosen color is correct or not
    change label color.
    :return: None
    """
    global qn
    if qn == colors[x.get()]:  # checks if user chose correctly
        score.set(score.get() + 1)  # increment the score

    qn = random.choice(colors)  # chose a random color for next iteration
    label.config(background=qn)  # change the color for next iteration


# ---------END METHODS-------------------------------------------------------------------------------------


# =========================MAIN WINDOW ======================================
window = Tk()
window.resizable(False, False)

x = IntVar()  # user choice
score = IntVar()  # score
timer = IntVar()  # timer

#  --- timer ---
frame_1 = Frame(window)  # to make the timer on top side
frame_1.pack(side=TOP)

Label(
    frame_1,
    font=("Arial", 14, "bold"),
    foreground='gold',
    background='black',
    height=3,
    width=22,
    relief=RAISED,
    bd=5,
    text="Time remaining :"
).pack(side=LEFT)

time_label = Label(
    frame_1,
    font=("Arial", 14, "bold"),
    foreground='gold',
    background='black',
    height=3,
    width=12,
    relief=RAISED,
    bd=5,
    textvariable=timer
)
timer.set(TIMER)
time_label.pack(side=LEFT)

#  --- end timer ---

# --- arena ---
label = Label(
    window,
    font=("Arial", 23, "bold"),
    foreground='white',
    background=qn,
    height=3,
    width=22,
    relief=RAISED,
    bd=5,
    text="Choose this color!"

)
label.pack()

Label(
    window,
    font=("Arial", 5, "bold"),
    background='black',
    height=2,
    width=104,
    relief=RAISED,
    bd=5,
).pack()

for index in range(len(colors)):
    radio_button = Radiobutton(window,
                               font=("Impact", 30, "bold"),  # Cosmetic changes
                               variable=x,  # groups radio button together if they share same variable
                               value=index,  # assigns each radio button a different value
                               background=colors[index],  # add color
                               selectcolor=colors[index],
                               compound="left",
                               indicatoron=False,  # eliminate circle nd provide switches
                               width=20,  # change the width of the radio_buttons
                               command=check_change  # call check_change() when pressed
                               )
    radio_button.pack()

Label(window,
      font=("Arial", 5, "bold"),
      background='black',
      height=2,
      width=105,
      relief=RAISED,
      bd=5,
      ).pack()

# --- end arena ---

# --- score board ---
Label(
    window,
    font=("Arial", 14, "bold"),
    foreground='gold',
    background='black',
    height=3,
    width=22,
    relief=RAISED,
    bd=5,
    text="Score :"
).pack(side=LEFT)
Label(
    window,
    font=("Arial", 14, "bold"),
    foreground='gold',
    background='black',
    height=3,
    width=12,
    relief=RAISED,
    bd=5,
    textvariable=score
).pack(side=LEFT)
# --- end score board ---


update()
window.mainloop()
# ================END MAIN WINDOW======================================
