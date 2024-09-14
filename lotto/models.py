from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
            guess = origin[:6] # [10, 21, 36, 2, 15, 23]
            guess.sort() # [2, 10, 15, 21, 23, 36]
            self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
            # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨
