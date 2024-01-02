from django import forms
from .models import BlogPost

# create forms for contact page
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'post_image', 'slug','content']
        
    # validation on the fields
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title).exclude(id=self.instance.id)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title is already taken, please try another.")
        return title