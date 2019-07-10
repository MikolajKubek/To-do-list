from django.urls import path
from .views import home_view, delete_todo, switch_state, login_view, logout_view

app_name = 'todos'
urlpatterns = [
    path('', home_view, name="home_view"),
    path('<int:id>/delete/', delete_todo, name="delete"),
    path('<int:id>/switch/', switch_state, name="switch"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

]
