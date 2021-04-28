import sys
import json
import dijkstra
import input


input.input_data()
if __name__ == '__main__':

    with open(sys.argv[1], 'r') as data_file:
        datastore = json.load(data_file)

    distances = datastore['distances']
    requests = datastore['requests']
    vehicles = datastore['vehicles']

    for vehicle in vehicles:
        vehicle['available'] = True

    g = dijkstra.Graph()

    for distance in distances:
        if not distance['pincode1'] in g.get_vertices():
            g.add_vertex(distance['pincode1'])

        if not distance['pincode2'] in g.get_vertices():
            g.add_vertex(distance['pincode2'])

        g.add_edge(distance['pincode1'], distance['pincode2'], distance['distance'])


    def get_vehicle(vehicle_type, pincode):
        available_vehicles = [v for v in vehicles if v['type'] == vehicle_type and v['available']]

        if len(available_vehicles) > 0:
            g.reset_vertices()
            place = g.get_vertex(pincode)
            try:
                dijkstra.dijkstra(g, place)
            except:
                print("error")

            for av in available_vehicles:
                av['distance'] = g.get_vertex(av['pincode']).get_distance()

            available_vehicles = sorted(available_vehicles, key=lambda k: k['distance'])

        return available_vehicles


    for request in requests:
        ev = get_vehicle(request['vehicle_type'], request['pincode'])

        if len(ev) > 0:
            vehicles[vehicles.index(ev[0])]['available'] = False
            request['vehicle_id'] = ev[0]['id']
            request['distance'] = ev[0]['distance']
            if request['vehicle_type'] == 1:
                request['vehicle_type'] = "Ambulance"
            elif request['vehicle_type'] == 2:
                request['vehicle_type'] = "Police"
            else:
                request['vehicle_type'] = "Fire Brigade"
            print("Vehicle type- " + str(request['vehicle_type']) + ", To- " + str(
                request['pincode']) + ", Vehicle ID- " + str(request['vehicle_id']) + ".")
            print("Closest distance would be " + str(request['distance']) + "km")
