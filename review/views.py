from django.shortcuts import render, redirect
from .forms import ProductReviewForm


def submit_review(request):
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ProductReviewForm()
    return render(request, 'add/submit_review.html', {'form': form})


def thank_you(request):
    return render(request, 'add/thank_you.html')
