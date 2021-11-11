import pandas


class CreateHabit:
    # create a habit function with a dictionary
    def create_habit(self, habit, value, unit, period, time, deadline, streaks):
        habit_dict = {
            "Habit": habit,
            "Value": value,
            "Unit": unit,
            "Period": period,
            "Time": time,
            "Deadline": deadline,
            "Streaks": streaks
        }
        # save the data to csv in append mode without index number:
        new_data = pandas.DataFrame(habit_dict, index=[0])
        new_data.to_csv("storage_data_csv.csv", mode='a', header=False, index=False)
