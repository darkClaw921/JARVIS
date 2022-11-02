from loguru import logger
from localDataBase import sql


message = 'ты где'
@logger.catch
def get_last_location():
    last_location = sql.get_last_location()
    return last_location

@logger.catch
def update_last_location(location:str):
    b = sql.update(location)[0]
    return b
@logger.catch
def main(): 
    sql.send_first()
    update_last_location('табаго')
    a = get_last_location()
    logger.debug(a)

if __name__ == "__main__":
    main()

