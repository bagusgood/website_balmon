
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "Login - Balmon Kelas II Mataram"
admin.site.site_title = "Balmon Kelas II Mataram"
admin.site.index_title = "Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path('blog/', include("blog.urls")),
    path('profiles/', include("profiles.urls")),
    path("regulasi/", include("regulasi.urls")),
    path("pelayanan/", include("pelayanan.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
