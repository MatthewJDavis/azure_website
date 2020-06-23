from django.urls import include, path
from . views import GetPublishers, GetOffers, GetSkus, GetVersions, GetImage

app_name = 'display_images'

urlpatterns = [
    path('', GetPublishers.as_view(
        template_name='publishers.html'), name='publishers'),
    path('offers/<str:publisher>', GetOffers.as_view(
        template_name='offers.html'), name='offers'),
    path('skus/<str:publisher>/<str:offer>', GetSkus.as_view(
        template_name='skus.html'), name='skus'
    ),
    path('versions/<str:publisher>/<str:offer>/<str:sku>', GetVersions.as_view(
        template_name='versions.html'), name='versions'
    ),
    path('image/<str:publisher>/<str:offer>/<str:sku>/<str:version>', GetImage.as_view(
        template_name='image.html'), name='image'
    )
]
