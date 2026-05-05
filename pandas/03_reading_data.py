# run this once to create a fake CSV for practice
import pandas as pd

data = {
    'name': ['Sam', 'Raj', 'Priya', 'Amit', 'Neha'],
    'marks': [85, 90, 78, 60, 95],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Chennai'],
    'passed': [True, True, True, False, True]
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)  # saves CSV
print("CSV created!")

# Now we can read the CSV back into a DataFrame

d = pd.read_csv('students.csv')  # reads CSV
print(d)  # prints the DataFrame

# useful functions:-
print()

print(pd.read_csv('students.csv', nrows=3))        # load only 3 rows
print()
print(pd.read_csv('students.csv', usecols=['name'])) # load specific columns