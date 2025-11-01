from django.contrib import admin
from django.urls import path
from pages.views import home, bosh_sahifa, books, register, aloqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index/', bosh_sahifa, name="bosh_sahifa" ),
    path("kitoblar/", books, name="kitoblar"),
    path("register/", register, name="register"),
    path("aloqa/", aloqa, name="aloqa"),

]
