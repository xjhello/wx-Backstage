# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g
from common.libs.Helper import ops_render
# 创造蓝图对象
route_index = Blueprint('index_page', __name__)


@route_index.route("/")
def index():
    # current_user = g.current_user  # 在拦截器中获取的用户信息
    # current_user用户信息已经被封装到ops_render方法中了
    return ops_render('index/index.html')
    # return render_template('index/index.html',current_user=current_user)