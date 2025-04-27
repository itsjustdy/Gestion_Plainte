from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Issue
from .forms import IssueForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('issue_list')
    else:
        form = UserCreationForm()
    return render(request, 'issues/signup.html', {'form': form})

@login_required
def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            return redirect('issue_list')
    else:
        form = IssueForm()
    return render(request, 'issues/report_issue.html', {'form': form})

@login_required
def issue_list(request):
    issues = Issue.objects.filter(user=request.user)
    return render(request, 'issues/issue_list.html', {'issues': issues})

@login_required
def issue_detail(request, issue_id):
    issue = Issue.objects.get(id=issue_id, user=request.user)
    return render(request, 'issues/issue_detail.html', {'issue': issue})

@login_required
def update_issue_status(request, issue_id):
    issue = Issue.objects.get(id=issue_id, user=request.user)
    if request.method == 'POST':
        issue.status = request.POST.get('status')
        issue.save()
        return JsonResponse({'status': 'success', 'issue_id': issue.id})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
from django.shortcuts import render

@login_required
def logout_views(request):
    logout(request)
    return render(request, 'registration/logout.html')
    