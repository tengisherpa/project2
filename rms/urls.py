from django.urls import path
from .views import CategoryAPIView,CategoryDetail

urlpatterns=[
#    class based:
path('category/',CategoryAPIView.as_view()),
path('category/<id>/',CategoryDetail.as_view())
   
#    Function Based:
    # path('category',category),
    # path('category/<id>/',category_detail),
    # path('table',table),

]