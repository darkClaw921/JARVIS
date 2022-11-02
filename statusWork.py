
from dotenv import load_dotenv
from loguru import logger
from art import text2art
from bitrix24 import Bitrix24

from pprint import pprint
import os 

logger.add('log.log', level='INFO')

load_dotenv()
webhook = os.environ.get('webHook')

bit = Bitrix24(webhook)

tasksRU= {
        '49':['Разработка','💻'],
        '511':['Тестирование','📊'],
        '423':['Формирование задачи','✴'],
        '391':['Выполнено, ожидает подтверждения','⌛'],
        '395':['Выполнено','✅'],
        '419':['Задача сформирована','✳'],
        '441':['Оплачено','💵']
        }

@logger.catch
def get_tasks():
    #a = bit.callMethod('tasks.task.list', FILTER={'CREATED_BY':601}, select=['TITLE','STAGE_ID','DESCRIPTION'])#'RESPONSIBLE_ID':601,'GROUP_ID': 25,}, select=['TITLE'])
    a = bit.callMethod('tasks.task.list', FILTER={'ACCOMPLICE':601}, select=['TITLE','STAGE_ID','DESCRIPTION'])#'RESPONSIBLE_ID':601,'GROUP_ID': 25,}, select=['TITLE'])
    #a = bi.callMethod('tasks.task.get', taskId=1921, select=['TITLE','DESCRIPTION','STAGE_ID'])
    return a

@logger.catch
def prepare_str(tasks:list):
    string = '(J.A.R.V.I.S.) Статус активных работ Госпадина Герасимова:\n\n'
    for task in tasks['tasks']:
        stage = tasksRU[task['stageId']]
        descr = task['description'].split('§')[0]

        string +=f"    {task['title']} - {stage[0]} - {stage[1]} {descr} \n\n"
    return string

@logger.catch
def main():
    a = get_tasks()
    a = prepare_str(a)
    return a

if __name__ == '__main__':
    art = text2art('tasks', 'rand')
    print(art)
    main()

