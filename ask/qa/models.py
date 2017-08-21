class User(models.Model):
    name = models.CharField(max_length=24)
    friends = models.ManyToManyField('User')
    groups = models.ManyToManyField('Group')

class Group(models.Model):
    name = models.CharField(max_length=100)
    moderator = models.ForeignKey('User')
    

    Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
