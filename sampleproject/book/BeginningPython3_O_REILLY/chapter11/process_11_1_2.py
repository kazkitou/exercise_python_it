import multiprocessing as mp
import time
import random


def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, "dish")
        time.sleep(random.choice([1, 2, 3]))
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print("Drying", dish, "dish")
        time.sleep(random.choice([5, 6, 7]))
        input.task_done()


if __name__ == "__main__":
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ["salad", "bread", "entree", "dessert"]
    washer(dishes, dish_queue)
    dish_queue.join()
