from django.contrib import admin
from django.urls import path
from money_management_app.views import index, income, expense
from django.urls import path, include
from money_management_app.views  import register
from money_management_app.views import user_logout


from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', login_required(index), name='index'),
    path('income/', login_required(income), name='income'),
    path('expense/', login_required(expense), name='expense'),
    path('', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
