from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib.auth.decorators import user_passes_test
from blog.forms import BlogForm, TagForm
from blog.models import Blog, Category, Tag

def superuser_only(user):
    return (user.is_authenticated() and user.is_superuser)

@user_passes_test(superuser_only, login_url="/")
def index(request):
    blogs = Blog.objects.all().order_by('-posted')
    tags = Tag.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs, 'tags':tags})

@user_passes_test(superuser_only, login_url="/")
def add_blog(request):
    id = request.GET.get('id', None)
    if (id is not None):
        blog = get_object_or_404(Blog, id = id)
    else:
        blog = None
        
    if (request.method == 'POST'):
        if (request.POST.get('control') == 'delete'):
            blog.delete()
            messages.add_message(request, messages.INFO, 'Entry Deleted!')
            return HttpResponseRedirect(reverse('blog:index'))
        
        form = BlogForm(request.POST, instance = blog)
        if (form.is_valid()):
            form.save()
            messages.add_message(request, messages.INFO, 'Entry Added!')
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = BlogForm(instance = blog)
    return render(request, 'blog/add_blog.html', {'form':form, 'blog':blog})

@user_passes_test(superuser_only, login_url="/")
def add_tag(request):
    id = request.GET.get('id', None)
    if (id is not None):
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None

    if (request.method == 'POST'):
        if (request.POST.get('control') == 'delete'):
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect(reverse('blog:index'))

        form = TagForm(request.POST, instance=tag)
        if (form.is_valid()):
            t = form.save(commit=False)
            t.slug = slugify(t.label)
            t.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect(reverse('blog:index'))

    else:
        form = TagForm(instance=tag)

    return render(request, 'blog/add_tag.html', {'form':form, 'tag':tag})

@user_passes_test(superuser_only, login_url="/")
def tag_search(request, **kwargs):
    slug = kwargs['slug']
    tag = get_object_or_404(Tag, slug=slug)
    blog = tag.blogs.all()
	
    return render(request, 'blog/tag_search.html', {'blogs':blog, 'tag':tag})
