#项目架构
lang_notebook/
├── manage.py                     #Django管理脚本
├── lang_notebook/                # 项目配置目录
│   ├── __init__.py
│   ├── settings.py               # 配置文件，建议拆分 dev/prod
│   ├── urls.py                   # 全局路由
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── users/                    # 用户系统（注册、登录、权限等）
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│
│   ├── notebooks/                # 笔记本 & 子本 & 任务页
│   │   ├── models/               # 模型子目录，分拆结构
│   │   │   ├── notebook.py
│   │   │   ├── sub_notebook.py
│   │   │   ├── note_leaf.py
│   │   │   └── note.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│
│   ├── configs/                  # note_config 配置模型
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│
│   ├── tasks/                    # AI任务调度
│   │   ├── models.py             # task表
│   │   ├── celery_tasks.py       # celery任务定义（调用模型、embedding等）
│   │   ├── views.py
│   │   └── urls.py
│
│   └── ai_service/               # 外部嵌入式模型调用（Flask服务或 LLM API）
│       ├── client.py             # 调用 embedding / 去重 / 模型微服务
│       └── utils.py
│
├── requirements.txt
├── Dockerfile
├── celery.py                     # Celery 启动器
└── .env                          # 环境变量配置
