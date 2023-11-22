from flask import Blueprint, jsonify, request, current_app, g

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    user_name = request.json.get('user_name')
    user_ip = request.json.get('user_ip')
    network_name = request.json.get('network_name')

    if user_name and user_ip and network_name:
        result = g.db.create_user_and_join_network(user_name, user_ip, network_name)
        return jsonify(result)
    else:
        return jsonify({'error': 'Missing user or server information'}), 400

@users_blueprint.route('/users/by-network/<network_name>', methods=['GET'])
def get_users_by_network(network_name):
    users = g.db.get_users_by_network_name(network_name)
    return jsonify(users)

