from rest_framework import serializers

from drf_problems import PROBLEM_CODE_CHOICES


class ErrorDescriptionSerializer(serializers.Serializer):
    status = serializers.IntegerField(min_value=300, max_value=500)
    code = serializers.ChoiceField(choices=PROBLEM_CODE_CHOICES)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()

    class Meta:
        fields = ('status', 'code', 'title', 'description')

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if instance:
            self.instance = {
                'status': instance.status_code,
                'code': getattr(instance, 'code', instance.default_code),
                'title': getattr(instance, 'title', instance.default_detail),
                'description': getattr(instance, 'description', 'Not Provided.')
            }
