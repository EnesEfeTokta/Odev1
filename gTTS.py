from gtts import gTTS 
import os
text = "Merhaba" # Söylemesi istediğimiz şeyi yazıyoruz.
language = 'tr' # Ana dili yazıyoruz (Kısaltmalı).
speech = gTTS(text = text, lang = language, slow = False) # Konuşmayı tanımlıyoruz.
speech.save("text.mp3") # Tek seferliğine kayıt edecek dosyanın uzantısı ile birlikte isim veriyoruz.
os.system("start text.mp3") # Ses dosyasını çalıştırıyor.