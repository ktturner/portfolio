from __future__ import unicode_literals

from django.db import models

class Pattern(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    def __unicode__(self):
        return self.name

class Illustration(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    def __unicode__(self):
        return self.name

class Sketchbook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    def __unicode__(self):
        return self.name

def get_image_path_pattern(instance, filename):
    return '/'.join(['pattern_images', instance.pattern.slug, filename])

class UploadPattern(models.Model):
    pattern = models.ForeignKey(Pattern, related_name="uploads_pattern")
    image = models.ImageField(upload_to=get_image_path_pattern)

def get_image_path_illustration(instance, filename):
    return '/'.join(['illustration_images', instance.illustration.slug, filename])

class UploadIllustration(models.Model):
    illustration = models.ForeignKey(Illustration, related_name="uploads_illustration")
    image = models.ImageField(upload_to=get_image_path_illustration)

def get_image_path_sketchbook(instance, filename):
    return '/'.join(['sketchbook_images', instance.sketchbook.slug, filename])

class UploadSketchbook(models.Model):
    sketchbook = models.ForeignKey(Sketchbook, related_name="uploads_sketchbook")
    image = models.ImageField(upload_to=get_image_path_sketchbook)
