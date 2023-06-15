from app.models import *
import random

colleges = ['college_of_computer', 'engineering_college', 'school_of_media', 'academy_of_fine_arts', 'conservatory_of_music']
genders = ['man', 'women']
ids = 2019416000
for i in range(300):
    flag = random.randint(0, 3)
    if flag == 0:
        Tutor.objects.create_user(id = ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)], is_recruiting_specialized=True, gender=genders[random.randint(0, 1)])
    elif flag == 1:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)], is_recruiting_specialized=True, is_recruiting_learning=True, gender=genders[random.randint(0, 1)])
    elif flag == 2:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)], gender=genders[random.randint(0, 1)])
    else:
        Tutor.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
                                  college=colleges[random.randint(0, 4)],
                                  is_recruiting_learning=True, gender=genders[random.randint(0, 1)])
    ids += 1

# from app.models import *
# import random
#
# colleges = ['college_of_computer', 'engineering_college', 'school_of_media', 'academy_of_fine_arts', 'conservatory_of_music']
# type = ['special_master', 'learning_master']
# genders = ['man', 'women']
# ids = 2020416000
# for i in range(300):
#     Student.objects.create_user(id=ids, date_of_birth='2022-05-06', username=i, password='123456',
#                                   college=colleges[random.randint(0, 4)], student_type=type[random.randint(0, 1)], gender=genders[random.randint(0, 1)])
#     ids += 1
