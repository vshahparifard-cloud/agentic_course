from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))
hti.output_path = 'slides/session_1_compare'
os.makedirs('slides/session_1_compare', exist_ok=True)

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
        radial-gradient(circle at 15% 20%, rgba(0, 242, 254, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 85% 80%, rgba(127, 0, 255, 0.15) 0%, transparent 45%);
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 20px;
}
.badge-tag {
    background: linear-gradient(135deg, #00f2fe 0%, #b026ff 100%);
    color: #ffffff;
    padding: 8px 24px;
    border-radius: 30px;
    font-weight: 800;
    font-size: 1.2rem;
    box-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
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

/* Comparison Table Layout */
.table-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
    margin: 28px 0;
}
.col-card {
    background: rgba(18, 20, 32, 0.85);
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.col-card.col-api {
    border: 1px solid rgba(148, 163, 184, 0.3);
}
.col-card.col-chat {
    border: 1px solid rgba(249, 212, 35, 0.4);
}
.col-card.col-agent {
    border: 2px solid #00f2fe;
    box-shadow: 0 0 25px rgba(0, 242, 254, 0.25);
    background: rgba(18, 20, 32, 0.95);
}
.col-header {
    display: flex;
    align-items: center;
    gap: 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 16px;
}
.col-icon {
    font-size: 1.8rem;
}
.col-title {
    font-size: 1.5rem;
    font-weight: 800;
    color: #fff;
}
.feature-list {
    display: flex;
    flex-direction: column;
    gap: 14px;
}
.feature-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.feat-label {
    font-size: 0.95rem;
    color: #94a3b8;
    font-weight: 600;
}
.feat-val {
    font-size: 1.15rem;
    color: #f8fafc;
    line-height: 1.5;
}
.feat-val.highlight {
    color: #00f2fe;
    font-weight: 700;
}
.feat-val.badge-green {
    color: #00ff87;
    font-weight: 700;
}

/* Loop Diagram Cards */
.cards-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin: 36px 0;
}
.step-card {
    background: rgba(18, 20, 32, 0.85);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-radius: 20px;
    padding: 36px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 18px;
    position: relative;
}
.step-num {
    position: absolute;
    top: -18px;
    right: 24px;
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
    color: #08090f;
    font-size: 1rem;
    font-weight: 900;
    padding: 4px 14px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.5);
}
.card-h2 {
    font-size: 1.55rem;
    font-weight: 800;
    color: #ffffff;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 12px;
    margin-top: 10px;
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
    padding-top: 18px;
    color: #64748b;
    font-size: 1.1rem;
}
'''

slide1_table_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">جدول مقایسه جامع ۳ لایه اصلی هوش مصنوعی</h1>
        <p class="sub-title">تفاوت ساختاری مدل‌های خام/API، چت‌بات‌های وب و پلتفرم‌های ایجنتیک خودمختار</p>
    </div>
    <span class="badge-tag">جدول مقایسه‌ای | اسلاید ۱</span>
</div>

<div class="table-grid">
    <!-- Col 1: API -->
    <div class="col-card col-api">
        <div class="col-header">
            <i class="fa-solid fa-code col-icon" style="color: #94a3b8;"></i>
            <h2 class="col-title">۱. مدل خام / API</h2>
        </div>
        <div class="feature-list">
            <div class="feature-item">
                <span class="feat-label">ماهیت ساختاری:</span>
                <span class="feat-val">موتور استدلال و احتمال متنی (Stateless LLM)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">نوع ورودی / تعامل:</span>
                <span class="feat-val">درخواست تک-مرحله‌ای (Prompt ➔ Response)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">دسترسی به فایل‌سیستم:</span>
                <span class="feat-val">ندارد (مگر با کدنویسی برنامه‌نویس)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">چرخه خوداصلاحی:</span>
                <span class="feat-val">ندارد</span>
            </div>
        </div>
    </div>

    <!-- Col 2: Chatbot -->
    <div class="col-card col-chat">
        <div class="col-header">
            <i class="fa-solid fa-comments col-icon" style="color: #f9d423;"></i>
            <h2 class="col-title">۲. چت‌بات وب</h2>
        </div>
        <div class="feature-list">
            <div class="feature-item">
                <span class="feat-label">ماهیت ساختاری:</span>
                <span class="feat-val">رابط متنی وب (Passive Chat UI) + ابزار محدود</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">نوع ورودی / تعامل:</span>
                <span class="feat-val">گفتگوی نوبتی (شما سوال می‌پرسید، مدل جواب می‌دهد)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">دسترسی به فایل‌سیستم:</span>
                <span class="feat-val">محدود به Sandbox مرورگر و آپلود متنی</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">چرخه خوداصلاحی:</span>
                <span class="feat-val">ندارد (نیازمند راهنمایی کاربر)</span>
            </div>
        </div>
    </div>

    <!-- Col 3: Agent -->
    <div class="col-card col-agent">
        <div class="col-header">
            <i class="fa-solid fa-shield-halved col-icon" style="color: #00f2fe;"></i>
            <h2 class="col-title">۳. پلتفرم ایجنتیک</h2>
        </div>
        <div class="feature-list">
            <div class="feature-item">
                <span class="feat-label">ماهیت ساختاری:</span>
                <span class="feat-val highlight">سیستم‌عامل و دستیار خودمختار (Proactive Agent)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">نوع ورودی / تعامل:</span>
                <span class="feat-val highlight">هدف‌محور (Goal-driven / Task Execution)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">دسترسی به فایل‌سیستم:</span>
                <span class="feat-val badge-green">کامل و بومی (Local Workspace & Shell)</span>
            </div>
            <div class="feature-item">
                <span class="feat-label">چرخه خوداصلاحی:</span>
                <span class="feat-val badge-green">دارد (تست ➔ خواندن ارور ➔ دیباگ ➔ کامیت)</span>
            </div>
        </div>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

slide2_evolution_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">چگونه یک API ساده تبدیل به یک ایجنت خودمختار می‌شود؟</h1>
        <p class="sub-title">معماری چرخه‌ی کنترل (Control Loop) و پیوند LLM با ابزارهای سیستم‌عاملی</p>
    </div>
    <span class="badge-tag">معماری داخلی ایجنت | اسلاید ۲</span>
</div>

<div class="cards-grid-3">
    <div class="step-card">
        <span class="step-num">گام ۱: مغز محاسباتی</span>
        <div class="card-h2"><i class="fa-solid fa-microchip" style="color:#00f2fe; margin-left:10px;"></i>موتور استدلال (LLM Core)</div>
        <p class="card-p">استفاده از API مدل جمنای یا کلود به عنوان هسته تصمیم‌گیری برای تحلیل هدف کاربر، برنامه‌ریزی مراحل و انتخاب ابزار مناسب.</p>
    </div>

    <div class="step-card">
        <span class="step-num">گام ۲: لایه ابزارها</span>
        <div class="card-h2"><i class="fa-solid fa-wrench" style="color:#f9d423; margin-left:10px;"></i>Tool Calling & Native APIs</div>
        <p class="card-p">تعریف توابع عملیاتی واقعی (مانند `read_file`, `write_file`, `run_command`) جهت ایجاد امکان دسترسی ایجنت به فایل‌ها و ترمینال.</p>
    </div>

    <div class="step-card">
        <span class="step-num">گام ۳: حلقه خودمختار</span>
        <div class="card-h2"><i class="fa-solid fa-rotate" style="color:#00ff87; margin-left:10px;"></i>Autonomous Control Loop</div>
        <p class="card-p">قرار دادن فراخوانی API در یک حلقه کنترل که خروجی ابزارها را تحلیل کرده، باگ‌ها را رفع کرده و تا نیل به هدف ادامه می‌دهد.</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

hti.screenshot(html_str=slide1_table_html, save_as='slide_1.png')
hti.screenshot(html_str=slide2_evolution_html, save_as='slide_2.png')

print("2 Comparison & Evolution slides generated successfully!")
