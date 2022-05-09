import os
from typing import List
class File:
    def __init__(self, file_name):
      self.file_name = file_name

    def data_file(self) -> List[str]:
        path=os.getcwd()+'/infrastructure/'+ self.file_name
        data = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                data.append(line.rstrip())
        return data
    def direcctory(self):
        return os.getcwd()

