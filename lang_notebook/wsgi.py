# WSGI（Web Server Gateway Interface）是 Python Web 应用和 Web 服务器之间的通信协议。
# 它定义了一个标准的接口，让 Web 服务器（如 Gunicorn, uWSGI, Apache 等）能够与 Python Web 应用（如 Django）交互。
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lang_notebook.settings')

#这是在 wsgi.py 文件中定义的 WSGI 应用对象。
# Django 在启动时会加载这个 application 变量，它是一个可调用的 WSGI 应用对象，负责处理传入的 HTTP 请求。
application = get_wsgi_application()

