from services import service

service = service()

print("สวัสดีครับ ยินดีต้อนรับสู่ kuverse\nผมคือ AI สุดชาญฉลาด พร้อมตอบคำถามของคุณ")
while True:
    user_input = input('You: ')
    if user_input == '0': 
        break
    print(service.get_answer(service.find_question_group(service.find_closest_question(user_input))))