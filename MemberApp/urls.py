from django.conf.urls import url
from MemberApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^department/$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    url(r'^member$', views.memberApi),
    url(r'^member/([0-9]+)$', views.memberApi),

    url(r'^member/SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)