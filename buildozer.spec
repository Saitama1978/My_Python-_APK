[app]
title = RAMSaver Pro
package.name = ramsaverpro
package.domain = org.renante
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,psutil

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# (Opsyonal) Icon at Presplash - palitan kung may file ka na
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

android.api = 33
android.minapi = 21
android.accept_sdk_license = True
log_level = 2