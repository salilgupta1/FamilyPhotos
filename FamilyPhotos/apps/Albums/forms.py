from django import forms
from models import Album

class CreateAlbumForm(forms.ModelForm):
	title = forms.CharField(error_messages={'required':'You need a title'}, widget=forms.TextInput(attrs={'class':'col-md-6'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'col-md-8'}))
	photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'col-md-4'}))

	class Meta:
		model=Album
		fields=['title','description','photos']
	def __init__(self,*args,**kwargs):
		super(CreateAlbumForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})