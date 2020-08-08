from django.urls import path

from .views import (
    RelatedPhotoView,
    RelatedCollectionView,
    PhotoView,
    PhotoView2,
    BackgraundView
)

urlpatterns= [
    path('/related-photo/<photo_id>', RelatedPhotoView.as_view()),
    path('/related-collection/<photo_id>', RelatedCollectionView.as_view()),
    path('',PhotoView.as_view()),
    path('/back/<collection_name>',BackgraundView.as_view()),
    path('/search',PhotoView2.as_view())
]
