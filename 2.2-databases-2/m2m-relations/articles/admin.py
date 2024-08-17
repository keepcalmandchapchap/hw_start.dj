from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        check = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
               check = True
        if not check:
            raise ValidationError('Должен быть хотя-бы один главный тэг')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scopes
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)