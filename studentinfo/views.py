from django.shortcuts import render, redirect
from django.http import HttpResponse

items_list: list = []
pos: int = 0
status: bool = True

def home(request):
    context = dict()
    print(type(context))
    global pos

    if request.method =='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        pos+=1
        if age and fname and lname:
            items_list.append((pos, fname, lname, age))
            context = {
                'items': items_list
            }
        else:
            context['message'] = "empty value not allowed"

    if len(items_list)>0:
        context = {
            'items': items_list
        }
    return render (request, "home/index.html", context)
    
def edit_view(request, item_id):
    item = None
    for i in range(len(items_list)):
        if items_list[i][0] == item_id:
            item = items_list[i]
            break

    if not item:
        return HttpResponse("Items not found", status=404)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        updated_item = (item_id, fname, lname, age)
        items_list[i] = updated_item
        context = {
            'item': item
        }

        return redirect('home')

    context = {
        'item': item
    }   
    return render(request, 'home/edit_item.html', context)

def delete_view(request, item_id):
    global items_list
    items_list = [item for item in items_list if item[0] != item_id]
    return redirect('home') 