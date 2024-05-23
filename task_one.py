import pulp

# Створення моделі лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Об'єктивна функція (максимізація загальної кількості продуктів)
model += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
model += 2 * lemonade + fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "LemonJuice"
model += 2 * fruit_juice <= 40, "FruitPuree"

# Розв'язання моделі
model.solve()

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість Лимонаду: {lemonade.varValue}")
print(f"Кількість Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")
