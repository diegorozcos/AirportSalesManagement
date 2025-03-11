import random

CQL_FILE = 'data.cql'

MALE_GENDERS = [
    'male',
    'nonspecified'
]

FEMALE_GENDERS = [
    'female',
    'nonspecified'
]

MALE_NAMES = [
    'John Smith',
    'James Brown',
    'Michael Davis',
    'William Wilson',
    'David Jackson',
    'Christopher Martinez',
    'Robert Johnson',
    'Joseph Taylor'
]

FEMALE_NAMES = [
    'Emily Johnson',
    'Sarah Williams',
    'Jessica Lee',
    'Amanda Garcia',
    'Michelle Rodriguez',
    'Stephanie Hernandez',
    'Linda Davis',
    'Lauren Lopez'
]

AIRLINES = [
    'American Airlines',
    'Delta Airlines',
    'United Airlines',
    'Aeromexico'
]

CITIES = [
    'New York',
    'Los Angeles',
    'Chicago',
    'San Francisco',
    'Atlanta',
    'Miami',
    'Dallas',
    'Las Vegas',
    'Denver',
    'Seattle'
]

REASONS = [
    'On Vacation/Pleasure',
    'Business/Work',
    'Back Home'
]

TRANSIT = [
    'Airport Cab',
    'Rental Car',
    'Mobility as a Service',
]

STAY = [
    'Hotel',
    'Home',
    'Short-term Homestay',
    'Friends/Family'
]

def cql_stmt_generator(male_users=8, female_users=8, travels=500):
    male_users_stmt = "INSERT INTO users (gender, name) VALUES ('{}', '{}');"
    female_users_stmt = "INSERT INTO users (gender, name) VALUES ('{}', '{}');"
    travel_month_stmt = "INSERT INTO travel_month (day, year, month, airline, origin, destination, reason, connection, wait, transit, stay) VALUES ({}, {}, {}, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}');"
    connection_stmt = "INSERT INTO connection (day, year, month, airline, origin, destination, reason, connection, wait, transit, stay) VALUES ({}, {}, {}, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}');"
    hotel_marketing_stmt = "INSERT INTO hotel_marketing (day, year, month, airline, origin, destination, reason, connection, wait, transit, stay) VALUES ({}, {}, {}, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}');"

    with open(CQL_FILE, 'w') as fd:
        for i in range(male_users):
            gender = random.choice(MALE_GENDERS)
            male_name = random.choice(MALE_NAMES)
            fd.write(male_users_stmt.format(gender, male_name))
            fd.write('\n')
        fd.write('\n\n')
        
        for i in range(female_users):
            gender = random.choice(FEMALE_GENDERS)
            female_name = random.choice(FEMALE_NAMES)
            fd.write(female_users_stmt.format(gender, female_name))
            fd.write('\n')
        fd.write('\n\n')
        
        for i in range(travels):
            day = random.randint(1, 31)
            year = random.randint(2010, 2023)
            month = random.randint(1, 12)
            airline = random.choice(AIRLINES)
            city_from = random.choice(CITIES)
            city_to = random.choice(CITIES)
            reason = random.choice(REASONS)
            connection = random.choice([True, False])
            wait = random.randint(80, 300)
            transit = random.choice(TRANSIT)
            stay = random.choice(STAY)
            if connection == False:
                wait = 0
            fd.write(travel_month_stmt.format(day, year, month, airline, city_from, city_to, reason, connection, wait, transit, stay))
            fd.write('\n')
            fd.write(connection_stmt.format(day, year, month, airline, city_from, city_to, reason, connection, wait, transit, stay))
            fd.write('\n')
            fd.write(hotel_marketing_stmt.format(day, year, month, airline, city_from, city_to, reason, connection, wait, transit, stay))
        

def main():
    cql_stmt_generator()

if __name__ == '__main__':
    main()