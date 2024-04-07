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
        
    def create(self, validated_data):
        # Get tags data and category data from validated_data
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')

        note = Note.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            note.tags.add(tag)

        category, created = Category.objects.get_or_create(name=category_data['name'])
        note.category = category
        note.save()

        return note
    
        
    def update(self, instance, validated_data):
        # Get tags data and category data from validated_data
        # Return [] if tags is not in validated_data
        tags_data = validated_data.pop('tags', [])
        # Return None if category is not in validated_data
        category_data = validated_data.pop('category', None)

        instance = super(NoteSerializer, self).update(instance, validated_data)

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)

        if category_data is not None:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            instance.category = category
            instance.save()

        return instance


class NoteSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['note_id', 'title', 'summary', 'created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
    