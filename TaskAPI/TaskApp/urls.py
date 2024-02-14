from django.urls import re_path,path
from TaskApp import views

urlpatterns=[
    #path('tables/',views.tableApi)
    # path('tables/<int:SubjectA>/<int:SubjectB>/total',views.tableApi),
    re_path(r'^tables/(?P<SubjectA>\d+)/(?P<SubjectB>\d+)',views.tableApi)
    
] 


