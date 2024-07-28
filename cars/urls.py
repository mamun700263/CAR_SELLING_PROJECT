
from django.urls import path
#i have there in view DetailCarViwe,
from .views import *
urlpatterns = [
    #path to view car details and pk is car.id
    path('detailview/<int:pk>/',DetailCarView.as_view(),name='detailview'),
    # path('buycar/<int:car_id>',buycar,name='buycar'),
    path('comment/<int:car_id>',comment_form,name='comment'),
]
