from rest_framework import serializers
from note.models import Note, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Note
        fields =  ['note_id', 'title', 'content', 'created_at', 
                   'updated_at', 'tags', 'category']


class NoteSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['note_id', 'title', 'summary', 'created_at', 'updated_at']
        