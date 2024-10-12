import queue
import random
import time
from colorama import Fore, Back

request_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1000, 9999)
    request_queue.put(f"Request-{request_id}")
    print(Fore.GREEN + f"Generated request: Request-{request_id}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(Fore.LIGHTBLUE_EX + f"Processing {request}...")
        time.sleep(1)
        print(Fore.LIGHTBLUE_EX + (f"Processed {request}"))
    else:
        print(Back.YELLOW + ("Queue is empty, no requests to process."))


def main():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(2)
    except KeyboardInterrupt:
        print(Back.GREEN + ("Program stopped by user."))


if __name__ == "__main__":
    main()
