from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reader, Book  # Import Book if you haven't already
from django.contrib import messages

def home(request):
    return render(request, 'home.html', context={'current_tab': 'home'})

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        return render(request, 'welcome.html', context={'student_name': student_name})
    return redirect('home')

def readers(request):
    query = request.GET.get('search', '')  # Get the search query from the request
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        reader_id = request.POST.get('reader_id')
        address = request.POST.get('address')

        new_reader = Reader(reader_id=reader_id, name=name, contact_no=contact_no, address=address)
        new_reader.save()
        return redirect('readers')

    if query:
        all_readers = Reader.objects.filter(name__icontains=query)  # Filter by name
    else:
        all_readers = Reader.objects.all()  # Get all readers if no search query

    context = {
        'all_readers': all_readers,
        'readers': all_readers.count(),  # Count of total readers
        'search_query': query,  # Pass the query to retain in the search box
    }
    return render(request, 'readers.html', context)

def collections(request):
    books = Book.objects.all()  # Fetch all books from the model
    return render(request, 'category.html', {'books': books})

cart = {}

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Use get_object_or_404 for safety
    quantity = int(request.POST.get('quantity', 1))

    # Update cart
    if book_id in cart:
        cart[book_id]['quantity'] += quantity
        cart[book_id]['total_price'] = cart[book_id]['quantity'] * cart[book_id]['price']
    else:
        cart[book_id] = {
            'book': book,
            'quantity': quantity,
            'price': book.price,
            'total_price': book.price * quantity,
        }

    messages.success(request, f"{quantity} of '{book.name}' added to cart.")
    return redirect('collections')

def checkout(request):
    total_amount = sum(item['total_price'] for item in cart.values())
    context = {
        'cart_items': cart.values(),
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)

def payment_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        # Here you can add payment processing logic

        # Redirect to payment success page after processing
        return redirect('payment_success')

    return render(request, 'payment_info.html')

def payment_success(request):
    return render(request, 'payment_success.html')
