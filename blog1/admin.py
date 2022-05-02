from django.contrib import admin

# Register your models here.

from blog1.models import BlogPost
 
admin.site.register(BlogPost)


class BlogPostAdmin(admin.ModelAdmin):
    # pk:索引
    # 属性list_display表示要显示哪些属性
    list_display = ['pk','title','body','timestamp']
 
admin.site.register(BlogPost,BlogPostAdmin)
