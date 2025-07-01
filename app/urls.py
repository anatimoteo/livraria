from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from django.contrib import admin
from django.urls import include, path

from core.views.livro import LivroViewSet
from core.views import (
    AutorViewSet,
    CategoriaViewSet,
    CompraViewSet,
    EditoraViewSet,
    LivroViewSet,
    UserViewSet,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'users', UserViewSet, basename='users')
router.register(r'editoras', EditoraViewSet, basename='editoras')
router.register(r'livros', LivroViewSet, basename='livros')
router.register(r'autores', AutorViewSet, basename='autores')
router.register(r'compras', CompraViewSet, basename='compras')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/media/', include(uploader_router.urls)),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
