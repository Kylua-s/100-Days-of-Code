import tkinter as tk

# Constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Resets the time and the check marks
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lable.config(text="Timer")
    check_lable.config(text="")
    global reps
    reps = 0


# Calculates the reps, minutes and seconds
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_lable.config(text="Break", fg='#e7305b')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_lable.config(text="Break", fg='#e2979c')
    else:
        count_down(work_sec)
        timer_lable.config(text="Work", fg='#9bdeac')


# Shows the timer
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_lable.config(text=marks)


# Window settings
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg='#f7f5dd')

# Labels
timer_lable = tk.Label(text='Timer', bg='#f7f5dd', fg='#9bdeac', font=('Courier', 50, 'bold'))
timer_lable.grid(column=2, row=1, )

check_lable = tk.Label(text='✔', bg='#f7f5dd', fg='#9bdeac')
check_lable.grid(column=2, row=4)

# Buttons
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Backgroundimage
canvas = tk.Canvas(width=200, height=224, bg='#f7f5dd', highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=('Courier', 35, 'bold'))
canvas.grid(column=2, row=2)

window.mainloop()
