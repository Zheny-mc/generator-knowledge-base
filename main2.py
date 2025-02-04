from neo4j import GraphDatabase, RoutingControl


class Neo4jConnection:
    def __init__(self, uri, user, password, database="neo4j"):
        self.database = database
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_friend(self, name, friend_name):
        self.driver.execute_query(
            "MERGE (a:Person {name: $name}) "
            "MERGE (friend:Person {name: $friend_name}) "
            "MERGE (a)-[:KNOWS]->(friend)",
            name=name, friend_name=friend_name, database_=self.database,
        )

    def print_friends(self, name):
        records, _, _ = self.driver.execute_query(
            "MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
            "RETURN friend.name ORDER BY friend.name",
            name=name, database_=self.database, routing_=RoutingControl.READ,
        )
        for record in records:
            print(record["friend.name"])

    def close(self):
        self.driver.close()

DATABASE = "neo4j"
URI = "bolt://localhost:7687"
AUTH = {"user": "neo4j", "password": "rootroot"}

# Example usage
conn = Neo4jConnection(URI, AUTH["user"], AUTH["password"], DATABASE)
conn.add_friend("Arthur", "Guinevere")
conn.add_friend("Arthur", "Lancelot")
conn.add_friend("Arthur", "Merlin")
conn.add_friend("Arthur", "Evgenyi")
conn.print_friends("Arthur")
conn.close()







