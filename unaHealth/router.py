from base.views import GlucoseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('levels', GlucoseViewSet)