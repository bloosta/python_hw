numbers = [x ** 2 for x in range(1, 11)]

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdict = {day: index + 1 for index, day in enumerate(week)}

tags = {"Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"}
tagslower = {tag.lower() for tag in tags}

print(numbers)
print(weekdict)
print(tagslower)
