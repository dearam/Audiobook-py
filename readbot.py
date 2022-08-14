import pyttsx3
import PyPDF2
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time
from pygame import mixer
from pydub import AudioSegment
import os




url="https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/994863fc-12c5-48dd-9a7b-7ea038e7d0fc"
apikey='phLt1SvhOqqUVHXtdDLKk12KVb1CHMTjTRccVdvfdfOe'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

book =open("computer.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
for i in range(10,13):
    page=pdfReader.getPage(i)
    text=""
    text+=page.extract_text()
    print(text)
    print(len(text))
    with open('./speech{num}.mp3'.format(num=i), 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)

sound1 = AudioSegment.from_file("speech{num}.mp3".format(num=10), format="mp3")
sound2 = AudioSegment.from_file("speech{num}.mp3".format(num=11), format="mp3")
sound3 = AudioSegment.from_file("speech{num}.mp3".format(num=12), format="mp3")
louder=sound1+6
combined=sound1+sound2+sound3
file_handle=combined.export("output.mp3",format="mp3")
for i in range(10,13):
    os.remove("speech{num}.mp3".format(num=i))

mixer.init()
mixer.music.load("output.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

# # sound1 6 dB louder
# louder = sound1 + 6


# # sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
# combined = sound1 + sound2

# # simple export
# file_handle = combined.export("/path/to/output.mp3", format="mp3")


















# book =open("computer.pdf",'rb')
# pdfReader=PyPDF2.PdfFileReader(book)
# pages=pdfReader.numPages
# print(pages)
# speaker=pyttsx3.init()
# print(speaker.getProperty('rate'))
# speaker.setProperty('rate',125)
# speaker.setProperty('voice', 'english_rp+f3')
# # for num in range(8,253):
# #     page = pdfReader.getPage(num)
# #     text = page.extractText()
# #     speaker.say(text)
# #     speaker.runAndWait() 
# page=pdfReader.getPage(10)
# text=""
# text+=page.extract_text()
# speaker.say(text)
# speaker.runAndWait()
# print(page)


