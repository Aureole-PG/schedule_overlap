from infrastructure import File
from controller import Parser, Coincidence
import os
if __name__== '__main__':
    path= os.getcwd()+'/infrastructure/data2.txt' 
    dataset = File(path)
    result = []
    for data in dataset.data_file():
        user_data = Parser(data)
        if user_data.validate(user_data.data):
            schedule = []
            for i in user_data.parceSchedule():
                schedule.append({
                    'day': i.day,
                    'start': i.start,
                    'end': i.end
                })
            result.append({
                'name': user_data.user.name,
                'schedule': schedule
            })
    coincidence = Coincidence(result)
    for i in coincidence.compare():
        print(i)
    