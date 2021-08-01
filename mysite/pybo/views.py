from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Model_laws_data, Model_SKTL_Policy, Model_GuideManual, Model_Trend
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def home(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/home.html')

def laws_data(request):
    """
    pybo HOME 출력
    """

    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    laws_list = Model_laws_data.objects.order_by('-create_date')


    # 페이징 처리
    paginator = Paginator(laws_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'laws_list': page_obj}
    return render(request, 'pybo/laws_data.html', context)

def regulation_data(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/regulation_data.html')

def SKTL_Policy(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/SKTL_Policy.html')

def GuideManual(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/GuideManual.html')

def Trend(request):
    """
    pybo HOME 출력
    """
    return render(request, 'pybo/Trend.html')

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지(ex-localhost:8000/pybo/?page=1)

    # 조회
    question_list = Question.objects.order_by('-create_date')


    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기, question_list를 페이징 객체 paginator 로 변환
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) #id에 해당하는 Quesiton 객체를 get
    context = {'question': question} #위에서 get한 question 객체를 text 화
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    pybo  질문 등록
    """
    if request.method == 'POST': #저장하기
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm() #request.method 가 'GET'인 경우 호출됨, 질문등록하기
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)