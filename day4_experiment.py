import time
import random

# matrix animation

def matrix():
    start_time = time.time()
    numbers = random.sample(range(0, 10), 10)

    while time.time() - start_time < 10:
        print(random.sample(numbers, 10))
        time.sleep(0.08)

# loading animation

def loading():
    
    animation = ".", "..", "..."
    
    for x in animation:
        time.sleep(1)
        print(f"loading {x}")

# spinner animation

def spinner():

    spinner = ["|", "/", "-", "\\"]

    start_time = time.time()
    index = 0

    while time.time() - start_time < 5:
        print(spinner[index % len(spinner)], end='\r')
        time.sleep(0.1)
        index += 1
    
spinner()