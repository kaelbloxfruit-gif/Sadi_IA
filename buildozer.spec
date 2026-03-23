[app]
title = SADI AI
package.name = sadi_ai
package.domain = org.kael.sadi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,chardet,idna

# (Ajustes de Android)
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# (Permisos vitales para una IA/Asistente)
android.permissions = INTERNET, RECORD_AUDIO

[buildozer]
log_level = 2
warn_on_root = 1
