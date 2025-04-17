from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('py',views.py,name='py'),
    path('jsp',views.jsp,name='jsp'),
    path('pytst',views.pytst,name='pytst'),
    path('jtst',views.jtst,name='jtst'),
    path('bank',views.bank,name='bank'),
    path('sindet/<int:pk>',views.single_details,name='details'),
    path('edit/<int:fk>',views.update,name='edit'),
    path('create',views.create,name='create'),
    path('api',views.api),
]