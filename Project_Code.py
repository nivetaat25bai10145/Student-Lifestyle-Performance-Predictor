import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data = {
    'study': [2, 5, 6, 1, 7, 3, 4, 8],
    'sleep': [5, 7, 6, 4, 8, 6, 7, 7],
    'attendance': [60, 80, 90, 50, 95, 70, 85, 92],
    'screen': [6, 3, 2, 7, 2, 5, 4, 1],
    'exercise': [0, 1, 1, 0, 1, 0.5, 1, 1],
    'performance': ['Poor', 'Average', 'Good', 'Poor', 'Good', 'Average', 'Average', 'Good']}

df = pd.DataFrame(data)
X = df[['study', 'sleep', 'attendance', 'screen', 'exercise']]
y = df['performance']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def improvement_plan(study, sleep, attendance, screen, exercise):
    print("\nImprovement Plan:")

    if study < 4:
        print("- Increase study time to at least 4–6 hours daily")
    else:
        print("- Maintain your study consistency")

    if sleep < 6:
        print("- Get at least 6–8 hours of sleep")
    else:
        print("- Keep maintaining a healthy sleep routine")

    if attendance < 75:
        print("- Improve your attendance to above 75%")
    else:
        print("- Good attendance, keep it up")

    if screen > 4:
        print("- Reduce screen time to below 3–4 hours")
    else:
        print("- Screen time is well managed")

    if exercise < 1:
        print(" - keep trying to maintain 30-60 minutes of exercise daily")
    else:
        print("- Good job")

    print("- Stay consistent and follow a disciplined routine")


#user input
print("\nEnter student details:")

try:
    study = float(input("Study Hours: "))
    sleep = float(input("Sleep Hours: "))
    attendance = float(input("Attendance (%): "))
    screen = float(input("Screen Time (hours): "))
    exercise = float(input("Exercise Hours: "))
except ValueError:
    print("Invalid input! Enter numbers only.")
    exit()

input_data = pd.DataFrame([[study, sleep, attendance, screen, exercise]],
                          columns=['study', 'sleep', 'attendance', 'screen', 'exercise'])

prediction = model.predict(input_data)[0]
print("\nPredicted Performance:", prediction)

if prediction in ["Poor", "Average"]:
    improvement_plan(study, sleep, attendance, screen, exercise)
else:
    print("\nGreat! Keep maintaining your current routine.")
