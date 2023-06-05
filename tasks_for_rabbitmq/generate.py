import os
import time
import random
from interruptingcow import timeout


dir = f"{os.getcwd()}/tasks_for_rabbitmq/data/"
time_out = 5
working_time = 120


def file_generation():
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        with timeout(working_time, exception=RuntimeError):
            while True:
                filename = str(random.randint(1, 10000)) + ".txt"
                with open(dir + filename, "w") as f:
                    f.write(filename)
                time.sleep(time_out)
    except RuntimeError:
        pass
