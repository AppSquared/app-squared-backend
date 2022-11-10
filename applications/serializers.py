from rest_framework import serializers
from .models import Application, Company


class ApplicationSerializer(serializers.ModelSerializer):
    # companies = serializers.HyperlinkedRelatedField(
    #     view_name='company_detail',
    #     many=True,
    #     read_only=True
    # )
    application_url = serializers.ModelSerializer.serializer_url_field(
        view_name='application_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Application
        fields = ('id', 'owner', 'application_url', 'date_applied', 'notes', 'status')

# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Application
        # fields = ('id', 'name', 'phone_number', 'address', 'website', 'application')
