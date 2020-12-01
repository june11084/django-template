from django.shortcuts import render, redirect
# Create your views here.
from .forms import ProductForm
from .models import Product


def view_products(request):
    # Retrieve all the products and render products.html with the data
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)


def create_product(request):
    # Create a form instance and populate it with data from the request
    form = ProductForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return redirect('view_products')
    # if the request does not have post data, a blank form will be rendered
    return render(request, 'products/product-form.html', {'form': form})


def update_product(request, id):
    # Get the product based on its id
    product = Product.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = ProductForm(request.POST or None, instance=product)
    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('view_products')
    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'products/product-form.html', {'form': form})


def delete_product(request, id):
    # Get the product based on its id
    product = Product.objects.get(id=id)
    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        product.delete()
        # after deleting redirect to view_product page
        return redirect('view_products')
    # if the request is not post, render the page with the product's info
    return render(request, 'products/delete-confirm.html', {'product': product})
