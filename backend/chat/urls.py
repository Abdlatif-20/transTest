from django.urls import path
from .views import ConversationViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls