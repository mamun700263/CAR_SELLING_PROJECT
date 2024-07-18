
from django.urls import path
#i have there in view DetailCarViwe,
from .views import *
urlpatterns = [
    path('detailview/<int:pk>/',DetailCarView.as_view(),name='detailview'),
    # path('buycar/<int:pk>/',buycar,name='buycar'),
]
