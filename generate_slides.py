from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))

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
        radial-gradient(circle at 10% 20%, rgba(127, 0, 255, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(0, 242, 254, 0.15) 0%, transparent 45%);
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 24px;
}
.badge-tag {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
    color: #08090f;
    padding: 8px 24px;
    border-radius: 30px;
    font-weight: 800;
    font-size: 1.25rem;
    box-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
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
    border: 1px solid rgba(0, 242, 254, 0.25);
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
    background: rgba(0, 242, 254, 0.12);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #00f2fe;
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
        <h1 class="main-title">محدودیت‌های کلیدی معماری تک‌عاملی (Single-Agent)</h1>
        <p class="sub-title">چرا یک ایجنت به تنهایی توانایی پاسخگویی به مأموریت‌های پیچیده نرم‌افزاری را ندارد؟</p>
    </div>
    <span class="badge-tag">اسلاید ۱ از ۳ (مباحث جدید)</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-box-archive"></i></div>
        <h2 class="card-h2">سقف محدود کانتکست سایز</h2>
        <p class="card-p">در پروژه‌های بزرگ و گفتگوهای طولانی، حافظه پر شده و خروجی مدل دچار خطای توهم (Hallucination) و افت شدید دقت در ردیابی کدها می‌شود.</p>
    </div>
    
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-brain"></i></div>
        <h2 class="card-h2">انباشت بار شناختی (Cognitive)</h2>
        <p class="card-p">واگذاری همزمان استدلال، برنامه‌ریزی، کدنویسی، ساخت تست و رفع باگ به یک عامل واحد، موجب تمرکززدایی و اتخاذ تصمیمات اشتباه می‌شود.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-link-slash"></i></div>
        <h2 class="card-h2">خطاهای زنجیره‌ای بدون بازخورد</h2>
        <p class="card-p">به دلیل عدم وجود ایجنت ناظر مجزا، اولین خطای محاسباتی در تک‌ایجنت تثبیت شده و در مراحل بعدی توسعه تشدید و منتشر می‌گردد.</p>
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
        <h1 class="main-title">ضرورت گذار به معماری‌های چندایجنتی (Multi-Agent)</h1>
        <p class="sub-title">تفکیک مسئولیت‌ها، ایزوله‌سازی کانتکست و ارکستراسیون هوشمند عامل‌ها</p>
    </div>
    <span class="badge-tag">اسلاید ۲ از ۳ (مباحث جدید)</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-sitemap"></i></div>
        <h2 class="card-h2">تفکیک تخصصی مسئولیت‌ها</h2>
        <p class="card-p">تقسیم تسک‌های بزرگ به ایجنت‌های متخصص (Planner, Coder, Evaluator, Reviewer) جهت ارتقای خروجی تا بالاترین سطح کیفیت.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-layer-group"></i></div>
        <h2 class="card-h2">ایزوله‌سازی State و حافظه</h2>
        <p class="card-p">ارائه کانتکست اختصاصی به هر ایجنت، جلوگیری از آلودگی حافظه اصلی، کاهش مصرف توکن و حفظ تمرکز روی وظیفه محوله.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-user-shield"></i></div>
        <h2 class="card-h2">معماری ناظر و کارگزار</h2>
        <p class="card-p">ایجاد حلقه بازخورد (Feedback Loop) بین Supervisor و Worker جهت ارزیابی، اصلاح خودکار و تایید نهایی خروجی کدها.</p>
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
        <h1 class="main-title">تکامل پلتفرم‌های ایجنتیک: از چت‌بات تا دسترسی بومی به فایل‌سیستم</h1>
        <p class="sub-title">بررسی نسل جدید ایجنت‌های توسعه با دسترسی به محیط اجرای سیستم‌عامل</p>
    </div>
    <span class="badge-tag">اسلاید ۳ از ۳ (مباحث جدید)</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-comments"></i></div>
        <h2 class="card-h2">نسل اول: چت‌بات‌ها و APIها</h2>
        <p class="card-p">تعامل محدود متنی، عدم دسترسی به فایل‌سیستم، کپی‌پیست دستی کدها و ناتوانی در اجرای دستورات سیستم‌عامل.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-terminal"></i></div>
        <h2 class="card-h2">نسل دوم: ایجنت‌های بومی سیستم‌عامل</h2>
        <p class="card-p"><b>Claude Code (روی macOS) & OpenAI Codex:</b> اجرای خودکار دستورات ترمینال، دسترسی بومی به پروژه و مدیریت Git.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-gears"></i></div>
        <h2 class="card-h2">برنامه‌نویسی خودمختار (Agentic)</h2>
        <p class="card-p">اجرای کانتینرهای ایزوله داکر، نصب خودکار وابستگی‌ها، مانیتورینگ جریان فکری (Thought Tracing) و رفع باگ اتوماتیک.</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

os.makedirs('slides/session_1_new', exist_ok=True)
hti.output_path = 'slides/session_1_new'
hti.screenshot(html_str=slide1_html, save_as='slide_1.png')
hti.screenshot(html_str=slide2_html, save_as='slide_2.png')
hti.screenshot(html_str=slide3_html, save_as='slide_3.png')

print("3 New high-res slides generated successfully!")
