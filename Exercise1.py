from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Функція generate_request():
def generate_request():
    # Створити нову заявку (можна використовувати унікальний номер або інші дані)
    new_request = f"Request {time.time()}"
    # Додати заявку до черги
    queue.put(new_request)
    print(f"New request generated: {new_request}")

# Функція process_request():
def process_request():
    # Якщо черга не пуста:
    if not queue.empty():
        # Видалити заявку з черги
        processed_request = queue.get()
        # Обробити заявку (можна виконати потрібні дії)
        print(f"Processing request: {processed_request}")
    else:
        # Інакше, якщо черга пуста:
        print("Queue is empty. No requests to process.")

# Головний цикл програми:
while True:
    # Виконати generate_request() для створення нових заявок
    generate_request()
    # Виконати process_request() для обробки заявок
    process_request()
    # Затримка для імітації реального часу між подіями
    time.sleep(3)