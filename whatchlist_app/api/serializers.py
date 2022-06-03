from rest_framework import serializers
from whatchlist_app.models import *


''' ------------------------------------------ Watch list Serializer ----------------------------------------'''

class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watchlist
        fields = '__all__'

'''--------- Custom Field Class --------------'''
# class MyCustom(serializers.RelatedField):
#     def to_representation(self, value):
#         return f'{value.title}  ||  {value.created}'

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    ''' To only get name which is set on __str__ function of watchlist'''
    # watchlist = serializers.StringRelatedField(many=True)

    '''------To Get Hyperlinks of data--------  '''
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='detail'
    # )

    '''------------Custom Related Field---------------'''
    # watchlist = MyCustom(many=True,read_only=True)

    '''----To Get all data from watch list----'''
    watchlist = WatchListSerializer(many=True,read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


''' --------------------------------------serializers.ModelSerializer class--------------------------------- '''

# class MovieSerializer(serializers.ModelSerializer):

#     name_len = serializers.SerializerMethodField()   # extra field except model

#     class Meta:
#         model = Movie
#         fields = '__all__'

# #   To Add Additional field into serializer which is not in models
#     def get_name_len(self,obj):
#         return obj.name+ '  >> ' + 'rating'
    
# #   Field Level Validation  (validate_field)
#     def validate_name(self, value):
#         if len(value) <= 1:
#             raise serializers.ValidationError("Name lenght should be gt 1")
#         return value

# #   Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Des should be different...")
#         return data


''' --------------------------------------serializers.Serializer class---------------------------------  '''
#   Validators Functions
# def check_name(value):
#     if value == 'Jay':
#         raise ValidationError('Not Jay')
#     return value

# class MovieSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[check_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

# #   Field Level Validation  (validate_field)
#     def validate_name(self, value):
#         if len(value) <= 1:
#             raise serializers.ValidationError("Name lenght should be gt 1")
#         return value

# #   Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Des should be different...")
#         return data