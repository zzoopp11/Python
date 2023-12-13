money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month_now = 1  # Текущий месяц


while money_capital >= 0:
    if month_now != 1:  # В начале 1 месяца зарплата не начисляется и рост цен не происходит
        money_capital = money_capital + salary  # Бюджет текущего месяца до затрат
        spend = spend + spend * increase   # Сумма трат в текущем месяце
    money_capital = money_capital - spend  # Остаток после трат

    month_now += 1

months = month_now - 1  # Кол-во месяцев без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
