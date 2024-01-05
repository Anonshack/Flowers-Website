from rest_framework import serializers
from django.contrib.auth.models import User
from flowers.models import (
    FormaSayts,
    SeoContent,
    SeoCategory,
    Blogs,
    FlowersDelivery,
    SizeFlow,
    TypeDelivery,
    FlowersCommentVideos,
    FlowersImages,
    Flowers,
    SubCategoriya,
    Categoriya,
)


class UserSignInSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CategoriyaAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = '__all__'


class CategoriyaCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = ['id', 'title', 'img', 'status']

    def create(self, validated_data):
        return Categoriya.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class SubCategoriyaAllSerializers(serializers.ModelSerializer):
    id_categoriya = CategoriyaAllSerializers(read_only=True)

    class Meta:
        model = SubCategoriya
        fields = ['id', 'title', 'id_categoriya', 'status']


class SubCategoriyaCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategoriya
        fields = ['id', 'title', 'id_categoriya', 'status']

    def create(self, validated_data):
        return SubCategoriya.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FlowersImagesSer(serializers.ModelSerializer):
    class Meta:
        model = FlowersImages
        fields = '__all__'


class FlowersBaseAllSerializers(serializers.ModelSerializer):
    id_category = CategoriyaAllSerializers(read_only=True)
    id_sub_category = SubCategoriyaAllSerializers(read_only=True)
    flowers = FlowersImagesSer(many=True, read_only=True)

    class Meta:
        model = Flowers
        fields = ('id', 'name', 'cotent', 'rank', 'price', 'upa', 'con', 'like', 'iye', 'id_category', 'id_sub_category',
                  'create_date', 'flowers')


class FlowersBaseCrudSerializers(serializers.ModelSerializer):
    img = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = Flowers
        fields = ['id', 'name', 'cotent', 'rank', 'price', 'upa', 'con', 'like', 'iye', 'id_category',
                  'id_sub_category', 'img']

    def create(self, validated_data):
        img = validated_data.pop('img')
        flowers = Flowers.objects.create(**validated_data)
        for item in img:
            images = FlowersImages.objects.create(id_flowers=flowers, img=item)
            images.save()
        return flowers

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FlowersImagesAllSer(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True)

    class Meta:
        model = FlowersImages
        fields = ['id', 'id_flowers', 'img']


class FlowersImagesCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlowersImages
        fields = ['id', 'id_flowers', 'img']

    def create(self, validated_data):
        return FlowersImages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FlowersCommentVideoBaseSerializers(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True)

    class Meta:
        model = FlowersCommentVideos
        fields = ['id', 'id_flowers', 'comment', 'create_date']


class FlowersCommentVideoCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlowersCommentVideos
        fields = ['id', 'id_flowers', 'comment', 'create_date']

    def create(self, validated_data):
        return FlowersCommentVideos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TypeDeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeDelivery
        fields = '__all__'


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SizeFlow
        fields = '__all__'


class FlowersDeliveryBaseSerializers(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True, many=True)
    id_type_delivery = TypeDeliverySerializers(read_only=True)
    id_size = SizeSerializers(read_only=True)

    class Meta:
        model = FlowersDelivery
        fields = ['id', 'fowers', 'create_date']


class FlowersDeliveryCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlowersDelivery
        fields = ['id', 'fowers', 'create_date']

    def create(self, validated_data):
        return FlowersDelivery.objects.create(**validated_data)


class BlogAllBaseSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"


class BlogCrudBaseSerialiezers(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=False,
                                 required=False)

    class Meta:
        model = Blogs
        fields = "__all__"

    def create(self, validated_data):
        return Blogs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class SeoCategoryAllSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = SeoCategory
        fields = "__all__"


class SeoContentAllSerialiezers(serializers.ModelSerializer):
    id_seo = SeoCategoryAllSerialiezers(read_only=True)

    class Meta:
        model = SeoContent
        fields = "__all__"


class SeoContentCrudSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = SeoContent
        fields = ['id', 'title', 'content', 'id_seo']

    def create(self, validated_data):
        return SeoContent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class FormasAllSerizalisers(serializers.ModelSerializer):
    class Meta:
        model = FormaSayts
        fields = '__all__'


class FormaCreateSerizliers(serializers.ModelSerializer):
    class Meta:
        model = FormaSayts
        fields = '__all__'

    def create(self, validated_data):
        return FormaSayts.objects.create(**validated_data)
