from django import template

register = template.Library()

@register.filter
def is_updated(blog):
    return blog.updated_at > blog.created_at