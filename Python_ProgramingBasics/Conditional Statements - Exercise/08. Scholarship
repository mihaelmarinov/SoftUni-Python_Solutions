from math import floor

income_BGN = float(input())
avg_grade = float(input())
min_wage = float(input())

social_scholar = min_wage * 0.35
excel_scholar = avg_grade * 25

if income_BGN < min_wage and avg_grade >= 5.5:
    if social_scholar <= excel_scholar:
        print(f"You get a scholarship for excellent results {floor(excel_scholar)} BGN")
    else:
        print(f"You get a Social scholarship {floor(social_scholar)} BGN")

elif income_BGN < min_wage and avg_grade > 4.5:
    print(f"You get a Social scholarship {floor(social_scholar)} BGN")
elif avg_grade >= 5.5:
    print(f"You get a scholarship for excellent results {floor(excel_scholar)} BGN")
else:
    print("You cannot get a scholarship!")
