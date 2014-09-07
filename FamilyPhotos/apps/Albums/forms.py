from django import forms
from models import Album

class CreateAlbumForm(forms.ModelForm):
	title = forms.CharField(error_messages={'required':'You need a title'})
	description = forms.CharField()
	photos = forms.FileField()

	class Meta:
		model=Album
		fields=['title','description','photos']
	def __init__(self,*args,**kwargs):
		super(CreateAlbumForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})