# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:04
# @name: scy
# @FileName: student.py
# @Software: PyCharm
import hashlib

from django.contrib.auth.hashers import check_password
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from app.models import *
from app.views import get_cache, update_cache


# 登录
@require_http_methods(["POST"])
def student_login(request):
    data = request.POST
    id = data.get('id')
    password = data.get('password')
    if not id:
        return JsonResponse({
            'result': '学号不能为空'
        })
    if not password:
        return JsonResponse({
            'result': '密码不能为空'
        })
    try:
        user = Student.objects.get(id=id)
        if not check_password(password, user.password):
            return JsonResponse({
                'result': '密码不正确'
            })
        # 创建哈希对象
        hash_object = hashlib.sha256(id.encode())
        # 获取哈希值（加密后的结果）
        encrypted_id = hash_object.hexdigest()
        # 保存一天
        cache.set(encrypted_id, (id, 'student'), timeout=3600 * 24)
        return JsonResponse({
            'result': 'success',
            'user': encrypted_id,
        })
    except Student.DoesNotExist:
        return JsonResponse({
            'result': '用户不存在',
        })


# 登出
@require_http_methods(["GET"])
def student_logout(request):
    flag, user = get_cache(request)
    if flag:
        cache.delete(user)
        return JsonResponse({
            'result': 'success',
        })
    return JsonResponse({
        'result': 'success',
    })


# 修改密码
@require_http_methods(["POST"])
def modify_password(request):
    data = request.POST
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            "result": '用户未登录，不允许操作',
        })
    if not old_password:
        return JsonResponse({
            'result': '原密码不能为空',
        })
    if not new_password and not confirm_password:
        return JsonResponse({
            'result': '新密码不能为空',
        })
    if new_password != confirm_password:
        return JsonResponse({
            'result': '两次密码不相同或密码不能为初始密码',
        })
    user = Student.objects.filter(id=cache.get(user)[0])[0]
    if not check_password(old_password, user.password):
        return JsonResponse({
            'result': '原始密码不正确',
        })
    user.password = make_password(new_password)
    user.save()
    update_cache(request)
    return JsonResponse({
        'result': 'success'
    })


# 得到自己的信息
@require_http_methods(['GET'])
def get_info(request):
    flag, user_cache = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    user = Student.objects.filter(id=cache.get(user_cache)[0])[0]
    update_cache(request)
    if user.selected_tutor:
        my_tutor = user.selected_tutor.id
    else:
        my_tutor = None
    return JsonResponse({
        'result': 'success',
        'date': {
            'username': user.username,
            'date_of_birth': user.date_of_birth,
            'bio': user.bio,
            'email': user.email,
            'photo': user.photo.url,
            'phone': user.phone,
            'college': user.college,
            'id': user.id,
            'gender': user.gender,
            'is_selected': user.is_selected,
            'student_type': user.student_type,
            'tutor': my_tutor,
            'select_limit': user.select_limit,
            'select_count': user.select_count
        }
    })


# 修改自己信息
@require_http_methods(['POST'])
def modify_info(request):
    flag, user_cache = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    user = Student.objects.filter(id=cache.get(user_cache)[0])[0]
    photo = request.FILES.get('photo')
    data = request.POST
    date_of_birth = data.get('date_of_birth')
    bio = data.get('bio')
    email = data.get('email')
    phone = data.get('phone')
    if date_of_birth:
        user.date_of_birth = date_of_birth
    if photo:
        user.photo = photo
    if email:
        user.email = email
    if phone:
        user.phone = phone
    if bio:
        user.bio = bio
    user.save()
    update_cache(request)
    return JsonResponse({
        'result': 'success',
    })


# 查询导师
@require_http_methods(['GET'])
def get_tutor(request):
    flag, user_cache = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    user = Student.objects.filter(id=cache.get(user_cache)[0])[0]
    type = user.student_type
    college = user.get_college_display()
    if type == 'special_master':
        tutors = Tutor.objects.filter(is_recruiting_specialized=True, college=college)
    else:
        tutors = Tutor.objects.filter(is_recruiting_learning=True,  college=college)
    resp = []
    for tutor in tutors:
        resp.append({
            'username': tutor.username,
            'id': tutor.id,
            'photo': tutor.photo.url,
            'date_of_birth': tutor.date_of_birth,
            'college': tutor.college,
            'gender': tutor.gender,
            'research_area': tutor.research_area
        })
    update_cache(request)
    return JsonResponse({
        'result': 'success',
        'data': resp
    })


# 查询具体老师的信息
@require_http_methods(['POST'])
def get_tutor_info(request):
    data = request.POST
    tutor_id = data.get('tutor_id')
    user = Tutor.objects.filter(id=tutor_id)
    if not user:
        return JsonResponse({
            'result': '老师信息不存在'
        })
    user = user[0]
    return JsonResponse({
        'result': 'success',
        'date': {
            'username': user.username,
            'date_of_birth': user.date_of_birth,
            'bio': user.bio,
            'email': user.email,
            'photo': user.photo.url,
            'phone': user.phone,
            'college': user.college,
            'id': user.id,
            'gender': user.gender,
            'research_area': user.research_area,
            'is_recruiting_specialized': user.is_recruiting_specialized,
            'is_recruiting_learning': user.is_recruiting_learning,
            'enrollment_limit': user.enrollment_limit,
            'enrollment_count': user.enrollment_count,
        }
    })


# 选择导师
@require_http_methods(['POST'])
def select_tutor(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    user = Student.objects.filter(id=cache.get(user)[0])[0]
    tutor_id = request.POST.get('tutor_id')
    update_cache(request)
    if user.select_count >= user.select_limit:
        return JsonResponse({
            'result': '选择的导师已到达上限',
        })
    if user.selected_tutor:
        return JsonResponse({
            'result': '已有导师不能继续选择'
        })
    try:
        tutor = Tutor.objects.get(id=tutor_id)
        is_select = StudentTutor.objects.filter(student=user, tutor=tutor)
        if is_select:
            return JsonResponse({
                'result': '已经选择过该导师'
            })
        StudentTutor.objects.create(student=user, tutor=tutor)
        StudentLog.objects.create(student=user, tutor=tutor, operation_type='choose')
        user.select_count = int(user.select_count) + 1
        user.save()

        return JsonResponse({
            'result': 'success',
        })
    except Tutor.DoesNotExist:
        return JsonResponse({
            'result': '选择的导师不存在'
        })


# 取消选择
@require_http_methods(['POST'])
def deselect_tutor(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    user = Student.objects.filter(id=cache.get(user)[0])[0]
    tutor_id = request.POST.get('tutor_id')
    update_cache(request)
    try:
        tutor = Tutor.objects.get(id=tutor_id)
        select = StudentTutor.objects.get(tutor=tutor, student=user)
        if select.relationship_status == 'approve':
            return JsonResponse({
                'result': '导师已经同意无法取消'
            })
        user.select_count = max(0, int(user.select_count) - 1)
        StudentLog.objects.create(student=user, tutor=tutor, operation_type='cancel')
        select.delete()
        user.save()

        return JsonResponse({
            'result': 'success',
        })
    except Tutor.DoesNotExist:
        return JsonResponse({
            'result': '导师不存在'
        })
    except StudentTutor.DoesNotExist:
        return JsonResponse({
            'result': '该记录不存在'
        })


# 目前选择的导师
@require_http_methods(['GET'])
def get_select_tutor(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    try:
        user = Student.objects.get(id=cache.get(user)[0])
        select = StudentTutor.objects.filter(student=user)
        resp = []
        for sel in select:
            resp.append({
                'student_id': sel.student.id,
                'student_name': sel.student.username,
                'tutor_id': sel.tutor.id,
                'tutor_name': sel.tutor.username,
                'status': sel.relationship_status
            })
        return JsonResponse({
            'result': 'success',
            'data': resp
        })
    except StudentTutor.DoesNotExist:
        return JsonResponse({
            'result': "用户不存在",
        })


# 自己的选择记录
@require_http_methods(['GET'])
def get_select_tutor_record(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    try:
        user = Student.objects.get(id=cache.get(user)[0])
        record = StudentLog.objects.filter(student=user)
        resp = []
        for rec in record:
            resp.append({
                'student_id': rec.student.id,
                'student_name': rec.student.username,
                'tutor_id': rec.tutor.id,
                'tutor_name': rec.tutor.username,
                'type': rec.operation_type,
                'time': rec.operation_time,
            })
        return JsonResponse({
            'result': 'success',
            'data': resp
        })
    except StudentTutor.DoesNotExist:
        return JsonResponse({
            'result': "用户不存在",
        })


# 查看自己的导师
@require_http_methods(['GET'])
def get_my_tutor(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    try:
        user = Student.objects.get(id=cache.get(user)[0])
        tutor = user.selected_tutor
        if not tutor:
            return JsonResponse({
                'result': '目前未被导师选择'
            })
        return JsonResponse({
            'result': 'success',
            'data': {
                'tutor_name': tutor.username,
                'tutor_id': tutor.id
            }
        })
    except Student.DoesNotExist:
        return JsonResponse({
            'result': "用户不存在",
        })
