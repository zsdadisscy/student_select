# 人机交互作业，学生导师双选系统

## 数据库

## 开发日志

### 5.24

完善了数据库，删除无用键，删除了权限，删除了无用键，但是密码是明文待完善
数据库实现了汉化，优化数据库结构，不支持创建管理员，

### 5.29

继续完善了数据库，但是密码明文问题还是未解决，只是在admin后台创建是明文，用户自己修改可以加密，不再修复该问题

### 6.2

实现学生登录api /student/login/

### 6.4

基本实现所有api， 返回值字段都可见字知意，如不懂可[查看](./app/models.py)<br>
所有用户初始密码均为123456

1. ```/get_status/```检查用户登陆状态
   ```get```
   返回值 {
   'result': '未登录'/'tutor'/'student'
   }
   [代码实现](./app/views/__init__.py)
2. 学生api[代码实现](./app/views/student.py)

   1. ```/student/login/学生登录```

   ```post
   data {
   'id':
   'password'
   }
   返回值 {
   'result': 'success' / 错误信息
   }
   ```
   2. ```/student/logout/登出```

   ```get
    返回值{'result': 'success'}
   ```
   3. ```/student/modify_password/修改密码```

   ```
   post  登陆后可调用
   data{
    old_password:
    new_password:
    confirm_password:
   }
   返回值 {
    'result': 'success'/错误信息
   }
   ```
   4. ```/student/get_info/ 获得个人信息```

   ```
    get 登陆后可调用
   返回值 {
    'result': 'success' / 错误信息
        'date': {
            'username':
            'date_of_birth': 
            'bio': 
            'email': 
            'photo': 
            'phone': 
            'college': 
            'id': 
            'gender': 
            'student_type': 
            'tutor':
            'select_limit': 
            'select_count': 
        }
   }
   ```
   5. ```/student/modify_info/ 修改信息```

   ```
   POST 登陆后可调用
   data {
   photo
    date_of_birth
    bio 
    email 
    phone
   }
   返回值 {
   'result': 'success' / 错误信息
   }
   ```
   6. ```/student/get_tutor/ 获得自己学院，学硕/专硕，取决于自己的类型所有的导师```

   ```
     get 登陆后可调用
   返回值{
       'result': 'success' / 错误信息,
       'data': {
           'username': 
           'id': 
           'photo': 
           'date_of_birth': 
           'college': 
           'gender': 
           'research_area': 
       }
   }
   ```
   7. ```/student/get_tutor_info/ 查询具体老师的信息```

   ```
   POST
   data={
   tutor_id
   }
   返回值{
       'result': 'success',/错误信息
       'date': {
           'username': 
           'date_of_birth': 
           'bio': 
           'email': 
           'photo': 
           'phone': 
           'college': 
           'id': 
           'gender': 
           'research_area': 
           'is_recruiting_specialized': 
           'is_recruiting_learning': 
           'enrollment_limit': 
           'enrollment_count': 
       }
   }
   ```
   8. ```/student/select_tutor/ 选择导师```

   ```
    POST 登陆后可调用
   data={
   tutor_id
   }
   返回值 {
    'result': 'success'/ 错误信息
   }
   ```
   9. ```/student/deselect_tutor/ 取消选择导师```

   ```
   POST 登陆后可调用
   data {
   tutor_id
   }
   返回值 {
   'result': 'success' / 错误信息
   }
   ```
   10. ```/student/get_select_tutor/ 查看目前选择的导师```

   ```
   GET 登陆后可调用
   返回值 {
   'result' : 'success' / 错误信息,
   data : {
               'student_id': 
               'student_name': 
               'tutor_id': 
               'tutor_name': 
               'status': 
           }
   }
   ```
   11. ```/student/get_select_tutor_record/ 查看自己的选择记录```

   ```
    GET 登陆后可调用
   返回值 {
   'result':'success' / 错误信息
   data: {
                'student_id': 
                'student_name': 
                'tutor_id': 
                'tutor_name': 
                'type': 
                'time': 
            }
   }
   ```
   12. ```/student/get_my_tutor/ 查看自己的导师```

   ```
   GET 登陆后可调用
   返回值  {
   'result':'success' / 错误信息
   data: {
               'tutor_name': 
               'tutor_id': 
           }
   }
   ```
3. 导师api[代码实现](./app/views/tutor.py)

   1. ```/tutor/login/导师登录```

   ```post
   data {
   'id':
   'password'
   }
   返回值 {
   'result': 'success' / 错误信息
   }
   ```
   2. ```/tutor/logout/登出```

   ```get
    返回值{'result': 'success'}
   ```
   3. ```/tutor/modify_password/修改密码```

   ```
   post  登陆后可调用
   data{
    old_password:
    new_password:
    confirm_password:
   }
   返回值 {
    'result': 'success'/错误信息
   }
   ```
   4. ```/tutor/get_info/ 获得个人信息```

   ```
    get 登陆后可调用
   返回值 {
    'result': 'success' / 错误信息
        'date': {
            'username': 
            'date_of_birth': 
            'bio': 
            'email': 
            'photo': 
            'phone': 
            'college': 
            'id': 
            'gender': 
            'research_area': 
            'is_recruiting_specialized':
            'is_recruiting_learning': 
            'enrollment_limit': 
            'enrollment_count': 
        }
   }
   ```
   5. ```/tutor/modify_info/ 修改信息```

   ```
   POST 登陆后可调用
   data {
   research_area
   photo
    date_of_birth
    bio 
    email 
    phone
   }
   返回值 {
   'result': 'success' / 错误信息
   }
   ```
   6. ```/tutor/get_student_info/ 查看某个学生的具体信息```

   ```
     POST 
   data {
   student_id
   }
   返回值{
       'result': 'success' / 错误信息,
       'data': {
           'username': 
           'date_of_birth': 
           'bio': 
           'email': 
           'photo': 
           'phone': 
           'college': 
           'id': 
           'gender': 
           'student_type': 
       }
   }
   ```
   7. ```/tutor/get_select_student/ 查看选择自己的学生```

   ```
   GET
   返回值{
       'result': 'success',/错误信息
       'date': {
               'student_id':
               'student_name': 
               'status': 
           }
   }
   ```
   8. ```/tutor/processing_application/ 处理学生申请```

   ```
    POST 登陆后可调用
   data={
   student_id,
   processing: "通过"/"拒绝"
   }
   返回值 {
    'result': 'success'/ 错误信息
   }
   ```
   9. ```/tutor/get_my_student/ 查看自己的学生```

   ```
   GET 登陆后可调用
   返回值 {
   'result': 'success' / 错误信息
   data{
               'id': student.id,
               'username': student.username,
               'type': student.student_type
           }
   ```
