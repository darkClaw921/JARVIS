import traceback
import asyncio
import sqlite3
from loguru import logger
import time

class SqlLite:
    
    @logger.catch
    def __init__(self, nameDB: str, tableQuery: str):
        self.nameDB = nameDB
        self.conn = sqlite3.connect(nameDB)
        self.cur  = self.conn.cursor()
        try:
            self.cur.execute(tableQuery)
            self.send_first() 
        except Exception as e :
            print(f'База данных уже создана {__name__}[выполняеться подключение]')#, traceback.print_exc())
        self.conn.commit()

    #@asyncio.coroutine
    @logger.catch
    def send_first(self):
        print('Первая запись')
        self.cur.execute('insert into setting (last_location) values ("обoага")')
        self.conn.commit()

    @logger.catch
    def update(self, location:str):
        self.cur.execute(f"""update setting set last_location="{location}" where id = 1 """)
        self.conn.commit()
  
    @logger.catch
    def get_last_location1(self):
        query = """select * last_location from setting """
        """
            return: list - [0] номер последней строки
                           [1] последний id§
        """
        #query= f'select last_location from setting where id = 1'
        a = self.conn.execute(query)
        #print(list(a)[0])# не может быть чтобы листь меняло занче по адоесу list
        return list(a)[0]   
   
    def clear_column(self, nameTable):
        self.conn.execute(
        f"""
        DELETE FROM {nameTable} WHERE 1
        """)

print('создание таблицы')
sql = SqlLite('temp.db', """create table setting(
        id integer primary key,
        last_location text default 'Общага',
        temp text );""")
#get_last_locationgget_last_locationet_last_location
