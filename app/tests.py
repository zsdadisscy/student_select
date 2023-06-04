from app.models import *
import random

colleges = ['计算机学院', '工学院', '传媒学院', '美术学院', '音乐学院']
type = ['专硕', '学硕']
ids = 2019416000
for i in range(200):
    flag = random.randint(0, 3)
    if flag == 0:
        Tutor.objects.create_user(id = ids, date_of_birth='2022-05-06', username=i, password='123456', college=colleges[random.randint(0, 4)], is_recruiting_specialized=True)
    elif flag == 1:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)], is_recruiting_specialized=True, is_recruiting_learning=True)
    elif flag == 2:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)])
    else:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)],
                                  is_recruiting_learning=True)
    ids += 1