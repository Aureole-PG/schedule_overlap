from infrastructure import File
import os
path_test = os.getcwd()+'/test/test.txt'
rows=[
    '1'
    '1',
    '1'
]

def _create():
    with open(path_test, 'w', newline='') as test:
        for lines in rows:
            test.write(lines + os.linesep)

def _remove():
    os.remove(path_test)

def test_read_file():
    _create()
    
    test_file = File(path_test)
    result =test_file.data_file()
    assert result == rows 
    _remove()
