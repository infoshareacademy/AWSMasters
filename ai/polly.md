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


client = boto3.client('polly')

response = client.synthesize_speech(
    OutputFormat='mp3',
    Text=content,
    VoiceId='Maja'
)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(".", "audio.mp3")
        print(output);
        with open(output, "wb") as audioFile:
            audioFile.write(stream.read())
```