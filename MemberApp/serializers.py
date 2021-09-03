from rest_framework import serializers
from MemberApp.models import Departments, Members

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
        'DepartmentName')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('MemberId',
        'MemberName',
        'Department',
        'DateOfJoining',
        'PhotoFileName')
