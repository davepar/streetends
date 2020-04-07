from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    maintained_by = models.CharField(max_length=100)
    comments = models.TextField()
    city_district = models.CharField(max_length=100)
    image_url = models.URLField()
    material = models.CharField(max_length=100)
    current_status = models.CharField(max_length=100)
    maintenance_agreement = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def create_entry(file_values):
        simple_key_mapping = [
            'maintained_by', 'category', 'comments', 'material', 'current_status',
            'maintenance_agreement',
        ]
        key_mapping = {
            'PRIMARYDISTRICTCD': 'city_district',
            'SHORELINE_IMAGE': 'image_url',
        }
        for simple in simple_key_mapping:
            key_mapping[simple.upper()] = simple
        fields = {}
        for file_key, field_key in key_mapping.items():
            fields[field_key] = file_values[file_key]
        fields['name'], description = file_values['UNITDESC'].split('\r', 1)
        fields['description'] = description.strip(' |')
        new_entry = Park(**fields)
        new_entry.save()
