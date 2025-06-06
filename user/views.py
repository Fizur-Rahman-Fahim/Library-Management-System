from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from decimal import Decimal
from .models import UserProfile, User, generate_unique_library_card
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile with generated library card and additional info
            UserProfile.objects.create(
                user=user,
                library_card_number=generate_unique_library_card(),
                address=form.cleaned_data.get('address', ''),
                phone_number=form.cleaned_data.get('phone', '')
            )
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def deposit_money(request):
    if request.method == 'POST':
        try:
            amount = Decimal(request.POST.get('amount', '0'))
            if amount <= 0:
                messages.error(request, 'Please enter a valid amount greater than 0.')
                return redirect('user:deposit_money')
            user = request.user
            user.balance += amount
            user.save()
            messages.success(request, f'Successfully deposited ${amount}. New balance: ${user.balance}')
            return redirect('library:profile')
        except (ValueError, TypeError):
            messages.error(request, 'Please enter a valid amount.')
            return redirect('user:deposit_money')
            
    return render(request, 'user/deposit.html')

@login_required
def check_balance(request):
    balance = getattr(request.user, 'balance', 0)
    return render(request, 'user/balance.html', {'balance': balance})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')