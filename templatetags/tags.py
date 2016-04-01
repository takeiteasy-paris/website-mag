from django import template
from mag.models import *

register = template.Library()

# Réseaux sociaux
@register.inclusion_tag('mag/social_networks.html')
def show_social_networks():
	social_networks = SocialNetworkLink.objects.all().order_by('id')
	return {'social_networks': social_networks}