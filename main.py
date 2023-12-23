from queue import Queue

# Створюємо чергу
queue = Queue(maxsize=3)


def generate_request(queue, request_id):
    queue.put(request_id)
    print(f"Заявка #{request_id} додана до черги")

def process_request(queue):
    if not queue.empty():
        request_id = queue.get()
        print(f"Заявка #{request_id} оброблена")
    else:
        print("Черга порожня")


# Головний цикл програми
request_id = 1
while True:
    user_input = input("Натисніть Enter для продовження або введіть 'вихід' для завершення: ").strip().lower()
    if user_input == 'вихід':
        break

    if not queue.full():
        # Генеруємо нову заявку
        generate_request(queue, request_id)
        request_id += 1
    else:
        print("Черга заповнена")

    # Обробляємо одну заявку з черги
    process_request(queue)

# Виводимо статус черги
print("Черга порожня:", queue.empty())
print("Розмір черги:", queue.qsize())
