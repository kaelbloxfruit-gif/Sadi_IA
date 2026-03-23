[app]

# Información de la aplicación
title = SADI - Sistema de Inteligencia & Ciberseguridad
package.name = sadi
package.domain = org.sadi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Versión
version = 1.0.0
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,charset-normalizer,idna

# Optimizaciones de compilación
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = 

# Optimización de recursos
android.archs = arm64-v8a
android.allow_backup = True
android.meta_data = 

# Icono y splash (opcional)
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Optimizar memoria y rendimiento
android.entrypoint = org.renpy.android.PythonActivity
android.bootstrap = sdl2
android.features = android.hardware.usb.host

[buildozer]

# Logs
log_level = 2
warn_on_root = 1

# Compilación optimizada
android.release_artifact = apk
android.accept_sdk_license = True
android.skip_update = False

# Opciones de compilación para mejor rendimiento
android.gradle_options = org.gradle.jvmargs=-Xmx2048m
android.java_modules = java.base,java.logging