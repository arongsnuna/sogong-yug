from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "옷 별명을 입력해주세요",
            'rows': 20
        }
        # 자동으로 생성되는 html 태그들에 특정 클래스(부트스트랩)를 설정해주기 위해선 위처럼 widget을 사용해줘야 함
        # widget을 사용하기 위해서 생성자를 만들어줌
