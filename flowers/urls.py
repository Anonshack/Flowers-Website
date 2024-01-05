from django.urls import path
from flowers.views import *

urlpatterns = [
    # path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/', UserProfilesViews.as_view()),
    path('categoriya_base_all_views/', CategoriyaBaseAllViews.as_view()),
    path('categoriya_base_crud_views/<int:pk>/', CategoriyaBaseCrudViews.as_view()),
    path('sub_categoriya_base_all_views/', SubCategoriyaBaseAllViews.as_view()),
    path('sub_categoriya_base_crud_views/<int:pk>/', SubCategoriyaBaseCrudViews.as_view()),
    path('categoriya_deteile/<int:pk>/', CategoriyaDeteile.as_view()),

    # flowers urls
    path('flowers_base_all_views/', FlowersBaseAllViews.as_view()),
    path('flowers_all_views/', FlowersAllViews.as_view()),
    path('flowers_base_crud_views/<int:pk>/', FlowersBaseCrudViews.as_view()),
    path('flowers_images_post_views/<int:pk>/', FlowersImagesPostViews.as_view()),

    # flowers video urls
    path('flowers_video_commit_base_all_views/', FlowersVideoCommitBaseAllViews.as_view()),
    path('flowers_video_commit_crud_views/<int:pk>/', FlowersVideoCommitCrudViews.as_view()),

    # flowers delivery urls
    path('flowers_delivery_base_all_views/', FlowersDeliveryBaseAllViews.as_view()),
    path('flowers_delivery_crud_views/<int:pk>/', FlowersDeliveryCrudViews.as_view()),

    # blogs urls
    path('blogs_base_all_views/', BlogsBaseAllViews.as_view()),
    path('blogs_base_crud_views/<int:pk>/', BlogsBaseCrudViews.as_view()),

    # SEO Urls
    path('seo_category_all_views/', SeoCategoryAllViews.as_view()),
    path('seo_content_base_all_views/', SeoContentBaseAllViews.as_view()),
    path('seo_content_crud_views/<int:pk>/', SeoContentCrudViews.as_view()),

    path('forma_get_base_all_views/', FormaGetBaseAllViews.as_view()),
    path('forma_deteile_base_all_views/<int:pk>/', FormaDteileBaseAllViews.as_view()),
]

