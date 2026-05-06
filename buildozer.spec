[app]
title = RAMSaver Pro
package.name = ramsaverpro
# In-update ko ang domain sa pangalan mo
package.domain = org.renantefullo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Mahalaga: Nilagyan ko ng version ang Python para hindi mag-error sa Gradle
requirements = python3==3.11.2,kivy,psutil

orientation = portrait
fullscreen = 0

# Android specific settings
android.api = 33
android.minapi = 21
# Gamitin ang NDK 25b para sa stability ng psutil
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Para sa mas malinaw na error logs kung sakali
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1