users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

book_of_visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

quantity_of_visits = len(users)
quantity_of_unique_visits = len(set(users))

book_of_visits["Общее количество"] = quantity_of_visits
book_of_visits["Уникальные посещения"] = quantity_of_unique_visits

print(book_of_visits)

