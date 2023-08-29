from rest_framework  import serializers
from .models import Post
class PostSerializers(serializers.ModelSerializer):
    #post_author = serializers.ReadOnlyField(source="author.username")

    class Meta:
     fields=('id','author','title','body','created_at')
     model=Post