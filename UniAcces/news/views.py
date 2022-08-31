from django.shortcuts import render
import requests,json
from news.models import Article
from django.contrib.auth.models import User
def homepage(request):
    data=Article.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def post_detail(request,slug):
    return render(request,'post_detail.html')

def signup_page(request):
    context={}
    if request.method=='POST':
        captcha_token=request.POST['g-recaptcha-response']
        captcha_url="https://www.google.com/recaptcha/api/siteverify"
        captcha_secret="6LedVMAhAAAAALUZVcSndIJEwwXBkRYsSwntFOYh"
        captcha_data={"secret":captcha_secret,"response":captcha_token}
        captcha_server_response=requests.post(url=captcha_url,data=captcha_data)
        captcha_json=json.loads(captcha_server_response.text)
        if captcha_json['success']==False:
                 context['status'] = 'Invaild recaptcha!'
                 context['col'] = 'alert-danger'
        else:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user=User.objects.create_user(username,email,password)
            user.save()
            context['status']='User created successfully!'
            context['col']='alert-success'
    return render(request,'signup.html',context)