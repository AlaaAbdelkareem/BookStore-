"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from store.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name='home'),
    path('accounts/profile/', views.index,name='home'),

    # path('test/<int:param>', views.index),
    path('admin/', admin.site.urls),
    path('signup', views.signup,name='signup'),
    path('login', auth_views.login, {'template_name': 'login.html'},name='login'),
    path('logout', auth_views.logout, {'next_page': 'login'},name='logout'),


    # Books
    path('book/', views.allBooks, name='books'),
    # path('search/<book_name>', views.search),
    path('book/<int:book_id>', views.getBook, name='book'),

    # # Author // with his books
    path('author/<int:author_id>', views.author),

    # # Author // with his books
    # path('category/', views.allCategories),
    # path('category/<int:id>', views.getCategory),

    # Categories
    path('category/<int:cat_id>', views.getCategoryBooks),

    #Sreach
    path('search',views.search),   
    #path('edit', views.edit_profile, name='edit'),
    path('updateUser', views.edit, name='updateUser'),
    path('updateUserPassword',views.changePassword,name='changePasswordUser')





]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
