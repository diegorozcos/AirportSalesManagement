import logging 
import time

log = logging.getLogger()

CREATE_KEYSPACE = """
        CREATE KEYSPACE IF NOT EXISTS {}
        WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' : {} }}
        """

# Creación de tablas
CREATE_USERS_TABLE = """
        CREATE TABLE IF NOT EXISTS users ( 
            gender text,
            name text,
            PRIMARY KEY ((gender), name)
        )
"""

CREATE_TRAVEL_MONTH_TABLE = """
        CREATE TABLE IF NOT EXISTS travel_month (
            day decimal, 
            year decimal,
            month decimal,
            airline text,
            origin text,
            destination text,
            reason text,
            connection boolean,
            wait decimal,
            transit text,
            stay text,
            PRIMARY KEY ((month), reason, transit)
        ) 
"""

CREATE_CONNECTION_TABLE = """
        CREATE TABLE IF NOT EXISTS connection (
            day decimal, 
            year decimal,
            month decimal,
            airline text,
            origin text,
            destination text,
            reason text,
            connection boolean,
            wait decimal,
            transit text,
            stay text,
            PRIMARY KEY ((connection), origin, wait)
        )
"""

CREATE_HOTEL_MARKETING_TABLE = """
        CREATE TABLE IF NOT EXISTS hotel_marketing (
            day decimal,
            year decimal,
            month decimal,
            airline text,
            origin text,
            destination text,
            reason text,
            connection boolean,
            wait decimal,
            transit text,
            stay text,
            PRIMARY KEY ((connection), origin, reason, stay)
        )
"""

# Creación de consultas para el primer problema a resolver
SELECT_DEMANDED_DATE_BY_MONTH = """
        SELECT COUNT(month) AS demanded_month
        FROM travel_month
        WHERE month = ? AND reason = 'On Vacation/Pleasure' AND transit = 'Rental Car' 
"""

# Creación de consultas para el segundo problema a resolver
SELECT_CONNECTION_FLIGHTS = """
        SELECT COUNT(connection) AS connection_flights
        FROM connection
        WHERE connection = true AND wait > 100 AND origin = ?
"""

# Creación de consultas para el tercer problema a resolver
SELECT_HOTEL_MARKETING = """
        SELECT COUNT(connection) AS connection_flights
        FROM hotel_marketing
        WHERE connection = true AND origin = ? AND reason = 'Business/Work' AND stay = 'Hotel'
"""

# Funciones 
def create_keyspace(session, keyspace, replication_factor):
    log.info(f"Creating keyspace: {keyspace} with replication factor {replication_factor}")
    session.execute(CREATE_KEYSPACE.format(keyspace, replication_factor))

def create_schema(session):
    log.info("Creating model schema")
    session.execute(CREATE_USERS_TABLE)
    session.execute(CREATE_TRAVEL_MONTH_TABLE)
    session.execute(CREATE_CONNECTION_TABLE)
    session.execute(CREATE_HOTEL_MARKETING_TABLE)

def get_demanded_date_by_month(session, month):
    log.info(f"Getting demanded date by month: {month}")
    stmt = session.prepare(SELECT_DEMANDED_DATE_BY_MONTH)
    result = session.execute(stmt, [month])
    count = result[0][0]
    print(f"The month number {month} appears {count} times in the DB, with the given conditions.")
    time.sleep(3)
    if count >= 50:
        print(f"Month number {month} has a high demand, it is recommended to introduce marketing campaigns for car rentals.")
    else:
        print(f"Month number {month} has a low demand, it is not recommended to introduce marketing campaigns for car rentals.")
    time.sleep(3)

def get_connection_flights(session, origin):
    log.info(f"Getting connection flights.")
    stmt = session.prepare(SELECT_CONNECTION_FLIGHTS)
    result = session.execute(stmt, [origin])
    count = result[0][0]
    print(f"There are {count} conecting flights with a waiting time greater than 100 minutes at the {origin} airport.")
    time.sleep(3)
    if count >= 100:
        print(f"There are {count} flights with connection and with a waiting time greater than 100 minutes, it is recommended to introduce food services at the airport.")
    else:
        print(f"There are only {count} flights with connection and with a waiting time greater than 100 minutes, it is not recommended to introduce food services at the airport.")
    time.sleep(3)

def get_hotel_marketing(session, origin):
    log.info(f"Getting connection flights where travelers stay at the hotel during their wait time.")
    stmt = session.prepare(SELECT_HOTEL_MARKETING)
    result = session.execute(stmt, [origin])
    count = result[0][0]
    print(f"There are {count} flights where travelers stay at the hotel during their wait time and travel for business at the {origin} airport.")
    time.sleep(3)
    if count >= 100:
        print(f"There are {count} flights where travelers stay at the hotel during their wait time and travel for business, it is recommended to introduce marketing campaigns for hotels.")
    else:
        print(f"There are only {count} flights where travelers stay at the hotel during their wait time and travel for business, it is not recommended to introduce marketing campaigns for hotels.")
    time.sleep(3)