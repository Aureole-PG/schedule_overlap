from typing import List
from datetime import datetime
from domain import Schedule, User
class Parser:
    def __init__(self, data: str):
        self.data = data.replace(' ','')
        self._namePosition()
        self._parserUser()

    def _parserUser(self) -> User:
        self.user = User(self.data[:self.name_position])
        return self.user

    def _dateFormat(self, date: str) -> Schedule:
        day = date[:2]
        hours = date[2:].split('-')
        start = datetime.strptime(hours[0], '%H:%M')
        end = datetime.strptime(hours[1], '%H:%M')
        result = Schedule(day, start, end)
        return result
    def _namePosition(self):
        self.name_position = self.data.find('=')

    def parceSchedule(self) -> List[Schedule]:
        schedules = self.data[self.name_position+1:].split(',')
        self.schedule= [self._dateFormat(i) for i in schedules] 
        return self.schedule
    
    


    def validate(self, data:str) -> bool:
        if len(data) == 0:
            return False
        if  '=' not in data:
            return False
        return True


    