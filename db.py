from neo4j import GraphDatabase

class NetworkDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()

    def get_networks_with_latency(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n:Network)-[r:CONNECTED_TO]->(m:Network)
                RETURN n.name AS Source, m.name AS Destination, r.latency AS Latency
                                 """)
            return result.data()
    
    def get_networks_by_latency(self, max_latency):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n:Network)-[r:CONNECTED_TO]->(m:Network)
                WHERE r.latency <= $latencyParam
                RETURN n.name AS Source, m.name AS Destination, r.latency AS Latency
            """, latencyParam=int(max_latency))
            return result.data()

    def get_network_by_name(self, network_name):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (network:Network {name: $name_param})
                RETURN network
            """, name_param = network_name)
            return result.data()
    
    def create_user_and_join_network(self, user_name, user_ip, network_name):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (network:Network {name: $networkName})
                CREATE (user:User {name: $userName, ip: $userIP})-[:JOINED]->(network)
                RETURN user, network
            """, userName=str(user_name), userIP=str(user_ip), networkName=str(network_name))
            return list(result.data())
    
    def get_users_by_network_name(self, network_name):
        with self.driver.session() as session:
            query = """
            MATCH (n:Network {name: $networkName})<-[:JOINED]-(u:User)
            RETURN u
            """
            result = session.run(query, networkName=network_name)
            return result.data()
    
    def get_shortest_path_details(self, start_network, end_network):
        with self.driver.session() as session:
            query = """
            MATCH (start:Network {name: $start}), (end:Network {name: $end})
            MATCH path = shortestPath((start)-[:CONNECTED_TO*]-(end))
            RETURN 
                start.name AS start,
                end.name AS end,
                [node in nodes(path) | node.name] AS path,
                length(path) AS length,
                reduce(totalLatency = 0, r in relationships(path) | totalLatency + r.latency) AS TotalLatency
            """
            result = session.run(query, start=start_network, end=end_network)
            return result.single()