from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Link, Vote
from .forms import LinkForm

from django.core.urlresolvers import reverse_lazy
from django.contrib.comments.models import Comment

class RandomGossipMxin(object):
	def get_context_data(self, **kwargs):
		context = super(RandomGossipMxin, self).get_context_data(**kwargs)
		context[u"randomquip"] = Comment.objects.order_by('?')[0]
		return context

class LinkListView(RandomGossipMxin, ListView):
	model = Link

	queryset = Link.with_votes.all()
	paginate_by = 3


class LinkCreateView(CreateView):
	model = Link
	form_class = LinkForm

	def form_valid(self, form):
		f = form.save(commit=False)
		f.rank_score = 0.0
		f.submitter = self.request.user
		f.save()

		return super(CreateView, self).form_valid(form)

class LinkDetailView(DetailView):
	model = Link


class LinkUpdateView(UpdateView):
	model = Link
	form_class = LinkForm

class LinkDeleteView(DeleteView):
	model = Link
	success_url = reverse_lazy("home")