# Множество всех языков
all_languages = set()

# Словарь студентов с языками, которые они знают
students = {
    'Иван': {'английский', 'испанский', 'китайский'},
    'Мария': {'английский', 'французский'},
    'Ольга': {'немецкий', 'китайский'},
    'Андрей': {'испанский', 'немецкий', 'итальянский'}
}

# Собираем множество уникальных языков
for languages in students.values():
    all_languages |= languages

# Выводим отсортированный список языков
print("Список всех языков:", sorted(all_languages))

# Находим студентов, которые знают китайский язык
students_know_chinese = [name for name, languages in students.items() if 'китайский' in languages]

# Выводим список студентов, которые знают китайский язык
print("Студенты, знающие китайский язык:", students_know_chinese)
