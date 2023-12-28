import json
import random

class service:
    
    datafile = {
        "dialog_set": "./resource/dialog_set.json"
    }
    dialog_dict = {}

    def __init__(self, caller: str = None):
        self.load_dialog_set()

    def read_json(self, file_location: str):
        return json.load(open(file_location,"r",encoding = 'utf-8'))

    def get_dialog_set(self):
        return self.read_json(self.datafile["dialog_set"])
        
    def load_dialog_set(self):
        self.dialog_dict = self.get_dialog_set()

    def find_matching_group(self, string: str):
        finding_group = self.dialog_dict.copy()
        finding_group.pop("")
        for i in finding_group:
            if string in finding_group[i]['question']:
                return i
        return ""

    def get_answers(self, from_group: str = ""):
        if from_group not in list(self.dialog_dict.keys()): raise Exception("err")
        if from_group == "": return self.dialog_dict[from_group]
        return self.dialog_dict[from_group]['answer']
    
    def get_answer(self, from_group: str = ""):
        return random.choice(self.get_answers(from_group))
        
    