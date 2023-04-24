import sqlite3

con_staffer = sqlite3.connect('db/staffers.sqlite')
cur_staffer = con_staffer.cursor()
staffers = [i for i in cur_staffer.execute("""SELECT * FROM staffers""").fetchall()]
print(staffers)