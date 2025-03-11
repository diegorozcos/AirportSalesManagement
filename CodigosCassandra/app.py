import logging
import os
import time

from cassandra.cluster import Cluster

import cassandra_model as model

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('proyectoIntegrador.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars releated to Cassandra App
CLUSTER_IPS = os.getenv('CASSANDRA_CLUSTER_IPS', 'localhost')
KEYSPACE = os.getenv('CASSANDRA_KEYSPACE', 'proyectointegrador')
REPLICATION_FACTOR = os.getenv('CASSANDRA_REPLICATION_FACTOR', '1')

def print_menu():
    menu_options = {
        1: 'Introduction of rental car marketing campaigns: ',
        2: 'Introduction of food services at the airport: ',
        3: 'Introduction of hotel marketing campaigns: ',
        4: 'Exit'
    }
    for i in menu_options.keys():
        print(f"{i}. {menu_options[i]}")

def main():
    log.info("Connecting to Cluster")
    cluster = Cluster(CLUSTER_IPS.split(','))
    session = cluster.connect()

    model.create_keyspace(session, KEYSPACE, REPLICATION_FACTOR)
    session.set_keyspace(KEYSPACE)

    model.create_schema(session)
    
    print("Welcome to the travel agency application. ")

    while (True):
        time.sleep(1)
        print_menu()
        time.sleep(1)
        option = int(input("Select an option: "))
        if option == 1:
            month = int(input("Enter a month number: "))
            model.get_demanded_date_by_month(session, month)
        if option == 2:
            origin = input(str("Enter an origin airport: "))
            model.get_connection_flights(session, origin)
        if option == 3:
            origin = input(str("Enter an origin airport: "))
            model.get_hotel_marketing(session, origin)
        if option == 4:
            exit(0)

if __name__ == '__main__':
    main()