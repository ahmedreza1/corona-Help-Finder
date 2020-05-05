import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from covid.models import MyPost, MyProfile, MyPayment, FakeCheck
from . import models
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http.response import HttpResponseRedirect

#### Normal Pages Related Views ####

class HomeView(TemplateView):
    template_name = "covid/home.html"

def chose_state(request):
    state = request.POST.get('state')
    models.State.objects.create(state=state)

    stuff_for_frontend = {
    'state': state,
    }
    return render(request, 'covid/chose_state.html', stuff_for_frontend)

class TipsViews(TemplateView):
    template_name = "covid/tips.html"

class InfoView(TemplateView):
    template_name = "covid/info.html"

class DashboardView(TemplateView):
    template_name = "covid/dashboard.html"

    def dashboard(request):
    # Let's assume that the visitor uses an iPhone...
        request.user_agent.is_mobile # returns True
        request.user_agent.is_tablet # returns False
        request.user_agent.is_touch_capable # returns True
        request.user_agent.is_pc # returns False
        request.user_agent.is_bot # returns False

        # Accessing user agent's browser attributes
        request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
        request.user_agent.browser.family  # returns 'Mobile Safari'
        request.user_agent.browser.version  # returns (5, 1)
        request.user_agent.browser.version_string   # returns '5.1'

        # Operating System properties
        request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
        request.user_agent.os.family  # returns 'iOS'
        request.user_agent.os.version  # returns (5, 1)
        request.user_agent.os.version_string  # returns '5.1'

        # Device properties
        request.user_agent.device  # returns Device(family='iPhone')
        request.user_agent.device.family  # returns 'iPhone'



#### Orginisations Profile related Views ####
@method_decorator(login_required, name="dispatch")    
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "address", "phone_no", "description", "pic", "purpose", "mail"]
  
class MyProfileListView(ListView):
    model = MyProfile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        profList = MyProfile.objects.filter(Q(name__icontains = si) | Q(phone_no__icontains = si)).order_by("-id");
        # for p1 in profList:
        #     p1.followed = False
        #     ob = FollowUser.objects.filter(profile = p1,followed_by=self.request.user.myprofile)
        #     if ob:
        #         p1.followed = True
        return profList

  
class MyProfileDetailView(DetailView):
    model = MyProfile
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the user posts
        user_posts = MyPost.objects.filter(uploaded_by_id=self.kwargs['pk']).order_by('-cr_date')
        bank_details = MyPayment.objects.filter(author=self.kwargs['pk'])
        context['user_posts'] = user_posts
        context['bank_details'] = bank_details
        return context


#### Orginisations work/post related views ####
@method_decorator(login_required, name="dispatch")    
class MyPostCreate(CreateView):
    model = MyPost
    fields = ["title", "body", "main_pic", "pic_one", "pic_two", "pic_three", "pic_four", "pic_five", "amount_spend", "total_donars"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")    
class MyPostListView(ListView):
    model = MyPost
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by = self.request.user.myprofile)).filter(Q(title__icontains = si) | Q(body__icontains = si)).order_by("-id");
 

class MyPostDetailView(DetailView):
    model = MyPost

@method_decorator(login_required, name="dispatch")    
class MyPostDeleteView(DeleteView):
    model = MyPost

@method_decorator(login_required, name="dispatch")
class MyPostUpdateView(UpdateView):
    model = MyPost
    fields = ["title", "body", "main_pic", "pic_one", "pic_two", "pic_three", "pic_four", "pic_five", "amount_spend", "total_donars"]



#### Orginisations Bank Account related views ####
@method_decorator(login_required, name="dispatch")
class MyPaymentCreate(CreateView):
    model = MyPayment
    fields = ["account_num", "bank_name", "ifsc", "beneficiary_name"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")
class MyPaymentUpdateView(UpdateView):
    model = MyPayment
    fields = ["account_num", "bank_name", "ifsc", "beneficiary_name"]


#### FakeCheck Views ####
class FakecheckListView(ListView):
    model = FakeCheck
    def get_queryset(self):
        sf = self.request.GET.get("sf")
        if sf == None:
            sf = ""
        return FakeCheck.objects.filter(Q(msg__icontains = sf)).order_by("-id");
