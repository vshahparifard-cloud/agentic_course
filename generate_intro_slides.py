from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))
hti.output_path = 'slides/session_1_intro'
os.makedirs('slides/session_1_intro', exist_ok=True)

css = '''
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 1920px;
    height: 1080px;
    background: #08090f;
    color: #f8fafc;
    font-family: 'Vazirmatn', sans-serif;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-image: 
        radial-gradient(circle at 15% 20%, rgba(0, 242, 254, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 80%, rgba(176, 38, 255, 0.15) 0%, transparent 45%);
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 24px;
}
.badge-tag {
    background: linear-gradient(135deg, #b026ff 0%, #7f00ff 100%);
    color: #ffffff;
    padding: 8px 24px;
    border-radius: 30px;
    font-weight: 800;
    font-size: 1.25rem;
    box-shadow: 0 0 20px rgba(176, 38, 255, 0.4);
}
.title-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.main-title {
    font-size: 2.5rem;
    font-weight: 900;
    color: #ffffff;
}
.sub-title {
    font-size: 1.35rem;
    color: #94a3b8;
}
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin: 36px 0;
}
.slide-card {
    background: rgba(18, 20, 32, 0.85);
    border: 1px solid rgba(176, 38, 255, 0.3);
    border-radius: 20px;
    padding: 36px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.icon-box {
    width: 64px;
    height: 64px;
    background: rgba(176, 38, 255, 0.15);
    border: 1px solid rgba(176, 38, 255, 0.4);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #b026ff;
    font-size: 1.8rem;
}
.card-h2 {
    font-size: 1.55rem;
    font-weight: 800;
    color: #ffffff;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 12px;
}
.card-p {
    font-size: 1.2rem;
    color: #cbd5e1;
    line-height: 1.8;
}
.footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 20px;
    color: #64748b;
    font-size: 1.15rem;
}
'''

slide1_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">مقدمه: ایجنت هوش مصنوعی (AI Agent) چیست؟</h1>
        <p class="sub-title">تعریف عامل خودمختار، تفاوت آن با چت‌بات‌های عادی و چرخه ادراک-استدلال-اقدام</p>
    </div>
    <span class="badge-tag">مقدمه دوره | اسلاید ۱</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-robot"></i></div>
        <h2 class="card-h2">تعریف ایجنت خودمختار</h2>
        <p class="card-p">سیستم هوشمندی که دارای هدف (Goal) است و به صورت مستقل برای رسیدن به آن برنامه‌ریزی، تصمیم‌گیری و اقدام می‌کند.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-comments"></i></div>
        <h2 class="card-h2">چت‌بات عادی vs ایجنت</h2>
        <p class="card-p">چت‌بات‌های متنی فقط به پرامپت پاسخ متنی می‌دهند؛ اما ایجنت مجهز به ابزارها، قابلیت دسترسی به فایل و انجام عملیات است.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-rotate"></i></div>
        <h2 class="card-h2">چرخه ادراک - استدلال - اقدام</h2>
        <p class="card-p"><b>Perception:</b> دریافت ورودی پروژه<br><b>Reasoning:</b> تحلیل و برنامه‌ریزی با LLM<br><b>Action:</b> فراخوانی ابزارها و ویرایش کدها</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

slide2_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">مؤلفه‌ها و پارامترهای اصلی یک ایجنت (Agent Parameters)</h1>
        <p class="sub-title">بررسی مدل پایه (LLM Backbone)، تاریخ کات‌آف (Cutoff Date) و کانتکست سایز</p>
    </div>
    <span class="badge-tag">مقدمه دوره | اسلاید ۲</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-microchip"></i></div>
        <h2 class="card-h2">موتور اصلی (LLM Backbone)</h2>
        <p class="card-p">مغز هوشمند ایجنت که بر روی داده‌های عظیم متنی و کدهای برنامه آموزش دیده است (مانند Gemini 3.1 Pro یا Claude 4.8).</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-calendar-xmark"></i></div>
        <h2 class="card-h2">تاریخ کات‌آف (Knowledge Cutoff)</h2>
        <p class="card-p">حد زمانی دانش مدل؛ ایجنت‌ها با اتصال به وب‌سرچ و ابزارهای زنده، محدودیت کات‌آف زمانی را به طور کامل برطرف می‌کنند.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-memory"></i></div>
        <h2 class="card-h2">ظرفیت کانتکست سایز</h2>
        <p class="card-p">حجم داده قابل پردازش در یک نشست (Context Window)، که ظرفیت حافظه کوتاه‌مدت و توانایی بررسی پروژه‌های بزرگ را تعیین می‌کند.</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

slide3_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">ابزارها و اتصال به دنیای واقعی (Tools & Grounding)</h1>
        <p class="sub-title">تبدیل مدل زبانی به ایجنت فعال با ابزارهای سیستم‌عاملی و Native Grounding</p>
    </div>
    <span class="badge-tag">مقدمه دوره | اسلاید ۳</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-wrench"></i></div>
        <h2 class="card-h2">فراخوانی ابزارها (Tool Calling)</h2>
        <p class="card-p">قابلیت ایجنت در صدور دستور اجرای توابع، فراخوانی APIهای خارجی و تعامل با دیتابیس‌ها برای دستیابی به اهداف.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-globe"></i></div>
        <h2 class="card-h2">اتصال زنده (Native Grounding)</h2>
        <p class="card-p">دسترسی بومی به فایل‌سیستم پروژه، جستجوی زنده در اینترنت، و استخراج دقیق اطلاعات بروز بدون واسطه.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-terminal"></i></div>
        <h2 class="card-h2">اجرای خودکار تسک‌ها</h2>
        <p class="card-p">اجرای دستورات ترمینال، تست کدهای نوشته‌شده، دیباگ خودکار و اصلاح باگ‌ها تا زمان رسیدن به نتیجه مطلوب.</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

hti.screenshot(html_str=slide1_html, save_as='slide_1.png')
hti.screenshot(html_str=slide2_html, save_as='slide_2.png')
hti.screenshot(html_str=slide3_html, save_as='slide_3.png')

print("3 Intro slides generated successfully!")
