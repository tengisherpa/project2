from django.urls import path
# from .views import CategoryAPIView,CategoryDetail
from .views import *
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('category',CategoryModelViewset,basename='category')
# router.register('category',CategoryDetailViewSet,basename='category-detail')
urlpatterns=[
    
    
    
# #    class based:
# path('category/',CategoryGenericAPIView.as_view()),
# path('category/<pk>/',CategoryDetail.as_view())
   
#    Function Based:
    # path('category',category),
    # path('category/<id>/',category_detail),
    # path('table',table),

] + router.urls