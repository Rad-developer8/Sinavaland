from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tour


def tour_list(request):
    tours = Tour.objects.filter(is_available=True).order_by('start_date')

    duration = request.GET.get('duration')
    if duration:
        tours = tours.filter(duration=duration)

    search = request.GET.get('search')
    if search:
        tours = tours.filter(title__icontains=search) | tours.filter(destination__icontains=search)

    paginator = Paginator(tours, 12)
    page = request.GET.get('page')
    tours = paginator.get_page(page)

    return render(request, 'tours/list.html', {
        'tours': tours,
        'durations': Tour.DURATION_CHOICES,
    })


def tour_detail(request, slug):
    tour = get_object_or_404(Tour, slug=slug, is_available=True)

    user_has_reserved = False
    if request.user.is_authenticated:
        user_has_reserved = request.user in tour.reserved_by.all()

    return render(request, 'tours/detail.html', {
        'tour': tour,
        'user_has_reserved': user_has_reserved,
    })


@login_required
def reserve_tour(request, slug):
    if request.method != 'POST':
        return redirect('tours:detail', slug=slug)

    tour = get_object_or_404(Tour, slug=slug, is_available=True)

    if request.user in tour.reserved_by.all():
        messages.warning(request, 'شما قبلاً این تور را رزرو کرده‌اید.')
    elif tour.available_seats <= 0:
        messages.error(request, 'ظرفیت این تور تکمیل شده است.')
    else:
        tour.reserved_by.add(request.user)
        messages.success(request, f'تور "{tour.title}" با موفقیت رزرو شد.')

    return redirect('tours:detail', slug=slug)


@login_required
def cancel_reservation(request, slug):
    tour = get_object_or_404(Tour, slug=slug)

    if request.user not in tour.reserved_by.all():
        messages.warning(request, 'شما رزروی برای این تور ندارید.')
    else:
        tour.reserved_by.remove(request.user)
        messages.success(request, 'رزرو شما با موفقیت لغو شد.')

    return redirect('tours:detail', slug=slug)


@login_required
def my_reservations(request):
    tours = request.user.reserved_tours.all()
    return render(request, 'tours/my_reservations.html', {'tours': tours})
