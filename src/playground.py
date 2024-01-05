import json
import random
from difflib import *

class service:
    
    datafile = {
        "dialog_set": "./resource/dialog_set.json",
        "log": "./resource/log.json"
    }
    dialog_dict = {}
    questions_log = {}

    def __init__(self):
        self.load_dialog_set()
        self.load_questions_log()

    def read_json(self, file_location: str):
        return json.load(open(file_location,"r",encoding = 'utf-8'))

    def get_dialog_set(self):
        return self.read_json(self.datafile["dialog_set"])
        
    def load_dialog_set(self):
        self.dialog_dict = self.get_dialog_set()

    def get_questions_log(self):
        return self.read_json(self.datafile["log"])

    def load_questions_log(self):
        self.questions_log = self.get_questions_log()

    def get_all_questions(self):
        all_questions = []
        for i in self.dialog_dict:
            all_questions += self.dialog_dict[i]['question']
        return all_questions
    
    def find_closest_question(self, msg: str):
        all_questions = self.get_all_questions()
        matches: list = get_close_matches(msg, all_questions, n=1, cutoff=0.7)
        return matches[0] if matches else ""
    
    def find_question_group(self, question: str):
        for i in self.dialog_dict:
            if question in self.dialog_dict[i]['question']:
                return i
        return ""


    def difflib_string(self, questions, msg: str = ""):
        matches: list = get_close_matches(msg, questions, n=1, cutoff=0.7)
        return True if matches else False
    
    # find matching group from string and return group name
    def find_matching_group(self, msg: str):
        finding_group = self.dialog_dict.copy()
        finding_group.pop("")
        for i in finding_group:
            if self.difflib_string(finding_group[i]['question'], msg): # string in finding_group[i]['question']:
                self.save_questions_log("match")
                return i
        self.save_questions_log("mismatch")
        return ""

    def save_questions_log(self, dialog_type, dialog_string):
        dialog_key = self.questions_log.get(dialog_type, {})
        if dialog_string in dialog_key:
            dialog_key[dialog_string] += 1
        else:
            dialog_key[dialog_string] = 1
        self.questions_log[dialog_type] = dialog_key

        json.dump(self.questions_log, open(self.datafile["log"], "w"), indent=2)

    # return list of answers from group
    def get_answers(self, from_group: str = ""):
        if from_group not in list(self.dialog_dict.keys()): raise Exception("err")
        if from_group == "": return self.dialog_dict[from_group]
        return self.dialog_dict[from_group]['answer']
    
    # return a random answer from group
    def get_answer(self, from_group: str = ""):
        return random.choice(self.get_answers(from_group))