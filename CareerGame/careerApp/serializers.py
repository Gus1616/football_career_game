from rest_framework import serializers



class MyDataSerializer(serializers.Serializer):
    # data = serializers.SerializerMethodField()
    # def get_data(self, obj):
    #     return obj
    data = serializers.DictField(child=serializers.ListField(child=serializers.CharField()))

