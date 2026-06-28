from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

@deconstructible
class MinWordsValidators(BaseValidator):
    message = 'минимум %(limit_value)d слов! Сейчас: %(show_value)d.'
    code = 'too_few_words'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x.split())

@deconstructible
class NoUpperCaseValidator(BaseValidator):
    message = 'поле не должно содержать больше 1 заглавной буквы'
    code = 'no_upper_case'

    def clean(self, x):
        return sum(1 for c in x if c.isupper())
    def compare(self, a, b):
        return a > b
