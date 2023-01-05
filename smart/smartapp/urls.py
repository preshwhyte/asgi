from django.urls import path
from . import views


urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('events/',views.events, name='events'),
    path('projects/',views.projects, name='projects'),
    path('contacts/', views.contact, name='contact'),
    path('addmember/', views.addmember, name='addmember'),
    path('membertext/', views.member_text, name='membertext'),
    path('membercsv/', views.member_csv, name='membercsv' ),
    path('drug-abuse/', views.drug, name='drug'),
    path('advocacies/',views.advocacy,name='advocacy'),
    path('post-covid palliatives/',views.pall,name='pall'),
    path('Rsu-anti-drug-abuse/' ,views.ust, name='ust'),
    path('World-environment-Day/' ,views.environ, name='environ'),
    path('other-activities/', views.others, name='others'),
    path('search/', views.search, name='search'),
    path('members/<showid>', views.sershow, name='show'),
    path('article/',views.article, name='article'),
    path('login/', views.signin, name='login')

]
