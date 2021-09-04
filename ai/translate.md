```
import boto3
import os
from contextlib import closing

content = " \
W Szczebrzeszynie chrząszcz brzmi w trzcinie \
I Szczebrzeszyn z tego słynie. \
Wół go pyta: ”Panie chrząszczu, \
Po co pan tak brzęczy w gąszczu?” \
”Jak to – po co? To jest praca, \
Każda praca się opłaca.” \
\
”A cóż za to Pan dostaje?” \
”Też pytanie! Wszystkie gaje, \
Wszystkie trzciny po wsze czasy, \
Łąki, pola oraz lasy, \
Nawet rzeczki, nawet zdroje, \
Wszystko to jest właśnie moje!” \
– Jan Brzechwa ”CHRZĄSZCZ” \
" \


client = boto3.client('translate')

response = client.translate_text(
    Text=content,
    SourceLanguageCode='pl',
    TargetLanguageCode='en'
)


print(response["TranslatedText"]);
```