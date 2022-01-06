from django.db import models


class products(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Cost_per_item=models.BigIntegerField()
    stock_quantity=models.BigIntegerField()
    volume=models.BigIntegerField()

    def get_Volume(self):
        Volume=self.Cost_per_item * self.stock_quantity
        return Volume

    def save(self,*args,**kwargs):
        self.Volume=self.get_Volume()
        super(products,self).save(*args,**kwargs)

    def __str__(self):
        return self.Name