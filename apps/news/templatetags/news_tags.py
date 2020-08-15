from django import template

from news.models import Category

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='Imper'):
    categories=Category.objects.all()
    return {"categories" : categories, "arg1":arg1,"arg2":arg2}

@register.filter
def attr(form, name_arg):
    # case attr:'class=customclass'
    attrs = form.field.widget.attrs
    try:
        name, arg = name_arg.split("=")
        attrs[name] = arg
        rendered = str(form)
    except:
        pass
    return form