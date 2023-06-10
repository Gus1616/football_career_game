from rest_framework import serializers



class MyDataSerializer(serializers.Serializer):
    data = serializers.SerializerMethodField()
    def get_data(self, obj):
        # Perform any necessary computation or transformation on the data here
        return obj
