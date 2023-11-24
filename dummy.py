import json
import random
import time

def generate_dummy_data():
    # Simulate the sensor sending data
    num_people = random.randint(0, 10)
    data = {'num_people': num_people}
    return json.dumps(data)

if __name__ == "__main__":
    while True:
        # Generate dummy data every 5 seconds
        dummy_data = generate_dummy_data()
        print("Sending dummy data:", dummy_data)

        # Simulate a delay between sensor readings
        time.sleep(5)
