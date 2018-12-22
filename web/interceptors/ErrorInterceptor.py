# -*- coding: utf-8 -*-
"""
错误拦截器
"""
from application import app
from common.libs.Helper import ops_render
from common.libs.LogService import LogService


@app.errorhandler(404)  # 捕捉404
def error_404( e ):
    LogService.addErrorLog( str( e ) )  # 记录错误
    return ops_render( 'error/error.html',{ 'status':404,'msg':'很抱歉！您访问的页面不存在' } )