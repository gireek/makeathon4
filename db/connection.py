import psycopg2
from sqlalchemy.orm import sessionmaker

from config.utils import config
from sqlalchemy import create_engine
from db import models
import pandas as pd
from proj_data.bhp_sep.raw import path as raw_path
# execute a statement
# print('PostgreSQL database version:')
# cur.execute('SELECT version()')
# # display the PostgreSQL database server version
# db_version = cur.fetchone()
# print(db_version)
# # close the communication with the PostgreSQL
# cur.close()

class DBConnnection(object):
    def __init__(self):
        self.__params = config()
        self.__connection=None
    def __connect(self):
        try:
            self.__connection = psycopg2.connect(**self.__params)
        except (Exception, psycopg2.DatabaseError) as error:
            raise error

    def get_connection(self):
        if self.__connection is None:
            self.__connect()
        return self.__connection

    def close_conection(self):
        if self.__connection is not None:
            self.__connection.close()

    def __del__(self):
        self.close_conection()





engine = create_engine(models.DATABASE_URI)
# models.Base.metadata.create_all(engine)

df = pd.read_csv(raw_path.get("Hackathon_DataSet_OctApr_Part1.txt"), sep='\t').drop('Id', 1).drop(
            'hackathon4',
            1).drop(
            'PIIntTSTicks', 1).drop('PIIntShapeID', 1)
Session = sessionmaker(bind=engine)
s = Session()
for row in df.values:
    print(len(row))
    flowline = models.Flowline(*row)
    s.add(flowline)
    s.commit()


# part_1['TimeStamp'] = pd.to_datetime(part_1['TimeStamp'])
#
# # part_1.to_sql('flowline', engine)
# print(len(df.columns))
# print(df.columns)
# dbc = DBConnnection()
# conn = dbc.get_connection()
# out = list(','.join(str(x) for x in y) for y in df.values)
# if len(df) > 0:
#     df_columns = list(df)
#     columns = ",".join(df_columns)
#     for column in out:
#         # print(column)
#         # value = "VALUES({})".format(",".join(["%s" for _ in column]))
#         insert_stmt = "INSERT INTO {} VALUES({})".format('flowline',column)
#         cur = conn.cursor()
#         try:
#             cur.execute(insert_stmt)
#             conn.commit()
#         except:
#             print("error")
#             pass
#     cur.close()
# del (conn)