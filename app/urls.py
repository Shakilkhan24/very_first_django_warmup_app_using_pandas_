from django.urls import path
from . import views

app_name = 'csvanalysis'

urlpatterns = [
    path('', views.index, name='index'),
    path('load_data/', views.load_data, name='load_data'),
    path('explore_data/', views.explore_data, name='explore_data'),
    path('explore_more/', views.explore_more,name='explore_more'),
    # path('select_filter/', views.select_filter, name='select_filter'),
    # path('manipulate_data/', views.manipulate_data, name='manipulate_data'),
    # path('analyze_data/', views.analyze_data, name='analyze_data'),
    # path('visualize_data/', views.visualize_data, name='visualize_data'),
]