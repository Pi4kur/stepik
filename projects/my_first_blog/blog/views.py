from django.http import HttpResponse

# Create your views here.
def posts(request):
    return HttpResponse('All posts of blog')


def post_by_name(request, name_post):
    return HttpResponse(f'Information about post: {name_post}')


def post_by_number(request, number_post):
    return HttpResponse(f'Information about post with number: {number_post}')