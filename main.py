from tkinter import *   # Usually it is not recommended to import all functions, but in this case it is easier and
# the message box has to be imported separately. I don't know why
from tkinter import messagebox
from datetime import datetime, timedelta
from create_habit import CreateHabit
import pandas
from random import randint

# create Habit class:
new_habit = CreateHabit()

# constants:

BACKGROUND = "#1597E5"
FONT_TEXT = ("Areal", 10, "bold")

# ----------------------------------------------#time-------------------------------------------------------------

time_now = datetime.now()
date = time_now.strftime("%d/%m/%Y")
time_hours = time_now.strftime("%H:%M:%S")


def time_past(deadline):
    past_time = (time_now - timedelta(days=deadline))
    return past_time


deadline_day = 1
deadline_week = 7
deadline_month = 30
deadline_year = 365

# -----------------------------------------#dropdown lists--------------------------------------------------------

# read and append the data with pandas:
with open("storage_data_csv.csv") as data:
    storage = pandas.read_csv(data)

# habit dictionary for a list with no duplicates habits:
habit_list = {n for n in storage["Habit"]}

# information list:
information_list = [
    "max. Value",
    "min. Value",
    "max. Streak",
    "same Period"
]
# -------------------------------------------#random_streaks_texts-------------------------------------------------
with open("streak_text_pool") as text_data:
    streak_text = text_data.readlines()


# -------------------------------------------#functions------------------------------------------------------------

# -------------------------------------------get_checked_start:

def checkbutton_daily1():
    # 1 if On button checked, otherwise 0.
    if checked_state_d1.get() == 1:
        text = checkbutton_d1.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_habit = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_habit) - 1, 0, -1):
                if list_habit[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_d1 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_d1: datetime = datetime.strptime(time_stored_d1, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_d1.date() == time_past(deadline_day).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_daily2():
    # 1 if On button checked, otherwise 0.
    if checked_state_d2.get() == 1:
        text = checkbutton_d2.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_d2 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_d2) - 1, 0, -1):
                if list_d2[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_d2 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_d2 = datetime.strptime(time_stored_d2, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_d2.date() == time_past(deadline_day).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_daily3():
    # 1 if On button checked, otherwise 0.
    if checked_state_d3.get() == 1:
        text = checkbutton_d3.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_d3 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_d3) - 1, 0, -1):
                if list_d3[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_d3 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_d3 = datetime.strptime(time_stored_d3, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_d3.date() == time_past(deadline_day).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_day, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_weekly1():
    # 1 if On button checked, otherwise 0.
    if checked_state_w1.get() == 1:
        text = checkbutton_w1.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_w1 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_w1) - 1, 0, -1):
                if list_w1[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_w1 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_w1 = datetime.strptime(time_stored_w1, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_w1.date() > time_past(deadline_week).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_weekly2():
    # 1 if On button checked, otherwise 0.
    if checked_state_w2.get() == 1:
        text = checkbutton_w2.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_w2 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_w2) - 1, 0, -1):
                if list_w2[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_w2 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_w2 = datetime.strptime(time_stored_w2, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_w2.date() > time_past(deadline_week).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_weekly3():
    # 1 if On button checked, otherwise 0.
    if checked_state_w3.get() == 1:
        text = checkbutton_w3.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_w3 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_w3) - 1, 0, -1):
                if list_w3[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_w3 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_w3 = datetime.strptime(time_stored_w3, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_w3.date() > time_past(deadline_week).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_week, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_monthly1():
    # 1 if On button checked, otherwise 0.
    if checked_state_m1.get() == 1:
        text = checkbutton_m1.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_m1 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_m1) - 1, 0, -1):
                if list_m1[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_m1 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_m1 = datetime.strptime(time_stored_m1, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_m1.date() > time_past(deadline_month).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_monthly2():
    # 1 if On button checked, otherwise 0.
    if checked_state_m2.get() == 1:
        text = checkbutton_m2.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_m2 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_m2) - 1, 0, -1):
                if list_m2[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_m2 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_m2 = datetime.strptime(time_stored_m2, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_m2.date() > time_past(deadline_month).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_monthly3():
    # 1 if On button checked, otherwise 0.
    if checked_state_m3.get() == 1:
        text = checkbutton_m3.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_m3 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_m3) - 1, 0, -1):
                if list_m3[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_m3 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_m3 = datetime.strptime(time_stored_m3, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_m3.date() > time_past(deadline_month).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_month, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_yearly1():
    # 1 if On button checked, otherwise 0.
    if checked_state_y1.get() == 1:
        text = checkbutton_y1.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_y1 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_y1) - 1, 0, -1):
                if list_y1[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_y1 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_y1 = datetime.strptime(time_stored_y1, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_y1.date() > time_past(deadline_year).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_yearly2():
    # 1 if On button checked, otherwise 0.
    if checked_state_y2.get() == 1:
        text = checkbutton_y2.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_y2 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_y2) - 1, 0, -1):
                if list_y2[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_y2 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_y2 = datetime.strptime(time_stored_y2, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_y2.date() > time_past(deadline_year).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


def checkbutton_yearly3():
    # 1 if On button checked, otherwise 0.
    if checked_state_y3.get() == 1:
        text = checkbutton_y3.cget("text")
        # if there is no habit signed function should stop:
        if text == "No Tasks":
            return
        else:
            # getting a list with the habit name from the checkbox:
            list_y3 = storage["Habit"] == f"{text}"
            # index variable
            x = 0
            # looping through the index list from last and if its true then stop.
            # want to get the last saved habit with the same name
            for n in range(len(list_y3) - 1, 0, -1):
                if list_y3[n]:
                    x = n
                    break
            # get the right data:
            habit = storage.iloc[x]["Habit"]
            value = storage.iloc[x]["Value"]
            unit = storage.iloc[x]["Unit"]
            period = storage.iloc[x]["Period"]
            time = f"{date}-{time_hours}"
            time_stored_y3 = storage.iloc[x]["Time"]
            # converted_string to date format:
            date_time_conv_y3 = datetime.strptime(time_stored_y3, "%d/%m/%Y-%H:%M:%S")
            # checking if the converted date is the deadline date:
            if date_time_conv_y3.date() > time_past(deadline_year).date():
                # streaks +1:
                streaks = int(storage.iloc[x]["Streaks"]) + 1
                # create the same habit only with new time and a streak:
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
                if streaks >= 1:
                    # if there is a streak a random streak saying is displayed:
                    info_display.config(anchor=N,
                                        text=f"Good Job! Streak {streaks}!!\n"
                                             f"{streak_text[randint(0, len(streak_text) - 1)]}")
            else:
                # if the user missed the deadline then the habit will be saved with 0 streaks:
                streaks = 0
                new_habit.create_habit(habit, value, unit, period, time, deadline_year, streaks)
                messagebox.showinfo(title="Habit updated!", message="Habit saved successfully!")
    else:
        return


# ----------------------------------------end_checked_button-----------------------------

# get_functions:


def get_habit():
    # getting and setting the variables:
    habit = habit_entry.get()
    value = value_entry.get()
    unit = unit_entry.get()
    period = selected_period.get()
    time = f"{date}-{time_hours}"
    deadline = 0
    streaks = "0"
    # checking user input for deleting a habit:
    if len(habit) > 1 and len(value) == 0:
        # asking user if he wants to delete the task:
        answer = messagebox.askokcancel(title="Deleting Habit",
                                        message=f"Are you sure, that you want to delete the habit: {habit}?")
        if answer:
            # creating a boolean list with the habit name:
            list_habit = (storage["Habit"] == habit)
            # going through the list if there is a habit with the name
            for n in list_habit:
                if n:
                    # if there is a name stored, creating a new storage csv without the habit that user wants to delete:
                    storage_new = storage[storage["Habit"] != habit]
                    storage_new.to_csv("storage_data_csv.csv", mode='w', header=True, index=False)
                else:
                    pass
            # confirmation of deleting the list
            messagebox.showinfo(title="Habits updated!", message="Habit deleted successfully!")
            return
        else:
            # deleting the entries:
            habit_entry.delete(0, END)
            value_entry.delete(0, END)
            unit_entry.delete(0, END)
            return

    # checking user input:
    if len(habit) == 0 or len(value) == 0 or len(unit) == 0:
        enter_values()
        return
    # checking the deadline(in days) for a habit:
    if period == "Daily":
        deadline = deadline_day
    elif period == "Weekly":
        deadline = deadline_week
    elif period == "Monthly":
        deadline = deadline_month
    elif period == "Yearly":
        deadline = deadline_year
    elif period == "":
        # if period is missing:
        enter_values()
        return
    # calling the new_habit function from the CreateHabit class with all the necessary variable:
    new_habit.create_habit(habit, value, unit, period, time, deadline, streaks)
    # message for successful saving:
    messagebox.showinfo(title="Habit Saved!", message="Habit saved successfully!")
    # deleting the entries, because of possible miss clicks:
    habit_entry.delete(0, END)
    value_entry.delete(0, END)
    unit_entry.delete(0, END)
    # mouse focus:
    habit_entry.focus()


# function for a missing input:
def enter_values():
    messagebox.showwarning(title="Missing Field", message="Please enter all fields")
    # deleting the entries:
    habit_entry.delete(0, END)
    value_entry.delete(0, END)
    unit_entry.delete(0, END)
    # mouse focus:
    habit_entry.focus()


# ------------------------------------# get info function(very long)-------------------------------------:
def get_info():
    habit_info = selected_habit.get()
    period_info = selected_info_period.get()
    information = selected_info.get()

    # -------All currently Habits:
    if habit_info == "All currently Habits":
        sorted_habits = ""
        for n in habit_list:
            sorted_habits += f"\n{n}"
        info_display.config(anchor=N, text=f"All your saved Habits:\n{sorted_habits}")
        return

    # ------------------------------------max.Value-------------:

    # if max. Value and Daily is selected:
    if information == "max. Value" and period_info == "Daily":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a daily period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Daily":
            value = 0
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) > float(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} max. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not daily:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if max. Value and Weekly is selected:
    if information == "max. Value" and period_info == "Weekly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a weekly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Weekly":
            value = 0
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) > float(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} max. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not weekly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if max. Value and Monthly is selected:
    if information == "max. Value" and period_info == "Monthly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a monthly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Monthly":
            value = 0
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) > float(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} max. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not monthly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if max. Value and Yearly is selected:
    if information == "max. Value" and period_info == "Yearly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a monthly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Yearly":
            value = 0
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) > float(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} max. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not yearly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # ------------------------------------min.Value-------------:

    # if min. Value and Daily is selected:
    if information == "min. Value" and period_info == "Daily":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a daily period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Daily":
            # first value of the habit:
            value = storage.loc[filtered_info]["Value"].iloc[0]
            # checking all possible habits with the same name and getting the min. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) < float(value):
                    value = n
            # display the min. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} min. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not daily:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if min. Value and Weekly is selected:
    if information == "min. Value" and period_info == "Weekly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a weekly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Weekly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Value"].iloc[0]
            # checking all possible habits with the same name and getting the min. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) < float(value):
                    value = n
            # display the min. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} min. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not weekly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if min. Value and Monthly is selected:
    if information == "min. Value" and period_info == "Monthly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a monthly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Monthly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Value"].iloc[0]
            # checking all possible habits with the same name and getting the min. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) < float(value):
                    value = n
            # display the min. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} min. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not monthly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if min. Value and Yearly is selected:
    if information == "min. Value" and period_info == "Yearly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # getting the unit for the selected habit:
        unit = storage.loc[filtered_info]["Unit"]
        # checking if the habit has a monthly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Yearly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Value"].iloc[0]
            # checking all possible habits with the same name and getting the min. value:
            for n in (storage.loc[filtered_info]["Value"]):
                if float(n) < float(value):
                    value = n
            # display the min. value:
            info_display.config(anchor=N,
                                text=f"Your {period_info} min. Value for {habit_info} is {value}{unit.iloc[0]}")
        else:
            # display if the habit is not Yearly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # ---------max.streaks-------------------------

    # if streaks and daily
    if information == "max. Streak" and period_info == "Daily":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # checking if the habit has a daily period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Daily":
            # first value of the habit:
            value = storage.loc[filtered_info]["Streaks"].iloc[0]
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Streaks"]):
                if int(n) > int(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N, text=f"Your max. Streak for {habit_info} is {value} Days!")
        else:
            # display if the habit is not daily:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if streaks and weekly
    if information == "max. Streak" and period_info == "Weekly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # checking if the habit has a weekly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Weekly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Streaks"].iloc[0]
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Streaks"]):
                if int(n) > int(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N, text=f"Your max. Streak for {habit_info} is {value} Weeks!")
        else:
            # display if the habit is not weekly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if streaks and monthly
    if information == "max. Streak" and period_info == "Monthly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # checking if the habit has a monthly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Monthly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Streaks"].iloc[0]
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Streaks"]):
                if int(n) > int(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N, text=f"Your max. Streak for {habit_info} is {value} Months!")
        else:
            # display if the habit is not monthly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # if streaks and yearly
    if information == "max. Streak" and period_info == "Yearly":
        # saved data filtered:
        filtered_info = storage["Habit"] == habit_info
        # checking if the habit has a yearly period:
        if storage.loc[filtered_info]["Period"].iloc[0] == "Yearly":
            # first value of the habit:
            value = storage.loc[filtered_info]["Streaks"].iloc[0]
            # checking all possible habits with the same name and getting the max. value:
            for n in (storage.loc[filtered_info]["Streaks"]):
                if int(n) > int(value):
                    value = n
            # display the max. value:
            info_display.config(anchor=N, text=f"Your max. Streak for {habit_info} is {value} Years!")
        else:
            # display if the habit is not yearly:
            info_display.config(anchor=N, text=f"There is no {period_info} Period for the Habit: {habit_info}!!!")

    # ------getting same period habit info:

    # daily habits
    if information == "same Period" and period_info == "Daily":
        # empty string:
        daily_habit = ""
        # boolean for the period
        filtered_daily_habit = storage["Period"] == "Daily"
        # boolean for the period
        for n in range(len(filtered_daily_habit) - 1, 0, -1):
            # if there is a true:
            if filtered_daily_habit[n]:
                # if the name is not already in the list:
                if f"{storage.iloc[n]['Habit']}" not in daily_habit:
                    daily_habit += f"{storage.iloc[n]['Habit']}\n"
            else:
                pass
        # displaying the info:
        info_display.config(anchor=N, text=f"Your {period_info} Habits is/are:\n {daily_habit}")

    # weekly habits:
    if information == "same Period" and period_info == "Weekly":
        # empty string:
        weekly_habit = ""
        # boolean for the period
        filtered_weekly_habit = storage["Period"] == "Weekly"
        # going through the filtered boolean reverse:
        for n in range(len(filtered_weekly_habit) - 1, 0, -1):
            # if there is a true:
            if filtered_weekly_habit[n]:
                # if the name is not already in the list:
                if f"{storage.iloc[n]['Habit']}" not in weekly_habit:
                    weekly_habit += f"{storage.iloc[n]['Habit']}\n"
            else:
                pass
        # displaying the info:
        info_display.config(anchor=N, text=f"Your {period_info} Habits is/are:\n {weekly_habit}")

    # monthly habits:
    if information == "same Period" and period_info == "Monthly":
        # empty string:
        monthly_habit = ""
        # boolean for the period
        filtered_monthly_habit = storage["Period"] == "Monthly"
        # going through the filtered boolean reverse:
        for n in range(len(filtered_monthly_habit) - 1, 0, -1):
            # if there is a true:
            if filtered_monthly_habit[n]:
                # if the name is not already in the list:
                if f"{storage.iloc[n]['Habit']}" not in monthly_habit:
                    monthly_habit += f"{storage.iloc[n]['Habit']}\n"
            else:
                pass
        # displaying the info:
        info_display.config(anchor=N, text=f"Your {period_info} Habits is/are:\n {monthly_habit}")

    # yearly habits:
    if information == "same Period" and period_info == "Yearly":
        # empty string:
        yearly_habit = ""
        # boolean for the period
        filtered_yearly_habit = storage["Period"] == "Yearly"
        # going through the filtered boolean reverse:
        for n in range(len(filtered_yearly_habit) - 1, 0, -1):
            # if there is a true:
            if filtered_yearly_habit[n]:
                # if the name is not already in the list:
                if f"{storage.iloc[n]['Habit']}" not in yearly_habit:
                    yearly_habit += f"{storage.iloc[n]['Habit']}\n"
            else:
                pass
        # displaying the info:
        info_display.config(anchor=N, text=f"Your {period_info} Habits is/are:\n {yearly_habit}")


# -----------------------------------------#layout of the gui-----------------------------------------------------

# window creation:
window = Tk()
window.title("Habit Tracking App v1.00")
window.config(padx=50, pady=50, bg=BACKGROUND)

# layout:

# entries:
habit_entry = Entry(width=22)
habit_entry.grid(row=2, column=0, padx=5, pady=5)
value_entry = Entry(width=12)
value_entry.grid(row=2, column=1, padx=5, pady=5)
unit_entry = Entry(width=12)
unit_entry.grid(row=2, column=2, padx=5, pady=5)

# text labels:
habit_text = Label(text="Habit", bg=BACKGROUND, font=FONT_TEXT)
habit_text.grid(row=1, column=0)
value_text = Label(text="Value", bg=BACKGROUND, font=FONT_TEXT)
value_text.grid(row=1, column=1)
unit_text = Label(text="Unit", bg=BACKGROUND, font=FONT_TEXT)
unit_text.grid(row=1, column=2)
period_text = Label(text="Period", bg=BACKGROUND, font=FONT_TEXT)
period_text.grid(row=1, column=3)
date_label = Label(text=f"Date: {date}", bg=BACKGROUND, font=FONT_TEXT)
date_label.grid(row=0, column=5)
habit_info_text = Label(text="Stored Habit Info", bg=BACKGROUND, font=FONT_TEXT)
habit_info_text.grid(row=3, column=5)
period_info_text = Label(text="Period Info", bg=BACKGROUND, font=FONT_TEXT)
period_info_text.grid(row=4, column=5)
info_text = Label(text="Information", bg=BACKGROUND, font=FONT_TEXT)
info_text.grid(row=5, column=5)
daily_text = Label(text="-Daily Tasks-", bg=BACKGROUND, font=FONT_TEXT)
daily_text.grid(row=7, column=0, padx=5, pady=(25, 5))
weekly_text = Label(text="-Weekly Tasks-", bg=BACKGROUND, font=FONT_TEXT)
weekly_text.grid(row=7, column=1, padx=5, pady=(25, 5))
monthly_text = Label(text="-Monthly Tasks-", bg=BACKGROUND, font=FONT_TEXT)
monthly_text.grid(row=7, column=3, padx=5, pady=(25, 5))
yearly_text = Label(text="-Yearly Tasks-", bg=BACKGROUND, font=FONT_TEXT)
yearly_text.grid(row=7, column=4, padx=5, pady=(25, 5))

# dropdowns:
selected_period = StringVar()
period_dropdown = OptionMenu(window, selected_period, "Daily", "Weekly", "Monthly", "Yearly")
period_dropdown.config(width=10, highlightthickness=0)
period_dropdown.grid(row=2, column=3, padx=5, pady=5)
selected_habit = StringVar()
habit_dropdown = OptionMenu(window, selected_habit, "All currently Habits", *habit_list)
habit_dropdown.config(width=27, highlightthickness=0)
habit_dropdown.grid(row=3, column=3, columnspan=2, padx=5, pady=5)
selected_info_period = StringVar()
period_info_dropdown = OptionMenu(window, selected_info_period, "Daily", "Weekly", "Monthly", "Yearly")
period_info_dropdown.config(width=27, highlightthickness=0)
period_info_dropdown.grid(row=4, column=3, columnspan=2, padx=5, pady=5)
selected_info = StringVar()
information_dropdown = OptionMenu(window, selected_info, *information_list)
information_dropdown.config(width=27, highlightthickness=0)
information_dropdown.grid(row=5, column=3, columnspan=2, padx=5, pady=5)

# buttons:
okay_button = Button(text="Ok", highlightthickness=0, width=12, command=get_habit)
okay_button.grid(row=2, column=4)
info_button = Button(text="Get Info", highlightthickness=0, width=12, command=get_info)
info_button.grid(row=6, column=4)

# display:
info_display = Label(height=10, width=47)
info_display.grid(row=3, column=0, columnspan=3, rowspan=4, padx=5, pady=5)

# check buttons:

# ------------------------------------------#checked--status#------------------------------------------------------

# --------------------------------checked_daily:
filtered_daily = (storage["Period"] == "Daily")
daily_list = []
for d in storage.loc[filtered_daily, "Habit"]:
    if d not in daily_list:
        daily_list.append(d)
    else:
        pass

# daily - variable to hold on to checked state, 0 is off, 1 is on.
try:
    task_d1 = f"{daily_list[0]}"
    checked_state_d1 = IntVar()
    checkbutton_d1 = Checkbutton(text=task_d1, variable=checked_state_d1, command=checkbutton_daily1, bg=BACKGROUND)
    checked_state_d1.get()
    checkbutton_d1.grid(row=8, column=0, padx=5, pady=5)
except IndexError:
    pass

try:
    task_d2 = f"{daily_list[1]}"
    checked_state_d2 = IntVar()
    checkbutton_d2 = Checkbutton(text=task_d2, variable=checked_state_d2, command=checkbutton_daily2, bg=BACKGROUND)
    checked_state_d2.get()
    checkbutton_d2.grid(row=9, column=0, padx=5, pady=5)
except IndexError:
    pass

try:
    task_d3 = f"{daily_list[2]}"
    checked_state_d3 = IntVar()
    checkbutton_d3 = Checkbutton(text=task_d3, variable=checked_state_d3, command=checkbutton_daily3, bg=BACKGROUND)
    checked_state_d3.get()
    checkbutton_d3.grid(row=10, column=0, padx=5, pady=5)
except IndexError:
    pass

# --------------------------------checked_weekly:


filtered_weekly = (storage["Period"] == "Weekly")
weekly_list = []
for w in storage.loc[filtered_weekly, "Habit"]:
    if w not in weekly_list:
        weekly_list.append(w)
    else:
        pass

# weekly - variable to hold on to checked state, 0 is off, 1 is on.
try:
    task_w1 = f"{weekly_list[0]}"
    checked_state_w1 = IntVar()
    checkbutton_w1 = Checkbutton(text=task_w1, variable=checked_state_w1, command=checkbutton_weekly1, bg=BACKGROUND)
    checked_state_w1.get()
    checkbutton_w1.grid(row=8, column=1, padx=5, pady=5)
except IndexError:
    pass

try:
    task_w2 = f"{weekly_list[1]}"
    checked_state_w2 = IntVar()
    checkbutton_w2 = Checkbutton(text=task_w2, variable=checked_state_w2, command=checkbutton_weekly2, bg=BACKGROUND)
    checked_state_w2.get()
    checkbutton_w2.grid(row=9, column=1, padx=5, pady=5)
except IndexError:
    pass

try:
    task_w3 = f"{weekly_list[2]}"
    checked_state_w3 = IntVar()
    checkbutton_w3 = Checkbutton(text=task_w3, variable=checked_state_w3, command=checkbutton_weekly3, bg=BACKGROUND)
    checked_state_w3.get()
    checkbutton_w3.grid(row=10, column=1, padx=5, pady=5)
except IndexError:
    pass

# --------------------------------checked_monthly:


filtered_monthly = (storage["Period"] == "Monthly")
monthly_list = []
for m in storage.loc[filtered_monthly, "Habit"]:
    if m not in monthly_list:
        monthly_list.append(m)
    else:
        pass

# monthly - variable to hold on to checked state, 0 is off, 1 is on.
try:
    task_m1 = f"{monthly_list[0]}"
    checked_state_m1 = IntVar()
    checkbutton_m1 = Checkbutton(text=task_m1, variable=checked_state_m1, command=checkbutton_monthly1, bg=BACKGROUND)
    checked_state_m1.get()
    checkbutton_m1.grid(row=8, column=3, padx=5, pady=5)
except IndexError:
    pass

try:
    task_m2 = f"{monthly_list[1]}"
    checked_state_m2 = IntVar()
    checkbutton_m2 = Checkbutton(text=task_m2, variable=checked_state_m2, command=checkbutton_monthly2, bg=BACKGROUND)
    checked_state_m2.get()
    checkbutton_m2.grid(row=9, column=3, padx=5, pady=5)
except IndexError:
    pass

try:
    task_m3 = f"{monthly_list[1]}"
    checked_state_m3 = IntVar()
    checkbutton_m3 = Checkbutton(text=task_m3, variable=checked_state_m3, command=checkbutton_monthly3, bg=BACKGROUND)
    checked_state_m3.get()
    checkbutton_m3.grid(row=10, column=3, padx=5, pady=5)
except IndexError:
    pass

# --------------------------------checked_yearly:
filtered_yearly = (storage["Period"] == "Yearly")
yearly_list = []
for y in storage.loc[filtered_yearly, "Habit"]:
    if y not in yearly_list:
        yearly_list.append(y)
    else:
        pass

# yearly - variable to hold on to checked state, 0 is off, 1 is on.
try:
    task_y1 = f"{yearly_list[0]}"
    checked_state_y1 = IntVar()
    checkbutton_y1 = Checkbutton(text=task_y1, variable=checked_state_y1, command=checkbutton_yearly1, bg=BACKGROUND)
    checked_state_y1.get()
    checkbutton_y1.grid(row=8, column=4, padx=5, pady=5)
except IndexError:
    pass

try:
    task_y2 = f"{yearly_list[1]}"
    checked_state_y2 = IntVar()
    checkbutton_y2 = Checkbutton(text=task_y2, variable=checked_state_y2, command=checkbutton_yearly2, bg=BACKGROUND)
    checked_state_y2.get()
    checkbutton_y2.grid(row=9, column=4, padx=5, pady=5)
except IndexError:
    pass

try:
    task_y3 = f"{yearly_list[2]}"
    checked_state_y3 = IntVar()
    checkbutton_y3 = Checkbutton(text=task_y3, variable=checked_state_y3, command=checkbutton_yearly3, bg=BACKGROUND)
    checked_state_y3.get()
    checkbutton_y3.grid(row=10, column=4, padx=5, pady=5)
except IndexError:
    pass

# --------------------------------------------layout_end----------------------------------------------------------

# ----------------------------------------------info box----------------------------------------------------------

# creating empty lists for missed strike:
zero_streaks_list = []
zero_streaks_list_w = []

# going through the habit list:
for n in habit_list:
    # boolean for habits and the daily deadline:
    no_streak = (storage["Deadline"] == deadline_day) & (storage["Habit"] == n)
    # going through the boolean from back:
    for k in range(len(no_streak) - 1, 0, -1):
        # want the first True in the boolean:
        if no_streak[k]:
            # get the right stored time data:
            time_stored = storage.iloc[k]["Time"]
            # converted_string to date format:
            date_time_conv = datetime.strptime(time_stored, "%d/%m/%Y-%H:%M:%S")
            # if the user has still time left for the habit than break:
            if date_time_conv.date() >= time_past(deadline_day).date():
                break
            # else checking if the converted date is in the deadline and append the index number:
            elif date_time_conv.date() < time_past(deadline_day).date():
                zero_streaks_list.append(k)
                break

# going through the habit list:
for n in habit_list:
    # boolean for habits and the week deadline:
    no_streak = (storage["Deadline"] == deadline_week) & (storage["Habit"] == n)
    # going through the boolean from back:
    for k in range(len(no_streak) - 1, 0, -1):

        if no_streak[k]:
            # get the right stored time data:
            time_stored = storage.iloc[k]["Time"]
            # converted_string to date format:
            date_time_conv = datetime.strptime(time_stored, "%d/%m/%Y-%H:%M:%S")
            # if the user has still time left for the habit than break:
            if date_time_conv.date() >= time_past(deadline_week).date():
                break
            # else checking if the converted date is in the deadline and append the index number:
            elif date_time_conv.date() < time_past(deadline_week).date():
                zero_streaks_list_w.append(k)
                break

# create new text for the display info:
text_missed_daily = "Your missed Daily Habits are:\n"
text_missed_weekly = "Your missed Weekly Habits are:\n"
# if the list is not empty append all habits to the text:
if len(zero_streaks_list) > 0:
    for m in zero_streaks_list:
        text_missed_daily += f"{storage.iloc[m]['Habit']}\n"
# if the list is empty write:
else:
    text_missed_daily += f"NONE! Good Job!\n"

# if the list is not empty append all habits to the text:
if len(zero_streaks_list_w) > 0:
    for o in zero_streaks_list_w:
        text_missed_weekly += f"{storage.iloc[o]['Habit']}\n"
# if the list is empty write:
else:
    text_missed_weekly += f"NONE! Good Job!\n"

text_start = f"Welcome to the Habit Tracker APP!\n" \
             f"Your last stored Habit was:\n" \
             f"{storage['Habit'][len(storage) - 1]} on {storage['Time'][len(storage) - 1]}\n" \
             f"{text_missed_daily}\n" \
             f"{text_missed_weekly}"

info_display.config(anchor=N, text=text_start)

# refreshing the window:
window.mainloop()
