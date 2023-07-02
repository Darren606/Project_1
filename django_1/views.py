import json
from itertools import count

from django.db.models import Q, Avg, Max, Count
from django.http import HttpResponse
from django.shortcuts import render
from django_1.models import UsernameModel, EmployeeModel, DeptModel, Id_num, RoleModel
from django.http import HttpResponse

def test_db(request):
    test1()
    return HttpResponse('333333333')

    # return HttpResponse('23544')


# def test1():
#     p = UsernameModel(username='dsfag',password='123')
#     p.save()
#
#     UsernameModel.objects.create(username='dfgs', password='123')

# def test2():
#     result = UsernameModel.objects.get(pk=1)
#     print(result)


# def test2():
#     exists = UsernameModel.objects.filter(id__gt=2).exists()
#     if exists:
#         print("At least one object exists with id greater than 2")
#     else:
#         print("No objects exist with id greater than 2")
# def test3():
#     result = UsernameModel.objects.all().order_by("-id")
#     for p in result:
#            print(p)
#

def test5():
    qu = UsernameModel.objects.filter(id=5)
    if qu.exists():
        obj = qu.update(username='woodylyu')
        print(obj)  # Prints the number of objects updated (should be 1)
    else:
        print("No object found with id=3")


def test6():
    obj, created = UsernameModel.objects.update_or_create(id=5, defaults={'username': 'woody'})
    print(obj)
    print(created)


def test7():
    obj, created = UsernameModel.objects.update_or_create(id=4, defaults={'username': 'li'})
    print(obj)
    print(created)


def test3():
    query = UsernameModel.objects.filter(username__contains='s')
    if query:
        print[query]
        return HttpResponse('Logined successfully')
    else:
        print('5')


def test8():
    query = UsernameModel.objects.filter(id=7)
    if query.exists():
        query.delete()
        print('Deleted successfully')
    else:
        print('No objects found')


def test2():
    queryset = UsernameModel.objects.filter(id__gte=2)
    c = queryset.count()
    for obj in queryset:
        print(obj, c)


def test3():
    obj, updated = EmployeeModel.objects.update_or_create(id=1, defaults={'name': 'sanny', 'wage': 2000, 'age': 18})
    print(updated)
    print(obj)


def test2():
    data = [
        {'id': 2, 'name': 'sammy', 'wage': 2000, 'age': 18},
        {'id': 3, 'name': 'john', 'wage': 1200, 'age': 25},
        {'id': 4, 'name': 'emma', 'wage': 4500, 'age': 30},
        {'id': 5, 'name': 'lucy', 'wage': 8000, 'age': 51},
        {'id': 6, 'name': 'island', 'wage': 2800, 'age': 38},
        {'id': 7, 'name': 'emmy', 'wage': 6000, 'age': 45}
    ]

    for item in data:
        obj, updated = EmployeeModel.objects.update_or_create(id=item['id'], defaults=item)
        print(updated)
        print(obj)


"""Add DEPT_ID OF EMPLOYEE"""
def test2():
    data = [
        {'id': 2, 'name': 'sammy', 'wage': 2000, 'age': 18, 'dept': DeptModel.objects.get(id=4)},
        {'id': 3, 'name': 'john', 'wage': 1200, 'age': 25, 'dept': DeptModel.objects.get(id=4)},
        {'id': 4, 'name': 'emma', 'wage': 4500, 'age': 30, 'dept': DeptModel.objects.get(id=5)},
        {'id': 5, 'name': 'lucy', 'wage': 8000, 'age': 51, 'dept': DeptModel.objects.get(id=5)},
        {'id': 6, 'name': 'island', 'wage': 2800, 'age': 38, 'dept': DeptModel.objects.get(id=7)},
        {'id': 7, 'name': 'emmy', 'wage': 6000, 'age': 45, 'dept': DeptModel.objects.get(id=6)}
    ]

    for item in data:
        obj, updated = EmployeeModel.objects.update_or_create(id=item['id'], defaults=item)
        print(updated)
        print(obj)



def test2():
    data = [
        {'id': 2, 'name': 'sammy', 'wage': 2000, 'age': 18},
        {'id': 3, 'name': 'john', 'wage': 1200, 'age': 25},
        {'id': 4, 'name': 'emma', 'wage': 4500, 'age': 30},
        {'id': 5, 'name': 'lucy', 'wage': 8000, 'age': 51},
        {'id': 6, 'name': 'island', 'wage': 2800, 'age': 38},
        {'id': 7, 'name': 'emmy', 'wage': 6000, 'age': 45}
    ]

    for item in data:
        queryset = EmployeeModel.objects.filter(id=item['id'])
        deleted_count, _ = queryset.delete()
        if deleted_count > 0:
            print(f"Deleted object with id {item['id']} successfully")
        else:
            print(f"No object found with id {item['id']}")


def test2():
    queryset = EmployeeModel.objects.filter(Q(Q(id__gte=3) & Q(Q(wage__gt=2500) & Q(age__gt=30))))
    for i in queryset:
        print(i)


def test2():
    queryset = EmployeeModel.objects.raw('select * from t_Employee where wage > %s',(3000,))
    for i in queryset:
        print(i)

def test2():
    queryset = EmployeeModel.objects.aggregate(my_avg=Avg('wage'))
    for i in queryset.values():
        print(i)


def test2():
    queryset = EmployeeModel.objects.aggregate(my_avg=Max('wage'))
    for i in queryset.values():
        print(i)




def test2():
    D1 = DeptModel.objects.create(name='IDE Group', address='Auckland')
    D2 = DeptModel.objects.create(name='IDE Group Akl_Branch', address='Auckland', parent_id=D1.id)
    D3 = DeptModel.objects.create(name='IDE Group Mel_Branch', address='Melbourne', parent_id=D1.id)
    D4 = DeptModel.objects.create(name='IDE Group Syd_Branch', address='Sydney', parent_id=D1.id)
    D5 = DeptModel.objects.create(name='HR Dept', address='Melbourne', parent_id=D3.id)

    return HttpResponse('111111')

def test2():
    obj = EmployeeModel.objects.create(name='many',wage='65000',age='40',dept_id=8)
    i = obj.save()
    print(i)


def test2():
    obj = DeptModel.objects.filter(name__contains='HR')
    if obj:
      obj.delete()
      print('deleted successfully')
    else:
       print('Can not find the items')


""" ID NUMBER  ONE TO ONE FIELD"""
def test2():
    ic = Id_num.objects.create(id_number='56565476544')
    em = EmployeeModel.objects.get(pk=3)
    em.id_numbers = ic
    em.save()



def test2():
    r1 = RoleModel.objects.create(name='courier')
    r2 = RoleModel.objects.create(name='buyer')
    r3 = RoleModel.objects.create(name='accountant')
    em = EmployeeModel.objects.get(pk=2)
    em.roles.add(r1,r2,r3)
    em.save()



def test2():
    queryset = EmployeeModel.objects.filter(age__gte=25)
    for obj in queryset:
        data = {
            'name': obj.name,
            'id': obj.id,
            'wage': obj.wage,
            'age': obj.age
        }
        json_data = json.dumps(data)
        print(json_data)


def test2():
   result = DeptModel.objects.values('name','address').annotate(c=Count('emp_list__name'))
   for i in result:
       print(i)


def test2():
    result = EmployeeModel.objects.annotate(c=Count('roles__name')).filter(c__gte=1).values('name','c')
    for d in result:
        print(d)


def test1():
    result = DeptModel.objects.annotate(cou=Count('emp_list__name')).values('name','cou').order_by('-cou')
    for d in result:
        print(d)
