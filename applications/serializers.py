from rest_framework import serializers
from .models import Application, Contact


class ApplicationSerializer(serializers.ModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(
        view_name='contact_detail',
        many=True,
        read_only=True
    )
    application_url = serializers.ModelSerializer.serializer_url_field(
        view_name='application_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Application
        fields = ('id', 'job_title', 'company_name', 'owner', 'application_url', 'date_applied', 'date_logged', 'notes', 'status', 'contacts')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    application = serializers.HyperlinkedRelatedField(
        view_name='application_detail', read_only=True)
    
    application_id = serializers.PrimaryKeyRelatedField(
        queryset=Application.objects.all(), source='application')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ('id', 'application', 'application_id', 'title', 'name', 'phone_number', 'email', 'notes', 'owner')