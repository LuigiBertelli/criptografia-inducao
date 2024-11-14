import eel
import cryptHandler



eel.init('web', allowed_extensions=['.js', '.html', '.css'])

@eel.expose
def encrypt(txt):
    return cryptHandler.encrypt(txt)

@eel.expose
def isDecriptable(txt):
    return cryptHandler.isDecriptable(txt)

@eel.expose
def decrypt(txt):
    return cryptHandler.decrypt(txt)
    
eel.start('main.html', mode='edge', size=(600, 600), port=0)