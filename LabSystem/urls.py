"""LabSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from login import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页及登录
    url(r'^index/$', views.index),
    url(r'^index2/$', views.index2),
    #科研模块
    url(r'^keyan/$', views.keyan),
    url(r'^keyan_participate/$', views.keyan_participate),
    url(r'^keyan_add_task/$', views.keyan_add_task),
    url(r'^keyan_ratify/$', views.keyan_ratify),
    url(r'^keyan_if_ratify_ajax/$', views.keyan_if_ratify_ajax),
    url(r'^keyan_except/$', views.keyan_except),
    url(r'^detail_info/$', views.detail_info),
    url(r'^modify_ajax/$', views.modify_ajax),
    url(r'^task_modify/$', views.task_modify),
    url(r'^add_task_member/$', views.add_task_member),
    #成果模块
    url(r'^achievement/$', views.achievement),
    url(r'^add_achievement/$', views.add_achievement),
    url(r'^journal_article_ajax/$', views.journal_article_ajax),
    url(r'^patent_ajax/$', views.patent_ajax),
    url(r'^conference_article_ajax/$', views.conference_article_ajax),
    url(r'^academic_monograph_ajax/$', views.academic_monograph_ajax),
    url(r'^software_patent_ajax/$', views.software_patent_ajax),
    #绩效模块
    url(r'^performance/$', views.performance),
    url(r'^performance_ajax/$', views.performance_ajax),
    #信息模块
    url(r'^information/$', views.information),
    url(r'^info_team/$', views.info_team),
    url(r'^info_add_user/$', views.info_add_user),
    url(r'^add_group_member/$', views.add_group_member),
    url(r'^change_password_ajax/$', views.change_password_ajax),
    url(r'^change_password/$', views.change_password),
    #经费模块
    url(r'^budget/$', views.budget),
    url(r'^budget_out/$', views.budget_out),
    url(r'^detail_budget_ajax/$', views.detail_budget_ajax),
    #资产模块
    url(r'^property/$', views.property),
    url(r'^if_ratify/$', views.if_ratify),
    url(r'^pro_purchase/$', views.pro_purchase),
    url(r'^property_all/$', views.property_all),
    url(r'^property_baofei/$', views.property_baofei),
    url(r'^scrap_ajax/$', views.scrap_ajax),
    #表单验证
    url(r'^check_id/$', views.check_id_ajax),
    url(r'^check_new_id/$', views.check_new_id_ajax),

    #登出
    url(r'^logout/$', views.logout),
    #测试
    url(r'^test/$', views.test),
    # url(r'^add_tec/$', views.add_tec),
    # url(r'^add_stu/$', views.add_stu),
    # url(r'^add_task/$', views.add_task),
    # url(r'^teacher_task/$', views.teacher_task),
    # url(r'^stu_task/$', views.stu_task),
    # url(r'^send_message/$', views.send_message),
    # url(r'^show_message1/$', views.show_message1),
    # url(r'^show_message2/$', views.show_message2),
    # url(r'^home0/$', views.home0),
    # url(r'^home1/$', views.home1),
    # url(r'^home2/$', views.home2),
    # url(r'^info0/$', views.info0),
    # url(r'^info1/$', views.info1),
    # url(r'^info2/$', views.info2),
]
