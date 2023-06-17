# 人机交互作业，学生导师双选系统
项目地址8.130.65.99:8002
------------------
## 环境配置
1. 后端
   1. 配置解释器，安装需要的包
      终端在项目根目录下即 onlineExam下
      执行<br>
      `python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
   2. 生成数据库mysql
      `python manage.py makemigrations`
      `python manage.py migrate`
   3. 创建管理员用户
      `python manage.py createsuperuser`
   4. 运行程序
      `python manage.py runserver 0.0.0.0:8000`<br>
      浏览器中输入127.0.0.1:8000<br>
      127.0.0.1:8000/admin 为管理员界面
2. 前端
   在student目录下执行```npm install```

## 项目说明
后端django

前段vue3，使用了ant-design-vue

采用的前端路由的方式，前后端分离开发

项目依赖请查看requirements.txt   package-lock.json

前端所使用的api全部在服务器，如果需要更改为自己的，请将8.130.65.99:8002换为自己的地址，
### 文件说明
1. app 
   1. templates html文件
   2. urls 路由
   3. views api实现
   4. models 数据库模型
2. media 图片
3. static 静态文件 如js css
4. student_select 项目根目录 
5. student 前端文件
   1. dist打包好的前段文件
   2. src 前端代码
      1. assets 前端所需的图片等
      2. components 组件
      3. router 路由
      4. store vuex
      5. view 页面
      

## 数据库
使用的默认sqlite3， 如需更改请更换student_select/settings.py 95行处文件

选择模型在app/models.py中，只需查看后台中的4个表，其他不予理会


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
            'is_selected':
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
### 6.8
完成了登陆界面，修改了部分api，后端部分更改了验证方式，凡是需要登录才能访问的api，均需向api传递一个参数user，user存在store中，

### 6.13
出现bug，学生009，请求用户信息服务器出错，无法加载可选老师

现修复一些bug， 关闭了debug模式
### 6.14
修复导师页面查看自己的学生，学院为英文bug
### 6.17
修复修改老师信息后，老师学院不对，学生无法查看自己学院的老师
修复老师界面通过学生的界面学生头像不会改变