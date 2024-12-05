import mysql.connector


def store_data(my_list):
    cnx = mysql.connector.connect(host='127.0.0.1',
                              database='truecar',
                              user='root',
                              password='root')
    cursor = cnx.cursor()
    counter = 0
    for brand, model, year, miles, price in my_list:
        query = (f"""INSERT INTO mycar (brand, model, year, miles, price)
                         VALUES 
                         ('{brand}', '{model}', '{year}', '{miles}', '{price}')""")
        cursor.execute(query)
        counter += 1
    print("added %i cars to database! " % counter)
    cnx.commit()
    cnx.close()


def clear_data():
    cnx = mysql.connector.connect(host='127.0.0.1',
                                  database='truecar',
                                  user='root',
                                  password='root')
    cursor = cnx.cursor()
    query = "TRUNCATE TABLE mycar"
    cursor.execute(query)
    print("database cleared! ")
    cnx.commit()
    cnx.close()


def read_data():
    cnx = mysql.connector.connect(user='root',
                                  database='truecar',
                                  host='127.0.0.1',
                                  password='root')
    cursor = cnx.cursor()
    query = "SELECT * FROM mycar"
    result = []
    cursor.execute(query)
    for (brand, model, year, miles, price) in cursor:
        result.append([year, miles, price])
    return result


def update_data(my_list):
    clear_data()
    store_data(my_list)


