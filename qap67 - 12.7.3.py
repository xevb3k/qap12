per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму: "))

# получаем список процентных ставок
percent_list = list(per_cent.values())
# получаем список возможных доходов
deposit = [round(x * money/100, 2) for x in percent_list]
# выводим максимальный дохоод
print("Максимальная сумма, которую вы можете заработать -", max(deposit))