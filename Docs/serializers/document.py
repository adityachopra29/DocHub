from rest_framework import serializers
from Docs.models.document import Document
from Docs.serializers.user import UserSerializer
from rest_framework.authentication import SessionAuthentication

class DocumentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True) # basicaly tells that when serializing the doc instance, there is the owner field. If we do not write this, the doc serializer dont know how to serialize this, so just taked the id and shows. By this line, it sends this obj to the user serializer to serialize. See the ouput by removing this line.
    class Meta:
        model = Document
        fields = '__all__'
    
    def create(self, validated_data):
        # validated_data is the deserializd data
        print("we creating a document")
        user = self.context['request'].user
        validated_data["owner"] = user
        instance = Document.objects.create(**validated_data)
        return instance
