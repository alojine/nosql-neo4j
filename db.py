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
                MATCH (n:Network {name: $name_param})
                RETURN n
            """, name_param = network_name)
            return result.data()
    
    def create_user_and_join_network(self, user_name, user_ip, network_name):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n:Network {name: $networkName})
                CREATE (u:User {name: $userName, ip: $userIP})-[:JOINED]->(n)
                RETURN u, n
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