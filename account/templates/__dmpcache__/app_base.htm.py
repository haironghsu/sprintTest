# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551245311.799178
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/account/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['menu']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!-- ')
        __M_writer(' -->\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n    App base stuff\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/account/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "37": 1, "38": 2, "43": 5, "49": 3, "55": 3, "61": 55}}
__M_END_METADATA
"""
