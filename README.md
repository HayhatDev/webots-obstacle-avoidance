# Obstacle Avoidance Robot

A robot that avoids obstacles using 8 IR sensors, built with Webots and Python.

## Demo
https://youtu.be/igUDx1FU_BU

## How It Works
- The robot reads 8 distance sensors continuously
- If an obstacle is detected, it turns away
- If stuck, it reverses and rotates 180 degrees

## Run It Yourself
1. Clone this repo
2. Open the .wbt file in Webots
3. Select the controller and run (obstacle_avoid.py)

## Author
Hayhat Tahir

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Obstacle Avoidance Robot 🤖

روبوت يتجنب العوائق باستخدام **Webots** و **Python**.

## الميزات
- ✅ 8 حساسات مسافة (IR sensors)
- ✅ تجنب العوائق من الأمام والخلف والجوانب
- ✅ اكتشاف العالق والخروج من الزوايا الضيقة
- ✅ طباعة قراءات الحساسات لحظة بلحظة

## التقنيات المستخدمة
- Webots R2025a
- Python
- Webots Controller API

## كيفية التشغيل
1. افتح ملف `.wbt` في Webots
2. اختر `obstacle_avoid.py` كـ controller للروبوت
3. اضغط Run ▶️

## فيديو توضيحي
https://youtu.be/igUDx1FU_BU

## المستقبل
- إضافة منطق اتباع الخط (Line Follower)
- التحكم عن بعد عبر الويب
