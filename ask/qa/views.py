from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect
# from .forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def index(request, *args, **kwargs):
    list = Question.objects.order_by('-id')
    # limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    questions = Question.objects.pagination(list, page)
    context = {
        'page':questions,
        'page': page
    }
    return render(request, 'qa/index.html', context)


@require_GET
def popular(request, *args, **kwargs):
    question_list = Question.objects.order_by('-rating')
    try:
        limit = request.GET.get('limit', 10)
    except ValueError:
        limit = 10
    paginator = Paginator(question_list, limit)
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/popular.html', context)


@require_GET
def question(request, question_id):
    """POST and GET methods needed"""
    q = get_object_or_404(Question, id=question_id)
    a = q.answer_set.all()
    context = {'question': q, 'answers': a}
    return render(request, 'qa/question.html', context)
