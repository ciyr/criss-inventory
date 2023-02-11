from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='homePage'),
    path('searchById',views.searchById,name='searchById'),
    path('searchByName',views.searchByName,name='searchByName'),
    path('login',views.login,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('add',views.add,name='add'),
    path('addQuantity',views.addQuantity,name='addQuantity'),
    path('issueQuantity',views.issueQuantity,name='issueQuantity'),
    path('viewTransactions',views.viewTransactions,name='viewTransactions'),
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)