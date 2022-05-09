from datetime import datetime
from controller import Coincidence

def test_compare():
    expected = [
        {'names': 'RENE-ASTRID', 'coincided': 3}
    ]
    data = [
        {
            'name': 'RENE', 
            'schedule': [
                {
                    'day': 'MO', 
                    'start': datetime(1900, 1, 1, 10, 15), 
                    'end': datetime(1900, 1, 1, 12, 0)
                }, 
                {'day': 'TU', 
                'start': datetime(1900, 1, 1, 10, 0), 
                'end': datetime(1900, 1, 1, 12, 0)
            }, 
            {
                'day': 'TH', 
                'start': datetime(1900, 1, 1, 13, 0), 
                'end': datetime(1900, 1, 1, 13, 15)
            }, 
            {
                'day': 'SA', 
                'start': datetime(1900, 1, 1, 14, 0), 
                'end': datetime(1900, 1, 1, 18, 0)
            }, 
            {
                'day': 'SU', 
                'start': datetime(1900, 1, 1, 20, 0), 
                'end': datetime(1900, 1, 1, 21, 0)
            }
        ]
    }, 
    {
        'name': 'ASTRID', 
        'schedule': [
            {
                'day': 'MO', 
                'start': datetime(1900, 1, 1, 10, 0), 
                'end': datetime(1900, 1, 1, 12, 0)
            }, 
            {
                'day': 'TH', 
                'start': datetime(1900, 1, 1, 12, 0), 
                'end': datetime(1900, 1, 1, 14, 0)
            }, 
            {
                'day': 'SU', 
                'start': datetime(1900, 1, 1, 20, 0), 
                'end': datetime(1900, 1, 1, 21, 0)
            }
        ]
    }
    ]

    coincidence = Coincidence(data)
    result = coincidence.compare()
    assert result == expected