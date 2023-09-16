from django.urls import path
from . import views
urlpatterns=[
             path('k/',views.run),
             path('l/',views.verma),
             path('my/',views.myfun ,name="myfun"),
             path('',views.read,name="home"),
             path('delt/<int:id>',views.delt,name="delt"),
             path('edit/<int:id>',views.edit,name="edit"),
            ]