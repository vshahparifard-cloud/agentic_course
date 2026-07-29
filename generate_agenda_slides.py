from html2image import Html2Image
import os

hti = Html2Image(size=(1920, 1080))
hti.output_path = 'slides/session_1_agenda'
os.makedirs('slides/session_1_agenda', exist_ok=True)

css_agenda = '''
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
        radial-gradient(circle at 10% 20%, rgba(0, 242, 254, 0.15) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(127, 0, 255, 0.15) 0%, transparent 45%);
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
.cards-grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin: 36px 0;
}
.slide-card {
    background: rgba(18, 20, 32, 0.85);
    border: 1px solid rgba(0, 242, 254, 0.25);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.icon-box {
    width: 56px;
    height: 56px;
    background: rgba(0, 242, 254, 0.12);
    border: 1px solid rgba(0, 242, 254, 0.3);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #00f2fe;
    font-size: 1.6rem;
}
.card-h2 {
    font-size: 1.4rem;
    font-weight: 800;
    color: #ffffff;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 10px;
}
.card-p {
    font-size: 1.1rem;
    color: #cbd5e1;
    line-height: 1.7;
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

css_timeline = '''
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
        radial-gradient(circle at 10% 20%, rgba(0, 255, 135, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 90% 80%, rgba(0, 242, 254, 0.08) 0%, transparent 50%);
}
.header-bar-timeline {
    display: flex;
    align-items: center;
    gap: 16px;
}
.accent-line {
    width: 6px;
    height: 48px;
    background: #00f2fe;
    border-radius: 4px;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
}
.main-title-timeline {
    font-size: 2.8rem;
    font-weight: 900;
    color: #ffffff;
}

/* Timeline Track Layout */
.timeline-container {
    position: relative;
    width: 100%;
    height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.timeline-line {
    position: absolute;
    width: 90%;
    height: 4px;
    background: rgba(255, 255, 255, 0.2);
    top: 50%;
    left: 5%;
    transform: translateY(-50%);
    z-index: 1;
}
.timeline-nodes {
    position: absolute;
    width: 90%;
    height: 100%;
    top: 0;
    left: 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
}
.node-item {
    position: relative;
    width: 22%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.node-circle {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #08090f;
    border: 5px solid #f9d423;
    box-shadow: 0 0 20px rgba(249, 212, 35, 0.8);
}
.node-content-below {
    position: absolute;
    top: 60px;
    text-align: center;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}
.node-content-above {
    position: absolute;
    bottom: 60px;
    text-align: center;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
}
.hour-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #00ff87;
    text-shadow: 0 0 10px rgba(0, 255, 135, 0.3);
}
.hour-desc {
    font-size: 1.25rem;
    color: #e2e8f0;
    line-height: 1.6;
    max-width: 340px;
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
<style>{css_agenda}</style>
</head>
<body>
<div class="header-bar">
    <div class="title-group">
        <h1 class="main-title">سرفصل مطالب جلسه اول (Session 01 Agenda)</h1>
        <p class="sub-title">اکوسیستم جمنای، کلود، معماری ایجنتیک و مدل‌های هوش مصنوعی (آپدیت ۲۰۲۶)</p>
    </div>
    <span class="badge-tag">اسلاید ۱ | سرفصل جامع</span>
</div>

<div class="cards-grid-4">
    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-robot"></i></div>
        <h2 class="card-h2">۱. چیستی ایجنت هوش مصنوعی</h2>
        <p class="card-p">تعریف عامل خودمختار، چرخه ادراک-استدلال-اقدام، پارامترهای مدل، تاریخ کات‌آف و نقش ابزارها (Native Grounding).</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-network-wired"></i></div>
        <h2 class="card-h2">۲. چالش تک‌عاملی & چندایجنتی</h2>
        <p class="card-p">محدودیت‌های Single-Agent، مدیریت کانتکست، گذار به سیستم‌های Multi-Agent و بررسی پلتفرم‌های Claude Code & Codex.</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-microchip"></i></div>
        <h2 class="card-h2">۳. انقلاب Context Window</h2>
        <p class="card-p">اتصال مستقیم به Workspace، تحلیل کدهای بزرگ و مقایسه فنی غول‌های هوش مصنوعی (Gemini 3.1, Claude 4.8, GPT-5.5).</p>
    </div>

    <div class="slide-card">
        <div class="icon-box"><i class="fa-solid fa-rocket"></i></div>
        <h2 class="card-h2">۴. پلتفرم‌ها & Agent-First</h2>
        <p class="card-p">بررسی Gemini UI, Vertex AI, Claude Artifacts، RAG با NotebookLM و رویکرد Agent-First با گوگل Antigravity.</p>
    </div>
</div>

<div class="footer-bar">
    <span>دوره تخصصی توسعه سیستم‌های خودمختار | Session 01</span>
    <span>Agentic AI Course 2026</span>
</div>
</body>
</html>'''

slide2_timeline_html = f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>{css_timeline}</style>
</head>
<body>
<div class="header-bar-timeline">
    <div class="accent-line"></div>
    <h1 class="main-title-timeline">برنامه جامع جلسه اول (۴ ساعت)</h1>
</div>

<div class="timeline-container">
    <div class="timeline-line"></div>
    <div class="timeline-nodes">
        <!-- Node 1: ساعت اول (RTL: Far Right) -->
        <div class="node-item">
            <div class="node-circle"></div>
            <div class="node-content-below">
                <h2 class="hour-title">ساعت اول</h2>
                <p class="hour-desc">تعریف ایجنت خودمختار، چت‌بات‌ها، پارامترها، کات‌آف، کانتکست سایز و ابزارها (Tools)</p>
            </div>
        </div>

        <!-- Node 2: ساعت دوم (Middle Right) -->
        <div class="node-item">
            <div class="node-circle"></div>
            <div class="node-content-above">
                <h2 class="hour-title">ساعت دوم</h2>
                <p class="hour-desc">معماری چت‌بات‌ها (RAG, Web Search) و مقایسه تفصیلی چت‌بات در برابر ایجنت</p>
            </div>
        </div>

        <!-- Node 3: ساعت سوم (Middle Left) -->
        <div class="node-item">
            <div class="node-circle"></div>
            <div class="node-content-below">
                <h2 class="hour-title">ساعت سوم</h2>
                <p class="hour-desc">محدودیت‌های تک‌عاملی (Single-Agent)، لزوم گذار به Multi-Agent و بررسی Claude Code & Codex</p>
            </div>
        </div>

        <!-- Node 4: ساعت چهارم (Far Left) -->
        <div class="node-item">
            <div class="node-circle"></div>
            <div class="node-content-above">
                <h2 class="hour-title">ساعت چهارم</h2>
                <p class="hour-desc">انقلاب Context Window، مقایسه مدل‌های ۲۰۲۶ و رویکرد Agent-First با Antigravity</p>
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

hti.screenshot(html_str=slide1_html, save_as='slide_1.png')
hti.screenshot(html_str=slide2_timeline_html, save_as='slide_2.png')

print("Agenda & Timeline slides successfully generated with exact timeline format!")
