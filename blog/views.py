from django.shortcuts import render

# Create your vies here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
