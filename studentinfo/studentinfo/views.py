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
        email = request.POST.get('email')
        course_name = request.POST.get('course_name')
        marks = request.POST.get('marks')
        pos+=1
        if marks and course_name and email and fname and lname:
            items_list.append((pos, fname, lname, email, course_name, marks))
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
        email = request.POST.get('email')
        course_name = request.POST.get('course_name')
        marks = request.POST.get('marks')

        updated_item = (item_id, fname, lname, email, course_name, marks)
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