"""timem URL Configuration

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
from django.conf.urls import url,include
from django.conf.urls.static import static
from teacher.views import home, ctti,dti,dti_dept,view_time,add_resources,update_resources,register_dept,register_subject,register_teacher,register_class,register_lab,register_sec,register_sem
from timem import settings
from teacher import views as tview
from rest_framework.urlpatterns import format_suffix_patterns
from timet.views import tfapi,mfapi,lfapi,rfapi,teacherapi,deptapi,secapi,semapi,crapi,lbapi
urlpatterns = [
    url(r'^(?P<id>[0-99]{1,2})/$',tview.master_tt, name='master_tt'),
    # url(r'^(?P<string>[\w\-]+)/$',tview.teacher_tt, name='teacher_tt'),
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^about/$',tview.about, name='about'),
    url(r'^tfapi$', tfapi.as_view(), name='tfapi'),
    url(r'^mfapi$', mfapi.as_view(), name='mfapi'),
    url(r'^lfapi$', lfapi.as_view(), name='lfapi'),
    url(r'^rfapi$', rfapi.as_view(), name='rfapi'),
    url(r'^teacherapi$', teacherapi.as_view(), name='teacherapi'),
    url(r'^deptapi$', deptapi.as_view(), name='deptapi'),
    url(r'^secapi$', secapi.as_view(), name='secapi'),
    url(r'^semapi$', semapi.as_view(), name='semapi'),
    url(r'^crapi$', crapi.as_view(), name='crapi'),
    url(r'^lbapi$', lbapi.as_view(), name='lbapi'),
    url(r'^generate/$', tview.generate, name='generate'),
    url(r'^ctti/$', ctti, name='ctti'),
    url(r'^timet1/$', tview.timet1, name='timet1'),
    url(r'^department/(?P<id>[0-99]{1,2})/$', dti_dept, name='dti'),
    url(r'^dti/$', dti, name='dti'),
    url(r'^view_time/$', view_time, name='view_time'),
    url(r'^add_department/$', register_dept, name='add_department'),
    url(r'^add_subject/$', register_subject, name='add_subject'),
    url(r'^click_here/$', tview.click_here, name='click_here'),
    url(r'^add_teacher/$', register_teacher, name='add_teacher'),
    url(r'^add_sem/$', register_sem, name='add_sem'),
    url(r'^add_sec/$', register_sec, name='add_sec'),
    url(r'^add_class/$', register_class, name='add_class'),
    url(r'^add_lab/$', register_lab, name='add_lab'),
    url(r'^add_resources/$', add_resources, name='add_resources'),
    url(r'^dti/(?P<string>[\w\-]+)/$', add_resources, name='add_resources'),
    url(r'^update_resources/$', update_resources, name='update_resources'),
    url(r'^view_resources/(?P<id>[0-99]{1,2})/$', tview.view_resources, name='view_resources'),
    path('admin/', admin.site.urls),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
