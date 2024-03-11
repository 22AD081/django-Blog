from django.urls import path
from .views import homes_views, login_views, chosen_views, template1_views, temp1_views, read_views, exam1_views
urlpatterns=[path('', homes_views, name='homes'),
             path('login/', login_views, name='login'),
             path('chosen/', chosen_views, name='chosen'),
             path('chosen/template1', template1_views, name='template1'),
             path('template1/temp1', temp1_views, name='temp1'),
             path('chosen/read', read_views, name='read'),
             path('chosen/exam1', exam1_views, name='exam1'),]