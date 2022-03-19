# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Company = namedtuple("Company", "name, year_income")


def input_company_info(i):
    name = input(f"Пожалуйста, введите название {i}-ой компании: ")
    quarter_1 = float(input("Пожалуйста, введите прибыль за первый квартал: "))
    quarter_2 = float(input("Пожалуйста, введите прибыль за второй квартал: "))
    quarter_3 = float(input("Пожалуйста, введите прибыль за третий квартал: "))
    quarter_4 = float(input("Пожалуйста, введите прибыль за четвертый квартал: "))
    return Company(name, quarter_1 + quarter_2 + quarter_3 + quarter_4)


count = int(input("Пожалуйста, введите количество компаний: "))
companies = []
avr = 0.0
for i in range(count):
    company = input_company_info(i + 1)
    avr += company.year_income
    companies.append(company)
avr /= count
over, below = "", ""
for company in companies:
    if company.year_income < avr:
        below += f"\n\t{company.name}"
    else:
        over += f"\n\t{company.name}"
print(f"Средняя годовая прибыль для всех предприятий: {avr}"
      f"\nКомпании с прибылью нижу средней: {below}"
      f"\nКомпании с прибылью выше средней: {over}")
