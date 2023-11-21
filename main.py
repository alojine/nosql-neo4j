from db import NetworkDB
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import os
load_dotenv()

URI = os.getenv('NEO4J_URI')
USER = os.getenv('NEO4J_USER')
PASSWORD = os.getenv('NEO4J_PASSWORD')

app = Flask(__name__)

@app.route('/networks', methods=['GET'])
def get_networks():
    networks_with_latency = db.get_networks_with_latency()
    return jsonify(networks_with_latency)

@app.route('/networks/latency/<latency>', methods=['GET'])
def get_networks_by_latency(latency):
    print(latency)
    networks_by_latency = db.get_networks_by_latency(latency)
    return jsonify(networks_by_latency)

@app.route('/networks/name/<name>', methods=['GET'])
def get_network_by_name(name):
    network_by_name = db.get_network_by_name(name)
    return jsonify(network_by_name)

@app.route('/networks/shortest-path/<start_network>/<end_network>', methods=['GET'])
def shortest_path_details(start_network, end_network):
    path_details = db.get_shortest_path_details(start_network, end_network)
    return jsonify(path_details)

@app.route('/users', methods=['POST'])
def create_user():
    user_name = request.json.get('user_name')
    user_ip = request.json.get('user_ip')
    network_name = request.json.get('network_name')

    if user_name and user_ip and network_name:
        result = db.create_user_and_join_network(user_name, user_ip, network_name)
        return jsonify(result)
    else:
        return jsonify({'error': 'Missing user or server information'}), 400

@app.route('/users/by-network/<network_name>', methods=['GET'])
def get_users_by_network(network_name):
    users = db.get_users_by_network_name(network_name)
    return jsonify(users)

if __name__ == "__main__":
    db = NetworkDB(URI, USER, PASSWORD)
    app.run(host='0.0.0.0', port=8080, debug=True)



