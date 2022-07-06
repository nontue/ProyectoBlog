from django.urls import path
from Blog import views
from Blog.views import PostCreate, PostDelete, PostDetail, PostList, PostUpdate

urlpatterns = [
    path('post/list', views.inicio, name='Inicio'),
    path('post', views.post, name='Post'),
    path('categoria', views.categoria, name='Categoria'),
    path('padre', views.padre, name='Padre'),
    path('postFormulario', views.postFormulario, name='PostFormulario'),
    path('busquedaCategoria', views.busquedaCategoria, name='BusquedaCategoria'),
    path('buscar', views.buscar, name='Buscar'),
    path('about', views.about, name='AboutMe'),
    #----------
    path('post/list/', PostList.as_view(), name= 'post_list'),
    path('post/<pk>', PostDetail.as_view(), name= 'post_detail'),
    path('post/new/', PostCreate.as_view(), name= 'post_create'),
    path('post/edit/<pk>', PostUpdate.as_view(), name= 'post_update'),
    path('post/delete/<pk>', PostDelete.as_view(), name= 'post_delete'),
    
]