from django.forms import ModelForm
from .models import User,Product,Review

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

