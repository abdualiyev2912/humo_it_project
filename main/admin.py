from django.contrib import admin
from main.models import Portfolio, PortfolioImage, Developer, Contact, Comment, New

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    inlines = [PortfolioImageInline]
    

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    search_fields = ('name', 'skills')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'created_at')
    search_fields = ('user_name', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)



@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('published_date', 'author')
    readonly_fields = ('published_date',)