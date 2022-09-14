from django.urls import path
from .views import BookList, BookDetailView


urlpatterns = [
    path('', BookList.as_view()),
    path('<int:id>', BookDetailView.as_view()),
]