from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if not self.forms[0].cleaned_data['is_main']:
            raise ValidationError('Первый тэг долже быть главным')
        for form in self.forms[1:]:
            if form.cleaned_data.get('is_main'):
                raise ValidationError('Главным можно отметить только первый тэг')
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