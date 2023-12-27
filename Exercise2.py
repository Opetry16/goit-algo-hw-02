from collections import deque

def is_palindrome(s):
    # Перетворити рядок у нижній регістр та видалити пробіли
    s = s.lower().replace(" ", "")
    
    # Створити двосторонню чергу та додати символи рядка
    char_queue = deque(s)

    # Порівняти символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    # Якщо всі символи співпали, рядок є паліндромом
    return True

# Приклад використання:
input_string = "I was on my Honeymoon in Nazare and very impressed by GIGANTIC WAVES. "
result = is_palindrome(input_string)

if result:
    print(f'Рядок "{input_string}" є паліндромом.')
else:
    print(f'Рядок "{input_string}" не є паліндромом.')