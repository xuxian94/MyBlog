from django.shortcuts import render
from easyblog.models import UserInfo,BlogBody
# Create your views here.
def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6]

    return render(request,
                  'index.html',
                  {'userinfo':userinfo,'blog_body':blog_body})

def article(request , blog_body_id='0'):
    print(blog_body_id)
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request,'view.html',{'blog_content':blog_content})