import json

# Manually written train data
train_data = [
    {"train_number": "IC552", "departure_time": "07:25", "arrival_time": "13:05"},
    {"train_number": "IC724", "departure_time": "13:20", "arrival_time": "19:17"},
]

# Manually written flight data
flight_data = [
    {"flight_number": "IB1832", "departure_time": "14:50", "arrival_airport": "MAD", "destination_city": "Madrid"},
    {"flight_number": "U24187", "departure_time": "14:55", "arrival_airport": "LYS", "destination_city": "Lyon"},
    {"flight_number": "AZ1296", "departure_time": "15:00", "arrival_airport": "LIN", "destination_city": "Milan"},
    {"flight_number": "LX1711", "departure_time": "15:00", "arrival_airport": "ZRH", "destination_city": "Zurich"},
    {"flight_number": "AZ1270", "departure_time": "15:15", "arrival_airport": "FCO", "destination_city": "Rome"},
    {"flight_number": "FR4112", "departure_time": "15:25", "arrival_airport": "BGY", "destination_city": "Milan"},
    {"flight_number": "FR6836", "departure_time": "15:30", "arrival_airport": "VLC", "destination_city": "Valencia"},
    {"flight_number": "VY6503", "departure_time": "16:00", "arrival_airport": "BCN", "destination_city": "Barcelona"},
    {"flight_number": "W64370", "departure_time": "16:05", "arrival_airport": "SOF", "destination_city": "Sofia"},
    {"flight_number": "FR638", "departure_time": "16:15", "arrival_airport": "PFO", "destination_city": "Pafos"},
    {"flight_number": "U24231", "departure_time": "16:15", "arrival_airport": "AMS", "destination_city": "Amsterdam"},
    {"flight_number": "AZ1290", "departure_time": "16:20", "arrival_airport": "LIN", "destination_city": "Milan"},
    {"flight_number": "UG1731", "departure_time": "16:30", "arrival_airport": "TUN", "destination_city": "Tunis"},
    {"flight_number": "Linz (LNZ)", "departure_time": "16:30", "arrival_airport": "LNZ", "destination_city": "Linz"},
    {"flight_number": "W46901", "departure_time": "16:35", "arrival_airport": "LGW", "destination_city": "London"},
    {"flight_number": "AF1179", "departure_time": "16:45", "arrival_airport": "CDG", "destination_city": "Paris"},
    {"flight_number": "U24266", "departure_time": "16:50", "arrival_airport": "BER", "destination_city": "Berlin"},
    {"flight_number": "FR4676", "departure_time": "16:55", "arrival_airport": "GOA", "destination_city": "Genoa"},
    {"flight_number": "U24183", "departure_time": "17:00", "arrival_airport": "ORY", "destination_city": "Paris"},
    {"flight_number": "FR1897", "departure_time": "17:05", "arrival_airport": "GDN", "destination_city": "Gdansk"},
    {"flight_number": "FR8693", "departure_time": "17:10", "arrival_airport": "TFS", "destination_city": "Tenerife"},
    {"flight_number": "U23578", "departure_time": "17:20", "arrival_airport": "MXP", "destination_city": "Milan"},
    {"flight_number": "LH1879", "departure_time": "18:15", "arrival_airport": "MUC", "destination_city": "Munich"},
    {"flight_number": "AZ1282", "departure_time": "18:25", "arrival_airport": "LIN", "destination_city": "Milan"},
    {"flight_number": "FR4314", "departure_time": "18:30", "arrival_airport": "CTA", "destination_city": "Catania"},
    {"flight_number": "BA535", "departure_time": "18:40", "arrival_airport": "LHR", "destination_city": "London"},
    {"flight_number": "FR4045", "departure_time": "18:40", "arrival_airport": "KRK", "destination_city": "Krakow"},
    {"flight_number": "FR59", "departure_time": "19:00", "arrival_airport": "BCN", "destination_city": "Barcelona"},
    {"flight_number": "U24109", "departure_time": "19:05", "arrival_airport": "CTA", "destination_city": "Catania"},
    {"flight_number": "TK1880", "departure_time": "19:20", "arrival_airport": "IST", "destination_city": "Istanbul"},
    {"flight_number": "AZ1274", "departure_time": "19:40", "arrival_airport": "FCO", "destination_city": "Rome"},
    {"flight_number": "6H346", "departure_time": "19:40", "arrival_airport": "TLV", "destination_city": "Tel Aviv"},
    {"flight_number": "FR1337", "departure_time": "19:55", "arrival_airport": "TLS", "destination_city": "Toulouse"},
    {"flight_number": "AZ1298", "departure_time": "20:05", "arrival_airport": "LIN", "destination_city": "Milan"},
    {"flight_number": "FR5937", "departure_time": "20:20", "arrival_airport": "MXP", "destination_city": "Milan"},
    {"flight_number": "TO3829", "departure_time": "20:20", "arrival_airport": "ORY", "destination_city": "Paris"},
    {"flight_number": "FR6841", "departure_time": "20:25", "arrival_airport": "DUB", "destination_city": "Dublin"},
    {"flight_number": "FR869", "departure_time": "20:35", "arrival_airport": "VCE", "destination_city": "Venice"},
    {"flight_number": "U23580", "departure_time": "20:55", "arrival_airport": "MXP", "destination_city": "Milan"},
    {"flight_number": "FR4119", "departure_time": "21:20", "arrival_airport": "BGY", "destination_city": "Milan"},
    {"flight_number": "FR9028", "departure_time": "21:20", "arrival_airport": "VIE", "destination_city": "Vienna"},
    {"flight_number": "FR1330", "departure_time": "21:55", "arrival_airport": "MAD", "destination_city": "Madrid"},
    {"flight_number": "FR4654", "departure_time": "22:05", "arrival_airport": "CAG", "destination_city": "Cagliari"},
    {"flight_number": "FR222", "departure_time": "22:15", "arrival_airport": "AGP", "destination_city": "Malaga"}
]
# Convert HH:MM time format to total minutes
def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

# Find valid train-flight connections
def find_connections(trains, flights, buffer_time=60):
    connections = []
    for train in trains:
        train_arrival = time_to_minutes(train["arrival_time"])
        for flight in flights:
            flight_departure = time_to_minutes(flight["departure_time"])
            if flight_departure >= train_arrival + buffer_time:
                connections.append({
                    "from": train["train_number"],
                    "to": flight["flight_number"],
                    "from_time": train["arrival_time"],
                    "to_time": flight["departure_time"],
                    "to_city": flight["destination_city"],
                })
    return connections

# Main Program
if __name__ == "__main__":
    # Find connections
    connections = find_connections(train_data, flight_data)
    
    # Export connections to JSON
    json_output = {
        "nodes": [
            {"id": "Napoli", "type": "hub"},
            {"id": "Rome", "type": "flight", "label": "AZ123"},
            {"id": "London", "type": "flight", "label": "U2335"},
            {"id": "Barcelona", "type": "flight", "label": "FR567"},
            {"id": "Frankfurt", "type": "flight", "label": "LH456"},
        ],
        "connections": [
            {
                "from": "Napoli",
                "to": conn["to_city"],
                "label": f"{conn['from']} -> {conn['to']}",
                "time": f"{conn['from_time']} -> {conn['to_time']}",
            }
            for conn in connections
        ],
    }
    
    with open("connections.json", "w") as file:
        json.dump(json_output, file, indent=4)
    print("Connections saved to connections.json.")

import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the connections from the JSON file
with open('connections.json', 'r') as file:
    data = json.load(file)

# Initialize a directed graph (since this is a directed connection)
G = nx.DiGraph()

# Add nodes and edges to the graph
for connection in data['connections']:
    from_node = connection['from']
    to_node = connection['to']
    # Adding the edges (connections between nodes)
    G.add_edge(from_node, to_node, label=connection['label'], time=connection['time'])

# Generate a layout for the nodes (cities)
pos = nx.spring_layout(G, seed=42)

# Create a visualization
plt.figure(figsize=(12, 12))

# Draw the nodes (cities)
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', alpha=0.8)

# Draw the edges (connections)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')

# Draw the node labels (city names)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='black')

# Draw the edge labels (flight labels and times)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Display the plot
plt.title('Train-Flight Connections')
plt.axis('off')
plt.show()

# After drawing the graph
plt.savefig("graph.png")  # Saves the graph to a file
