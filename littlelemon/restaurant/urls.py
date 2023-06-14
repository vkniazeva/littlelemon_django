#define URL route for index() view
from django.urls import path, include
from . import views
from  rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name = 'restaurant_menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),   
]

