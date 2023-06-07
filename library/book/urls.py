from django.urls import path
from book import views
app_name='book'
urlpatterns =[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('add',views.add,name='add'),
    path('addbook',views.add1,name='addbooks'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('veiw/',views.veiwbook,name='veiw'),
    path('student',views.veiw,name='veiwstudent'),
    path('factorial', views.factorial, name='factorial'),
    path('calculator', views.calculator, name='calculator'),
    path('veiwbook/<int:p>',views.veiw_book,name="veiwbook"),
    path('deletebook/<int:p>',views.delete_book,name="deletebook"),
    path('updatebook/<int:p>',views.update_book,name="updatebook"),
    path('search/',views.search,name="search"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),


]