import json
from difflib import *
import os

#def read_json(file_location: str):
    return json.load(open(file_location,"r",encoding = 'utf-8'))
    
def find_da_string(str) -> str | None:
    matches: list = get_close_matches(user_input, ['ไปเกษตรศาสตร์', 'puppy','ael','e','a'], n=1, cutoff=0.6)
    return matches if matches else None

#print(read_json("Dialog_Set.json"))
#
while True:
    user_input: str = input('You: ')
    if user_input == '=ext': 
        break
    result = find_da_string(user_input)
    if result == None:
        print("ยังไม่เข้าใจคำถามครับ")
    elif result != None:
        print(result)
