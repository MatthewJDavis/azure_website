from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_publishers, get_offers, get_skus, get_versions, get_image

class GetPublishers(TemplateView):
    template_name = 'publishers.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'publisher_list': get_publishers()
        }
        return context

class GetOffers(TemplateView):
    template_name = 'offers.html'

    def get_context_data(self, publisher):
        context = {
            'offer_dictionary': get_offers(publisher)
        }
        return context

class GetSkus(TemplateView):
    template_name = 'skus.html'

    def get_context_data(self, publisher, offer):
        context = {
            'sku_dictionary': get_skus(publisher, offer)
        }
        return context

class GetVersions(TemplateView):
    template_name = 'versions.html'

    def get_context_data(self, publisher, offer, sku):
        context = {
            'version_dictionary': get_versions(publisher, offer, sku)
        }
        return context

class GetImage(TemplateView):
    template_name = 'image.html'

    def get_context_data(self, publisher, offer, sku, version):
        context = {
            'image_dictionary': get_image(publisher, offer, sku, version)
        }
        return context
