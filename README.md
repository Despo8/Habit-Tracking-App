# Habit Tracking App

It's a simple GUI-driven tracking program for your habits.


## Getting Started

These instructions will give you a copy of the project running on your local computer for development and testing 
purposes.

### Prerequisites

The coding was done with the integrated development environment PyCharm in Python 3.9.
Recommendation for the software for testing and building.

- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

### Installing

Using your preferred file manager, copy the files to a directory under the project root 
or add the entire folder to your PyCharmProjects.

Example:

    C:\Users\UserName\PycharmProjects\Habit_Tracking_App_v1.0



Open the project in PyCharm under:

File --> Open --> Habit_Tracking_App_v1.0

## Usage

Run the main.py. You should then see the graphical user interface.

### Create a new Habit

Enter the required fields (Habit, Value, Unit, Period) and click on "Ok"

    Hiking, 25, km, Weekly

### Analyse your habits

There are 5 predefined habits saved from the start. You can get the necessary information from the drop-down menu next 
to the information label. Click "Get Info" when you have defined your requirements.

    All currently Habits --> Get Info --> Displays all of your saved Habits
    Cycling/Daily/max.Value --> Get Info --> Displays your saved maximum distance that you have ridden
    Daily/same Period --> Get Info --> Displays your saved habits that have the same period

Attention: "All currently Habits" will always be displayed if you have this parameter in the drop-down selected and 
click on "Get Info".

### Checking off

To check off a saved habit, click the checkbox next to its name.

### Deleting Habits

To delete a saved habit, write the name in the "Habit" field and click on "Ok"

    Hiking


### Streaks Text

If you want to add additional "streaks sayings", you can simply add new lines in the "streak_text_pool.txt" file.


## Contributing

Requests are welcomed.
For mayor changes, please open an issue first to discuss what you would like to change.


## Authors

  - **Despo8** 
  

## Acknowledgments

  - Professor Max

