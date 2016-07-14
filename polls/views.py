from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question, List, Item

# Create your views here.

def home(request):
    return render(request, "polls/home.html", {})
    

def listdetail(request):

    return render(request, 'polls/listdetail.html', {})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def profile(request):
    return render(request, 'polls/profile.html', {})


def list(request):

  todo_listing = []

  for todo_list in List.objects.all():  

    todo_dict = {}  

    todo_dict['list_object'] = todo_list

    todo_dict['item_count'] = todo_list.item_set.count()  

    todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()  

    todo_dict['items_name'] = todo_list.item_set

   

    todo_listing.append(todo_dict)  


    return render(request, 'polls/list.html', {'todo_listing': todo_listing})




