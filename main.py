print("How many hours do you work in one week?")

weeklyHours = int(input())

print("How much money do you earn hourly?")

hourlyPay = int(input())

if weeklyHours > 40:
  default = hourlyPay * 40
  salary = (hourlyPay * 1.5) * (weeklyHours - 40) + default
  # print(salary)
else:
  salary = hourlyPay * weeklyHours
  # print(salary)

salaryString = str(salary)

overtimeString = str(salary - default)

defaultString = str(default)

print("\nYour pay is $" + salaryString + ", your regular pay is $" + defaultString, "and your overtime pay is $" + overtimeString + ".")