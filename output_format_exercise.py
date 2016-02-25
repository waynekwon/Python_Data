first_year_gpa=int(input())
second_year_gpa=int(input())
increase=((second_year_gpa-first_year_gpa)/first_year_gpa)*100
print(increase)

print('%.1f%%' %increase)