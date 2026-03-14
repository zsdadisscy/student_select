# Student-Tutor Selection System (学生导师双选系统)

[English](#english) | [中文](#中文)

<a name="english"></a>
## English

This is a Human-Computer Interaction (HCI) assignment project—a Student-Tutor Selection System developed using **Django** (Backend) and **Vue 3** (Frontend). The system facilitates a two-way selection process where students can view and select tutors, and tutors can review and approve applications. It also includes a backend management interface based on SimpleUI.

### 🛠 Tech Stack

#### Backend
- **Framework**: Python, Django 4.2.1
- **Admin Interface**: SimpleUI 4.0.2 (Django Admin theme)
- **Database**: SQLite (Default) / MySQL (Supported)
- **Dependency Management**: `requirements.txt`

#### Frontend
- **Framework**: Vue.js 3
- **UI Component Library**: Ant Design Vue
- **Routing/State Management**: Vue Router, Vuex
- **HTTP Client**: Axios
- **Dependency Management**: `package.json`

### ✨ Features

- **Role Management**: Supports three roles: Student, Tutor, and Administrator.
- **Student Side**:
  - Login/Logout/Change Password.
  - View personal information and modify specific profile details.
  - Browse tutor list (filter by department).
  - Apply for tutors, cancel applications, view application status, and history.
- **Tutor Side**:
  - Login/Logout/Change Password.
  - Maintain academic information and admission quotas.
  - View applicant list.
  - Audit student applications (Approve/Reject).
  - View enrolled students.
- **Admin Interface**:
  - Enhanced interface using SimpleUI.
  - Visual management of students, tutors, selection relationships, and operation logs.

### 📂 Directory Structure

```bash
.
├── app/                    # Backend application core logic
│   ├── models.py           # Database models (Student, Tutor, Selection, Log)
│   ├── views/              # API implementation
│   ├── urls/               # Route configuration
│   └── ...
├── student/                # Frontend Vue project directory
│   ├── src/                # Source code
│   ├── public/             # Static assets
│   ├── package.json        # Frontend dependencies
│   └── ...
├── student_select/         # Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main routing
│   └── ...
├── media/                  # User-uploaded files (avatars, etc.)
├── static/                 # Static files
├── db.sqlite3              # Default database file
├── manage.py               # Django management script
└── requirements.txt        # Backend dependencies list
```

### 🚀 Setup & Run

#### 1. Backend Configuration
Ensure Python 3.8+ is installed.

```bash
# 1. Enter project root
cd student_select_project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Database migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser (for admin access)
python manage.py createsuperuser

# 5. Start development server
python manage.py runserver 0.0.0.0:8000
```
- **Service URL**: `http://127.0.0.1:8000`
- **Admin Panel**: `http://127.0.0.1:8000/admin`

#### 2. Frontend Configuration
Ensure Node.js and npm are installed.

```bash
# 1. Enter frontend directory
cd student

# 2. Install dependencies
npm install

# 3. Start development server
npm run serve
```
- **Access URL**: Typically `http://localhost:8080`

#### 3. Production Build
To build the frontend for deployment:
```bash
npm run build
```
The built files will be in `student/dist`.

### ⚙️ Configuration

- **Database**: Defaults to SQLite. To use MySQL, modify the `DATABASES` section in `student_select/settings.py`.
- **API Endpoint**: The frontend calls the backend API using the server IP by default. For local development, update the API base URL in the frontend (usually in `src/main.js` or Axios config) to point to your local backend (e.g., `http://127.0.0.1:8000`).

### 📝 API Overview

The system uses a decoupled architecture. Key API paths:
- **Public**: `/get_status/` (Check login status)
- **Student Module** (`/student/...`): `login/`, `logout/`, `modify_password/`, `get_info/`, `modify_info/`, `get_tutor/`, `select_tutor/`, `deselect_tutor/`
- **Tutor Module** (`/tutor/...`): `login/`, `logout/`, `modify_password/`, `get_info/`, `modify_info/`, `processing_application/`, `get_my_student/`

### 📄 License
This project is an HCI course assignment, intended for learning and exchange only.

---

<a name="中文"></a>
## 中文

这是一个基于 **Django** (后端) 和 **Vue 3** (前端) 开发的人机交互作业项目——学生导师双选系统。该系统实现了学生查看导师信息并进行选择、导师查看申请并进行审核的双向选择流程，并包含一个基于 SimpleUI 的后台管理界面。

### 🛠 技术栈

#### 后端
- **框架**: Python, Django 4.2.1
- **管理后台**: SimpleUI 4.0.2 (美化 Django Admin)
- **数据库**: SQLite (默认) / MySQL (支持配置)
- **依赖管理**: `requirements.txt`

#### 前端
- **框架**: Vue.js 3
- **UI 组件库**: Ant Design Vue
- **路由/状态管理**: Vue Router, Vuex
- **HTTP 客户端**: Axios
- **依赖管理**: `package.json`

### ✨ 功能特性

- **角色管理**: 支持学生、导师和管理员三种角色。
- **学生端**:
  - 登录/登出/修改密码。
  - 查看个人信息及修改部分资料。
  - 浏览导师列表（支持按学院筛选）。
  - 申请导师、取消申请、查看申请状态及历史记录。
- **导师端**:
  - 登录/登出/修改密码。
  - 维护个人学术信息及招生名额。
  - 查看申请学生列表。
  - 审核学生申请（通过/拒绝）。
  - 查看已招收的学生。
- **后台管理**:
  - 使用 SimpleUI 美化的后台界面。
  - 可视化管理学生、导师、选课关系及操作日志数据。

### 📂 目录结构

```bash
.
├── app/                    # 后端应用核心逻辑
│   ├── models.py           # 数据库模型 (Student, Tutor, Selection, Log)
│   ├── views/              # API 接口实现
│   ├── urls/               # 路由配置
│   └── ...
├── student/                # 前端 Vue 项目目录
│   ├── src/                # 源代码
│   ├── public/             # 静态资源
│   ├── package.json        # 前端依赖配置
│   └── ...
├── student_select/         # Django 项目配置目录
│   ├── settings.py         # 项目配置文件
│   ├── urls.py             # 总路由
│   └── ...
├── media/                  # 用户上传文件存储 (头像等)
├── static/                 # 静态文件
├── db.sqlite3              # 默认数据库文件
├── manage.py               # Django 管理脚本
└── requirements.txt        # 后端依赖列表
```

### 🚀 环境搭建与运行

#### 1. 后端配置
确保您的环境已安装 Python 3.8+。

```bash
# 1. 进入项目根目录
cd student_select_project

# 2. 安装依赖
pip install -r requirements.txt

# 3. 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 4. 创建管理员账户 (用于登录后台)
python manage.py createsuperuser

# 5. 启动开发服务器
python manage.py runserver 0.0.0.0:8000
```
- **服务地址**: `http://127.0.0.1:8000`
- **后台管理**: `http://127.0.0.1:8000/admin`

#### 2. 前端配置
确保您的环境已安装 Node.js 和 npm。

```bash
# 1. 进入前端目录
cd student

# 2. 安装依赖
npm install

# 3. 启动开发服务
npm run serve
```
- **访问地址**: 通常为 `http://localhost:8080`

#### 3. 构建生产环境代码
如果需要部署前端：
```bash
npm run build
```
构建后的文件位于 `student/dist` 目录。

### ⚙️ 配置说明

- **修改后端数据库**: 默认使用 SQLite。如需使用 MySQL，请修改 `student_select/settings.py` 中的 `DATABASES` 配置段。
- **修改 API 地址**: 前端调用后端的 API 地址默认指向服务器IP。如果您在本地开发，请修改前端代码中的 API 请求基地址（通常在 `src/main.js` 或 Axios 配置文件中），将其指向本地后端地址（如 `http://127.0.0.1:8000`）。

### 📝 API 概览

系统采用前后端分离架构，主要 API 路径如下：
- **公共**: `/get_status/` (检查登录状态)
- **学生模块**: `login/`, `logout/`, `modify_password/`, `get_info/`, `modify_info/`, `get_tutor/`, `select_tutor/`, `deselect_tutor/`
- **导师模块**: `login/`, `logout/`, `modify_password/`, `get_info/`, `modify_info/`, `processing_application/`, `get_my_student/`

### 📄 License
本项目作为人机交互课程作业，仅供学习交流使用。
