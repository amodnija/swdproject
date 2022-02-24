from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.db.models import Count




from .models import Leave
from .forms import LeaveForm, ApprovalForm


class LeaveList(ListView):
    # model = Leave
    context_object_name = 'all_leaves'

    def get_queryset(self):
        return Leave.objects.filter()

    def get_context_data(self, **kwargs):

        context = super(LeaveList, self).get_context_data(**kwargs)
        return context



class LeaveView(DetailView):
    # model = Leave
    context_object_name = 'leave'

    def get_queryset(self):
        return Leave.objects.filter()

    def get_context_data(self, **kwargs):

        context = super(LeaveView, self).get_context_data(**kwargs)
        return context


def leave_req(request):
    submitted = False
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            fieldname = leave.name
            c = Leave.objects.filter(name=fieldname).count()
            print(c)
            if c>10:
                leave.availibilty = "No"
            else:
                leave.availibilty = "Yes"
            Leave(id=leave.id,name=leave.name,leavestart=leave.leavestart,leaveend=leave.leaveend,reason=leave.reason,availibilty=leave.availibilty,approval=leave.approval).save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = LeaveForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'demo/leave.html', {'form': form, 'submitted': submitted})
