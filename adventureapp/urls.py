from django.urls import path
from . import views

app_name = "adventureapp"

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('rightpath/',views.rigthpath,name='rightpath'),
    path('leftpath/',views.leftpath,name='leftpath'),
    path('blue/',views.blue,name='blue'),
    path('green/',views.green,name='green'),
    path('safe/',views.safe,name='safe'),
    path('open/',views.open,name='open'),
    path('close/',views.close,name='close'),
    path('forest/',views.forest,name='forest'),
    path('park/',views.park,name='park'),
    path('safeopen/',views.safeopen,name='safeopen'),
    path('safepark/',views.safepark,name='safepark'),
    path('bad/',views.bad,name='bad'),
    path('line/',views.line,name='line'),
    path('go/',views.go,name='go'),
    path('going/',views.going,name='going'),
    path('neck/',views.neck,name='neck'),
    path('back/',views.back,name='back'),
    path('love/',views.love,name='love'),
    path('win/',views.win,name='win')
]