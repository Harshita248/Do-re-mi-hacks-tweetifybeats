import simpleaudio as sa
path='./audio/'
pianoNotes = {
    "1": path + "C.wav",
    "2": path + "D.wav",
    "3": path + "E.wav",
    "4": path + "F.wav",
    "5": path + "G.wav",
    "6": path + "A.wav",
    "7": path + "B.wav",
    "8": path + "C1.wav"
}

wave_obj = sa.WaveObject.from_wave_file(pianoNotes.get('1'))
play_obj = wave_obj.play()
play_obj.wait_done()