from django.shortcuts import render
def post_list(request):
    return render(request, 'blog2/post_list.html', {})
# Create your views here.
