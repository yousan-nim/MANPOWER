from django.db import models

class ManpowerData(models.Model):
    id = models.IntegerField(primary_key=True)
    Seed_RepDate = models.IntegerField()
    Seed_Year = models.IntegerField()
    Seeds_YearWeek = models.IntegerField()
    Seed_Varity = models.TextField() 
    Seed_RDCSD = models.TextField() 
    Seed_Stock2Sale = models.TextField() 
    Seed_Season = models.IntegerField() 
    Seed_Crop_Year = models.TextField() 
    
    def __str__(self): 
        return self._id
    
    
    
