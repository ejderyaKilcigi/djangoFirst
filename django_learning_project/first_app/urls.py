from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:num1>/", view=views.switch_num, name="switch"),
    path("<str:item>/", view=views.course, name="course"),
    path("<int:num1>/<int:num2>/", view=views.multiply_view, name="multiply"),
    

]