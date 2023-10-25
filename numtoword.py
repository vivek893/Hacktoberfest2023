# convert number into Words .
from num2words import num2words
def numtoword(number):
    # Most common usage.
    print(num2words(number))
    # Other variants, according to the type of article.
    print(num2words(number, to = 'ordinal'))
    print(num2words(number, to = 'ordinal_num'))
    print(num2words(number, to = 'year'))
    print(num2words(number, to = 'currency'))
    # Language Support.
    print(num2words(number, lang ='es'))
num=int(input("Enter a number:"))
numtoword(num)
