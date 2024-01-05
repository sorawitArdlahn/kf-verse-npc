import json
import secrets
from difflib import get_close_matches


class service:
    datafile = {
        "dialog_set": "./resource/dialog_set.json",
        "log": "./resource/log.json",
    }
    dialog_dict = {}
    questions_log = {}

    def __init__(self):
        self.load_dialog_set()
        self.load_questions_log()

    def read_json(self, file_location: str):
        return json.load(open(file_location, "r", encoding="utf-8"))

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
        finding_group = self.dialog_dict.copy()
        finding_group.pop("")
        for i in finding_group:
            all_questions += finding_group[i]["question"]
        return all_questions

    def find_closest_question(self, msg: str):
        all_questions = self.get_all_questions()
        matches: list = get_close_matches(msg, all_questions, n=1, cutoff=0.7)
        self.save_questions_log("match", msg) if matches else self.save_questions_log("mismatch", msg)
        return matches[0]  if matches else ""

    def find_question_group(self, question: str):
        finding_group = self.dialog_dict.copy()
        finding_group.pop("")
        for i in finding_group:
            if question in finding_group[i]["question"]:
                return i
        return ""

    def save_questions_log(self, dialog_type, question):
        dialog_key = self.questions_log.get(dialog_type, {})
        if question in dialog_key:
            dialog_key[question] += 1
        else:
            dialog_key[question] = 1
        self.questions_log[dialog_type] = dialog_key

        with open(self.datafile["log"], "w", encoding="utf-8") as file:
            json.dump(self.questions_log, file, indent=4, ensure_ascii=False)

    # return list of answers from group
    def get_answers(self, from_group: str = ""):
        if from_group not in list(self.dialog_dict.keys()):
            raise ValueError("Invalid group")
        if from_group == "":
            return self.dialog_dict[from_group]
        return self.dialog_dict[from_group]["answer"]

    # return a random answer from group
    def get_answer(self, from_group: str = ""):
        return secrets.choice(self.get_answers(from_group))
