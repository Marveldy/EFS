from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@freezer.register_generator
def all_pages():
    yield '/'          # 首页
    yield '/about/'    # “关于我们”子页面（注意结尾的斜杠）

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
        /* 业务卡片 */
        .cards {
            display: flex; gap: 32px; flex-wrap: wrap;
            justify-content: center; margin-top: 60px;
        }
        .card {
            background: #ffffff; border: 1px solid #dce3eb;
            border-radius: 16px; padding: 40px 28px; flex: 1;
            min-width: 260px; max-width: 340px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0,102,204,0.12);
        }
        .card-icon { font-size: 42px; margin-bottom: 20px; }
        .card h3 {
            font-size: 24px; font-weight: 600; margin-bottom: 12px;
            color: #0b2b44;
        }
        .card p { color: #5e6f82; font-size: 15px; }
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
                <a href="/about/">关于我们</a>   <!-- 注意结尾斜杠 -->
                <a href="#">新闻中心</a>
                <a href="#">招贤纳士</a>
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
    </div>

    <div class="section">
        <h2 style="text-align:center; font-size:36px; letter-spacing:4px; margin-bottom:12px;">核心业务</h2>
        <p style="text-align:center; color:#5e6f82; max-width:600px; margin:0 auto 40px;">
            泰拉集团在120多个国家开展业务，致力于通过科学技术推动人类进步。
        </p>
        <div class="cards">
            <div class="card">
                <div class="card-icon">🌾</div>
                <h3>农业生物技术</h3>
                <p>开发适应极端气候的作物基因，保障全球粮食安全。我们在诺文斯克地区的试验田已取得突破性进展。</p>
            </div>
            <div class="card">
                <div class="card-icon">🧪</div>
                <h3>前沿科技研究</h3>
                <p>超导材料、量子通信、神经接口……我们的实验室永远走在已知与未知的边界。</p>
            </div>
            <div class="card">
                <div class="card-icon">🏗️</div>
                <h3>全球基础设施</h3>
                <p>承包港口、电站、物流网络建设，为新兴经济特区提供全套解决方案。</p>
            </div>
        </div>
    </div>

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

# 注意：路由统一使用结尾斜杠
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
        }
        .nav-top {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 14px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        }
        .nav-logo {
            height: 44px;
            width: auto;
        }
        .nav-bottom {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 18px 60px;
            background: transparent;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        }
        .bottom-logo {
            position: absolute;
            left: 60px;
            top: 50%;
            transform: translateY(-50%);
            height: 34px;
            width: auto;
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
            margin: 160px auto 80px;
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
        <div class="nav-top">
            <img src="/static/terralogo.png" alt="Terra Group Logo" class="nav-logo">
        </div>
        <div class="nav-bottom">
            <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/">产品与服务</a>
                <a href="/about/" style="color: #0066cc;">关于我们</a>   <!-- 当前页面高亮，注意结尾斜杠 -->
                <a href="#">新闻中心</a>
                <a href="#">招贤纳士</a>
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)