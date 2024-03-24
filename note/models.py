from django.db import models


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_tags(self):
        if self.tags.all():
            return ', '.join([tag.name for tag in self.tags.all()])
        else:
            return ''
    
    def get_category(self):
        if self.category:
            return self.category.name
        else:
            return ''
        