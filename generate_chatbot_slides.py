from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))
hti.output_path = 'slides/session_1_chatbot'
os.makedirs('slides/session_1_chatbot', exist_ok=True)

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
        radial-gradient(circle at 10% 20%, rgba(249, 212, 35, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(0, 242, 254, 0.12) 0%, transparent 45%);
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 24px;
}
.badge-tag {
    background: linear-gradient(135deg, #f9d423 0%, #ff4e50 100%);
    color: #08090f;
    padding: 8px 24px;
    border-radius: 30px;
    font-weight: 800;
    font-size: 1.25rem;
    box-shadow: 0 0 20px rgba(249, 212, 35, 0.4);
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
    border: 1px solid rgba(249, 212, 35, 0.3);
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
    background: rgba(249, 212, 35, 0.15);
    border: 1px solid rgba(249, 212, 35, 0.4);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #f9d423;
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
        <h1 class="main-title">معماری و قابلیت‌های چت‌بات‌های پیشرفته (Modern Chatbots)</h1>
        <p class="sub-title">مکانیزم‌های داخلی و فناوری‌های بکاررفته در Claude, Gemini و ChatGPT</p>
    </div>
    <span class="badge-tag">بخش چت‌بات‌ها | اسلاید ۱</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-users-gears"></i></div>
        <h2 class="card-h2">ارکستراسیون چندایجنتی داخلی</h2>
        <p class="card-p">چت‌بات‌های پیشرفته پشت صحنه از ایجنت‌های داخلی (مسیریاب، جستجوگر و سنتزکننده) برای تجزیه پرامپت‌ها استفاده می‌کنند.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
        <h2 class="card-h2">جستجوی زنده وب & RAG داخلی</h2>
        <p class="card-p">فراخوانی موتورهای جستجو (Google Search) و بازیابی هوشمند داده‌ها (RAG) برای پاسخگویی به اخبار و اطلاعات لحظه‌ای.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-laptop-code"></i></div>
        <h2 class="card-h2">محیط Sandbox & Vision</h2>
        <p class="card-p">اجرای کدهای پایتون در محیط ایزوله، تحلیل مستقیم تصاویر و تولید خروجی‌های تعاملی بصری (مانند Claude Artifacts).</p>
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
        <h1 class="main-title">مقایسه تفصیلی: چت‌بات‌های وب در برابر ایجنت‌های خودمختار</h1>
        <p class="sub-title">مرز تمایز رابط‌های چت‌محور (Chat UI) با سیستم‌های عملیاتی خودمختار (Agentic)</p>
    </div>
    <span class="badge-tag">بخش چت‌بات‌ها | اسلاید ۲</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-comment-dots"></i></div>
        <h2 class="card-h2">چت‌بات‌های وب (Chat UI)</h2>
        <p class="card-p">پاسخگویی به صورت <b>منفعل (Passive)</b> به هر پرامپت، محدود به مرورگر و Sandbox ایزوله، بدون دسترسی مستقیم به فایل‌سیستم محلی.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-gears"></i></div>
        <h2 class="card-h2">ایجنت‌های خودمختار (Agents)</h2>
        <p class="card-p">اقدام <b>فعالانه (Proactive)</b> بر اساس هدف، دسترسی بومی به فایل سیستم، ترمینال و Git (مانند Claude Code & agy CLI) با خوداصلاحی.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-code-compare"></i></div>
        <h2 class="card-h2">تفاوت در چرخه بازخورد</h2>
        <p class="card-p"><b>چت‌بات:</b> نیازمند هدایت کاربر به ازای هر گام.<br><b>ایجنت:</b> اجرای خودمختار تسک، تست کد و رفع خودکار باگ تا تایید نهایی.</p>
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

print("2 Chatbot architecture slides generated successfully!")
