# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:04
# @name: scy
# @FileName: tutor.py
# @Software: PyCharm
import hashlib

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from app.views import get_cache, update_cache
from app.models import *


# 登录
@require_http_methods(["POST"])
def tutor_login(request):
    data = request.POST
    id = data.get('id')
    password = data.get('password')
    if not id:
        return JsonResponse({
            'result': '工号不能为空'
        })
    if not password:
        return JsonResponse({
            'result': '密码不能为空'
        })
    try:
        user = Tutor.objects.get(id=id)
        if not check_password(password, user.password):
            return JsonResponse({
                'result': '密码不正确'
            })
        # 创建哈希对象
        hash_object = hashlib.sha256(id.encode())

        # 获取哈希值（加密后的结果）
        encrypted_id = hash_object.hexdigest()
        request.session['user'] = encrypted_id
        # 保存一天
        cache.set(encrypted_id, (id, 'tutor'), timeout=3600 * 24)
        return JsonResponse({
            'result': 'success'
        })
    except Tutor.DoesNotExist:
        return JsonResponse({
            'result': '用户不存在',
        })


# 登出
@require_http_methods(["GET"])
def tutor_logout(request):
    flag, user = get_cache(request)
    if flag:
        del request.session['user']
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
    user = Tutor.objects.filter(id=cache.get(user)[0])[0]
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
    user = Tutor.objects.filter(id=cache.get(user_cache)[0])[0]
    update_cache(request)
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


# 修改信息
@require_http_methods(['POST'])
def modify_info(request):
    flag, user_cache = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    user = Tutor.objects.filter(id=cache.get(user_cache)[0])[0]
    photo = request.FILES.get('photo')
    data = request.POST
    date_of_birth = data.get('date_of_birth')
    bio = data.get('bio')
    email = data.get('email')
    phone = data.get('phone')
    research_area = data.get('research_area')
    if research_area:
        user.research_area = research_area
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


# 查看学生的信息
@require_http_methods(['POST'])
def get_student_info(request):
    data = request.POST
    student_id = data.get('student_id')
    user = Student.objects.filter(id=student_id)
    if not user:
        return JsonResponse({
            'result': '学生信息不存在'
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
            'student_type': user.student_type,
        }
    })


# 查看选择自己的学生
@require_http_methods(['GET'])
def get_select_student(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    try:
        user = Tutor.objects.get(id=cache.get(user)[0])
        select = StudentTutor.objects.filter(tutor=user)
        resp = []
        for sel in select:
            resp.append({
                'student_id': sel.student.id,
                'student_name': sel.student.username,
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


# 处理学生申请
@require_http_methods(['POST'])
def processing_application(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    student_id = request.POST.get('student_id')
    processing = request.POST.get('processing')
    try:
        student = Student.objects.get(id=student_id)
        tutor = Tutor.objects.get(id=cache.get(user)[0])
        select = StudentTutor.objects.get(student=student, tutor=tutor)
        if processing == '通过':
            if student.selected_tutor:
                return JsonResponse({
                    'result': '学生已有导师'
                })
            if tutor.enrollment_limit >= tutor.enrollment_count:
                return JsonResponse({
                    'result': '学生已达到上线'
                })
            select.relationship_status = 'accepted'
            student.selected_tutor = tutor
            tutor.enrollment_limit = int(tutor.enrollment_limit) + 1
            tutor.save()
            student.save()
            StudentLog.objects.create(student=student, tutor=tutor, operation_type='approve')
        elif processing == '拒绝':
            select.relationship_status = 'rejected'
            StudentLog.objects.create(student=student, tutor=tutor, operation_type='reject')
        select.save()
        return JsonResponse({
            'result': 'success'
        })
    except Student.DoesNotExist:
        return JsonResponse({
            'result': '学生不存在'
        })
    except Tutor.DoesNotExist:
        return JsonResponse({
            'result': '导师不存在'
        })
    except Student.DoesNotExist:
        return JsonResponse({
            'result': '学生还未选择你'
        })


# 查看自己的学生
@require_http_methods(['GET'])
def get_my_student(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '用户未登录'
        })
    update_cache(request)
    try:
        user = Tutor.objects.get(id=cache.get(user)[0])
        students = user.tutor_student.all()
        resp = []
        for student in students:
            resp.append({
                'id': student.id,
                'username': student.username,
                'type': student.student_type
            })
        return JsonResponse({
            'result': 'success',
            'data': resp
        })
    except Tutor.DoesNotExist:
        return JsonResponse({
            'result': "用户不存在",
        })
