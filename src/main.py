from services import service
from difflib import *

service = service()

print("สวัสดีครับ ยินดีต้อนรับสู่ kuverse\nผมคือ AI สุดชาญฉลาด พร้อมตอบคำถามของคุณ")
while True:
    user_input = input('You: ')
    if user_input == '0': 
        break
    print(service.get_answer(service.find_matching_group(user_input)))