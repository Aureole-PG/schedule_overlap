from typing import List

class Coincidence:
    def __init__(self, schedule: List):
       self.schedule = schedule
    
    def compare(self) -> List:
        result=[]
        for idx, user in enumerate(self.schedule):
            for user_to_compare in self.schedule[idx+1:]:
                coincided_schedule = self._countCoincidedSchedule(user['schedule'], user_to_compare['schedule'])
                result.append({'names':user['name']+'-'+user_to_compare['name'], 'coincided':coincided_schedule})
        return result 

    def _countCoincidedSchedule(self, schedule: List, schedule_to_compare: List) -> int:
        count = 0
        for date in schedule:
            time = list(filter(lambda x: x['day'] == date['day'],schedule_to_compare ))   
            coincidences = list(filter(lambda x: x['start'] < date['end'] and x['end'] > date['start']  ,time ))
            count += len(coincidences)
        return count