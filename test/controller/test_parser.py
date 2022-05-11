from datetime import datetime
import pytest
from controller import Parser
from domain import Schedule



@pytest.mark.parametrize(
    ['data','expected_name'],
    [
        ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ASTRID'),
        ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'RENE'),
        ('ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES'),
    ]
)
def test_parser_user(data, expected_name):
    parser = Parser(data)  

    result = parser.user.name
    
    assert result == expected_name


def test_parser_schedule():
    expected_schedules = [
        Schedule('MO',datetime(1,1,1,10,0), datetime(1,1,1,12,0)),
        Schedule('TH',datetime(1,1,1,12,0), datetime(1,1,1,14,0)),
        Schedule('SU',datetime(1,1,1,20,0), datetime(1,1,1,21,0)),
      ]
    parser = Parser('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')  
    
    results = parser.parceSchedule()

    assert all([expected.day == result.day for expected, result in zip(expected_schedules, results) ])
    assert all([expected.start.hour == result.start.hour for expected, result in zip(expected_schedules, results)] ) 
    assert all([expected.end.hour == result.end.hour for expected, result in zip(expected_schedules, results)] ) 

