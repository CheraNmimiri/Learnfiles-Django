from django.contrib import admin
from .models import Info
from django.http import HttpResponse
from django.core import serializers
# Register your models here.


def export_as_json(modeladmin , request , queryset):
    
    response = HttpResponse(content_type = "application/json")
    serializers.serialize("json" , queryset , stream = response)
    return response


def make_published_status(modeladmin , request , queryset):

    count = queryset.update(status = "published")
    
    if count == 1:  
        message_bit = "1 info was"
    else:
        message_bit ="{} info were".format(count)

    modeladmin.message_user(request , "{} successfullt marked as published".format(message_bit))
    
def make_draft_status(modeladmin , request , queryset):

    count = queryset.update(status = "draft")
    
    if count ==1 :
        message_bit = "1 info was"
    else:
        message_bit = "%d info were" % (count)

    modeladmin.message_user(request , "%s successfully marked as draft" % (message_bit))

make_published_status.short_description = "Change marked info to publish"
make_draft_status.short_description = "Change marked info to draft"
export_as_json.short_description = "Show as json marked info "


@admin.register(Info)
class PostAdmin(admin.ModelAdmin):
    list_display = ("username", "created", "status")
    prepopulated_fields = {"username": ("first_name",)}
    list_filter = ("username", "created", "status")
    search_fields = ("username", "first_name" , "last_name")
    ordering = ["status" , "age"]
    actions= [make_published_status , make_draft_status, export_as_json]
    


