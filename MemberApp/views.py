from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MemberApp.models import Departments, Members
from MemberApp.serializers import DepartmentSerializer, MemberSerializer

from django.core.files.storage import default_storage


# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method =='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
   
    elif request.method == 'POST':
        department_data= JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Sucessfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
   
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer= DepartmentSerializer(department
        , data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Sucessfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
   
    elif request.method =='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)
      
@csrf_exempt
def memberApi(request, id=0):
    if request.method =='GET':
        members = Members.objects.all()
        members_serializer = MemberSerializer(members, many=True)
        return JsonResponse(members_serializer.data, safe=False)
   
    elif request.method == 'POST':
        member_data= JSONParser().parse(request)
        member_serializer = MemberSerializer(data = member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse("Added Sucessfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
   
    elif request.method =='PUT':
        member_data = JSONParser().parse(request)
        member = Members.objects.get(MemberId = member_data['MemberId'])
        member_serializer= MemberSerializer(member, data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse("Updated Sucessfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
   
    elif request.method =='DELETE':
        member=Members.objects.get(MemberId=id)
        member.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile'] 
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name, safe=False)