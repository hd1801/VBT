#Extracts a new word daily from dictionary.com
from win10toast import ToastNotifier #will be used to pop notification
import requests
import json
from fetch_def import get_meaning
from fetch_def import get_wordtype
from fetch_def import get_prononciation
from fetch_def import get_WoD
w=get_WoD()
WoD=w   + '''meaning : '''+ get_meaning(w)
toaster = ToastNotifier()
#toaster.show_toast("Word of the day",WoD, icon_path=None, duration=10, callback_on_click=lambda: print("Clicked!"))
toaster.show_toast("Word of the day",WoD, icon_path=None, duration=10)
