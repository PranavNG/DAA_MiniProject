import json


def input_data():
    print("Vehicle type:")
    print("1. Ambulance")
    print("2. Police")
    print("3. Fire Brigade")
    veh_type = int(input())
    pc = int(input("Enter your Pincode "))
    Data = {}
    Data['vehicles'] = []
    Data['vehicles'].append({
        "id": 1,
        "type": 1,
        "pincode": 64149
    })
    Data['vehicles'].append({
        "id": 2,
        "type": 1,
        "pincode": 64149
    })
    Data['vehicles'].append({
        "id": 3,
        "type": 2,
        "pincode": 64149
    })
    Data['vehicles'].append({
        "id": 4,
        "type": 3,
        "pincode": 64149
    })
    Data['vehicles'].append({
        "id": 5,
        "type": 3,
        "pincode": 64150
    })
    Data['vehicles'].append({
        "id": 6,
        "type": 3,
        "pincode": 64151
    })
    Data['vehicles'].append({
        "id": 7,
        "type": 2,
        "pincode": 64152
    })
    Data['vehicles'].append({
        "id": 8,
        "type": 3,
        "pincode": 64152
    })
    Data['vehicles'].append({
        "id": 9,
        "type": 1,
        "pincode": 64153
    })
    Data['vehicles'].append({
        "id": 10,
        "type": 2,
        "pincode": 64153
    })
    Data['vehicles'].append({
        "id": 11,
        "type": 3,
        "pincode": 64154
    })
    Data['vehicles'].append({
        "id": 12,
        "type": 2,
        "pincode": 64155
    })
    Data['vehicles'].append({
        "id": 13,
        "type": 2,
        "pincode": 64155
    })
    Data['vehicles'].append({
        "id": 14,
        "type": 1,
        "pincode": 64156
    })
    Data['vehicles'].append({
        "id": 15,
        "type": 1,
        "pincode": 64156
    })
    Data['vehicles'].append({
        "id": 16,
        "type": 2,
        "pincode": 64156
    })
    Data['vehicles'].append({
        "id": 17,
        "type": 1,
        "pincode": 64157
    })
    Data['vehicles'].append({
        "id": 18,
        "type": 3,
        "pincode": 64157
    })
    Data['vehicles'].append({
        "id": 19,
        "type": 1,
        "pincode": 64158
    })
    Data['vehicles'].append({
        "id": 20,
        "type": 1,
        "pincode": 64158
    })
    Data['vehicles'].append({
        "id": 21,
        "type": 2,
        "pincode": 64158
    })
    Data['vehicles'].append({
        "id": 22,
        "type": 3,
        "pincode": 64158
    })
    Data['vehicles'].append({
        "id": 23,
        "type": 3,
        "pincode": 64158
    })
    Data['vehicles'].append({
        "id": 24,
        "type": 2,
        "pincode": 64159
    })
    Data['vehicles'].append({
        "id": 25,
        "type": 3,
        "pincode": 64159
    })
    Data['vehicles'].append({
        "id": 26,
        "type": 1,
        "pincode": 64160
    })
    Data['vehicles'].append({
        "id": 27,
        "type": 2,
        "pincode": 64161
    })
    Data['vehicles'].append({
        "id": 28,
        "type": 2,
        "pincode": 64161
    })
    Data['vehicles'].append({
        "id": 29,
        "type": 1,
        "pincode": 64162
    })
    Data['vehicles'].append({
        "id": 30,
        "type": 3,
        "pincode": 64162
    })
    Data['vehicles'].append({
        "id": 31,
        "type": 3,
        "pincode": 64162
    })
    Data['vehicles'].append({
        "id": 32,
        "type": 1,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 33,
        "type": 2,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 34,
        "type": 2,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 35,
        "type": 2,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 36,
        "type": 3,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 37,
        "type": 3,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 38,
        "type": 3,
        "pincode": 64163
    })
    Data['vehicles'].append({
        "id": 39,
        "type": 2,
        "pincode": 64165
    })
    Data['vehicles'].append({
        "id": 40,
        "type": 3,
        "pincode": 64165
    })
    Data['vehicles'].append({
        "id": 41,
        "type": 2,
        "pincode": 64166
    })
    Data['vehicles'].append({
        "id": 42,
        "type": 2,
        "pincode": 64166
    })
    Data['vehicles'].append({
        "id": 43,
        "type": 3,
        "pincode": 64166
    })
    Data['requests'] = []
    Data['requests'].append({
        "id": 1,
        "vehicle_type": veh_type,
        "pincode": pc,
        "vehicle_id": 0,
        "distance": 0
    })
    Data['distances'] = []
    Data['distances'].append({
        "pincode1": 64149,
        "pincode2": 64150,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64150,
        "pincode2": 64151,
        "distance": 2
    })
    Data['distances'].append({
        "pincode1": 64151,
        "pincode2": 64152,
        "distance": 3
    })
    Data['distances'].append({
        "pincode1": 64150,
        "pincode2": 64153,
        "distance": 2
    })
    Data['distances'].append({
        "pincode1": 64152,
        "pincode2": 64153,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64150,
        "pincode2": 64154,
        "distance": 7
    })
    Data['distances'].append({
        "pincode1": 64154,
        "pincode2": 64155,
        "distance": 6
    })
    Data['distances'].append({
        "pincode1": 64151,
        "pincode2": 64154,
        "distance": 6
    })
    Data['distances'].append({
        "pincode1": 64152,
        "pincode2": 64156,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64153,
        "pincode2": 64156,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64149,
        "pincode2": 64150,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64151,
        "pincode2": 64157,
        "distance": 5
    })
    Data['distances'].append({
        "pincode1": 64156,
        "pincode2": 64157,
        "distance": 6
    })
    Data['distances'].append({
        "pincode1": 64156,
        "pincode2": 64158,
        "distance": 5
    })
    Data['distances'].append({
        "pincode1": 64158,
        "pincode2": 64159,
        "distance": 6
    })
    Data['distances'].append({
        "pincode1": 64159,
        "pincode2": 64153,
        "distance": 5
    })
    Data['distances'].append({
        "pincode1": 64158,
        "pincode2": 64160,
        "distance": 5
    })
    Data['distances'].append({
        "pincode1": 64160,
        "pincode2": 64161,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64161,
        "pincode2": 64162,
        "distance": 7
    })
    Data['distances'].append({
        "pincode1": 64162,
        "pincode2": 64163,
        "distance": 3
    })
    Data['distances'].append({
        "pincode1": 64163,
        "pincode2": 64164,
        "distance": 6
    })
    Data['distances'].append({
        "pincode1": 64164,
        "pincode2": 64165,
        "distance": 8
    })
    Data['distances'].append({
        "pincode1": 64165,
        "pincode2": 64162,
        "distance": 7
    })
    Data['distances'].append({
        "pincode1": 64164,
        "pincode2": 64166,
        "distance": 4
    })
    Data['distances'].append({
        "pincode1": 64166,
        "pincode2": 64167,
        "distance": 9
    })
    Data['distances'].append({
        "pincode1": 64167,
        "pincode2": 64157,
        "distance": 11
    })

    with open('Data.json', 'w') as outfile:
        json.dump(Data, outfile)
