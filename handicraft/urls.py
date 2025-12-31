from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.static import serve
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, ProductSitemap, CategorySitemap


def healthcheck(request):
    return HttpResponse("OK")


def make_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin",
            "shivshaktistone0@gmail.com",
            "shivadmin123",
        )
        return HttpResponse("Superuser created.")
    return HttpResponse("Already exists.")

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
}

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("products/", include("products.urls")),
    path("contact/", include("contact.urls")),
    path("healthz/", healthcheck),
    # SECURITY RISK: 'make-superuser/' path should be deleted or protected in production.
    path("make-superuser/", make_superuser),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
]

# MEDIA files (admin se upload wali images)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
# ]

# STATIC files agar chaho (usually whitenoise handle kar raha hoga)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Shiv-Shakti-Stone"
admin.site.site_title = "Shiv-Shakti-Stone"
admin.site.index_title = "Shiv-Shakti-Stone"
