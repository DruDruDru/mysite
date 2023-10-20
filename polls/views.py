from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['pk']
        question = get_object_or_404(Question, pk=question_id)

        user_can_not_vote = question.choice_set.filter(voted_by=self.request.user).exists()

        context['user_can_not_vote'] = user_can_not_vote

        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['pk']
        question = Question.objects.get(pk=question_id)
        choices = question.choice_set.all()

        all_votes = sum(choice.votes for choice in choices)

        percents = []
        for choice in choices:
            if all_votes == 0:
                percents.append(0)
            else:
                percents.append(round(choice.votes * 100 / all_votes, 2))
        percents_choices = zip(choices, percents)

        context['percents_choices'] = percents_choices
        return context

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if question.choice_set.filter(voted_by=request.user).exists():
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'вы не сделали выбор'
        })
    else:
        selected_choice.votes += 1
        selected_choice.voted_by.add(request.user)
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

