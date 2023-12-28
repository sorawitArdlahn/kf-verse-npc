from services import service
from difflib import *

service = service()

dialog_dict = service.get_dialog_set()

print(dialog_dict)

while True:
    user_input = input('You: ')
    if user_input == '0': 
        break
    print(service.get_answer(service.find_matching_group(user_input)))