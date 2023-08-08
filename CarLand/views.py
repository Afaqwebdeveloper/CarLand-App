from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ad, CarFeature
from .forms import AdForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('CarLand:home')
        else:
            return render(request, 'CarLand/login.html', {'error': 'Invalid username or password'})

    return render(request, 'CarLand/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('CarLand:home')
        else:
            return render(request, 'CarLand/register.html', {'error': 'Passwords do not match'})

    return render(request, 'CarLand/register.html')

def logout_view(request):
    logout(request)
    return render(request, 'CarLand/logout.html')

@login_required
def post_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('CarLand:ad_list')
    else:
        form = AdForm()

    return render(request, 'CarLand/post_ad.html', {'form': form})

def ad_list(request):
    ads = Ad.objects.all()

    brand = request.GET.get('brand')
    model = request.GET.get('model')
    year = request.GET.get('year')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    if brand:
        ads = ads.filter(brand__name=brand)
    if model:
        ads = ads.filter(model__name=model)
    if year:
        ads = ads.filter(year=year)
    if price_min:
        ads = ads.filter(price__gte=price_min)
    if price_max:
        ads = ads.filter(price__lte=price_max)

    context = {
        'ads': ads,
    }
    return render(request, 'CarLand/ad_list.html', context)

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    contact_visible = request.user.is_authenticated
    return render(request, 'CarLand/ad_detail.html', {'ad': ad, 'contact_visible': contact_visible})

def filter_ads(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price_min = request.POST.get('price_min')
        price_max = request.POST.get('price_max')
        ads = Ad.objects.all()

        if brand:
            ads = ads.filter(brand=brand)

        if model:
            ads = ads.filter(model=model)

        if year:
            ads = ads.filter(year=year)

        if price_min and price_max:
            ads = ads.filter(price__gte=price_min, price__lte=price_max)

    else:
        ads = Ad.objects.all()

    return render(request, 'CarLand/ad_list.html', {'ads': ads})

def sort_ads(request):
    sort_by = request.GET.get('sort_by', 'date_published')  
    ads = Ad.objects.all()

    if sort_by == 'year':
        ads = ads.order_by('year')
    elif sort_by == 'price':
        ads = ads.order_by('price')
    elif sort_by == 'date_published':
        ads = ads.order_by('-date_published')

    return render(request, 'CarLand/ad_list.html', {'ads': ads})

def home(request):
    featured_cars = CarFeature.objects.all()
    return render(request, 'CarLand/home.html', {'featured_cars': featured_cars})
