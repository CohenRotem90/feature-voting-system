from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FeatureRequest, Vote
from .forms import FeatureForm
from django.db import IntegrityError
from django.db.models import Count

@login_required
def feature_list(request):
    features = FeatureRequest.objects.annotate(
        votes_count=Count('vote')
    ).order_by('-votes_count', '-created_at')
    return render(request, 'feature_voting/feature_list.html', {'features': features})

@login_required
def feature_create(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.created_by = request.user
            feature.save()
            return redirect('feature_list')
    else:
        form = FeatureForm()
    return render(request, 'feature_voting/feature_form.html', {'form': form})

@login_required
def vote_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    try:
        Vote.objects.create(user=request.user, feature=feature)
    except IntegrityError:
        pass  # Already voted
    return redirect('feature_list')