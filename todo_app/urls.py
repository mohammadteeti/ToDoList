

from django.urls import path,include
from todo_app.views import ListListView,ItemListView,ListCreate ,ItemUpdate,ItemCreate,ItemDelete
urlpatterns = [
path("",ListListView.as_view(),name="index"),  
path("list/<int:list_id>",ItemListView.as_view(),name="list")  ,
# path("item/<int:pk>",ItemDetail.as_view(),name="item-detail"),
path("list/add/",ListCreate.as_view(),name="list-add"),
path("list/<int:list_id>/item/add",ItemCreate.as_view(),name="item-add"),
path("list/<int:list_id>/item/<int:pk>",ItemUpdate.as_view(),name="item-update"),
path("list/<int:list_id>/item/delete/<int:pk>",ItemDelete,name="item-delete")
]