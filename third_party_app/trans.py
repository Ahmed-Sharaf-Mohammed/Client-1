from mtranslate import translate
import polib
import os

def translate_po_file(po_file_path, target_language):
    # Load the .po file
    po = polib.pofile(po_file_path)

    # Translate the messages in the .po file
    for entry in po:
        if entry.msgstr:
            translated_text = translate(entry.msgstr, to_language=target_language)
            entry.msgstr = translated_text

    # Save the translated .po file
    po.save()
