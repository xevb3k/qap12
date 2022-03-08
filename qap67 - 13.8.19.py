
tikets = int(input('Введите количество приобретаемых билетов: '))

# создаем список возрастов длиной tikets
age_list = [int(input(f'Введите возраст {x+1} посетителя: ')) for x in range(tikets)]
# список цен билетов
prict_list = []

# добавляем в списк цены в зависимости от возраста, возраст менее 18 не учитывается
for age in age_list:
    if age>=25:
        prict_list.append(1390)
    elif age>=18:
        prict_list.append(990)
        
# считаем скидку
discount = 1 if tikets<=3 else 0.9
# выводим сумму с учетом скидки
print(f'Сумма к оплате (скидка {100-discount*100}%): ', sum(prict_list)*discount)
