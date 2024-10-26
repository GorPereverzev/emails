import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
my_name = "Гордей"
friend_name = "Илья"
website ="https://dvmn.org/referrals/xupy2VM6ArUX4Vp5cFLRBDTAsKNfALwwo7K1Fjwn/"
email_from = 'Gorpereverzev@yandex.ru'
email_to = 'Gorpereverzev@yandex.ru'

message = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

message = message.replace("%website%", website)
message = message.replace("%friend_name%", friend_name)
message = message.replace("%my_name%", my_name)

letter = """From: {email_from}
To:  {email_to}
Subject: имейлы
Content-Type: text/plain; charset="UTF-8";

{message}
""".format(email_from=email_from, email_to=email_to, message=message)

encoding_letter = letter.encode('utf-8')

login = 'Gorpereverzev'
password = os.getenv('PASSWORD')
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, encoding_letter)
server.quit()
