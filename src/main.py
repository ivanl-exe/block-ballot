import eel

WEB_ROOT = 'web'
WEB_FILENAME = 'index.html'

if __name__ == '__main__':
    eel.init(WEB_ROOT)
    eel.start(WEB_FILENAME, port = 8000)