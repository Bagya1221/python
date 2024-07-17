import requests

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def get_traffic_info(start, destination):
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": start,
        "destination": destination,
        "key": API_KEY,
        "traffic_model": "best_guess",  # Use real-time traffic data
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            # Extract relevant information (e.g., duration, traffic conditions)
            duration = data["routes"][0]["legs"][0]["duration"]["text"]
            traffic_condition = data["routes"][0]["legs"][0]["traffic_speed_entry"]
            incidents = data["routes"][0].get("legs")[0].get("steps")[0].get("traffic_condition")
            return duration, traffic_condition, incidents
        else:
            print(f"Error fetching traffic data: {data.get('error_message', 'Unknown error')}")
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
    return None, None, None

if __name__ == "__main__":
    start_point = input("Enter starting point: ")
    destination_point = input("Enter destination: ")

    duration, traffic, incidents = get_traffic_info(start_point, destination_point)

    if duration:
        print(f"Estimated travel time: {duration}")
        print(f"Traffic conditions: {traffic}")
        if incidents:
            print(f"Incidents: {incidents}")
    else:
        print("Unable to fetch traffic data.")
