# 学生导师双选系统 (Student-Tutor Selection System)

这是一个基于 **Django** (后端) 和 **Vue 3** (前端) 开发的人机交互作业项目——学生导师双选系统。该系统实现了学生查看导师信息并进行选择、导师查看申请并进行审核的双向选择流程，并包含一个基于 SimpleUI 的后台管理界面。

## 🛠 技术栈 (Tech Stack)

### 后端 (Backend)

- **框架**: Python, Django 4.2.1
- **管理后台**: SimpleUI 4.0.2 (美化 Django Admin)
- **数据库**: SQLite (默认) / MySQL (支持配置)
- **依赖管理**: `requirements.txt`

### 前端 (Frontend)

- **框架**: Vue.js 3
- **UI 组件库**: Ant Design Vue
- **路由/状态管理**: Vue Router, Vuex
- **HTTP 客户端**: Axios
- **依赖管理**: `package.json`

## ✨ 功能特性 (Features)

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

## 📂 目录结构 (Directory Structure)

Bash

```
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

## 🚀 环境搭建与运行 (Setup & Run)

### 1. 后端配置 (Backend)

确保您的环境已安装 Python 3.8+。

Bash

```
# 1. 进入项目根目录
cd student_select_project  # 假设这是您的根目录名称

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

### 2. 前端配置 (Frontend)

确保您的环境已安装 Node.js 和 npm。

Bash

```
# 1. 进入前端目录
cd student

# 2. 安装依赖
npm install

# 3. 启动开发服务
npm run serve
```

- **访问地址**: 通常为 `http://localhost:8080` (具体请看控制台输出)

### 3. 构建生产环境代码

如果需要部署前端：

Bash

```
npm run build
```

构建后的文件位于 `student/dist` 目录。

## ⚙️ 配置说明 (Configuration)

### 修改后端数据库

默认使用 SQLite。如需使用 MySQL，请修改 `student_select/settings.py` 中的 `DATABASES` 配置段，并确保已安装 MySQL 驱动。

### 修改 API 地址

前端调用后端的 API 地址默认指向服务器IP。如果您在本地开发，请确保修改前端代码中的 API 请求基地址（通常在 `src/main.js` 或 Axios 配置文件中），将其指向本地后端地址（如 `http://127.0.0.1:8000`）。

## 📝 API 概览 (API Overview)

系统采用前后端分离架构，主要 API 路径如下：

- **公共**: `/get_status/` (检查登录状态)
- **学生模块** (`/student/...`):
  - `login/`, `logout/`, `modify_password/`
  - `get_info/`, `modify_info/`
  - `get_tutor/` (获取导师列表), `select_tutor/` (选择), `deselect_tutor/` (取消)
- **导师模块** (`/tutor/...`):
  - `login/`, `logout/`, `modify_password/`
  - `get_info/`, `modify_info/`
  - `processing_application/` (处理申请), `get_my_student/` (查看学生)

详细 API 参数及返回值请参考代码中的 `views` 目录。

## 📄 License

本项目作为人机交互课程作业，仅供学习交流使用。
