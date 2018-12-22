# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):  # 重载flask对象，配置分步加载
    def __init__(self, import_name, template_folder=None, root_path=None):  # 重载初始化方法,重置template位置
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)  # 重构,改变template，static等默认值
        self.config.from_pyfile('config/base_setting.py')  # 加载配置
        # export ops_config=local（设置环境变量加载不同的配置文件）
        if "ops_config" in os.environ:  # 加载配置文件
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)  # 注册到app


db = SQLAlchemy()  # 初始化orm对象
app = Application(__name__, template_folder=os.getcwd()+"/web/templates/", root_path=os.getcwd())
manager = Manager(app)  # 将App进行包装

"""
函数模板：将方法注入到模板中
"""
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')