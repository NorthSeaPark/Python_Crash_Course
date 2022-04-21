from die import Die


die = Die()

# 掷骰子，并将其结果放在一个列表里
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)\

print(frequencies)
