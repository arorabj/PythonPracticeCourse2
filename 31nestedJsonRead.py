import json

json_string = '''{
    "response_code": 200,
    "train_number": "12229",
    "position": "at Source",
    "route": [
        {
            "no": 1,
            "has_arrived": false,
            "has_departed": false,
            "scharr": "Source",
            "scharr_date": "15 Nov 2015",
            "actarr_date": "15 Nov 2015",
            "station": "LKO",
            "actdep": "22:15",
            "schdep": "22:15",
            "actarr": "00:00",
            "distance": "0",
            "day": 0
        },
        {
            "actdep": "23:40",
            "scharr": "23:38",
            "schdep": "23:40",
            "actarr": "23:38",
            "no": 2,
            "has_departed": false,
            "scharr_date": "15 Nov 2015",
            "has_arrived": false,
            "station": "HRI",
            "distance": "101",
            "actarr_date": "15 Nov 2015",
            "day": 0
        }
    ]
}'''

json_data = json.loads(json_string)

train_number = json_data["train_number"]

print (json_data["route"])
print (json_data["route"][1])
print (json_data["route"][1]["actdep"])

has_arrived = json_data["route"][0]["has_arrived"]
print(has_arrived)  # Output: 12229

for i in json_data["route"]:
    print (i ["scharr"])