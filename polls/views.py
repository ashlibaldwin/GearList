from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import redirect
from .models import Choice, Question, List, Item
from .forms import ItemForm, ListForm
from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def home(request):
    return render(request, "polls/home.html", {})


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

    lists = List.objects.all()

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
            return redirect('list_detail', pk=list.pk)
    
    else:
        form = ListForm()


    return render(request, 'polls/list.html', {'lists': lists, 'form': form})


def list_detail(request, pk):

  
    lists = List.objects.get(id=pk)
    items =lists.item_set.all()


    form = ItemForm

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.todo_list = lists
            item.save()
            form = ItemForm
            return HttpResponseRedirect('')

    else:
        form = ItemForm()


    return render(request, 'polls/list_detail.html', {'items': items, 'form': form, 'lists':lists})

def delete_item(request, pk):
    

    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return HttpResponseRedirect('list')
    return render(request, 'polls/delete_item.html', {'object':item})



