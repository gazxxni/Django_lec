from django.shortcuts import render
from .models import Content

# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request,'pages/company_info.html')

def content_list(request):
    contents = Content.objects.all()  # 모든 콘텐츠를 가져옵니다.
    return render(request, 'pages/content_list.html', {'content_list': contents})