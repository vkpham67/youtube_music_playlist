'''
pip install pillow
pip install opencv-python
'''
import pyautogui as pag

def playartist():
    artist = input(str('Choose an artist: '))

    # Open Chrome
    pag.press('win')
    pag.typewrite('chrome')
    pag.press('enter')

    # Open Youtube
    chrome_http = pag.locateCenterOnScreen('./image_ref/chrome_http.png', confidence=.7)
    while chrome_http == None:
        chrome_http = pag.locateCenterOnScreen('./image_ref/chrome_http.png', confidence=.7)
        print('Awaiting Image')

    pag.moveTo(chrome_http)
    pag.click()
    pag.typewrite('youtube.com')
    pag.press('enter')

    # Go to artist
    youtube_search = pag.locateCenterOnScreen('./image_ref/youtube_search.png', confidence=.8)
    while youtube_search == None:
        youtube_search = pag.locateCenterOnScreen('./image_ref/youtube_search.png', confidence=.8)
        print('Awaiting U2')

    pag.moveTo(youtube_search)
    pag.click()
    pag.typewrite(artist)
    pag.press('enter')

    # Play Playlist
    youtube_playlist = pag.locateCenterOnScreen('./image_ref/youtube_playlist.png', confidence=.7)
    while youtube_playlist == None:
        youtube_playlist = pag.locateCenterOnScreen('./image_ref/youtube_playlist.png', confidence=.7)
        print('Awaiting Playlist')

    pag.moveTo(youtube_playlist)
    pag.click()

playartist()