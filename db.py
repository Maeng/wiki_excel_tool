import configparser
import pymysql.cursors
config = configparser.ConfigParser()
config.read('config.ini')


class DB:
    def __init__(self):
        self.connection = pymysql.connect(host=config['DATABASE']['HOST'],
                                          port=int(config['DATABASE']['PORT']),
                                          user=config['DATABASE']['USER'],
                                          db='wiki',
                                          password=config['DATABASE']['PASSWORD'],
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor,
                                          use_unicode=True,
                                          autocommit=True)

    def __del__(self):
        self.connection.close()

    def get_procedure(self, sql, argv):
        with self.connection.cursor() as cursor:
            cursor.callproc(sql, argv)
            result = [r for r in cursor]
            cursor.close()
            return result

    def query(self, sql, argv=None):
        with self.connection.cursor() as cursor:
            cursor.executemany(sql, argv)
            cursor.close()

    def select(self, sql, argv=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, argv)
            return cursor.fetchall()
