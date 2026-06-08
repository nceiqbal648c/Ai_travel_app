[app]
title = AI Travel Anywhere
package.name = aitravelanywhere
package.domain = org.ia
source.dir = .
source.include_exts = py,png,jpg,jpeg,html,css,js
version = 0.0.7

# প্রয়োজনীয় রিকোয়ারমেন্টস (যা যা লাইব্রেরি লাগবে)
requirements = python3,flask,yt-dlp,requests,jinja2,werkzeug,itsdangerous,click

orientation = portrait
fullscreen = 1

# অ্যান্ড্রয়েড স্পেসিফিক পারমিশন (যাতে ফাইল ফোনে সেভ হতে পারে)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# অ্যান্ড্রয়েড আর্কিটেকচার সেটআপ
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
