# Rebuild the single-file deck

presentation.src.html is the editable source; presentation.html is the generated
self-contained build (fonts, images, Chart.js and both dashboard demos inlined).
After editing the source or anything under demo/, rebuild from the talk folder:

    python build/inline.py

Needs network once only if the Google font files are missing (they are fetched
from fonts.gstatic.com and embedded as base64).
