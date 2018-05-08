from io import BytesIO
from django import forms
from django.conf import settings
import cognitive_face as CF


class VerifyForm(forms.Form):
    photo1 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='첫번째 사진')
    photo2 = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='두번째 사진')

    def verify(self):
        attributes = 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'

        self.photo1_data = self.cleaned_data['photo1'].read()
        self.photo2_data = self.cleaned_data['photo2'].read()

        ret1 = CF.face.detect(BytesIO(self.photo1_data), face_id=True, landmarks=False, attributes=attributes)
        ret2 = CF.face.detect(BytesIO(self.photo2_data), face_id=True, landmarks=False, attributes=attributes)
        ret_verify = CF.face.verify(ret1[0]['faceId'], ret2[0]['faceId'])

        self.result = {
            'ret1': ret1,
            'ret2': ret2,
            'ret_verify': ret_verify,
        }

        return self.result

