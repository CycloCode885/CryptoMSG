from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
import cryptocode



Builder.load_file('mainstruct.kv')




class MyLayout(TabbedPanel):


    def copyto(instance):
        Clipboard.copy(instance.ids.encmsg.text)

    def pastefrom(instance):
        instance.ids.decmsg.text = Clipboard.paste()

    def Encrypt(instance):

        if instance.ids.keyenc.text:
            if instance.ids.keyenc.text == 'INSERT KEY!':
                return
            try:
                t2enc = instance.ids.encmsg.text
                key = instance.ids.keyenc.text
                encrypted = cryptocode.encrypt(t2enc,key)
                instance.ids.encmsg.text = encrypted
            except:
                pass
        else:
            instance.ids.keyenc.text = 'INSERT KEY!'

    def Decrypt(instance):

        if instance.ids.keydec.text:
            if instance.ids.keydec.text == '!INVALID KEY!':
                return
            try:
                t2dec = instance.ids.decmsg.text
                key = instance.ids.keydec.text
                decrypted = cryptocode.decrypt(t2dec,key)
                instance.ids.decmsg.text = decrypted
            except:
                pass
        else:
            instance.ids.keydec.text = '!INVALID KEY!'


class CryptoMSG(App):
    def build(self):

        return MyLayout()

if __name__ == '__main__':
    CryptoMSG().run()
