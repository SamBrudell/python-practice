#loops
import time

animation = ".", "..", "..."
for x in animation:
    time.sleep(1)
    print(f"loading {x}")
    
import time

spinner = ["|", "/", "-", "\\"]

start_time = time.time()
index = 0

while time.time() - start_time < 5:
    print(spinner[index % len(spinner)], end='\r')
    time.sleep(0.1)
    index += 1