import pandas as pd
import json
from src.config import USER_DATA_PATH, DRONE_DATA_PATH, MISSION_DATA_PATH, USER_JSON_PATH, DRONE_JSON_PATH, MISSION_JSON_PATH

def load_user_data():
    try:
        return pd.read_excel(USER_DATA_PATH)
    except FileNotFoundError:
        print(f"Error: User data file not found ar {USER_DATA_PATH}")
    except Exception as e:
        print(f"Error loading user data: {e}")


def load_drone_data():
    try:
        with open(DRONE_DATA_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Invalid JSON format ")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in drone data file at {DRONE_DATA_PATH}")
    except Exception as e:
        print(f"Error loadinf drone data: {e}")
    return None


def load_mission_data():
    try:
        return pd.read_csv(MISSION_DATA_PATH)
    except FileNotFoundError:
        print(f"Error: Mission data file not found at {MISSION_DATA_PATH}")
    except Exception as e:
        print(f"Error loading mission data: {e}")
    return None

def save_to_json(data, path):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data to {path}: {e}")

def aggregate_data():
    user_data = load_user_data()
    drone_data = load_drone_data()
    mission_data = load_mission_data()

    if user_data is not None:
        user_data = user_data.to_dict(orient='records')
        print("Saving User Data")
        save_to_json(user_data, USER_JSON_PATH)
    else:
        print("Skipping user data due to errors.")

    if drone_data is not None:
        print("Saving drone data.")
        save_to_json(drone_data, DRONE_JSON_PATH)
    else:
        print("Skipping drone data due to errors.")

    if mission_data is not None:
        mission_data = mission_data.to_dict(orient='records')
        print("Saving mission data.")
        save_to_json(mission_data, MISSION_JSON_PATH)
    else:
        print("Skipping mission data due to errors.")


    return user_data if user_data is not None else None, drone_data, mission_data if mission_data is not None else None


if __name__ == "__main__":
    aggregate_data()