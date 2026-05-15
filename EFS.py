from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@freezer.register_generator
def all_pages():
    yield '/'
    yield '/about/'
    yield '/careers/'
    yield '/news/'       # 新闻中心

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terra Group | 泰拉集团</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
    <style>
        /* 定义本地 Versa 字体 */
        @font-face {
            font-family: 'Versa';
            src: url('/static/fonts/Versa.woff2') format('woff2');
            font-weight: normal;
            font-style: normal;
            font-display: swap;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            color: #1a2a3a;
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
        }
        /* 导航栏容器 */
        nav {
            position: fixed; top: 0; width: 100%;
            z-index: 1000;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            background: transparent;
            transition: background 0.4s ease;
        }
        nav:hover {
            background: rgba(255,255,255,0.95);
            border-bottom: 1px solid #e0e7ef;
        }
        /* 上半部分 Logo 行 */
        .nav-top {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 14px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
            overflow: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        }
        .nav-top.hide-logo {
            max-height: 0;
            padding-top: 0;
            padding-bottom: 0;
            opacity: 0;
            box-shadow: none;
        }
        .nav-logo {
            height: 44px;
            width: auto;
        }
        /* 下半部分 链接行 + 搜索 */
        .nav-bottom {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
            transition: background 0.4s ease, box-shadow 0.4s ease;
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        }
        /* 左侧小Logo（上半隐藏时显示） */
        .bottom-logo {
            position: absolute;
            left: 60px;
            top: 50%;
            transform: translateY(-50%);
            height: 34px;
            width: auto;
            display: none;
            z-index: 2;
        }
        .nav-top.hide-logo ~ .nav-bottom .bottom-logo {
            display: block;
        }
        /* 搜索框（默认半透明） */
        .search-box {
            position: absolute;
            right: 60px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            width: 280px;
            padding: 7px 18px;
            border: 1px solid rgba(255,255,255,0.8);
            border-radius: 24px;
            background: rgba(255,255,255,0.25);
            backdrop-filter: blur(4px);
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            z-index: 2;
        }
        .search-box:hover {
            border-color: #ffffff;
            background: rgba(255,255,255,0.35);
        }
        .search-box .search-icon {
            font-size: 18px;
            color: #ffffff;
        }
        .search-box span {
            font-size: 16px;
            color: #ffffff;
            text-shadow: 0 1px 3px rgba(0,0,0,0.6);
        }
        /* 导航链接 */
        .nav-links {
            display: flex;
            gap: 0;
            align-items: center;
        }
        .nav-links a {
            color: #ffffff;
            text-decoration: none;
            font-size: 17px;
            font-weight: 600;
            text-shadow: 0 0 2px rgba(0,0,0,0.8), 0 1px 4px rgba(0,0,0,0.7);
            transition: color 0.3s, text-shadow 0.3s;
        }
        .nav-links a:hover {
            color: #00d4ff;
        }
        /* 分隔符 */
        .nav-links a:not(:last-child)::after {
            content: "|";
            margin-left: 28px;
            margin-right: 28px;
            color: inherit;
            opacity: 0.6;
        }
        /* 上半隐藏时，下半部分变为不透明白色背景 */
        .nav-top.hide-logo ~ .nav-bottom {
            background: rgba(255,255,255,0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .nav-top.hide-logo ~ .nav-bottom .nav-links a {
            color: #4a5c6c;
            text-shadow: none;
        }
        .nav-top.hide-logo ~ .nav-bottom .nav-links a:hover {
            color: #0066cc;
        }
        .nav-top.hide-logo ~ .nav-bottom .search-box {
            border-color: #b0bec5;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .nav-top.hide-logo ~ .nav-bottom .search-box .search-icon {
            color: #0066cc;
        }
        .nav-top.hide-logo ~ .nav-bottom .search-box span {
            color: #5e6f82;
            text-shadow: none;
        }
        /* 悬停时整体变白 */
        nav:hover .nav-bottom {
            background: transparent;
            box-shadow: 0 2px 12px rgba(0,0,0,0.12);
        }
        nav:hover .nav-links a {
            color: #4a5c6c;
            text-shadow: none;
        }
        nav:hover .nav-links a:hover {
            color: #0066cc;
        }
        nav:hover .search-box {
            border-color: #b0bec5;
            background: #ffffff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        nav:hover .search-box:hover {
            border-color: #0066cc;
            background: #ffffff;
        }
        nav:hover .search-box .search-icon {
            color: #0066cc;
        }
        nav:hover .search-box span {
            color: #5e6f82;
            text-shadow: none;
        }
        /* 通用区块 */
        .section {
            padding: 100px 60px 80px;
            max-width: 1200px;
            margin: 0 auto;
        }
        /* 首屏 - 视频背景 */
        .hero {
            min-height: 100vh;
            display: flex; flex-direction: column;
            justify-content: center; align-items: center;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .bg-video {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            z-index: 0;
        }
        .overlay {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.35);
            z-index: 1;
        }
        /* 向下滚动箭头 */
        .scroll-hint {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 40px;
            color: rgba(255,255,255,0.8);
            text-shadow: 0 2px 8px rgba(0,0,0,0.5);
            z-index: 2;
            animation: bounce 2s infinite;
            cursor: default;
            user-select: none;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateX(-50%) translateY(0);
            }
            40% {
                transform: translateX(-50%) translateY(-15px);
            }
            60% {
                transform: translateX(-50%) translateY(-8px);
            }
        }
        .hero h1 {
            font-size: clamp(48px, 10vw, 90px); font-weight: 800;
            letter-spacing: 8px;
            color: #ffffff;
            text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000, 0 0 8px rgba(0,0,0,0.8);
            margin-bottom: 16px;
            position: relative; z-index: 2;
            text-transform: uppercase;
            font-family: 'Versa', 'Orbitron', 'Michroma', sans-serif;
        }
        .hero p.tagline {
            font-size: 22px;
            letter-spacing: 4px;
            color: rgba(255,255,255,0.95);
            text-shadow: 0 2px 8px rgba(0,0,0,0.5);
            margin-bottom: 40px;
            position: relative; z-index: 2;
            font-family: 'Georgia', 'Times New Roman', serif;
            font-style: italic;
        }
        .hero .btn {
            border: 2px solid #ffffff; color: #ffffff;
            padding: 14px 48px; font-size: 16px; letter-spacing: 4px;
            background: rgba(0,0,0,0.3);
            backdrop-filter: blur(4px);
            cursor: default;
            text-transform: uppercase; border-radius: 4px;
            transition: all 0.3s; display: inline-block;
            user-select: none;
            position: relative; z-index: 2;
        }
        .hero .btn:hover {
            background: rgba(255,255,255,0.2);
            border-color: #00b4d8;
            color: #00b4d8;
        }
        /* 英文副标题 */
        .about-subtitle {
            text-align: center;
            font-size: 18px;
            color: #a0a8b5;
            font-family: 'Helvetica Neue', 'Arial', sans-serif;
            font-weight: 500;
            letter-spacing: 2px;
            margin-bottom: 0;
        }
        /* 中文主标题 */
        .about-title {
            text-align: center;
            font-size: 56px;
            letter-spacing: 2px;
            margin-bottom: 6px;
            font-weight: 700;
            color: #0b2b44;
        }
        /* “走进泰拉” 板块样式 */
        .about-box {
            display: flex;
            background: #ffffff;
            border-radius: 20px;
            box-shadow: 0 12px 36px rgba(0,0,0,0.08);
            overflow: hidden;
            margin-top: 40px;
            min-height: 380px;
        }
        .about-img {
            width: 48%;
            object-fit: cover;
            flex-shrink: 0;
        }
        .about-content {
            padding: 56px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .about-content p {
            font-size: 17px;
            color: #4a5c6c;
            line-height: 1.8;
            margin-bottom: 28px;
        }
        /* 按钮 */
        .more-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #0066cc;
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 14px 28px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
            align-self: flex-start;
            height: 52px;
            box-sizing: border-box;
        }
        .more-btn .arrow-icon {
            font-size: 30px;
            font-weight: 900;
            line-height: 1;
            transition: transform 0.3s ease, margin 0.3s ease;
            order: 0;
            margin-top: -6px;
        }
        .more-btn .btn-text {
            max-width: 0;
            overflow: hidden;
            white-space: nowrap;
            transition: max-width 0.4s ease, margin 0.3s ease, opacity 0.3s ease;
            opacity: 0;
            margin-left: 0;
            order: 1;
        }
        .more-btn:hover .btn-text {
            max-width: 120px;
            opacity: 1;
            margin-left: 10px;
        }
        .more-btn:hover .arrow-icon {
            order: 1;
            margin-left: 0;
            margin-top: -6px;
        }
        .more-btn:hover .btn-text {
            order: 0;
        }
        /* 新闻动态 */
        .news-list {
            display: flex; flex-direction: column; gap: 24px;
            margin-top: 40px;
        }
        .news-item {
            border-left: 4px solid #0077b6; padding-left: 28px;
            background: #fff; padding: 24px 28px; border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.02);
            transition: border-color 0.3s;
        }
        .news-item:hover { border-left-color: #00b4d8; }
        .news-date {
            font-size: 13px; color: #8393a5; letter-spacing: 2px;
            margin-bottom: 6px;
        }
        .news-title {
            font-size: 20px; font-weight: 600; color: #0b2b44;
        }
        .news-desc {
            font-size: 15px; color: #4a5c6c; margin-top: 8px;
        }
        /* 页脚 */
        footer {
            text-align: center; padding: 60px 20px 40px;
            border-top: 1px solid #dce3eb; background: #fff;
        }
        footer p {
            color: #8393a5; font-size: 13px;
        }
    </style>
</head>
<body>
    <nav id="mainNav">
        <div class="nav-top" id="navTop">
            <img src="/static/terralogo.png" alt="Terra Group Logo" class="nav-logo">
        </div>
        <div class="nav-bottom">
            <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            <a href="#" class="search-box" id="searchLink">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>   <!-- 更新链接 -->
                <a href="/careers/">招贤纳士</a>
                <a href="#">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="hero" id="heroSection">
        <video autoplay muted loop playsinline class="bg-video">
            <source src="/static/background.mp4" type="video/mp4">
            <img src="/static/background.jpg" alt="Terra Group 背景">
        </video>
        <div class="overlay"></div>
        <h1>TERRAGROUP</h1>
        <p class="tagline">Virtus in Scientia</p>
        <span class="btn">探索我们的研究</span>
        <div class="scroll-hint">↓</div>
    </div>

    <!-- 走进泰拉板块 -->
    <div class="section" style="max-width: 1400px;">
        <p class="about-subtitle">ABOUT TERRAGROUP</p>
        <h2 class="about-title">走进泰拉</h2>
        <div class="about-box">
            <img src="/static/about-preview.jpg" alt="走进泰拉" class="about-img">
            <div class="about-content">
                <p>
                    泰拉集团（Terra Group）成立于1998年，总部位于英国，是一家业务遍及全球120多个国家的跨国巨头。
                    我们以“Virtus in Scientia”（潜心科研）为核心理念，专注农业生物技术、前沿科技研究与全球基础设施建设。
                    集团旗下拥有40余家大型企业，从诺文斯克到刚果，我们以科学的力量重塑未来。
                </p>
                <a href="/about/" class="more-btn">
                    <span class="arrow-icon">→</span>
                    <span class="btn-text">了解更多</span>
                </a>
            </div>
        </div>
    </div>

    <!-- 新闻动态 -->
    <div class="section">
        <h2 style="font-size:32px; letter-spacing:3px;">新闻动态</h2>
        <div class="news-list">
            <div class="news-item">
                <div class="news-date">2025.10.12</div>
                <div class="news-title">Terra Group Labs 在诺文斯克新建三级生物实验室</div>
                <div class="news-desc">该实验室将专注于传染病学研究，进一步强化集团在全球公共卫生领域的领导地位。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.09.28</div>
                <div class="news-title">集团与 USEC 国际安保续签战略合作协议</div>
                <div class="news-desc">USEC 将继续为泰拉集团在全球的资产及人员提供安全保障服务。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.08.15</div>
                <div class="news-title">刚果（金）矿业项目顺利投产</div>
                <div class="news-desc">该矿区的稀土与铀矿开采将为清洁能源与医疗同位素供应提供关键原料。</div>
            </div>
        </div>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>

    <script>
        const nav = document.getElementById('mainNav');
        const navTop = document.getElementById('navTop');
        const hero = document.getElementById('heroSection');
        const searchLink = document.getElementById('searchLink');

        function updateHeroPadding() {
            const navHeight = nav.offsetHeight;
            if (hero) {
                hero.style.paddingTop = navHeight + 'px';
            }
        }
        if (hero) {
            updateHeroPadding();
            window.addEventListener('resize', updateHeroPadding);
        }

        function handleScroll() {
            const scrollY = window.scrollY;
            if (scrollY > 100) {
                navTop.classList.add('hide-logo');
            } else if (scrollY <= 5) {
                navTop.classList.remove('hide-logo');
            }
        }
        window.addEventListener('scroll', handleScroll);
        handleScroll();

        searchLink.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('搜索功能暂未开放');
        });
    </script>
</body>
</html>
    '''

@app.route('/about/')
def about():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>关于我们 | Terra Group</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            color: #1a2a3a;
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
        }
        nav {
            position: fixed; top: 0; width: 100%;
            z-index: 1000;
            border-bottom: 1px solid #e0e7ef;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .nav-bottom {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
        }
        .bottom-logo {
            position: absolute;
            left: 60px;
            top: 50%;
            transform: translateY(-50%);
            height: 34px;
            width: auto;
            display: block;
            z-index: 2;
        }
        .search-box {
            position: absolute;
            right: 60px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            width: 280px;
            padding: 7px 18px;
            border: 1px solid #b0bec5;
            border-radius: 24px;
            background: #ffffff;
            cursor: pointer;
            text-decoration: none;
            z-index: 2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover {
            border-color: #0066cc;
        }
        .search-box .search-icon {
            font-size: 18px;
            color: #0066cc;
        }
        .search-box span {
            font-size: 16px;
            color: #5e6f82;
        }
        .nav-links {
            display: flex;
            gap: 0;
            align-items: center;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 17px;
            font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #0066cc;
        }
        .nav-links a:not(:last-child)::after {
            content: "|";
            margin-left: 28px;
            margin-right: 28px;
            color: #b0bec5;
            opacity: 0.6;
        }
        .container {
            max-width: 1000px;
            margin: 120px auto 80px;
            padding: 0 40px;
        }
        h1 {
            font-size: 48px;
            font-weight: 700;
            color: #0b2b44;
            margin-bottom: 24px;
            border-bottom: 4px solid #0077b6;
            display: inline-block;
            padding-bottom: 8px;
        }
        p {
            font-size: 18px;
            color: #4a5c6c;
            line-height: 1.8;
            margin-bottom: 20px;
        }
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid #dce3eb;
            background: #fff;
        }
        footer p {
            color: #8393a5;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/">产品与服务</a>
                <a href="/about/" style="color: #0066cc;">关于我们</a>
                <a href="/news/">新闻中心</a>   <!-- 更新链接 -->
                <a href="/careers/">招贤纳士</a>
                <a href="#">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>关于 Terra Group</h1>
        <p>
            泰拉集团国际控股公司 (Terra Group International) 是一家业务遍及全球超过120个国家的跨国巨头，
            旗下拥有超过40家大型企业。集团官方宣称主要业务为农业与生物技术研究，但实际上其影响力横跨
            军事、政治、前沿科学、金融、采矿等多个领域。
        </p>
        <p>
            我们的座右铭是 <strong>Virtus in Scientia</strong>（潜心科研）。在诺文斯克经济特区，
            泰拉集团承包了大量的基础设施建设，并在此地开展了诸多尖端科技项目。然而，诸多迹象表明，
            集团与当地的私人武装、联合国维和部队甚至神秘主义势力有着千丝万缕的联系……
        </p>
        <p>
            <a href="/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/careers/')
def careers():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>招贤纳士 | Terra Group</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            color: #1a2a3a;
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
        }
        nav {
            position: fixed; top: 0; width: 100%;
            z-index: 1000;
            border-bottom: 1px solid #e0e7ef;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .nav-bottom {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
        }
        .bottom-logo {
            position: absolute;
            left: 60px;
            top: 50%;
            transform: translateY(-50%);
            height: 34px;
            width: auto;
            display: block;
            z-index: 2;
        }
        .search-box {
            position: absolute;
            right: 60px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            width: 280px;
            padding: 7px 18px;
            border: 1px solid #b0bec5;
            border-radius: 24px;
            background: #ffffff;
            cursor: pointer;
            text-decoration: none;
            z-index: 2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover {
            border-color: #0066cc;
        }
        .search-box .search-icon {
            font-size: 18px;
            color: #0066cc;
        }
        .search-box span {
            font-size: 16px;
            color: #5e6f82;
        }
        .nav-links {
            display: flex;
            gap: 0;
            align-items: center;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 17px;
            font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #0066cc;
        }
        .nav-links a:not(:last-child)::after {
            content: "|";
            margin-left: 28px;
            margin-right: 28px;
            color: #b0bec5;
            opacity: 0.6;
        }
        .container {
            max-width: 1000px;
            margin: 120px auto 80px;
            padding: 0 40px;
        }
        h1 {
            font-size: 48px;
            font-weight: 700;
            color: #0b2b44;
            margin-bottom: 24px;
            border-bottom: 4px solid #0077b6;
            display: inline-block;
            padding-bottom: 8px;
        }
        .job-list {
            display: flex;
            flex-direction: column;
            gap: 24px;
            margin: 40px 0;
        }
        .job-card {
            background: #ffffff;
            border: 1px solid #dce3eb;
            border-radius: 12px;
            padding: 28px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }
        .job-card h2 {
            font-size: 24px;
            color: #0b2b44;
            margin-bottom: 8px;
        }
        .job-card .location {
            font-size: 14px;
            color: #8393a5;
            margin-bottom: 12px;
        }
        .job-card p {
            font-size: 16px;
            color: #4a5c6c;
            line-height: 1.6;
        }
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid #dce3eb;
            background: #fff;
        }
        footer p {
            color: #8393a5;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>   <!-- 更新链接 -->
                <a href="/careers/" style="color: #0066cc;">招贤纳士</a>
                <a href="#">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>加入我们</h1>
        <p style="font-size: 18px; color: #4a5c6c; line-height: 1.8; margin-bottom: 40px;">
            泰拉集团正在寻找那些勇于探索未知、挑战极限的人才。我们致力于通过科学技术重塑世界，
            如果你对前沿研究、全球基础设施建设或生物技术充满热情，这里将是你施展抱负的舞台。
        </p>

        <div class="job-list">
            <div class="job-card">
                <h2>高级生物信息学研究员</h2>
                <div class="location">📍 诺文斯克经济特区 · 泰拉实验室</div>
                <p>负责基因数据分析与算法开发，参与极端环境适应性基因组项目。要求熟悉 Python/R，具备 NGS 数据分析经验。</p>
            </div>
            <div class="job-card">
                <h2>基础设施项目经理</h2>
                <div class="location">📍 刚果（金） · 矿业分部</div>
                <p>统筹大型矿区的配套基建工程，管理跨国施工团队。要求 5 年以上工程管理经验，适应长期外派。</p>
            </div>
            <div class="job-card">
                <h2>量子通信系统工程师</h2>
                <div class="location">📍 保密地点 · 前沿实验室</div>
                <p>参与超导量子比特与量子密钥分发系统的设计与测试。要求物理学或电子工程博士学历，具备低温物理实验经验。</p>
            </div>
        </div>

        <p>
            <a href="/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

# 新增新闻中心路由
@app.route('/news/')
def news():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻中心 | Terra Group</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            color: #1a2a3a;
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
        }
        nav {
            position: fixed; top: 0; width: 100%;
            z-index: 1000;
            border-bottom: 1px solid #e0e7ef;
            background: rgba(255,255,255,0.95);
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .nav-bottom {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
        }
        .bottom-logo {
            position: absolute;
            left: 60px;
            top: 50%;
            transform: translateY(-50%);
            height: 34px;
            width: auto;
            display: block;
            z-index: 2;
        }
        .search-box {
            position: absolute;
            right: 60px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            align-items: center;
            gap: 8px;
            width: 280px;
            padding: 7px 18px;
            border: 1px solid #b0bec5;
            border-radius: 24px;
            background: #ffffff;
            cursor: pointer;
            text-decoration: none;
            z-index: 2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover {
            border-color: #0066cc;
        }
        .search-box .search-icon {
            font-size: 18px;
            color: #0066cc;
        }
        .search-box span {
            font-size: 16px;
            color: #5e6f82;
        }
        .nav-links {
            display: flex;
            gap: 0;
            align-items: center;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 17px;
            font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: #0066cc;
        }
        .nav-links a:not(:last-child)::after {
            content: "|";
            margin-left: 28px;
            margin-right: 28px;
            color: #b0bec5;
            opacity: 0.6;
        }
        .container {
            max-width: 1000px;
            margin: 120px auto 80px;
            padding: 0 40px;
        }
        h1 {
            font-size: 48px;
            font-weight: 700;
            color: #0b2b44;
            margin-bottom: 24px;
            border-bottom: 4px solid #0077b6;
            display: inline-block;
            padding-bottom: 8px;
        }
        .news-list {
            display: flex;
            flex-direction: column;
            gap: 24px;
            margin-top: 40px;
        }
        .news-item {
            border-left: 4px solid #0077b6;
            padding-left: 28px;
            background: #fff;
            padding: 24px 28px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            transition: border-color 0.3s;
        }
        .news-item:hover { border-left-color: #00b4d8; }
        .news-date {
            font-size: 13px;
            color: #8393a5;
            letter-spacing: 2px;
            margin-bottom: 6px;
        }
        .news-title {
            font-size: 20px;
            font-weight: 600;
            color: #0b2b44;
        }
        .news-desc {
            font-size: 15px;
            color: #4a5c6c;
            margin-top: 8px;
        }
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid #dce3eb;
            background: #fff;
        }
        footer p {
            color: #8393a5;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/" style="color: #0066cc;">新闻中心</a>   <!-- 当前高亮 -->
                <a href="/careers/">招贤纳士</a>
                <a href="#">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>新闻中心</h1>
        <p style="font-size: 18px; color: #4a5c6c; line-height: 1.8; margin-bottom: 40px;">
            了解泰拉集团在全球的最新动态、研究成果与战略合作。
        </p>

        <div class="news-list">
            <div class="news-item">
                <div class="news-date">2025.10.12</div>
                <div class="news-title">Terra Group Labs 在诺文斯克新建三级生物实验室</div>
                <div class="news-desc">该实验室将专注于传染病学研究，进一步强化集团在全球公共卫生领域的领导地位。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.09.28</div>
                <div class="news-title">集团与 USEC 国际安保续签战略合作协议</div>
                <div class="news-desc">USEC 将继续为泰拉集团在全球的资产及人员提供安全保障服务。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.08.15</div>
                <div class="news-title">刚果（金）矿业项目顺利投产</div>
                <div class="news-desc">该矿区的稀土与铀矿开采将为清洁能源与医疗同位素供应提供关键原料。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.07.02</div>
                <div class="news-title">泰拉集团发布2025年度可持续发展报告</div>
                <div class="news-desc">报告强调了集团在环境保护、社区共建及科研伦理方面的承诺与进展。</div>
            </div>
        </div>

        <p style="margin-top: 40px;">
            <a href="/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)