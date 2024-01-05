from django.contrib import admin
from flowers.models import (
    Categoriya,
    SubCategoriya,
    Flowers,
    FlowersImages,
    FlowersCommentVideos,
    TypeDelivery,
    SizeFlow,
    FlowersDelivery,
    Blogs,
    SeoCategory,
    SeoContent,
    FormaSayts,
)

models = [
    Categoriya,
    SubCategoriya,
    Flowers,
    FlowersImages,
    FlowersCommentVideos,
    TypeDelivery,
    SizeFlow,
    FlowersDelivery,
    Blogs,
    SeoCategory,
    SeoContent,
    FormaSayts]
for i in models:
    admin.site.register(i)
