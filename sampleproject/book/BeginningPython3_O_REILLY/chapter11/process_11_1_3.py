import threading, queue
import time


def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, "dish")
        time.sleep(5)
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print("Drying", dish, "dish")
        time.sleep(10)
        input.task_done()


if __name__ == "__main__":
    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ["salad", "bread", "entree", "dessert"]
    washer(dishes, dish_queue)
    dish_queue.join()