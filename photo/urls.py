from django.urls import path
from .views      import (
    RelatedPhotoView,
    RelatedCollectionView,
    PhotoView,
    UploadView,
    BackgraundView,
    CollectionMainView,
    FollowsView
)

urlpatterns= [
    path('/related-photo/<photo_id>', RelatedPhotoView.as_view()),
    path('/related-collection/<photo_id>', RelatedCollectionView.as_view()),
    path('',PhotoView.as_view()),
    path('/back/<collection_name>',BackgraundView.as_view()),
    path('/upload', UploadView.as_view()),
    path('/collection-main', CollectionMainView.as_view()),
    path('/f',FollowsView.as_view())
]
