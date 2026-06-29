from django.urls import path

from api.views import get_external_post, ExternalPostView, ExternalPostCommentsView

urlpatterns = [
    path('posts/<int:post_id>/', get_external_post, name='get-post'),
    path('posts/cbv/<int:post_id>/', ExternalPostView.as_view(), name='get-post-cbv'),
    path('posts/cbv/<int:post_id>/comments/', ExternalPostCommentsView.as_view(), name='get-post-comments-cbv')

]