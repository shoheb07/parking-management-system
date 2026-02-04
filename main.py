import json
import os
from datetime import datetime

DATA_FILE = "parking_data.json"
TOTAL_SLOTS = 10
RATE_PER_HOUR = 20  # parking charge


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def available_slots():
    return TOTAL_SLOTS - len(load_data())


def park_vehicle():
    data = load_data()

    if available_slots() <= 0:
        print("Parking Full!")
        return

    vehicle = {
        "vehicle_no": input("Vehicle Number: "),
        "vehicle_type": input("Vehicle Type (Car/Bike): "),
        "entry_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(vehicle)
    save_data(data)
    print("Vehicle parked successfully.")


def remove_vehicle():
    data = load_data()
    vno = input("Enter Vehicle Number: ")

    for v in data:
        if v["vehicle_no"] == vno:
            entry_time = datetime.strptime(v["entry_time"], "%Y-%m-%d %H:%M:%S")
            exit_time = datetime.now()
            hours = max(1, int((exit_time - entry_time).total_seconds() / 3600))
            fee = hours * RATE_PER_HOUR

            data.remove(v)
            save_data(data)

            print(f"Vehicle removed.")
            print(f"Time Parked: {hours} hour(s)")
            print(f"Parking Fee: ₹{fee}")
            return

    print("Vehicle not found.")


def view_parked_vehicles():
    data = load_data()

    if not data:
        print("No vehicles parked.")
        return

    print("\n--- Parked Vehicles ---")
    for v in data:
        print(f"Number: {v['vehicle_no']} | Type: {v['vehicle_type']} | Entry: {v['entry_time']}")


def menu():
    print("\n===== Parking Management System =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. View Parked Vehicles")
    print("4. Available Slots")
    print("5. Exit")
    return input("Choose option: ")


def main():
    while True:
        choice = menu()

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            view_parked_vehicles()
        elif choice == "4":
            print(f"Available Slots: {available_slots()}")
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()