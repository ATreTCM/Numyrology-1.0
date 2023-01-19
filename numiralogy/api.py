from rest_framework import routers
from answers import api_views as apies

router = routers.DefaultRouter()
router.register(r'social_predictions', apies.Social_predictionsViewset)
router.register(r'spiritual_predictions', apies.Spiritual_predictionsViewset)
router.register(r'personal_predictions', apies.Personal_predictionsViewset)
router.register(r'comments', apies.CommentsViewset)
router.register(r'services', apies.ServicesViewset)
router.register(r'users', apies.UsetViewset)
