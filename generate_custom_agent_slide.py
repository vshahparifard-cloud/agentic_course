from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))
hti.output_path = 'slides/session_1_custom'
os.makedirs('slides/session_1_custom', exist_ok=True)

css = '''
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    width: 1920px;
    height: 1080px;
    background: #08090f;
    color: #f8fafc;
    font-family: 'Vazirmatn', sans-serif;
    padding: 50px 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(0, 255, 135, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(0, 242, 254, 0.12) 0%, transparent 45%);
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 20px;
}
.badge-tag {
    background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
    color: #08090f;
    padding: 8px 24px;
    border-radius: 30px;
    font-weight: 800;
    font-size: 1.2rem;
    box-shadow: 0 0 20px rgba(0, 255, 135, 0.4);
}
.title-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.main-title {
    font-size: 2.5rem;
    font-weight: 900;
    color: #ffffff;
}
.sub-title {
    font-size: 1.3rem;
    color: #94a3b8;
}
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
    margin: 28px 0;
}
.slide-card {
    background: rgba(18, 20, 32, 0.85);
    border: 1px solid rgba(0, 255, 135, 0.3);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 18px;
}
.icon-box {
    width: 60px;
    height: 60px;
    background: rgba(0, 255, 135, 0.12);
    border: 1px solid rgba(0, 255, 135, 0.3);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #00ff87;
    font-size: 1.8rem;
}
.card-h2 {
    font-size: 1.5rem;
    font-weight: 800;
    color: #ffffff;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 10px;
}
.card-p {
    font-size: 1.15rem;
    color: #cbd5e1;
    line-height: 1.75;
}
.highlight-box {
    background: rgba(0, 242, 254, 0.08);
    border-right: 4px solid #00f2fe;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 1.05rem;
    color: #60efff;
}
.footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 18px;
    color: #64748b;
    font-size: 1.1rem;
}
'''

slide_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">توسعه سیستم‌های ایجنتیک سفارشی (Custom Agentic Systems)</h1>
        <p class="sub-title">ساخت ایجنت‌های تخصصی با فریم‌ورک‌های LangGraph, AutoGen و CrewAI</p>
    </div>
    <span class="badge-tag">پیش‌نمایش نقشه راه | اسلاید سفارشی</span>
</div>

<div class="cards-grid">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-cubes"></i></div>
        <h2 class="card-h2">چرا سیستم سفارشی؟</h2>
        <p class="card-p">امکان کدنویسی منطق‌های پیچیده کسب‌وکار، کنترل ۱۰۰٪ روی چرخه تصمیم‌گیری و اتصال ایجنت به دیتابیس‌های سازمانی (SQL & Vector DBs).</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-diagram-project"></i></div>
        <h2 class="card-h2">فریم‌ورک‌های برتر توسعه</h2>
        <p class="card-p"><b>LangGraph & LangChain:</b> گراف‌های تعاملی و مدیریت State.<br><b>CrewAI & AutoGen:</b> معماری‌های نقش‌محور (Role-based) و چندعاملی.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-graduation-cap"></i></div>
        <h2 class="card-h2">نقشه راه دوره (Session 04)</h2>
        <p class="card-p">در <b>جلسه چهارم</b>، ساخت و ارکستراسیون کامل این سیستم‌های چندایجنتی سفارشی به صورت ۱۰۰٪ عملی آموزش داده خواهد شد.</p>
        <div class="highlight-box">
            <i class="fa-solid fa-lightbulb"></i> کارگاه عملی اصلی در Session 04 برگزار می‌شود.
        </div>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01 ➔ Session 04 Preview</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

hti.screenshot(html_str=slide_html, save_as='slide_1.png')

print("Custom Agentic Systems slide generated successfully!")
