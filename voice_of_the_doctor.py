import os
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Converts text to speech using gTTS and saves it as an MP3 file.
    Returns the path to the saved MP3 file.
    """
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    return output_filepath
