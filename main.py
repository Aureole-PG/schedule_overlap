from infrastructure import File
from controller import Parcer, Coincidence

if __name__== '__main__':
    dataset = File('data.txt')
    result = []
    for data in dataset.data_file():
        user_data = Parcer(data)
        if user_data.validate(user_data.data):
            schedule = []
            print(user_data.data)
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
    