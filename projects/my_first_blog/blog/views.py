from django.http import HttpResponse

# Create your views here.
def posts(request):
    return HttpResponse('All posts of blog')

def post_by_name(request, name_post):
    return HttpResponse(f'Information about post: {name_post}')