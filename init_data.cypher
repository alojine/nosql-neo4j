//init_data

// init networks
// CREATE (n1:Network {name: "TALLINN", category: "WAN"}),
//        (n2:Network {name: "RYGA", category: "WAN"}),
//        (n3:Network {name: "VILNIUS", category: "WAN"}),
//        (n4:Network {name: "MINSK", category: "WAN"}),
//        (n5:Network {name: "WARSAW", category: "WAN"}),
//        (n6:Network {name: "GDANSK", category: "WAN"}),
//        (n7:Network {name: "BERLIN", category: "WAN"}),
//        (n8:Network {name: "PRAHA", category: "WAN"}),
//        (n9:Network {name: "HAMBURG", category: "WAN"}),
//        (n10:Network {name: "AMSTERDAM", category: "WAN"}),
//        (n11:Network {name: "LONDON", category: "WAN"})

// init relations
// MATCH (n1:Network {name: 'RYGA'})
// MATCH (n2:Network {name: 'TALLINN'})
// CREATE (n1)-[:CONNECTED_TO {latency: 60}]->(n2)

// MATCH (n1:Network {name: 'RYGA'})
// MATCH (n2:Network {name: 'VILNIUS'})
// CREATE (n1)-[:CONNECTED_TO {latency: 40}]->(n2)

// MATCH (n1:Network {name: 'GDANSK'})
// MATCH (n2:Network {name: 'VILNIUS'})
// CREATE (n1)-[:CONNECTED_TO {latency: 50}]->(n2)

// MATCH (n1:Network {name: 'GDANSK'})
// MATCH (n2:Network {name: 'WARSAW'})
// CREATE (n1)-[:CONNECTED_TO {latency: 50}]->(n2)

// MATCH (n1:Network {name: 'VILNIUS'})
// MATCH (n2:Network {name: 'MINSK'})
// CREATE (n1)-[:CONNECTED_TO {latency: 70}]->(n2)

// MATCH (n1:Network {name: 'MINSK'})
// MATCH (n2:Network {name: 'VILNIUS'})
// CREATE (n1)-[:CONNECTED_TO {latency: 70}]->(n2)

// MATCH (n1:Network {name: 'BERLIN'})
// MATCH (n2:Network {name: 'WARSAW'})
// CREATE (n1)-[:CONNECTED_TO {latency: 80}]->(n2)

// MATCH (n1:Network {name: 'WARSAW'})
// MATCH (n2:Network {name: 'BERLIN'})
// CREATE (n1)-[:CONNECTED_TO {latency: 80}]->(n2)

// MATCH (n1:Network {name: 'BERLIN'})
// MATCH (n2:Network {name: 'GDANSK'})
// CREATE (n1)-[:CONNECTED_TO {latency: 70}]->(n2)

// MATCH (n1:Network {name: 'GDANSK'})
// MATCH (n2:Network {name: 'BERLIN'})
// CREATE (n1)-[:CONNECTED_TO {latency: 70}]->(n2)

// MATCH (n1:Network {name: 'PRAHA'})
// MATCH (n2:Network {name: 'BERLIN'})
// CREATE (n1)-[:CONNECTED_TO {latency: 75}]->(n2)

// MATCH (n1:Network {name: 'AMSTERDAM'})
// MATCH (n2:Network {name: 'LONDON'})
// CREATE (n1)-[:CONNECTED_TO {latency: 100}]->(n2)

// MATCH (n:Network {name: 'WARSAW'})-[r:CONNECTED_TO]->()
// DELETE r

// GET all networks and their latency connections
// MATCH (n:Network)-[r:CONNECTED_TO]->(m:Network)
// RETURN n.name AS Source, m.name AS Destination, r.latency AS Latency

// MATCH (s:Network {name: "VILNIUS"})
// CREATE (u:User {name: "Tomas", ip: "192.33.12.1"})-[:JOINED]->(s)
// RETURN u, s

// MATCH (u:User {name: "Anton"})-[r:JOINED]->()
// DELETE r, u

// MATCH (n) WHERE ID(n) = 21
// DETACH DELETE n

// GET shortest path between two specified networks
// MATCH (start:Network {name: "Network A"}), (end:Network {name: "Network D"})
// MATCH path = shortestPath((start)-[:CONNECTED_TO*]-(end))
// RETURN path, reduce(totalLatency = 0, r in relationships(path) | totalLatency + r.latency) AS TotalLatency

// Find networks directly connected to a specific network with latency less than a certain value:
// MATCH (n:Network {name: "Network A"})-[r:CONNECTED_TO]->(m:Network)
// WHERE r.latency < 40
// RETURN m.name AS ConnectedNetwork, r.latency AS Latency

// MATCH (n:Network {name: 'VILNIUS'})
// RETURN n


