from flask import Blueprint, jsonify, current_app, g

networks_blueprint = Blueprint('networks_blueprint', __name__)

@networks_blueprint.route('/', methods=['GET'])
def get_networks():
    networks_with_latency = g.db.get_networks_with_latency()
    return jsonify(networks_with_latency)

@networks_blueprint.route('/latency/<latency>', methods=['GET'])
def get_networks_by_latency(latency):
    print(latency)
    networks_by_latency = g.db.get_networks_by_latency(latency)
    return jsonify(networks_by_latency)

@networks_blueprint.route('/name/<name>', methods=['GET'])
def get_network_by_name(name):
    network_by_name = g.db.get_network_by_name(name)
    return jsonify(network_by_name)

@networks_blueprint.route('/shortest-path/<start_network>/<end_network>', methods=['GET'])
def shortest_path_details(start_network, end_network):
    path_details = g.db.get_shortest_path_details(start_network, end_network)
    return jsonify(path_details)

@networks_blueprint.route('/all-paths-details/<start_network>/<end_network>', methods=['GET'])
def get_all_paths_details(start_network, end_network):
    paths_details = g.db.get_all_paths_details_between_networks(start_network, end_network)
    return jsonify(paths_details)