from typing import List
from datetime import datetime
from domain import Schedule, User
class Parcer:
    def __init__(self, data: str):
        self.data = data.replace(' ','')
        self.namePosition()
        self.parcerUser()

    def parcerUser(self) -> User:
        self.user = User(self.data[:self.name_position])
        return self.user

    def parceSchedule(self) -> List[Schedule]:
        schedules = self.data[self.name_position+1:].split(',')
        self.schedule= [self.dateFormat(i) for i in schedules] 
        return self.schedule
    

    def dateFormat(self, date: str) -> Schedule:
        day = date[:2]
        hours = date[2:].split('-')
        start = datetime.strptime(hours[0], '%H:%M')
        end = datetime.strptime(hours[1], '%H:%M')
        result = Schedule(day, start, end)
        return result

    def validate(self, data:str) -> bool:
        if len(data) == 0:
            return False
        if  '=' not in data:
            return False
        return True


    def namePosition(self):
        self.name_position = self.data.find('=')