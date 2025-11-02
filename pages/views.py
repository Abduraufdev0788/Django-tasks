from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


books1 = [
    {
        "id": 1,
        "name": "O‘tgan kunlar",
        "author": "Abdulla Qodiriy",
        "price": 45000,
        "img": "https://upload.wikimedia.org/wikipedia/uz/3/3b/Otgan_kunlar_kitobi.jpg",
        "description": "O‘zbek adabiyotining ilk romanlaridan biri. Asarda o‘tgan davr voqealari, muhabbat va fidoyilik haqida so‘z yuritiladi."
    },
    {
        "id": 2,
        "name": "Mehrobdan chayon",
        "author": "Abdulla Qodiriy",
        "price": 40000,
        "img": "https://kitobxon.com/img_knigi/2314.jpg",
        "description": "Asarda din va jamiyat o‘rtasidagi ziddiyatlar, insoniy qadriyatlar va adolat haqida so‘z yuritiladi."
    },
    {
        "id": 3,
        "name": "Kecha va kunduz",
        "author": "Cho‘lpon",
        "price": 38000,
        "img": "https://kitobxon.com/img_knigi/2067.jpg",
        "description": "Cho‘lponning eng mashhur asarlaridan biri. Inson ruhiyati, ijtimoiy tengsizlik va ozodlik g‘oyalariga bag‘ishlangan."
    },
    {
        "id": 4,
        "name": "Dunyoning ishlari",
        "author": "O‘tkir Hoshimov",
        "price": 42000,
        "img": "https://kitobxon.com/img_knigi/220.jpg",
        "description": "O‘tkir Hoshimovning hayotiy hikoyalari asosida yozilgan asar. Oddiy odamlarning ichki dunyosi va mehr-muhabbat haqida."
    },
    {
        "id": 5,
        "name": "Sarob",
        "author": "Cho‘lpon",
        "price": 37000,
        "img": "https://kitobxon.com/img_knigi/1673.jpg",
        "description": "Sevgi, orzu va adolat orqasidan quvgan insonlarning murakkab hayoti tasvirlangan asar."
    },
    {
        "id": 6,
        "name": "Ikki eshik orasi",
        "author": "O‘tkir Hoshimov",
        "price": 41000,
        "img": "https://kitobxon.com/img_knigi/2143.jpg",
        "description": "O‘zbekistonning o‘tgan asrdagi hayoti, inson or-nomusi va hayot sinovlari haqida chuqur falsafiy asar."
    },
    {
        "id": 7,
        "name": "Sariq devni minib",
        "author": "Xudoyberdi To‘xtaboyev",
        "price": 35000,
        "img": "https://kitobxon.com/img_knigi/57.jpg",
        "description": "Bolalar uchun yozilgan mashhur sarguzasht asar. Jasorat, do‘stlik va halollik haqida hikoya qiladi."
    },
    {
        "id": 8,
        "name": "Jimjitlik",
        "author": "Erkin A’zam",
        "price": 39000,
        "img": "https://kitobxon.com/img_knigi/3289.jpg",
        "description": "Insonning ichki dunyosi, yolg‘izlik va hayotdagi jimjitlikni falsafiy tarzda tasvirlaydigan asar."
    },
    {
        "id": 9,
        "name": "Bolalik",
        "author": "G‘afur G‘ulom",
        "price": 36000,
        "img": "https://kitobxon.com/img_knigi/158.jpg",
        "description": "Yozuvchining bolalik xotiralari asosida yozilgan asar. Mehr, sabr va bolalik orzulari haqida."
    },
    {
        "id": 10,
        "name": "Alkimyogar",
        "author": "Paulo Coelho",
        "price": 50000,
        "img": "https://kitobxon.com/img_knigi/147.jpg",
        "description": "Jahon miqyosida mashhur falsafiy roman. Inson orzularining qudrati va hayot yo‘lini topish haqida."
    },
]





def home(requests:HttpRequest):
  return render(request=requests, template_name='home.html')

def bosh_sahifa(requests:HttpRequest):
  return render(request=requests, template_name="index.html")

def books_view(requests:HttpRequest):
  context = {
    'books': books1,
  }
  return render(request=requests, template_name="books.html", context=context)

def register(requests:HttpRequest):
  return render(request=requests, template_name="register.html")

def aloqa(requests:HttpRequest):
  return render(request=requests, template_name="contact.html")

def books_detail(requests:HttpRequest, book_id:int):
  for book in books1:
    if book['id'] == book_id:
      return render(request=requests, template_name='book_detail.html', context={'book':book})