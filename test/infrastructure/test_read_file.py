from infrastructure import File
import os
test_file = os.getcwd()+'/test/test.txt'
rows=[
    '1'
    '1',
    '1'
]

def _create():
    with open(test_file, 'w', newline='') as test:
        for lines in rows:
            test.write(lines + os.linesep)

def _remove():
    os.remove(test_file)

def test_read_file():
    _create()
    
    file_readed = File(test_file)
    result =file_readed.data_file()
    assert result == rows 
    _remove()
