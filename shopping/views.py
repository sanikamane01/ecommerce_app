from django.shortcuts import render
from .models import Product



def create_product(request):
    msg = ""
    
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        brand = request.POST.get("brand")
        price = request.POST.get("price")
        discount_price = request.POST.get("discount_price")
        quantity = request.POST.get("quantity")
        in_stock = request.POST.get("in_stock")
        category = request.POST.get("category")
        image = request.POST.get("image")
        
        categories = ['electronics', 'clothing', 'books', 'kitchen', 'footwear']
        if category not in categories:
            msg = "Category must be one of the following: electronics, clothing, books, kitchen, footwear"
        
        if Product.objects.filter(name=name).exists():
            msg = "This product is already exist"
        
        elif int(price) <= 0:
            msg ="Price must be greater than 0"
       
        elif int(quantity) <= 0:
            msg = "Quantity must be greater than 0"
        
        elif not name or not description or not brand or not price or not discount_price or not quantity or not in_stock or not category :
            msg = "any filed of these cant be epmty"

        elif discount_price and float(discount_price )>= float(price) :
            msg = "Discount price must be less then actual price"

        elif not image :
            msg = "Product image must be required"

        elif quantity < 0 :
            msg = "Quantity must not be in negative"

        elif price >= 0 :
            msg = "Price must be greater then 0"
        
        else :  
            Product.objects.create(
            name=name,
            description=description,
            brand=brand,
            price=price,
            discount_price=discount_price,
            quantity=quantity,
            in_stock=in_stock,
            category=category,
            image=image,
        )

        msg = "Product created successfully"

    return render(request, "create_product.html", {"msg": msg})


def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, "get_product.html", {"products": products})  


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

        all_products=Product.objects.filter(category=category).filter(category=category)
        print(len(all_products))

        if not category:
            msg="category must not be empty"

        elif (len(all_products)) == 0 :
            msg="product is not available"

        

    
    return render(request,"search_products.html",{"products":all_products, "msg":msg}) 


    
