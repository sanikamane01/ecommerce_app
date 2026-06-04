from django.shortcuts import render
from .models import Product, Cart


def create_product(request):
    msg = ""
    newproduct = ""

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        discount_price = request.POST.get("discount_price")
        quantity = request.POST.get("quantity")
        in_stock = request.POST.get("in_stock")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        
        print(in_stock)
        if in_stock is None :
            stock_status=False

        else :
            stock_status=True



        categories = ['electronics', 'clothing', 'books', 'kitchen', 'footwear']

        if category not in categories:
            msg = "Category must be one of the following: electronics, clothing, books, kitchen, footwear"
        
        if Product.objects.filter(name=name).exists():
            msg = "This product is already exist"
        
        elif not name or not description or not brand or not price or not discount_price or not quantity or not category :
            msg = "any filed of these cant be epmty"

        elif float(price) <= 0:
            msg ="Price must be greater than 0"
       
        elif int(quantity) <= 0:
            msg = "Quantity must be greater than 0"


        elif float(discount_price )>= float(price) :
            msg = "Discount price must be less then actual price"

        # elif not image :
        #     msg = "Product image must be required"

        
        
        else :  
            newproduct = Product.objects.create(
            name=name,
            description=description,
            brand=brand,
            price=price,
            discount_price=discount_price,
            quantity=quantity,
            in_stock=stock_status,
            category=category,
            image=image,
            )
            newproduct.save()
            msg = "Product created successfully"

    return render(request, "create_product.html", {"msg": msg, "newproduct":newproduct})


def get_products(request):
    msg = ""
    products = Product.objects.all()
    
    # user wants to search products by category
    if request.method == "POST":
        
        # search
        if request.POST.get("category"):
            category = request.POST.get("category")
            products = Product.objects.filter(category=category)

        # add to cart
        if request.POST.get("product_id"):
            
            # check if user is logged in
            if not request.user.is_authenticated:
                msg = "Please login before adding any items to the cart.."
            else:

                product_id = request.POST.get("product_id")
                user_id = request.user.id
                

                if Cart.objects.filter(user_id=user_id, product_id=product_id).exists():
                    msg = "Product already in the cart"
                else:
                    Cart.objects.create(
                        product_id = product_id,
                        user_id = user_id
                    ).save()
                    msg ="Item has been added into cart"
            
    return render(request, "get_product.html", {"products": products,"msg":msg})  


def update_product(request):
    filtered_product=""
    msg=""
    
    if request.method == "POST" :
        name = request.POST.get("name")
        product_id = request.POST.get("product_id")
        description = request.POST.get("description")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        discount_price = request.POST.get("discount_price")
        quantity = request.POST.get("quantity")
        in_stock = request.POST.get("in_stock")
        category = request.POST.get("category")
        image = request.POST.get("image")

        
        if not product_id :
            msg="please enter product id"

        else :
            
            print(in_stock)
            if in_stock is  None :
                stock_status = False
            else :
                stock_status = True
            print(stock_status)

            
            
            if Product.objects.filter(id=product_id).exists():  
                filtered_product=Product.objects.filter(id=product_id)
                
                filtered_product.update(
                                        name=name,
                                        category=category,
                                        in_stock=stock_status,      
                                        quantity=quantity,
                                        discount_price=discount_price,
                                        price=price,
                                        brand=brand,
                                        description=description
                                        )
                print(filtered_product)
                msg="product updated"
                
            else:
                msg="product not found"
    
    return render(request, "update_product.html", {"updated_product":filtered_product ,"msg":msg})


def delete_product(request):
    msg = " "
    if request.method == "POST":
        product_id = request.POST.get("product_id")

        if Product.objects.filter(id=product_id).exists():
            Product.objects.filter(id=product_id).delete()   
            msg= "product Deleted"
        else:
            msg = "employee not found"

    return render(request, "delete_product.html" , {"msg":msg})


def search_products(request):
    msg=""
    all_products=""

    if request.method == "POST":

        category = request.POST.get("category")
     

        all_products = Product.objects.filter(category=category)      
    return render(request,"search_products.html",{"products":all_products, "msg":msg})


def my_cart_items(request):
    my_userid = request.user.id

    carts = Cart.objects.filter(user_id = my_userid)
    print(carts)
    

def add_to_cart(request):
    
    return render(request, "get_product.html")

    

    
