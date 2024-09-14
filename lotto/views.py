from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):

    # request.POST -> dict
    # - dict의 key == input tag의 name 값
    # - dict의 value == input tag의 value 값 (== USER의 입력값)
    # request.POST['fname'] -> '안녕하세요.'
    # request.POST['lname'] -> '반갑습니다.'

    lottos = GuessNumbers.objects.all() 

    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict

def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            lotto = form.save(commit = False)
            lotto.generate()

            return redirect('index')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})


    form = PostForm()

    return render(request, 'lotto/form.html', {'form': form})

def hello(request):

    # data = GuessNumbers.object.all()
    # data = GuessNumbers.object.()

    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(pk = lottokey)

    return render(request, 'lotto/detail.html', {'lotto': lotto})
