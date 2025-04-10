# grocery_list = [
#     {'name': 'apple', 'quantity': 2, 'price': 3},
#     {'name': 'banana', 'quantity': 5, 'price': 2},
#     {'name': 'carrot', 'quantity': 4, 'price': 1}
#   ]

def total_bill_amount(grocery_list):
    total = 0
    for item in grocery_list:
        amt = item['price']*item['quantity'] 
        total += amt
    return total 

def max_quantity_item(grocery_list):
    return max(grocery_list, key = lambda x: x['quantity'])['name'] 

def sort_by_total_amount(grocery_list):
   return sorted(grocery_list, key= lambda x: (-(x['price'] * x['quantity']), x['name']))

def grocery_list_request(grocery_list : list, request : str ):
    if request == 'total_bill_amount':
        return total_bill_amount(grocery_list)
    elif request == 'max_quantity_item':
        return max_quantity_item(grocery_list)
    elif request == 'sort_by_total_amount':
        return sort_by_total_amount(grocery_list)
    
grocery_list = eval(input())

print (grocery_list_request(grocery_list,'total_bill_amount'))
print(grocery_list_request(grocery_list, 'max_quantity_item'))
print(grocery_list_request(grocery_list,'sort_by_total_amount'))
