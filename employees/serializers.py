from rest_framework import serializers
from .models import Employee, Phone
from django.contrib.auth.models import User

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['number']

class EmployeeSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'salary', 'phone']

    def create(self, validated_data):
        # Pop phone data and create or get the Phone object
        phone_data = validated_data.pop('phone')
        phone, created = Phone.objects.get_or_create(number=phone_data['number'])

        # Create the employee instance with the phone object and other validated data
        employee = Employee.objects.create(phone=phone, **validated_data)
        return employee
    
    def update(self, instance, validated_data):
        # Pop phone data to update the phone object
        print('in update')
        phone_data = validated_data.pop('phone')

        # Update phone object if phone data exists
        if phone_data:
            phone, created = Phone.objects.get_or_create(number=phone_data['number'])
            instance.phone = phone
        
        # Update the other fields of the employee
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.salary = validated_data.get('salary', instance.salary)
        
        # Save the updated employee instance
        instance.save()
        return instance
    
    def delete(self, instance):
        # Delete the employee instance
        print('in delete')
        instance.delete()
        return None