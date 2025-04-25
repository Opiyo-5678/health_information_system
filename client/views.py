from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import HealthProgram, Client, Enrollment
from .forms import HealthProgramForm, ClientForm, EnrollmentForm, ClientSearchForm
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ClientSerializer


def index(request):
    return render(request, 'index.html')


def program_create(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Health program created successfully!')
            return redirect('program_create')
    else:
        form = HealthProgramForm()
    
    programs = HealthProgram.objects.all().order_by('-created_at')
    return render(request, 'program_create.html', {
        'form': form,
        'programs': programs
    })


def client_register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client registered successfully!')
            return redirect('client_list')
    else:
        form = ClientForm()
    
    return render(request, 'client_register.html', {'form': form})


def client_list(request):
    form = ClientSearchForm(request.GET)
    clients = Client.objects.all().order_by('last_name', 'first_name')
    
    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            clients = clients.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query)
            )
    
    return render(request, 'client_list.html', {
        'clients': clients,
        'form': form
    })


def client_profile(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    enrollments = Enrollment.objects.filter(client=client).select_related('program')
    
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.client = client
            
            program = form.cleaned_data['program']
            if Enrollment.objects.filter(client=client, program=program).exists():
                messages.error(request, f'Client is already enrolled in {program.name}')
            else:
                enrollment.save()
                messages.success(request, f'Client enrolled in {program.name} successfully!')
            
            return redirect('client_profile', client_id=client.id)
    else:
        form = EnrollmentForm()
    
    return render(request, 'client_profile.html', {
        'client': client,
        'enrollments': enrollments,
        'form': form
    })
    

class ClientAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'