from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .forms import *

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class AgentReferalViewSet(viewsets.ModelViewSet):
    queryset = AgentReferal.objects.all()
    serializer_class = AgentReferalSerializer
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
class AgentList(ListView):
    model = Agent



class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes',
              'mobile_number','phone_number','email_id','media_name']

class AgentAddrLocArefCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes',
              'mobile_number','phone_number','email_id','media_name']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddrLocArefCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST)
            data['address'] = AddressFormSet(self.request.POST)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST)
        else:
            data['location'] = LocationFormSet()
            data['address'] = AddressFormSet()
            data['agentreferal'] = AgentReferalFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        agentreferal = context['agentreferal']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid() and agentreferal.is_valid():
                location.instance = self.object
                address.instance = self.object
                agentreferal.instance = self.object
                location.save()
                address.save()
                agentreferal.save()
        return super(AgentAddrLocArefCreate, self).form_valid(form)

class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number','phone_number','email_id','media_name']


class AgentAddrLocArefUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes', 'mobile_number','phone_number','email_id','media_name']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddrLocArefUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST, instance=self.object)
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST, instance=self.object)
        else:
            data['location'] = LocationFormSet(instance=self.object)
            data['address'] = AddressFormSet(instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        address = context['address']
        agentreferal = context['agentreferal']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid() and address.is_valid() and agentreferal.is_valid():
                location.instance = self.object
                address.instance = self.object
                agentreferal.instance = self.object
                location.save()
                address.save()
                agentreferal.save()

        return super(AgentAddrLocArefUpdate, self).form_valid(form)


class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')


