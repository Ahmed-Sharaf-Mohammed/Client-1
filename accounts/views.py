from django.shortcuts import render
import subprocess, os, mtranslate,polib
from third_party_app.views import make_messages, translate_po_file, compile_translations


def home(request):
    return render(request, 'accounts/index.html')