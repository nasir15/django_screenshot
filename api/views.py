import random
import pyautogui
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from PIL import Image

def home(request):
   if request.method == "POST":
      ss = pyautogui.screenshot()
      img_name = f'myimg{random.randint(1000,9999)}.png'
      ss.save(settings.MEDIA_ROOT/img_name)
      messages.success(request,'screenshot has been taken')

    
      image_1 = Image.open(settings.MEDIA_ROOT/img_name)
      im_1 = image_1.convert('RGB')
      pdf_name = f'mypdf{random.randint(1000,9999)}.pdf'
      im_1.save(settings.MEDIA_ROOT/pdf_name)
    #   os.remove(screenshot_path)

      return render(request,'index.html',{'img':img_name})
   return render(request,'index.html')
