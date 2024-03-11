from django.http import HttpResponse
from django.template import loader
from .models import Post
def homes_views(request):
    template=loader.get_template('homes.html')
    return HttpResponse(template.render())
def login_views(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def chosen_views(request):
    template=loader.get_template('chosen.html')
    return HttpResponse(template.render())
def template1_views(request):
    template=loader.get_template('template1.html')
    return HttpResponse(template.render())
def temp1_views(request):
    template=loader.get_template('temp1.html')
    return HttpResponse(template.render())
def read_views(request):
    template=loader.get_template('read.html')
    return HttpResponse(template.render())
def exam1_views(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    template = loader.get_template('exam1.html')
    return HttpResponse(template.render(context, request))
# Create your views here.



