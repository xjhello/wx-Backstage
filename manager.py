# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server
import www

# web server，自定义命令，runserver自定义server命令，里面是参数，可以取代app.run()
manager.add_command("runserver",
                    Server(host='0.0.0.0', port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))


def main():
    manager.run()  # 使用自定义启动方法，启动为manager.py runserver


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback  # 打印所有错误信息

        traceback.print_exc()
