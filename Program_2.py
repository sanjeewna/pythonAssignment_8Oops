class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change > 0:
            self.current_speed = min(self.current_speed + change, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + change, 0)

# Main program
if __name__ == "__main__":
    # Create a new car
    new_car = Car("ABC-123", 142)

    # Accelerate the car
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)

    # Print out the current speed of the car
    print("Current Speed after acceleration:", new_car.current_speed, "km/h")

    # Use emergency brake
    new_car.accelerate(-200)

    # Print out the final speed after emergency brake
    print("Final Speed after emergency brake:", new_car.current_speed, "km/h")