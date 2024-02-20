import mysql.connector
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class DB:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host="localhost",
            user="user_name",
            password="password",
            database="db_name"
        )

    def create_laptops_table(self):
        cursor = self.db.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS laptops (
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(50),
          price VARCHAR(50),
          screen_size VARCHAR(50)
        )
        """

        try:
            cursor.execute(create_table_query)
            self.db.commit()
        except mysql.connector.Error as err:
            logger.error(f"Error creating table: {err}")
        finally:
            cursor.close()

    def insert_laptops_data(self, laptops_data):
        cursor = self.db.cursor()

        insert_query = """
            INSERT INTO laptops (name, price, screen_size)
            VALUES (%s, %s, %s)
        """

        # convert list of dictionaries into list of tuples needed for executemany:
        laptops_data = [
            (laptop['name'], laptop['price'], laptop['screen_size'])
            for laptop in laptops_data
        ]
        logger.debug(laptops_data)

        try:
            cursor.executemany(insert_query, laptops_data)
            self.db.commit()
            logger.info(f"Successfully inserted: {len(laptops_data)} rows.")
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")


if __name__ == "__main__":
    db = DB()
    db.create_laptops_table()

    data = [
        {
            'name': "laptop_name1",
            'price': "price_laptop1",
            'screen_size': "laptop_screen_size1",

        },
        {
            'name': "laptop_name2",
            'price': "price_laptop2",
            'screen_size': "laptop_screen_size2",
        }
    ]

    db.insert_laptops_data(data)