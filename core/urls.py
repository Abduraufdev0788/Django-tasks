from django.contrib import admin
from django.urls import path
from pages.views import home, bosh_sahifa, books_view, register, aloqa, books_detail

app_name = "book"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('index/', bosh_sahifa, name="bosh_sahifa" ),
    path("kitoblar/", books_view, name="kitoblar"),
    path("register/", register, name="register"),
    path("aloqa/", aloqa, name="aloqa"),
    path('kitoblar/<int:book_id>', books_detail, name="kitob_malumotlari" )
]
