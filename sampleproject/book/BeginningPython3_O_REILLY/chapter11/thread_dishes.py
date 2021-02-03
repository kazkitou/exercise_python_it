import threading, queue
import time

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        time.sleep(5)
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        time.sleep(10)
        input.task_done()

# はじめに
# 標準PythonシステムはGIL(グローバルインタープリタロック)を使っている。
# そのためスレッドを使ってもCPUバウンドな処理は高速化されない。
# CPUバウンド -> CPU処理待ち。数値処理の実行中が該当する。
# I/Oバウンド -> I/O処理待ち。CPUではなくメモリなどのアクセスが該当する。
if __name__ == "__main__":
    dish_queue = queue.Queue()
    for n in range(2):
        # 書籍では"daemon=True"が記載されていないため、queue.Queue().join()が完了しない。
        # deamon=False(Default)で同等動作を実現するには、作成した全threadに対してthread.join()を行う必要がある。
        # daemon=True --> DaemonThread
        # daemon=False -> UserThread
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue, ), daemon=True)
        dryer_thread.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()