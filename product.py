#product details with price in dollar
catalog={
    "product A": 20,
    "product B": 40,
    "product C": 50
}
#discount details
discount={
    "flat_10_discount":10,
    "bulk_5_discount":5,
    "bulk_10_discount":10,
    "tiered_50_discount":50

}

quantity=[]
gift_wraps=[]
#quantities of product entered into an empty list
for product in catalog:

    q=int(input("enter the quantity of {} ".format(product)))
    quantity.append(q)
    gift_wrap=input("wrap {} as a gift(yes/no)".format(product))
    gift_wraps.append(gift_wrap.lower()=="yes") 
sum1=0  
#sum of quantity
for q1 in quantity:
    sum1+=q1
sub_Total=0
gift_wrap_fee=0   
#totalamount,subtotal and gift value calculation
for i,product in enumerate(catalog):
    Total_amount=catalog[product]*quantity[i]
    if gift_wraps[i]:
        Total_amount += quantity[i]
        gift_wrap_fee += quantity[i]
    
    sub_Total+=Total_amount
#discount calc
for rule in discount:
    if rule =="flat_10_discount" and sub_Total>200:
        discount_name=rule
        discount_amount=discount[rule]

    elif rule =="bulk_5_discount":
        for i,product in enumerate(catalog):
            if quantity[i]>10:
                discount_name=rule
                discount_amount = catalog[product]*quantity[i]/100
                break

    elif rule =="bulk_10_discount" and sum1>20:
        discount_name=rule
        discount_amount=sub_Total*discount[rule]/100
    elif rule == "tiered_50_discount" and sum1>30 and any(qty>15 for qty in quantity):
        discount_name=rule
        discountable = [max(qty-15,0) for qty in quantity]
        discount_amount= sum(discountable)*catalog[product]*0.5

shipping_fee = sum1//2
total = sub_Total-discount_amount+shipping_fee

#output
for i,product in enumerate(catalog):
    print ("\nproduct detalis of {}".format(product))
    Total_amount=catalog[product]*quantity[i]

    if gift_wraps[i]:
        Total_amount +=quantity[i]
        print("Quantity:{},Total:${}".format(quantity[i],Total_amount))
    else:

        print("Quantity:{},Total:${}".format(quantity[i],Total_amount))

    print("subtotal:${}".format(sub_Total))
    print("Discount name:{}".format(discount_name))
    print("Discount amount:${}".format(discount_amount))
    print("Total Gift wrap fee:${}".format(gift_wrap_fee))
    print("Total shipping fee:${}".format(shipping_fee))
    print("Total:${}".format(total))




