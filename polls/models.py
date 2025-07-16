from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #Cái choices này giống như enum
    #khai báo kiểu constraint
    # Kid = 'kid'
    # Young = 'young'
    # idk = 'idk'
    # cái bên dưới đổi "kid" -> Kid
    age_range = [
        ("kid", "0-14"),
        ("young", "15-20"),
        ("idk", "21-999"),
    ]
    age = models.CharField(max_length=5, choices=age_range, default='kid') # nếu xài constraint thì có thể default = Kid
    #Với choices truy vấn thì bth nó sẽ hiện cái key
    #Muốn hiện value -> x.get_[field choices]_display()
    
    #khai báo kiểu enumration class
    difficulties = models.TextChoices("Difficulty", "Easy Normal Hảd")
    difficulty = models.CharField(blank=True, choices=difficulties, max_length=10 )
    # Khởi tạo enable blank không default thì sẽ để là '' -> server crash -> chỉnh lại nằm trong enum xong restart server thì bình thường -> restart server xong chỉnh lại '' thì lại chạy bình thường (?)
    # cái null và blank hơi khó hiểu, cần case thực tế cho dễ hiểu hơn

    #Group choice, cái bên ngoài cùng chỉ dán nhãn chứ vẫn xem bên trong là chủ yếu (trừ group single other)
    question_type_choices=[
        ("Quiz",(("MC", "Multi-choice"), ("SC", "Single-choice"))),
        ("Text",(("FT", "Filling-text"), ("WA", "Write-answer"))),
        ("Other", "Other")
    ]
    question_type = models.CharField(choices=question_type_choices, max_length=20, default="SC")
    #Xem trong trang admin hoặc shell dễ hình dung hơn

    #define cách model thể hiện trong table (__str__ giống toString), cái này là cách 1, cách 2 nhìn trong admin.py
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #khóa ngoại, tự động thiết lập relationship kể cả khi không khai báo 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #KHi này bên question có thể lấy ds choice bằng syntax [tên model]_set (vis dụ question.choice_set.?)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)