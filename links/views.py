from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Link, Vote
from .forms import LinkForm, VoteForm

from django.core.urlresolvers import reverse_lazy
from django.contrib.comments.models import Comment

from django.shortcuts import redirect, get_object_or_404

import json
from django.http import HttpResponse

class RandomGossipMxin(object):
	def get_context_data(self, **kwargs):
		context = super(RandomGossipMxin, self).get_context_data(**kwargs)
		context[u"randomquip"] = Comment.objects.order_by('?')[0]
		return context

class LinkListView(RandomGossipMxin, ListView):
	model = Link

	queryset = Link.with_votes.all()
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(LinkListView, self).get_context_data(**kwargs)
		if self.request.user.is_authenticated():
			voted = Vote.objects.filter(voter=self.request.user)
			links_in_page = [link.id for link in context["object_list"]]
			voted = voted.filter(link_id__in=links_in_page)
			voted = voted.values_list('link_id', flat=True)
			context["voted"] = voted
		return context


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

class JSONFormMixin(object):
	def create_response(self, vdict=dict(), valid_form=True):
		response = HttpResponse(json.dumps(vdict), content_type='application/json')
		response.status = 200 if valid_form else 500
		return response

class VoteFormBaseView(FormView):
	form_class = VoteForm

	def create_response(self, vdict=dict(), valid_form=True):
		response = HttpResponse(json.dumps(vdict))
		response.status = 200 if valid_form else 500
		return response

	def form_valid(self, form):
		link = get_object_or_404(Link, pk=form.data["link"])
		user = self.request.user
		prev_votes = Vote.objects.filter(voter=user, link=link)
		has_voted = (prev_votes.count() > 0)

		ret = {"success": 1}
		if not has_voted:
			v = Vote.objects.create(voter=user, link=link)
			ret["voteobj"] = v.id
			print "Voted"
		else:
			prev_votes[0].delete()
			print "Removed Vote"

		return self.create_response(ret, False)

	def form_invalid(self, form):
		ret = {"sucess": 0, "form_errors": form.errors}
		return self.create_response(ret, False)

class VoteFormView(JSONFormMixin, VoteFormBaseView):
    pass