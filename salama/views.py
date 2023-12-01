from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from salama.models import OrderForm
from salama.forms import register_form, UserRegistrationForm, UserLoginForm, Salama_OrderForm
from django.contrib.auth.decorators import login_required


def home(request):
    stored_messages = messages.get_messages(request)
    return render(request, 'index.html', {'messages': stored_messages})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Congratulations our esteemed customer! You have successfully registered with Salama Millers ltd. as a customer! Welcome!')
            return redirect('handlesignup')
    else:
        form = register_form()
        return render(request, 'customerregister.html', {'form': form})


def handlesignup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # # Check if a user with the same username already exists
            # if User.objects.filter(username=username).exists():
            #     messages.error(request, 'Username already exists. Please choose a different username.')
            #     return render(request, 'customersignup.html', {'form': form})
            form.save()
            messages.success(request,
                             'Congratulations our esteemed customer!You have successfully created your Salama Millers customer account! Welcome!')
            return redirect('handlelogin')
        else:
            return render(request, 'customersignup.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'customersignup.html', {'form': form})


def handlelogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}! You have been successfully logged in.')
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = UserLoginForm()
    return render(request, 'customerlogin.html', {'form': form})


def handlelogout(request):
    logout(request)
    return redirect('handlelogin')


# When you add @login_required above a view function definition, it restricts access to that view.
# If a user tries to access that view without being logged in, Django automatically redirects them to the login page.
@login_required
def create_order(request):
    if request.method == 'POST':
        form = Salama_OrderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,
                                 'Order created successfully! We shall inform you once processed. Thank you for '
                                 'shopping with us.')
                return redirect('view_orders')
            except:
                pass
    else:
        form = Salama_OrderForm()
    return render(request, 'order.html', {'form': form})


def view_orders(request):
    orders = OrderForm.objects.all()
    return render(request, 'view_orders.html', {'form': orders})


def edit(request, id):
    order = OrderForm.objects.get(id=id)
    return render(request, 'edit.html', {'order': order})


def updateData(request, id):
    order = OrderForm.objects.get(id=id)
    form = Salama_OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order')
    else:
        return render(request, 'edit.html', {'order': order})


def delete(request, id):
    order = OrderForm.objects.get(id=id)
    order.delete()
    return redirect('order')
