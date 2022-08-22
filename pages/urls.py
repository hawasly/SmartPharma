from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index , name='index'),
    path('activesubstance',views.active_substance,name='substance'),
    path('allcompany',views.companies,name='companies'),
    path('company/<companyid>',views.company,name='company'),
    path('addcompany',views.addcompany,name='addcompany'),
    path('company/<companyid>/edit',views.editcompany,name='editcompany'),
]

urlpatterns += staticfiles_urlpatterns()