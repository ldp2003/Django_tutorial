from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('endpoint1', views.endpoint1, name='endpoint1'),
    path('testing', views.testing, name='testing'),
    path('generic/', views.QuestionListView.as_view(), name='question_list'),
]