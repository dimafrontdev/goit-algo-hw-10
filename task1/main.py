from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="maximize-production", sense=LpMaximize)

# Визначення змінних
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Додавання обмежень
model += (2 * lemonade + 1 * fruit_juice <= 100, "water_constraint")
model += (1 * lemonade <= 50, "sugar_constraint")
model += (1 * lemonade <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

# Цільова функція
model += lemonade + fruit_juice

# Розв'язання задачі
model.solve()

# Вивід результатів
print(f"Максимальна кількість лимонаду для виробництва: {lemonade.varValue} одиниць")
print(
    f"Максимальна кількість фруктового соку для виробництва: {fruit_juice.varValue} одиниць"
)
print(
    f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue} одиниць"
)
