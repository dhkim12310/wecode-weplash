from django.views     import View
from django.http      import JsonResponse
from django.db.models import Prefetch
from django.db.models   import Q

from .models        import (
    HashTag,
    Photo,
    BackGroundColor
)
from account.models import (
    User,
    Collection,
    Like
)

class RelatedPhotoView(View):
    PHOTO_LIMIT = 20

    def get(self, request, photo_id):
        try:
            if Photo.objects.filter(id=photo_id).exists():
                related_tags = list(HashTag.objects.filter(photo__id = photo_id).values_list('name', flat=True))
                photos = Photo.objects.filter(hashtag__name__in = related_tags).exclude(id=photo_id).prefetch_related("user").distinct()
                result = [{
                    "id"                 : photo.id,
                    "image"              : photo.image,
                    "location"           : photo.location,
                    "user_first_name"    : photo.user.first_name,
                    "user_last_name"     : photo.user.last_name,
                    "user_name"          : photo.user.user_name,
                    "user_profile_image" : photo.user.profile_image
                } for photo in photos[:self.PHOTO_LIMIT]]

                return JsonResponse({"tags" : related_tags, "data" : result}, status=200)
            return JsonResponse({"message" : "NON_EXISTING_PHOTO"}, status=401)
        except ValueError:
            return JsonResponse({"message" : "INVALID_PHOTO"}, status=400)

class RelatedCollectionView(View):
    LIMIT_NUM = 3

    def get(self, request, photo_id):
        try:
            if Photo.objects.filter(id=photo_id).exists():
                collections = Collection.objects.filter(
                    photocollection__photo__id = photo_id
                ).exclude(user=User.objects.get(user_name='weplash')).prefetch_related(
                    Prefetch("photo_set"),
                    Prefetch("photo_set__hashtag")
                )

                result = [{
                    "id"              : collection.id,
                    "image"           : [photo.image for photo in collection.photo_set.all()[:self.LIMIT_NUM]],
                    "name"            : collection.name,
                    "photos_number"   : collection.photo_set.all().count(),
                    "user_first_name" : collection.user.first_name,
                    "user_last_name"  : collection.user.last_name,
                    'tags'            : [tag.name for tag in collection.photo_set.filter().first().hashtag.all()[:self.LIMIT_NUM]]
                } for collection in collections]

                return JsonResponse({'data' : result}, status=200)
            return JsonResponse({"message" : "NON_EXISTING_PHOTO"}, status=401)
        except ValueError:
            return JsonResponse({"message" : "INVALID_PHOTO"}, status=400)


class PhotoView(View):
    def get(self,request):   
        try:
            query = Q()
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 20))
            category = request.GET.get('category',None)
            user = request.GET.get('user',None)
            user_category = request.GET.get('user_category',None)
            if category:
                query.add(Q(collection = Collection.objects.get(
                    user = User.objects.get(user_name='weplash'),
                    name = category
                )),query.AND)
            elif user:
                if user_category == 'photos':
                    query.add(Q(user = User.objects.get(
                        user_name = user
                    )),query.AND)
                elif user_category == 'likes':
                    query.add(Q(like__user = User.objects.get(
                        user_name = user
                    )),query.AND)
                else:
                    query.add(Q(collection__user = User.objects.get(
                        user_name = user
                    ), collection__name = user_category),query.AND)

            photos = Photo.objects.filter(query).prefetch_related("user")
            data = [{
                "id" : photo.id,
                "image" : photo.image,
                "location" : photo.location,
                "user_first_name" : photo.user.first_name,
                "user_last_name" : photo.user.last_name,
                "user_profile_image" : photo.user.profile_image,
                "user_name" : photo.user.user_name,
                "width" : photo.width,
                "height" : photo.height
            } for photo in photos[offset*limit:(offset+1)*limit]]
            
            return JsonResponse({"data":data},status=200)
        
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)

class PhotoView2(View):
    def get(self,request):   
        try:
            query = Q()
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 20))
            category = request.GET.get('category',None)
            user = request.GET.get('user',None)
            hashtag = request.GET.get('hashtag',None)
            user_category = request.GET.get('user_category',None)
            
            if category:
                query.add(Q(collection = Collection.objects.get(
                    user = User.objects.get(user_name='weplash'),
                    name = category
                )),query.AND)
            elif user:
                if user_category == 'photos':
                    query.add(Q(user = User.objects.get(
                        user_name = user
                    )),query.AND)
                elif user_category == 'likes':
                    query.add(Q(like__user = User.objects.get(
                        user_name = user
                    )),query.AND)
                else:
                    query.add(Q(collection__user = User.objects.get(
                        user_name = user
                    ), collection__name = user_category),query.AND)

            elif hashtag:
                query.add(Q(hashtag = HashTag.objects.get(
                    name = hashtag
                )),query.AND)

            photos = Photo.objects.filter(query).prefetch_related("user","hashtag")

            data = [{
                "id" : photo.id,
                "image" : photo.image,
                "location" : photo.location,
                "user_first_name" : photo.user.first_name,
                "user_last_name" : photo.user.last_name,
                "user_profile_image" : photo.user.profile_image,
                "user_name" : photo.user.user_name,
                "width" : photo.width,
                "height" : photo.height,
            } for photo in photos[offset*limit:(offset+1)*limit]]
            
            return JsonResponse({"data":data},status=200)
        
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"},status=400)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)

class BackgraundView(View):
    def get(self,request, collection_name):
        try:
            photos = Photo.objects.filter(
                collection = Collection.objects.get(name=collection_name)
                ).prefetch_related("user","background_color")
            data = [{
                "id" : photo.id,
                "background_color" : photo.background_color.name,
                "width" : photo.width,
                "height" : photo.height
            }for photo in photos]
            return JsonResponse({"data":data},status=200)

        except ValueError:
                return JsonResponse({"message":"VALUE_ERROR"},status=400)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)
            
