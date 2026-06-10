from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def products(request):
    # Initialize cart data in session if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = {}
        
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity_str = request.POST.get('quantity', '1')

        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 1

        if quantity <= 0:
            quantity = 1

        cart = request.session.get('cart', {})

        cart[product_name] = cart.get(product_name, 0) + quantity

        request.session['cart'] = cart


        request.session['cart_count'] = sum(cart.values())

        request.session.modified = True


    return redirect('products')

def checkout(request):
    cart = request.session.get('cart', {})
    prices = {
        'Turmeric Powder': 120,
        'Chilli Powder': 150,
        'Garam Masala': 180,
        'Chicken Masala': 160,
        'Coriander Powder': 130,
        'Pepper Powder': 200,
        'Cumin Powder': 190,
        'Rasam Powder': 140,
    }

    cart_items = []
    subtotal = 0

    for product_name, quantity in cart.items():
        price = prices.get(product_name, 0)
        item_total = price * quantity
        subtotal += item_total
        cart_items.append({
            'name': product_name,
            'quantity': quantity,
            'price': price,
            'total': item_total,
        })

    final_total = subtotal

    context = {'cart_items': cart_items, 'subtotal': subtotal, 'final_total': final_total}
    return render(request, 'checkout.html', context)