""" Posts Admin Classes. """

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Local
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    list_display = ['username','title','photo','created','modified']
    fieldsets = (
        ('Post',{
            'fields':(
                ('profile','title'),
                'photo',
            )
        },),
    )


class PostInline(admin.StackedInline):
    """Post In-line For User Admin"""
    model = Post
    can_delete = False
    verbose_name_plural = 'Posts'

class UserAdmin (BaseUserAdmin):
    """ Add Post admin to base user admin """
    inlines = (PostInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
