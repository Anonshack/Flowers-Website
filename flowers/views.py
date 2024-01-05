# from django.shortcuts import render
# from .models import Flowers
# from .serializers import FlowersBaseCrudSerializers
# from rest_framework import generics, status
# from rest_framework.response import Response
# # Create your views here.
#
#
# class FlowersViewAPI(generics.ListAPIView):
#     serializer_class = FlowersBaseCrudSerializers
#     queryset = Flowers.objects.all()
#
#     def post(self, request):
#         if request.method == 'GET':
#             serializers = FlowersBaseCrudSerializers(data=request.data)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response(serializers.data, status=status.HTTP_201_CREATED)

from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from flowers.renderers import UserRenderers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.http import JsonResponse
from flowers.pagination import *
from .serializers import *
from flowers.models import *
from .serializers import UserSignInSerializers


# def get_token_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'accsess': str(refresh.access_token)
#     }


# class UserSiginInViews(APIView):
#     render_classes = [UserRenderers]
#
#     def post(self, request, format=None):
#         serializers = UserSignInSerializers(data=request.data, partial=True)
#         if serializers.is_valid(raise_exception=True):
#             username = request.data['username']
#             password = request.data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 tokens = get_token_for_user(user)
#                 return Response({'token': tokens, 'message': 'Welcome to the system'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': {'none_filed_error': ['This user is not available to the system']}}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfilesViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriyaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        objects_list = Categoriya.objects.all()
        serializer = CategoriyaAllSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = CategoriyaCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img=request.data.get('img'))
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriyaBaseCrudViews(APIView):
    parser_class = [MultiPartParser, FormParser]
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = Categoriya.objects.filter(id=pk)
        serializers = CategoriyaAllSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = CategoriyaCrudSerializers(instance=Categoriya.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = Categoriya.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class SubCategoriyaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagi_class = LargeResultsSetPagination

    def get(self, request, format=None):
        objects_list = SubCategoriya.objects.all()
        serializer = SubCategoriyaAllSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = SubCategoriyaCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategoriyaBaseCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = SubCategoriya.objects.filter(id=pk)
        serializers = SubCategoriyaCrudSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = SubCategoriyaCrudSerializers(instance=SubCategoriya.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = SubCategoriya.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class CategoriyaDeteile(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = SubCategoriya.objects.filter(id_categoriya__id=pk)
        serializers = SubCategoriyaCrudSerializers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class FlowersBaseAllViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = FlowersBaseAllSerializers
    render_classes = [UserRenderers]
    parser_class = (MultiPartParser, FormParser)
    perrmisson_class = [IsAuthenticated]

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None):
        instance = Flowers.objects.all().order_by('-pk')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = FlowersBaseCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowersAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        instance = Flowers.objects.all().order_by('-pk')
        serializer = FlowersBaseAllSerializers(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlowersBaseCrudViews(APIView):
    parser_class = [MultiPartParser, FormParser]
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = Flowers.objects.filter(pk=pk)
        seriz = FlowersBaseAllSerializers(objects_list, many=True)
        return Response({'flowers': seriz.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = FlowersBaseCrudSerializers(instance=Flowers.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = Flowers.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class FlowersImagesPostViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = FlowersImages.objects.filter(id_flowers__id=pk).order_by('-pk')
        print(objects_list)
        serializer = FlowersImagesAllSer(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = FlowersImagesCrudSerializers(instance=FlowersImages.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = FlowersImages.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class FlowersVideoCommitBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = FlowersCommentVideoBaseSerializers

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None):
        objects_list = FlowersCommentVideos.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = FlowersCommentVideoCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowersVideoCommitCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = FlowersCommentVideos.objects.filter(id=pk).order_by('-pk')
        serializer = FlowersCommentVideoBaseSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = FlowersCommentVideoCrudSerializers(instance=FlowersCommentVideos.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = FlowersCommentVideos.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class FlowersDeliveryBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = FlowersDeliveryBaseSerializers

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None):
        objects_list = FlowersDelivery.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = FlowersDeliveryCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowersDeliveryCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = FlowersDelivery.objects.filter(id=pk).order_by('-pk')
        serializer = FlowersDeliveryBaseSerializers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        objects_get = FlowersDelivery.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class BlogsBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = BlogAllBaseSerialiezers

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None):
        objects_list = Blogs.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializers = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializers = self.serializer_class(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = BlogCrudBaseSerialiezers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(img=request.data.get('img'))
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogsBaseCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = Blogs.objects.filter(id=pk)
        serializer = BlogAllBaseSerialiezers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        blog = Blogs.objects.filter(id=pk)[0]
        serializers = BlogCrudBaseSerialiezers(instance=blog, data=request.data, context={'img': blog.img}, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        objects_get = Blogs.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)


class SeoCategoryAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        objects_list = SeoCategory.objects.all()
        serializer = SeoCategoryAllSerialiezers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SeoContentBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        objects_list = SeoContent.objects.all()
        serializer = SeoContentAllSerialiezers(objects_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = SeoContentCrudSerialiezers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SeoContentCrudViews(APIView):
    parser_class = [MultiPartParser, FormParser]
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = SeoContent.objects.filter(id=pk)
        serializers = SeoContentAllSerialiezers(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializers = SeoContentCrudSerialiezers(instance=SeoContent.objects.filter(id=pk)[0], data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response({'error': 'update error data'}, status=status.HTTP_400_BAD_REQUEST)


class FormaGetBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    serializer_class = FormasAllSerizalisers

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None):
        instance = FormaSayts.objects.all().order_by('-pk')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FormaDteileBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, pk, format=None):
        objects_list = SeoContent.objects.filter(id=pk)
        serializers = FormaSayts(objects_list, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        objects_get = FormaSayts.objects.get(id=pk)
        objects_get.delete()
        return Response({'message': "Delete success"}, status=status.HTTP_200_OK)
