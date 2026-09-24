from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@freezer.register_generator
def all_pages():
    yield '/'              # 游戏入口（新首页）
    yield '/desktop/'      # 模拟桌面
    yield '/home/'         # 泰拉集团主页
    yield '/about/'
    yield '/careers/'
    yield '/news/'
    yield '/products/'
    yield '/contact/'
    # 新闻详情页
    yield '/news/2025-10-12/'
    yield '/news/2025-09-28/'
    yield '/news/2025-08-15/'
    yield '/news/2025-07-02/'
    yield '/news-portal/'
    yield '/news-portal/medical-accident/'
    yield '/news-portal/search/'
    yield '/oracle/'

# ========== 游戏入口（网站首页） ==========
@app.route('/')
def game_entry():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>逃离石家庄 · 网页解谜</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            width: 100vw; height: 100vh;
            background: #050510;
            font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        /* 星空背景 */
        .stars-canvas {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 0;
        }
        /* 主卡片 */
        .main-card {
            position: relative; z-index: 10;
            text-align: center; padding: 50px 40px;
            background: rgba(10,10,25,0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(100,180,255,0.15);
            border-radius: 32px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.8), 0 0 80px rgba(70,130,255,0.1);
            max-width: 550px; width: 90%;
        }
        /* Logo 图片 */
        .logo-img {
            display: block;
            margin: 0 auto 35px;
            max-width: 75%;
            height: auto;
            filter: drop-shadow(0 0 20px rgba(80,160,255,0.6));
            animation: logoPulse 3s ease-in-out infinite;
        }
        @keyframes logoPulse {
            0%, 100% { filter: drop-shadow(0 0 15px rgba(80,160,255,0.5)); }
            50% { filter: drop-shadow(0 0 30px rgba(80,160,255,0.9)); }
        }
        .intro-text {
            color: #b0c4de; font-size: 17px; line-height: 1.8;
            margin-bottom: 40px; max-width: 450px;
            margin-left: auto; margin-right: auto;
        }
        .start-btn {
            display: inline-block; padding: 16px 48px;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            border: none;
            color: #fff; font-size: 20px; font-weight: 700;
            letter-spacing: 6px; text-decoration: none;
            border-radius: 50px;
            box-shadow: 0 8px 25px rgba(0,100,255,0.4);
            transition: all 0.3s ease;
            position: relative; overflow: hidden;
        }
        .start-btn:hover {
            background: linear-gradient(135deg, #2a5298, #1e3c72);
            box-shadow: 0 12px 35px rgba(0,140,255,0.6);
            transform: translateY(-3px);
        }
        .start-btn::after {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.3) 10%, transparent 70%);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .start-btn:hover::after {
            opacity: 1;
        }
        .version {
            position: absolute; bottom: 20px; right: 30px;
            color: rgba(255,255,255,0.3); font-size: 13px;
            letter-spacing: 2px; z-index: 20;
        }
    </style>
</head>
<body>
    <!-- 星空背景用 canvas 绘制 -->
    <canvas class="stars-canvas" id="starsCanvas"></canvas>

    <div class="main-card">
        <img src="/static/EFSlogo.png" alt="逃离石家庄" class="logo-img">
        <p class="intro-text">
            一通深夜的未接来电，一张泛黄的旧照片，<br>
            你的挚友在石家庄郊外失踪。<br>
            警方已放弃搜寻，但你知道——<br>
            真相，就藏在数字的缝隙之中。<br>
            这是一场跨越虚拟与现实的解谜之旅，<br>
            你，准备好了吗？
        </p>
        <a href="/desktop/" class="start-btn">开 始 游 戏</a>
    </div>
    <div class="version">v1.0 · ARG</div>

    <script>
        // 星空粒子动画
        const canvas = document.getElementById('starsCanvas');
        const ctx = canvas.getContext('2d');
        let width, height;
        const stars = [];

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resize);
        resize();

        // 生成星星
        const starCount = 150;
        for (let i = 0; i < starCount; i++) {
            stars.push({
                x: Math.random() * width,
                y: Math.random() * height,
                r: Math.random() * 1.5 + 0.5,
                alpha: Math.random(),
                delta: (Math.random() - 0.5) * 0.02,
                speed: Math.random() * 0.5 + 0.1
            });
        }

        function drawStars() {
            ctx.clearRect(0, 0, width, height);
            stars.forEach(s => {
                s.alpha += s.delta;
                if (s.alpha <= 0.2 || s.alpha >= 1) s.delta *= -1;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(255,255,255,${s.alpha})`;
                ctx.fill();
                // 移动
                s.y -= s.speed;
                if (s.y < -5) {
                    s.y = height + 5;
                    s.x = Math.random() * width;
                }
            });
            requestAnimationFrame(drawStars);
        }
        drawStars();
    </script>
</body>
</html>
    '''

# ========== 模拟桌面 ==========
@app.route('/desktop/')
def desktop():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>桌面</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }
        body {
            width: 100vw; height: 100vh;
            background: url('/static/desktop-wallpaper.jpg') center/cover no-repeat #007bff;
            background-size: cover;
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            overflow: hidden;
        }
        .desktop-icons {
            position: absolute; top: 20px; left: 20px;
            display: flex; flex-direction: column; gap: 25px;
        }
        .desktop-icon {
            display: flex; flex-direction: column; align-items: center;
            width: 80px; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
            cursor: pointer; padding: 5px;
        }
        .desktop-icon:hover { background: rgba(255,255,255,0.2); border-radius: 8px; }
        .desktop-icon img { width: 48px; height: 48px; margin-bottom: 4px; }
        .desktop-icon span { font-size: 13px; text-align: center; }
        .taskbar {
            position: absolute; bottom: 0; left: 0; right: 0;
            height: 48px; background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(10px); display: flex;
            align-items: center; justify-content: space-between;
            color: #333; z-index: 1000;
            border-top: 1px solid rgba(0,0,0,0.1);
        }
        .start-btn {
            background: none; border: none; color: #333;
            font-size: 18px; padding: 0 20px; height: 100%;
            cursor: pointer; display: flex; align-items: center; gap: 6px;
        }
        .start-btn:hover { background: rgba(0,0,0,0.05); }
        .start-btn img { height: 24px; width: auto; }
        .taskbar-icons { display: flex; align-items: center; gap: 2px; flex: 1; padding: 0 10px; }
        .taskbar-icon {
            width: 40px; height: 40px;
            display: flex; align-items: center; justify-content: center;
            border-radius: 4px; cursor: pointer;
        }
        .taskbar-icon:hover { background: rgba(0,0,0,0.1); }
        .taskbar-icon img { width: 24px; height: 24px; }
        .taskbar-icon.active {
            background: rgba(0,0,0,0.1);
            box-shadow: inset 0 0 0 2px rgba(0,102,204,0.6);
            border-radius: 4px;
        }
        .taskbar-right {
            display: flex; flex-direction: column; align-items: flex-end;
            justify-content: center; padding: 0 15px; font-size: 12px;
            line-height: 1.3; color: #333;
        }
        .taskbar-right .time { font-size: 14px; font-weight: 600; }
        .taskbar-right .date { font-size: 11px; opacity: 0.8; }

        /* 窗口 */
        .window {
            position: absolute; width: 500px; height: 400px;
            background: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            display: none; flex-direction: column; overflow: hidden;
            min-width: 300px; min-height: 200px; z-index: 500;
            border-radius: 0;
        }
        .window.active { z-index: 600; }
        .window-titlebar {
            background: #ffffff; color: #333;
            padding: 8px 12px;
            display: flex; justify-content: space-between;
            align-items: center; cursor: move;
            border-bottom: 1px solid #ddd;
        }
        .window-title { font-size: 14px; color: #333; }
        .window-controls { display: flex; gap: 8px; }
        .window-controls button {
            background: none; border: none; color: #333;
            font-size: 16px; cursor: pointer; width: 24px; height: 24px;
            border-radius: 4px; display: flex; align-items: center; justify-content: center;
        }
        .window-controls button:hover { background: rgba(0,0,0,0.1); }
        .window-content { flex: 1; overflow: hidden; background: white; }

        /* 邮箱 */
        .mail-layout { display: flex; height: 100%; }
        .mail-sidebar { width: 150px; background: #f5f5f5; border-right: 1px solid #ddd; padding: 8px 0; }
        .mail-folder { padding: 8px 16px; cursor: pointer; font-size: 14px; color: #333; }
        .mail-folder:hover { background: #e0e0e0; }
        .mail-folder.active { background: #d0e4ff; font-weight: 600; }
        .mail-main { flex: 1; display: flex; flex-direction: row; }
        .mail-list { width: 30%; overflow-y: auto; border-right: 1px solid #ddd; }
        .mail-item { padding: 10px 16px; border-bottom: 1px solid #eee; cursor: pointer; }
        .mail-item:hover { background: #f0f0f0; }
        .mail-item.active { background: #e6f0ff; }
        .mail-item .subject { font-weight: 600; font-size: 14px; }
        .mail-item .from { font-size: 12px; color: #666; margin-top: 2px; }
        .mail-item .preview { font-size: 12px; color: #888; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .mail-preview {
            flex: 1; padding: 16px; overflow-y: auto;
            user-select: text;
        }
        .mail-preview .subject { font-size: 16px; font-weight: 700; margin-bottom: 8px; user-select: text; }
        .mail-preview .meta { font-size: 12px; color: #888; margin-bottom: 12px; user-select: text; }
        .mail-preview .body { font-size: 14px; color: #333; line-height: 1.6; user-select: text; }
        .mail-preview .body strong { font-weight: bold; user-select: text; }

        /* 其他程序 */
        .tarkov-loading { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px; }
        .tarkov-spinner { width: 48px; height: 48px; border: 5px solid #ddd; border-top: 5px solid #0066cc; border-radius: 50%; animation: spin 1s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .tarkov-warning { display: none; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 20px; }
        .tarkov-warning .icon { font-size: 48px; }
        .tarkov-warning .text { font-size: 20px; font-weight: bold; color: #c00; text-align: center; line-height: 1.5; }
        .tarkov-warning button { padding: 8px 24px; font-size: 16px; cursor: pointer; background: #0066cc; color: white; border: none; border-radius: 4px; }

        .notepad-menubar { display: flex; background: #f0f0f0; border-bottom: 1px solid #ccc; padding: 2px 0; }
        .notepad-menubar span { padding: 4px 12px; font-size: 13px; cursor: default; }
        .notepad-menubar span:hover { background: #d0d0d0; }
        .notepad-textarea { flex: 1; padding: 4px; font-family: 'Consolas', 'Courier New', monospace; font-size: 14px; border: none; outline: none; resize: none; width: 100%; height: 100%; background: white; color: #333; cursor: text; user-select: text; }
        .notepad-statusbar { display: flex; justify-content: space-between; padding: 4px 10px; background: #f0f0f0; border-top: 1px solid #ccc; font-size: 12px; color: #666; }

        /* 浏览器工具栏 */
        .browser-toolbar {
            display: flex; align-items: center; justify-content: center;
            height: 180px; background: transparent; border-bottom: none;
        }
        .browser-url-wrapper { position: relative; width: 80%; max-width: 800px; }
        .browser-url {
            width: 100%; padding: 14px 50px 14px 24px;
            border: 2px solid #ccc; border-radius: 30px; font-size: 18px;
            outline: none; box-sizing: border-box; transition: border-color 0.3s;
        }
        .browser-url:focus { border-color: #0066cc; }
        .browser-go-btn {
            position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
            background: none; border: none; font-size: 22px; cursor: pointer;
            color: #666; padding: 8px; border-radius: 50%;
        }
        .browser-go-btn:hover { background: #e0e0e0; color: #333; }
        .browser-view { flex: 1; background: #fff; display: flex; align-items: center; justify-content: center; }

        /* 微信 */
        .wechat-layout { display: flex; height: 100%; }
        .wechat-sidebar { width: 200px; background: #2b2b2b; display: flex; flex-direction: column; }
        .wechat-profile { padding: 20px; color: white; border-bottom: 1px solid #444; font-weight: bold; }
        .wechat-contacts { flex: 1; overflow-y: auto; }
        .wechat-contact {
            padding: 15px 20px; color: #ccc; cursor: pointer;
            border-bottom: 1px solid #333; display: flex; align-items: center; gap: 10px;
        }
        .wechat-contact:hover { background: #3a3a3a; }
        .wechat-contact.active { background: #3a3a3a; }
        .wechat-avatar {
            width: 40px; height: 40px; border-radius: 4px;
            background: #555; display: flex; align-items: center; justify-content: center;
            color: white; font-weight: bold;
        }
        .wechat-chat-area { flex: 1; display: flex; flex-direction: column; }
        .wechat-chat-header { padding: 15px; background: #f5f5f5; border-bottom: 1px solid #ddd; font-weight: bold; }
        .wechat-messages { flex: 1; padding: 20px; overflow-y: auto; background: #ececec; }
        .wechat-input-area { padding: 10px; background: #f5f5f5; border-top: 1px solid #ddd; display: flex; gap: 10px; }
        .wechat-input { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; outline: none; }
        .wechat-send-btn { padding: 8px 16px; background: #07c160; color: white; border: none; border-radius: 4px; cursor: pointer; }

        .resize-handle { position: absolute; z-index: 10; background: transparent; }
        .resize-handle.top    { top: 0; left: 0; right: 0; height: 6px; cursor: n-resize; }
        .resize-handle.bottom { bottom: 0; left: 0; right: 0; height: 6px; cursor: s-resize; }
        .resize-handle.left   { left: 0; top: 0; bottom: 0; width: 6px; cursor: w-resize; }
        .resize-handle.right  { right: 0; top: 0; bottom: 0; width: 6px; cursor: e-resize; }
        .resize-handle.top-left     { top: 0; left: 0; width: 14px; height: 14px; cursor: nw-resize; }
        .resize-handle.top-right    { top: 0; right: 0; width: 14px; height: 14px; cursor: ne-resize; }
        .resize-handle.bottom-left  { bottom: 0; left: 0; width: 14px; height: 14px; cursor: sw-resize; }
        .resize-handle.bottom-right { bottom: 0; right: 0; width: 14px; height: 14px; cursor: se-resize; }
    </style>
</head>
<body>
    <div class="desktop-icons">
        <div class="desktop-icon" onclick="openWindow('computer')"><img src="/static/desktop-mycomputer.ico" alt="此电脑"><span>此电脑</span></div>
        <div class="desktop-icon" onclick="openWindow('recycle')"><img src="/static/desktop-recyclebin.ico" alt="回收站"><span>回收站</span></div>
        <div class="desktop-icon" onclick="openWindow('browser')"><img src="/static/desktop-chrome.ico" alt="浏览器"><span>浏览器</span></div>
        <div class="desktop-icon" onclick="openWindow('notepad')"><img src="/static/desktop-notepad.ico" alt="记事本"><span>记事本</span></div>
        <div class="desktop-icon" onclick="openWindow('mail')"><img src="/static/desktop-mail.ico" alt="邮箱"><span>邮箱</span></div>
        <div class="desktop-icon" onclick="openWindow('wechat')"><img src="/static/wechat.png" alt="微信"><span>微信</span></div>
        <div class="desktop-icon" onclick="openWindow('tarkov')"><img src="/static/desktop-EscapeFromTarkov.ico" alt="逃离塔科夫"><span>逃离塔科夫</span></div>
    </div>

    <!-- 此电脑 -->
    <div class="window" id="computer-window">
        <div class="window-titlebar"><span class="window-title">此电脑</span><div class="window-controls"><button onclick="minimizeWindow('computer')">─</button><button onclick="closeWindow('computer')">✕</button></div></div>
        <div class="window-content">
            <p style="padding:20px;">📁 本地磁盘 (C:)</p>
            <p style="padding:0 20px;">📁 文档</p>
            <p style="padding:0 20px;">📁 图片</p>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 回收站 -->
    <div class="window" id="recycle-window">
        <div class="window-titlebar"><span class="window-title">回收站</span><div class="window-controls"><button onclick="minimizeWindow('recycle')">─</button><button onclick="closeWindow('recycle')">✕</button></div></div>
        <div class="window-content"><p style="padding:20px;color:#666;">回收站是空的。</p></div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 浏览器 -->
    <div class="window" id="browser-window" style="width:900px; height:600px;">
        <div class="window-titlebar"><span class="window-title">浏览器</span><div class="window-controls"><button onclick="minimizeWindow('browser')">─</button><button onclick="closeWindow('browser')">✕</button></div></div>
        <div class="window-content" style="display:flex; flex-direction:column;">
            <div class="browser-toolbar">
                <div class="browser-url-wrapper">
                    <input type="text" class="browser-url" id="browser-url" placeholder="输入网址..." onkeypress="if(event.key==='Enter')navigateBrowser()">
                    <button class="browser-go-btn" onclick="navigateBrowser()" title="搜索网页">🔍</button>
                </div>
            </div>
            <div class="browser-view" id="browser-view">
                <div style="text-align:center;color:#999;"><div style="font-size:48px;margin-bottom:20px;">🔍</div><div style="font-size:16px;">请在地址栏输入网址以访问</div></div>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 记事本 -->
    <div class="window" id="notepad-window" style="width:600px; height:450px;">
        <div class="window-titlebar"><span class="window-title">记事本</span><div class="window-controls"><button onclick="minimizeWindow('notepad')">─</button><button onclick="closeWindow('notepad')">✕</button></div></div>
        <div class="window-content" style="display:flex; flex-direction:column;">
            <div class="notepad-menubar">
                <span>文件(F)</span><span>编辑(E)</span><span>格式(O)</span><span>查看(V)</span><span>帮助(H)</span>
            </div>
            <textarea class="notepad-textarea" readonly>http://www.terragroup.com
www.toutiaoxinwen.com
www.oracle.com</textarea>
            <div class="notepad-statusbar"><span>第1行, 第1列</span><span>100%</span></div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 邮箱 -->
    <div class="window" id="mail-window" style="width:1200px; height:800px;">
        <div class="window-titlebar"><span class="window-title">邮箱 - Terra Mail</span><div class="window-controls"><button onclick="minimizeWindow('mail')">─</button><button onclick="closeWindow('mail')">✕</button></div></div>
        <div class="window-content">
            <div class="mail-layout">
                <div class="mail-sidebar">
                    <div class="mail-folder active">收件箱</div>
                    <div class="mail-folder">已发送</div>
                    <div class="mail-folder">草稿箱</div>
                    <div class="mail-folder">垃圾邮件</div>
                </div>
                <div class="mail-main">
                    <div class="mail-list" id="mail-list">
                        <div class="mail-item active" onclick="showMail('welcome')">
                            <div class="subject">欢迎加入 Terra Group</div>
                            <div class="from">Terra Group 人力资源部</div>
                            <div class="preview">尊敬的员工，欢迎您加入泰拉集团...</div>
                        </div>
                        <div class="mail-item" onclick="showMail('security')">
                            <div class="subject">⚠️ 安全警告：立即修改密码</div>
                            <div class="from">Terra Group 信息安全中心</div>
                            <div class="preview">我们发现您的账号存在异常登录活动...</div>
                        </div>
                    </div>
                    <div class="mail-preview" id="mail-preview">
                        <div class="subject">欢迎加入 Terra Group</div>
                        <div class="meta">发件人：Terra Group 人力资源部 &lt;hr@terragroup.com&gt; | 2025年10月1日</div>
                        <div class="body">
                            尊敬的员工，<br><br>
                            欢迎您正式加入 Terra Group 国际控股公司。我们致力于通过科学技术重塑世界，期待您为这一使命贡献力量。<br><br>
                            您的初始登录凭据为：<br>
                            用户名：employee001<br>
                            密码：welcome123<br><br>
                            请在首次登录后立即修改密码。如有疑问，请联系 IT 支持。<br><br>
                            此致<br>
                            Terra Group 人力资源部
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 微信 -->
    <div class="window" id="wechat-window" style="width:800px; height:550px;">
        <div class="window-titlebar"><span class="window-title">微信</span><div class="window-controls"><button onclick="minimizeWindow('wechat')">─</button><button onclick="closeWindow('wechat')">✕</button></div></div>
        <div class="window-content">
            <div class="wechat-layout">
                <div class="wechat-sidebar">
                    <div class="wechat-profile">张三</div>
                    <div class="wechat-contacts">
                        <div class="wechat-contact active">
                            <div class="wechat-avatar">李</div>
                            <span>李四</span>
                        </div>
                        <div class="wechat-contact">
                            <div class="wechat-avatar">王</div>
                            <span>王五</span>
                        </div>
                        <div class="wechat-contact">
                            <div class="wechat-avatar">赵</div>
                            <span>赵六</span>
                        </div>
                    </div>
                </div>
                <div class="wechat-chat-area">
                    <div class="wechat-chat-header">李四</div>
                    <div class="wechat-messages">
                        <div style="margin-bottom:10px;"><strong>李四：</strong>你好，这个项目进展如何？</div>
                        <div style="margin-bottom:10px;"><strong>我：</strong>一切顺利，明天可以上线。</div>
                        <div style="margin-bottom:10px;"><strong>李四：</strong>太好了，记得检查一下 Oracle 页面。</div>
                    </div>
                    <div class="wechat-input-area">
                        <input type="text" class="wechat-input" placeholder="输入消息...">
                        <button class="wechat-send-btn">发送</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 逃离塔科夫 -->
    <div class="window" id="tarkov-window" style="width:400px; height:300px;">
        <div class="window-titlebar"><span class="window-title">逃离塔科夫</span><div class="window-controls"><button onclick="closeWindow('tarkov')">✕</button></div></div>
        <div class="window-content">
            <div class="tarkov-loading" id="tarkov-loading">
                <div class="tarkov-spinner"></div>
                <div>正在加载...</div>
            </div>
            <div class="tarkov-warning" id="tarkov-warning">
                <div class="icon">⚠️</div>
                <div class="text">严重错误228<br>你不准逃离塔科夫！</div>
                <button onclick="closeWindow('tarkov')">确认</button>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>

    <!-- 任务栏 -->
    <div class="taskbar">
        <button class="start-btn"><img src="/static/desktop-windows.png" alt="开始"></button>
        <div class="taskbar-icons" id="taskbar-icons"></div>
        <div class="taskbar-right">
            <div class="time" id="clock-time"></div>
            <div class="date" id="clock-date"></div>
        </div>
    </div>

    <script>
        let zIndexCounter = 500;
        let activeWindows = {};
        let currentFocus = null;
        let tarkovTimer = null;
        let browserResetTimer = null;

        const iconMap = {
            computer: '/static/desktop-mycomputer.ico',
            recycle: '/static/desktop-recyclebin.ico',
            browser: '/static/desktop-chrome.ico',
            notepad: '/static/desktop-notepad.ico',
            mail: '/static/desktop-mail.ico',
            wechat: '/static/wechat.png',
            tarkov: '/static/desktop-EscapeFromTarkov.ico'
        };

        const VALID_URLS = [
            'http://www.terragroup.com',
            'https://www.terragroup.com',
            'www.terragroup.com',
            'http://www.toutiaoxinwen.com',
            'https://www.toutiaoxinwen.com',
            'www.toutiaoxinwen.com',
            'http://www.oracle.com',
            'https://www.oracle.com',
            'www.oracle.com'
        ];

        const mailData = {
            welcome: {
                subject: '欢迎加入 Terra Group',
                from: 'Terra Group 人力资源部 <hr@terragroup.com>',
                date: '2025年10月1日',
                body: `尊敬的员工，<br><br>
                    欢迎您正式加入 Terra Group 国际控股公司。我们致力于通过科学技术重塑世界，期待您为这一使命贡献力量。<br><br>
                    您的初始登录凭据为：<br>
                    用户名：employee001<br>
                    密码：welcome123<br><br>
                    请在首次登录后立即修改密码。如有疑问，请联系 IT 支持。<br><br>
                    此致<br>
                    Terra Group 人力资源部`
            },
            security: {
                subject: '⚠️ 安全警告：立即修改密码',
                from: 'Terra Group 信息安全中心 <security@terragroup.com>',
                date: '2025年10月12日',
                body: `您好，<br><br>
                    我们检测到您的账号在诺文斯克地区存在异常登录活动。作为安全预防措施，请立即修改您的密码。<br><br>
                    请访问内部系统 <strong style="user-select: text;">http://www.terragroup.com</strong> 并按照提示操作。如果您无法登录，请直接联系 IT 支持。<br><br>
                    为了您的账户安全，此链接将在24小时后过期。<br><br>
                    此致<br>
                    Terra Group 信息安全中心`
            }
        };

        function centerWindow(win) {
            const taskbarHeight = 48;
            const winWidth = win.offsetWidth;
            const winHeight = win.offsetHeight;
            const screenWidth = window.innerWidth;
            const screenHeight = window.innerHeight;
            const left = Math.max(0, (screenWidth - winWidth) / 2);
            const top = Math.max(0, (screenHeight - taskbarHeight - winHeight) / 2);
            win.style.left = left + 'px';
            win.style.top = top + 'px';
        }

        function createTaskbarIcon(name) {
            if (!activeWindows[name]) {
                const taskIcon = document.createElement('div');
                taskIcon.className = 'taskbar-icon';
                taskIcon.title = name;
                const img = document.createElement('img');
                img.src = iconMap[name] || '/static/desktop-mycomputer.ico';
                img.alt = name;
                taskIcon.appendChild(img);
                taskIcon.onclick = () => focusWindow(name);
                document.getElementById('taskbar-icons').appendChild(taskIcon);
                activeWindows[name] = taskIcon;
            }
        }

        function resetBrowserView() {
            const view = document.getElementById('browser-view');
            if (view) view.innerHTML = `<div style="text-align:center;color:#999;"><div style="font-size:48px;margin-bottom:20px;">🔍</div><div style="font-size:16px;">请在地址栏输入网址以访问</div></div>`;
        }

        function fullResetBrowser() {
            resetBrowserView();
            const urlInput = document.getElementById('browser-url');
            if (urlInput) urlInput.value = '';
        }

        function navigateBrowser() {
            const urlInput = document.getElementById('browser-url');
            const view = document.getElementById('browser-view');
            if (!urlInput || !view) return;
            const input = urlInput.value.trim().toLowerCase();
            if (browserResetTimer) { clearTimeout(browserResetTimer); browserResetTimer = null; }

            if (!VALID_URLS.includes(input)) {
                view.innerHTML = `<div style="text-align:center;color:#c00;"><div style="font-size:48px;margin-bottom:20px;">⚠️</div><div style="font-size:16px;">无法访问该网页</div><div style="font-size:13px;color:#666;margin-top:10px;">请检查网址是否正确</div></div>`;
                browserResetTimer = setTimeout(() => resetBrowserView(), 5000);
                return;
            }

            let target = '/home/';
            if (input.includes('toutiaoxinwen')) target = '/news-portal/';
            else if (input.includes('oracle')) target = '/oracle/';

            window.open(target, '_blank');
            view.innerHTML = `<div style="text-align:center;color:#0066cc;"><div style="font-size:48px;margin-bottom:20px;">🚀</div><div style="font-size:16px;">正在跳转到 ${input} ...</div></div>`;
            browserResetTimer = setTimeout(() => resetBrowserView(), 5000);
        }

        function showMail(mailId) {
            const data = mailData[mailId];
            if (!data) return;
            document.querySelectorAll('#mail-list .mail-item').forEach(item => item.classList.remove('active'));
            const targetItem = document.querySelector(`#mail-list .mail-item[onclick="showMail('${mailId}')"]`);
            if (targetItem) targetItem.classList.add('active');
            document.getElementById('mail-preview').innerHTML = `<div class="subject">${data.subject}</div><div class="meta">发件人：${data.from} | ${data.date}</div><div class="body">${data.body}</div>`;
        }

        function updateTaskbarActive() {
            for (const [name, icon] of Object.entries(activeWindows)) {
                if (name === currentFocus) icon.classList.add('active');
                else icon.classList.remove('active');
            }
        }

        function openWindow(name) {
            if (name === 'tarkov') {
                const win = document.getElementById('tarkov-window');
                if (!win) return;
                if (win.style.display === 'flex') { focusWindow('tarkov'); return; }
                if (win.style.display === 'none' && activeWindows[name]) { win.style.display='flex'; win.style.zIndex=++zIndexCounter; focusWindow(name); return; }
                document.getElementById('tarkov-loading').style.display = 'flex';
                document.getElementById('tarkov-warning').style.display = 'none';
                win.style.display = 'flex'; win.style.zIndex = ++zIndexCounter;
                centerWindow(win); createTaskbarIcon('tarkov'); focusWindow('tarkov');
                if (tarkovTimer) clearTimeout(tarkovTimer);
                tarkovTimer = setTimeout(() => {
                    document.getElementById('tarkov-loading').style.display = 'none';
                    document.getElementById('tarkov-warning').style.display = 'flex';
                }, 5000);
                return;
            }

            const win = document.getElementById(name + '-window');
            if (!win) return;
            if (win.style.display === 'flex') { focusWindow(name); return; }
            if (win.style.display === 'none' && activeWindows[name]) { win.style.display='flex'; win.style.zIndex=++zIndexCounter; focusWindow(name); return; }
            win.style.display = 'flex'; win.style.zIndex = ++zIndexCounter;
            centerWindow(win);
            if (name === 'browser') fullResetBrowser();
            createTaskbarIcon(name);
            focusWindow(name);
        }

        function focusWindow(name) {
            const win = document.getElementById(name + '-window');
            if (!win) return;
            if (win.style.display === 'none') { win.style.display = 'flex'; win.style.zIndex = ++zIndexCounter; }
            else { win.style.zIndex = ++zIndexCounter; }
            if (currentFocus !== name) { currentFocus = name; updateTaskbarActive(); }
        }

        function minimizeWindow(name) { document.getElementById(name + '-window').style.display = 'none'; if (currentFocus === name) { currentFocus = null; updateTaskbarActive(); } }

        function closeWindow(name) {
            document.getElementById(name + '-window').style.display = 'none';
            if (activeWindows[name]) { activeWindows[name].remove(); delete activeWindows[name]; }
            if (currentFocus === name) { currentFocus = null; updateTaskbarActive(); }
            if (name === 'tarkov' && tarkovTimer) { clearTimeout(tarkovTimer); tarkovTimer = null; }
            if (name === 'browser' && browserResetTimer) { clearTimeout(browserResetTimer); browserResetTimer = null; }
        }

        // 拖动
        document.querySelectorAll('.window').forEach(win => {
            const titlebar = win.querySelector('.window-titlebar');
            let offsetX, offsetY, isDragging = false;
            titlebar.addEventListener('mousedown', (e) => {
                isDragging = true;
                const winId = win.id.replace('-window', '');
                focusWindow(winId);
                win.style.zIndex = ++zIndexCounter;
                offsetX = e.clientX - win.offsetLeft; offsetY = e.clientY - win.offsetTop;
                document.addEventListener('mousemove', onMouseMove);
                document.addEventListener('mouseup', onMouseUp);
            });
            function onMouseMove(e) { if (!isDragging) return; win.style.left = (e.clientX - offsetX) + 'px'; win.style.top = (e.clientY - offsetY) + 'px'; }
            function onMouseUp() { isDragging = false; document.removeEventListener('mousemove', onMouseMove); document.removeEventListener('mouseup', onMouseUp); }
            win.addEventListener('mousedown', (e) => { if (e.target.closest('.resize-handle')) return; const winId = win.id.replace('-window', ''); focusWindow(winId); });
        });

        // 调整大小
        document.querySelectorAll('.resize-handle').forEach(handle => {
            const win = handle.closest('.window');
            handle.addEventListener('mousedown', (e) => {
                e.stopPropagation(); e.preventDefault();
                const startX = e.clientX, startY = e.clientY;
                const startLeft = win.offsetLeft, startTop = win.offsetTop;
                const startWidth = win.offsetWidth, startHeight = win.offsetHeight;
                const handleClass = handle.className;
                function onResizeMove(e) {
                    const dx = e.clientX - startX, dy = e.clientY - startY;
                    let newWidth = startWidth, newHeight = startHeight;
                    let newLeft = startLeft, newTop = startTop;
                    if (handleClass.includes('right')) newWidth = Math.max(300, startWidth + dx);
                    if (handleClass.includes('left')) { newWidth = Math.max(300, startWidth - dx); newLeft = startLeft + dx; }
                    if (handleClass.includes('bottom')) newHeight = Math.max(200, startHeight + dy);
                    if (handleClass.includes('top')) { newHeight = Math.max(200, startHeight - dy); newTop = startTop + dy; }
                    win.style.width = newWidth + 'px'; win.style.height = newHeight + 'px';
                    if (handleClass.includes('left') || handleClass.includes('right')) win.style.left = newLeft + 'px';
                    if (handleClass.includes('top') || handleClass.includes('bottom')) win.style.top = newTop + 'px';
                }
                function onResizeUp() { document.removeEventListener('mousemove', onResizeMove); document.removeEventListener('mouseup', onResizeUp); }
                document.addEventListener('mousemove', onResizeMove);
                document.addEventListener('mouseup', onResizeUp);
            });
        });

        // 时钟
        function updateClock() {
            const now = new Date();
            document.getElementById('clock-time').textContent = now.toLocaleTimeString('zh-CN', { hour12: false });
            document.getElementById('clock-date').textContent = now.toLocaleDateString('zh-CN');
        }
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
    '''

# ========== 泰拉集团主页（/home/） ==========
@app.route('/home/')
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
        @font-face { font-family:'Versa'; src:url('/static/fonts/Versa.woff2') format('woff2'); font-weight:normal; font-style:normal; font-display:swap; }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background-color:#f4f7fb; color:#1a2a3a; font-family:'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif; line-height:1.6; }
        nav { position:fixed; top:0; width:100%; z-index:1000; border-bottom:1px solid rgba(255,255,255,0.2); background:transparent; transition:background 0.4s; }
        nav:hover { background:rgba(255,255,255,0.95); border-bottom:1px solid #e0e7ef; }
        .nav-top { display:flex; justify-content:center; align-items:center; padding:14px 60px; background:transparent; backdrop-filter:blur(10px); overflow:hidden; transition:all 0.3s; box-shadow:0 2px 12px rgba(0,0,0,0.05); }
        .nav-top.hide-logo { max-height:0; padding-top:0; padding-bottom:0; opacity:0; box-shadow:none; }
        .nav-logo { height:44px; width:auto; }
        .nav-bottom { position:relative; display:flex; justify-content:center; align-items:center; padding:18px 60px; background:transparent; backdrop-filter:blur(10px); transition:background 0.4s, box-shadow 0.4s; box-shadow:0 2px 12px rgba(0,0,0,0.05); }
        .bottom-logo { position:absolute; left:60px; top:50%; transform:translateY(-50%); height:34px; width:auto; display:none; z-index:2; }
        .nav-top.hide-logo ~ .nav-bottom .bottom-logo { display:block; }
        .search-box { position:absolute; right:60px; top:50%; transform:translateY(-50%); display:flex; align-items:center; gap:8px; width:280px; padding:7px 18px; border:1px solid rgba(255,255,255,0.8); border-radius:24px; background:rgba(255,255,255,0.25); backdrop-filter:blur(4px); cursor:pointer; transition:0.3s; text-decoration:none; z-index:2; }
        .search-box:hover { border-color:#fff; background:rgba(255,255,255,0.35); }
        .search-box .search-icon { font-size:18px; color:#fff; }
        .search-box span { font-size:16px; color:#fff; text-shadow:0 1px 3px rgba(0,0,0,0.6); }
        .nav-links { display:flex; gap:0; align-items:center; }
        .nav-links a { color:#fff; text-decoration:none; font-size:17px; font-weight:600; text-shadow:0 0 2px rgba(0,0,0,0.8),0 1px 4px rgba(0,0,0,0.7); transition:0.3s; }
        .nav-links a:hover { color:#00d4ff; }
        .nav-links a:not(:last-child)::after { content:"|"; margin-left:28px; margin-right:28px; color:inherit; opacity:0.6; }
        .nav-top.hide-logo ~ .nav-bottom { background:rgba(255,255,255,0.95)!important; backdrop-filter:blur(10px); box-shadow:0 2px 12px rgba(0,0,0,0.1); }
        .nav-top.hide-logo ~ .nav-bottom .nav-links a { color:#4a5c6c; text-shadow:none; }
        .nav-top.hide-logo ~ .nav-bottom .nav-links a:hover { color:#0066cc; }
        .nav-top.hide-logo ~ .nav-bottom .search-box { border-color:#b0bec5; background:#fff; box-shadow:0 2px 8px rgba(0,0,0,0.06); }
        .nav-top.hide-logo ~ .nav-bottom .search-box .search-icon { color:#0066cc; }
        .nav-top.hide-logo ~ .nav-bottom .search-box span { color:#5e6f82; text-shadow:none; }
        nav:hover .nav-bottom { background:transparent; box-shadow:0 2px 12px rgba(0,0,0,0.12); }
        nav:hover .nav-links a { color:#4a5c6c; text-shadow:none; }
        nav:hover .nav-links a:hover { color:#0066cc; }
        nav:hover .search-box { border-color:#b0bec5; background:#fff; box-shadow:0 2px 8px rgba(0,0,0,0.06); }
        nav:hover .search-box:hover { border-color:#0066cc; }
        nav:hover .search-box .search-icon { color:#0066cc; }
        nav:hover .search-box span { color:#5e6f82; text-shadow:none; }
        .section { padding:100px 60px 80px; max-width:1200px; margin:0 auto; }
        .hero { min-height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; position:relative; overflow:hidden; }
        .bg-video { position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index:0; }
        .overlay { position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.35); z-index:1; }
        .scroll-hint { position:absolute; bottom:30px; left:50%; transform:translateX(-50%); font-size:40px; color:rgba(255,255,255,0.8); text-shadow:0 2px 8px rgba(0,0,0,0.5); z-index:2; animation:bounce 2s infinite; cursor:default; user-select:none; }
        @keyframes bounce { 0%,20%,50%,80%,100%{ transform:translateX(-50%) translateY(0); } 40%{ transform:translateX(-50%) translateY(-15px); } 60%{ transform:translateX(-50%) translateY(-8px); } }
        .hero h1 { font-size:clamp(48px,10vw,90px); font-weight:800; letter-spacing:8px; color:#fff; text-shadow:-2px -2px 0 #000,2px -2px 0 #000,-2px 2px 0 #000,2px 2px 0 #000,0 0 8px rgba(0,0,0,0.8); margin-bottom:16px; position:relative; z-index:2; text-transform:uppercase; font-family:'Versa','Orbitron','Michroma',sans-serif; }
        .hero p.tagline { font-size:22px; letter-spacing:4px; color:rgba(255,255,255,0.95); text-shadow:0 2px 8px rgba(0,0,0,0.5); margin-bottom:40px; position:relative; z-index:2; font-family:'Georgia','Times New Roman',serif; font-style:italic; }
        .hero .btn { border:2px solid #fff; color:#fff; padding:14px 48px; font-size:16px; letter-spacing:4px; background:rgba(0,0,0,0.3); backdrop-filter:blur(4px); cursor:default; text-transform:uppercase; border-radius:4px; transition:0.3s; display:inline-block; user-select:none; position:relative; z-index:2; }
        .hero .btn:hover { background:rgba(255,255,255,0.2); border-color:#00b4d8; color:#00b4d8; }
        .about-subtitle { text-align:center; font-size:18px; color:#a0a8b5; font-family:'Helvetica Neue','Arial',sans-serif; font-weight:500; letter-spacing:2px; margin-bottom:0; }
        .about-title { text-align:center; font-size:56px; letter-spacing:2px; margin-bottom:6px; font-weight:700; color:#0b2b44; }
        .about-box { display:flex; background:#fff; border-radius:20px; box-shadow:0 12px 36px rgba(0,0,0,0.08); overflow:hidden; margin-top:40px; min-height:380px; }
        .about-img { width:48%; object-fit:cover; flex-shrink:0; }
        .about-content { padding:56px; display:flex; flex-direction:column; justify-content:center; }
        .about-content p { font-size:17px; color:#4a5c6c; line-height:1.8; margin-bottom:28px; }
        .more-btn { display:inline-flex; align-items:center; justify-content:center; background-color:#0066cc; color:#fff; border:none; border-radius:8px; padding:14px 28px; font-size:18px; font-weight:600; cursor:pointer; text-decoration:none; transition:0.3s; position:relative; align-self:flex-start; height:52px; }
        .more-btn .arrow-icon { font-size:30px; font-weight:900; line-height:1; transition:0.3s; order:0; margin-top:-6px; }
        .more-btn .btn-text { max-width:0; overflow:hidden; white-space:nowrap; transition:max-width 0.4s, margin 0.3s, opacity 0.3s; opacity:0; margin-left:0; order:1; }
        .more-btn:hover .btn-text { max-width:120px; opacity:1; margin-left:10px; }
        .more-btn:hover .arrow-icon { order:1; margin-left:0; margin-top:-6px; }
        .more-btn:hover .btn-text { order:0; }
        .news-list { display:flex; flex-direction:column; gap:24px; margin-top:40px; }
        .news-item { border-left:4px solid #0077b6; padding-left:28px; background:#fff; padding:24px 28px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.02); transition:border-color 0.3s; }
        .news-item:hover { border-left-color:#00b4d8; }
        .news-date { font-size:13px; color:#8393a5; letter-spacing:2px; margin-bottom:6px; }
        .news-title { font-size:20px; font-weight:600; color:#0b2b44; }
        .news-title a { text-decoration:none; color:inherit; }
        .news-title a:hover { color:#0066cc; }
        .news-desc { font-size:15px; color:#4a5c6c; margin-top:8px; }
        footer { text-align:center; padding:60px 20px 40px; border-top:1px solid #dce3eb; background:#fff; }
        footer p { color:#8393a5; font-size:13px; }
    </style>
</head>
<body>
    <nav id="mainNav">
        <div class="nav-top" id="navTop"><img src="/static/terralogo.png" alt="Terra Group Logo" class="nav-logo"></div>
        <div class="nav-bottom">
            <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            <a href="#" class="search-box" id="searchLink"><span class="search-icon">🔍</span><span>搜索</span></a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="hero" id="heroSection">
        <video autoplay muted loop playsinline class="bg-video">
            <source src="/static/background.mp4" type="video/mp4">
            <img src="/static/background.jpg" alt="背景">
        </video>
        <div class="overlay"></div>
        <h1>TERRAGROUP</h1>
        <p class="tagline">Virtus in Scientia</p>
        <span class="btn">探索我们的研究</span>
        <div class="scroll-hint">↓</div>
    </div>

    <div class="section" style="max-width:1400px;">
        <p class="about-subtitle">ABOUT TERRAGROUP</p>
        <h2 class="about-title">走进泰拉</h2>
        <div class="about-box">
            <img src="/static/about-preview.jpg" alt="走进泰拉" class="about-img">
            <div class="about-content">
                <p>
                    泰拉集团（Terra Group）成立于1998年，总部位于英国，是一家业务遍及全球120多个国家的跨国巨头。我们以“Virtus in Scientia”（潜心科研）为核心理念，专注农业生物技术、前沿科技研究与全球基础设施建设。集团旗下拥有40余家大型企业，从诺文斯克到刚果，我们以科学的力量重塑未来。
                </p>
                <a href="/about/" class="more-btn"><span class="arrow-icon">→</span><span class="btn-text">了解更多</span></a>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 style="font-size:32px; letter-spacing:3px;">新闻动态</h2>
        <div class="news-list">
            <div class="news-item"><div class="news-date">2025.10.12</div><div class="news-title"><a href="/news/2025-10-12/">Terra Group Labs 在诺文斯克新建三级生物实验室</a></div><div class="news-desc">该实验室将专注于传染病学研究，进一步强化集团在全球公共卫生领域的领导地位。</div></div>
            <div class="news-item"><div class="news-date">2025.09.28</div><div class="news-title"><a href="/news/2025-09-28/">集团与 USEC 国际安保续签战略合作协议</a></div><div class="news-desc">USEC 将继续为泰拉集团在全球的资产及人员提供安全保障服务。</div></div>
            <div class="news-item"><div class="news-date">2025.08.15</div><div class="news-title"><a href="/news/2025-08-15/">刚果（金）矿业项目顺利投产</a></div><div class="news-desc">该矿区的稀土与铀矿开采将为清洁能源与医疗同位素供应提供关键原料。</div></div>
        </div>
    </div>

    <footer><p>© 2026 Terra Group International. All rights reserved.</p></footer>

    <script>
        const nav = document.getElementById('mainNav'); const navTop = document.getElementById('navTop'); const hero = document.getElementById('heroSection'); const searchLink = document.getElementById('searchLink');
        function updateHeroPadding() { const navHeight = nav.offsetHeight; if (hero) hero.style.paddingTop = navHeight + 'px'; }
        if (hero) { updateHeroPadding(); window.addEventListener('resize', updateHeroPadding); }
        function handleScroll() { const scrollY = window.scrollY; if (scrollY > 100) navTop.classList.add('hide-logo'); else if (scrollY <= 5) navTop.classList.remove('hide-logo'); }
        window.addEventListener('scroll', handleScroll); handleScroll();
        searchLink.addEventListener('click', function(e) { e.preventDefault(); console.log('搜索功能暂未开放'); });
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
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/" style="color: #0066cc;">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
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
            <a href="/home/">← 返回首页</a>
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
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/" style="color: #0066cc;">招贤纳士</a>
                <a href="/contact/">联系我们</a>
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
            <a href="/home/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

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
        .news-title a {
            text-decoration: none;
            color: inherit;
        }
        .news-title a:hover {
            color: #0066cc;
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
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/" style="color: #0066cc;">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
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
                <div class="news-title"><a href="/news/2025-10-12/">Terra Group Labs 在诺文斯克新建三级生物实验室</a></div>
                <div class="news-desc">该实验室将专注于传染病学研究，进一步强化集团在全球公共卫生领域的领导地位。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.09.28</div>
                <div class="news-title"><a href="/news/2025-09-28/">集团与 USEC 国际安保续签战略合作协议</a></div>
                <div class="news-desc">USEC 将继续为泰拉集团在全球的资产及人员提供安全保障服务。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.08.15</div>
                <div class="news-title"><a href="/news/2025-08-15/">刚果（金）矿业项目顺利投产</a></div>
                <div class="news-desc">该矿区的稀土与铀矿开采将为清洁能源与医疗同位素供应提供关键原料。</div>
            </div>
            <div class="news-item">
                <div class="news-date">2025.07.02</div>
                <div class="news-title"><a href="/news/2025-07-02/">泰拉集团发布2025年度可持续发展报告</a></div>
                <div class="news-desc">报告强调了集团在环境保护、社区共建及科研伦理方面的承诺与进展。</div>
            </div>
        </div>

        <p style="margin-top: 40px;">
            <a href="/home/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/products/')
def products():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>产品与服务 | Terra Group</title>
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
            max-width: 1200px;
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
        .service-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 32px;
            margin-top: 40px;
            justify-content: center;
        }
        .service-card {
            background: #ffffff;
            border: 1px solid #dce3eb;
            border-radius: 16px;
            padding: 40px 28px;
            flex: 1;
            min-width: 260px;
            max-width: 340px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
            transition: transform 0.3s, box-shadow 0.3s;
            text-align: center;
        }
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0,102,204,0.12);
        }
        .service-icon {
            font-size: 48px;
            margin-bottom: 20px;
        }
        .service-card h3 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 12px;
            color: #0b2b44;
        }
        .service-card p {
            font-size: 15px;
            color: #5e6f82;
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
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/" style="color: #0066cc;">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>我们的产品与服务</h1>
        <p style="font-size: 18px; color: #4a5c6c; line-height: 1.8; margin-bottom: 20px;">
            泰拉集团依托全球120多个国家的业务网络，为合作伙伴提供多元化的高科技产品与综合解决方案。
        </p>

        <div class="service-grid">
            <div class="service-card">
                <div class="service-icon">🌾</div>
                <h3>农业生物技术</h3>
                <p>基因编辑作物、抗逆品种培育、精准农业解决方案，保障全球粮食安全。</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🧪</div>
                <h3>前沿科技研究</h3>
                <p>超导材料、量子通信、神经接口等尖端技术，推动人类认知边界。</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🏗️</div>
                <h3>全球基础设施</h3>
                <p>港口、电站、物流网络建设，为新兴经济特区提供全套基础设施服务。</p>
            </div>
            <div class="service-card">
                <div class="service-icon">💻</div>
                <h3>信息技术与安全</h3>
                <p>大数据分析、网络安全、企业级云解决方案，守护数字资产。</p>
            </div>
            <div class="service-card">
                <div class="service-icon">⚕️</div>
                <h3>医疗健康</h3>
                <p>先进医疗器械、传染病防控、远程医疗系统，提升全球公共卫生水平。</p>
            </div>
            <div class="service-card">
                <div class="service-icon">⛏️</div>
                <h3>资源开发</h3>
                <p>稀土开采、清洁能源、矿产供应链管理，驱动绿色未来。</p>
            </div>
        </div>

        <p style="margin-top: 40px;">
            <a href="/home/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/contact/')
def contact():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>联系我们 | Terra Group</title>
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
        .contact-info {
            background: #ffffff;
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
            margin-bottom: 40px;
        }
        .contact-info h3 {
            font-size: 24px;
            color: #0b2b44;
            margin-bottom: 16px;
        }
        .contact-info p {
            font-size: 17px;
            color: #4a5c6c;
            margin-bottom: 12px;
        }
        .contact-form {
            background: #ffffff;
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #0b2b44;
        }
        input, textarea {
            width: 100%;
            padding: 12px 16px;
            border: 1px solid #dce3eb;
            border-radius: 8px;
            font-size: 16px;
            font-family: inherit;
            outline: none;
            transition: border-color 0.3s;
        }
        input:focus, textarea:focus {
            border-color: #0066cc;
        }
        .submit-btn {
            background-color: #0066cc;
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 14px 36px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }
        .submit-btn:hover {
            background-color: #0052a3;
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
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/" style="color: #0066cc;">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>联系我们</h1>
        <p style="font-size: 18px; color: #4a5c6c; line-height: 1.8; margin-bottom: 40px;">
            无论您是寻求合作、媒体咨询或客户服务，泰拉集团的专业团队随时为您服务。
        </p>

        <div class="contact-info">
            <h3>全球总部</h3>
            <p><strong>地址：</strong>英国伦敦金融城，Terra Group 大厦</p>
            <p><strong>电话：</strong>+44 20 7946 0958</p>
            <p><strong>邮箱：</strong>contact@terragroup.com</p>
            <h3 style="margin-top: 28px;">诺文斯克分部</h3>
            <p><strong>地址：</strong>诺文斯克经济特区，泰拉实验室</p>
            <p><strong>电话：</strong>+7 812 345 6789</p>
        </div>

        <div class="contact-form">
            <h3 style="margin-bottom: 24px;">发送消息</h3>
            <form action="#" method="post">
                <div class="form-group">
                    <label for="name">姓名</label>
                    <input type="text" id="name" name="name" placeholder="您的姓名">
                </div>
                <div class="form-group">
                    <label for="email">邮箱</label>
                    <input type="email" id="email" name="email" placeholder="your@email.com">
                </div>
                <div class="form-group">
                    <label for="message">留言</label>
                    <textarea id="message" name="message" rows="5" placeholder="请输入您的留言..."></textarea>
                </div>
                <button type="submit" class="submit-btn">发送</button>
            </form>
        </div>

        <p style="margin-top: 40px;">
            <a href="/home/">← 返回首页</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

# ========== 新闻详情页路由 ==========

@app.route('/news/2025-10-12/')
def news_2025_10_12():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terra Group Labs 在诺文斯克新建三级生物实验室 | 泰拉集团</title>
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
        .search-box:hover { border-color: #0066cc; }
        .search-box .search-icon { font-size: 18px; color: #0066cc; }
        .search-box span { font-size: 16px; color: #5e6f82; }
        .nav-links {
            display: flex; gap: 0; align-items: center;
        }
        .nav-links a {
            color: #4a5c6c; text-decoration: none;
            font-size: 17px; font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: #0066cc; }
        .nav-links a:not(:last-child)::after {
            content: "|"; margin-left: 28px; margin-right: 28px;
            color: #b0bec5; opacity: 0.6;
        }
        .container {
            max-width: 800px;
            margin: 120px auto 80px;
            padding: 0 40px;
        }
        .article-title {
            font-size: 36px;
            font-weight: 700;
            color: #0b2b44;
            margin-bottom: 12px;
        }
        .article-date {
            font-size: 14px;
            color: #8393a5;
            margin-bottom: 24px;
        }
        .article-body {
            font-size: 17px;
            color: #4a5c6c;
            line-height: 1.8;
        }
        .article-body p {
            margin-bottom: 16px;
        }
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid #dce3eb;
            background: #fff;
        }
        footer p { color: #8393a5; font-size: 13px; }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1 class="article-title">Terra Group Labs 在诺文斯克新建三级生物实验室</h1>
        <div class="article-date">2025年10月12日</div>
        <div class="article-body">
            <p>泰拉集团今日宣布，旗下核心研究机构 Terra Group Labs 已在诺文斯克经济特区内建成一座全新的三级生物安全实验室（BSL-3）。该实验室的落成标志着集团在传染病学研究领域迈入全新阶段，进一步巩固了其在全球公共卫生领域的领导地位。</p>
            <p>新实验室配备最先进的空气过滤系统和负压隔离装置，能够安全处理高致病性病原体。首席科学官表示，该设施将重点开展新型疫苗研发和抗病毒药物筛选，首批研究项目已获得集团内部专项基金支持。</p>
            <p>此次扩建也是泰拉集团对诺文斯克地区长期投资承诺的一部分，预计将创造超过200个高技能科研岗位。</p>
        </div>
        <p style="margin-top: 40px;">
            <a href="/news/">← 返回新闻中心</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/news/2025-09-28/')
def news_2025_09_28():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>集团与 USEC 国际安保续签战略合作协议 | 泰拉集团</title>
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
            left: 60px; top: 50%; transform: translateY(-50%);
            height: 34px; width: auto; display: block; z-index: 2;
        }
        .search-box {
            position: absolute;
            right: 60px; top: 50%; transform: translateY(-50%);
            display: flex; align-items: center; gap: 8px;
            width: 280px; padding: 7px 18px;
            border: 1px solid #b0bec5; border-radius: 24px;
            background: #ffffff; cursor: pointer; text-decoration: none;
            z-index: 2; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover { border-color: #0066cc; }
        .search-box .search-icon { font-size: 18px; color: #0066cc; }
        .search-box span { font-size: 16px; color: #5e6f82; }
        .nav-links {
            display: flex; gap: 0; align-items: center;
        }
        .nav-links a {
            color: #4a5c6c; text-decoration: none;
            font-size: 17px; font-weight: 600;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: #0066cc; }
        .nav-links a:not(:last-child)::after {
            content: "|"; margin-left: 28px; margin-right: 28px;
            color: #b0bec5; opacity: 0.6;
        }
        .container {
            max-width: 800px; margin: 120px auto 80px; padding: 0 40px;
        }
        .article-title {
            font-size: 36px; font-weight: 700; color: #0b2b44; margin-bottom: 12px;
        }
        .article-date { font-size: 14px; color: #8393a5; margin-bottom: 24px; }
        .article-body { font-size: 17px; color: #4a5c6c; line-height: 1.8; }
        .article-body p { margin-bottom: 16px; }
        footer {
            text-align: center; padding: 40px 20px;
            border-top: 1px solid #dce3eb; background: #fff;
        }
        footer p { color: #8393a5; font-size: 13px; }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1 class="article-title">集团与 USEC 国际安保续签战略合作协议</h1>
        <div class="article-date">2025年9月28日</div>
        <div class="article-body">
            <p>泰拉集团今日宣布，已与全球知名私人安保承包商 USEC 成功续签为期五年的战略合作协议。根据协议，USEC 将继续为泰拉集团在全球高风险地区的资产、人员及关键基础设施提供全方位的安全保障服务。</p>
            <p>此次续签扩大了合作范围，新增了诺文斯克经济特区的设施安保以及战略物资运输的护航服务。集团首席安全官表示，与 USEC 的长期合作是确保全球业务平稳运行的重要基石。</p>
            <p>USEC 方面承诺将部署最新型的监控与快速反应系统，以应对日益复杂的国际安全环境。</p>
        </div>
        <p style="margin-top: 40px;">
            <a href="/news/">← 返回新闻中心</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/news/2025-08-15/')
def news_2025_08_15():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>刚果（金）矿业项目顺利投产 | 泰拉集团</title>
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
            display: flex; justify-content: center; align-items: center;
            padding: 18px 60px;
            background: transparent; backdrop-filter: blur(10px);
        }
        .bottom-logo {
            position: absolute; left: 60px; top: 50%; transform: translateY(-50%);
            height: 34px; width: auto; display: block; z-index: 2;
        }
        .search-box {
            position: absolute; right: 60px; top: 50%; transform: translateY(-50%);
            display: flex; align-items: center; gap: 8px;
            width: 280px; padding: 7px 18px;
            border: 1px solid #b0bec5; border-radius: 24px;
            background: #ffffff; cursor: pointer; text-decoration: none;
            z-index: 2; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover { border-color: #0066cc; }
        .search-box .search-icon { font-size: 18px; color: #0066cc; }
        .search-box span { font-size: 16px; color: #5e6f82; }
        .nav-links {
            display: flex; gap: 0; align-items: center;
        }
        .nav-links a {
            color: #4a5c6c; text-decoration: none;
            font-size: 17px; font-weight: 600; transition: color 0.3s;
        }
        .nav-links a:hover { color: #0066cc; }
        .nav-links a:not(:last-child)::after {
            content: "|"; margin-left: 28px; margin-right: 28px;
            color: #b0bec5; opacity: 0.6;
        }
        .container {
            max-width: 800px; margin: 120px auto 80px; padding: 0 40px;
        }
        .article-title {
            font-size: 36px; font-weight: 700; color: #0b2b44; margin-bottom: 12px;
        }
        .article-date { font-size: 14px; color: #8393a5; margin-bottom: 24px; }
        .article-body { font-size: 17px; color: #4a5c6c; line-height: 1.8; }
        .article-body p { margin-bottom: 16px; }
        footer {
            text-align: center; padding: 40px 20px;
            border-top: 1px solid #dce3eb; background: #fff;
        }
        footer p { color: #8393a5; font-size: 13px; }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1 class="article-title">刚果（金）矿业项目顺利投产</h1>
        <div class="article-date">2025年8月15日</div>
        <div class="article-body">
            <p>泰拉集团在刚果（金）的综合性矿业项目今日正式投产。该矿区富含稀土元素及高品位铀矿，是集团全球资源开发战略的重要组成部分。项目采用了最新环保选矿工艺，显著降低了对周边生态的影响。</p>
            <p>投产后的矿区预计每年可提供数千吨稀土氧化物和数百吨铀精矿，不仅将为清洁能源与医疗同位素供应提供关键原料，还将为当地社区创造大量就业机会。集团表示，已与多家国际客户签订了长期供应协议。</p>
            <p>此外，配套的基础设施升级工程也已同步完成，包括一条专用铁路线和现代化的矿区宿舍，进一步提升了运营效率。</p>
        </div>
        <p style="margin-top: 40px;">
            <a href="/news/">← 返回新闻中心</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

@app.route('/news/2025-07-02/')
def news_2025_07_02():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>泰拉集团发布2025年度可持续发展报告 | 泰拉集团</title>
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
            display: flex; justify-content: center; align-items: center;
            padding: 18px 60px;
            background: transparent; backdrop-filter: blur(10px);
        }
        .bottom-logo {
            position: absolute; left: 60px; top: 50%; transform: translateY(-50%);
            height: 34px; width: auto; display: block; z-index: 2;
        }
        .search-box {
            position: absolute; right: 60px; top: 50%; transform: translateY(-50%);
            display: flex; align-items: center; gap: 8px;
            width: 280px; padding: 7px 18px;
            border: 1px solid #b0bec5; border-radius: 24px;
            background: #ffffff; cursor: pointer; text-decoration: none;
            z-index: 2; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .search-box:hover { border-color: #0066cc; }
        .search-box .search-icon { font-size: 18px; color: #0066cc; }
        .search-box span { font-size: 16px; color: #5e6f82; }
        .nav-links {
            display: flex; gap: 0; align-items: center;
        }
        .nav-links a {
            color: #4a5c6c; text-decoration: none;
            font-size: 17px; font-weight: 600; transition: color 0.3s;
        }
        .nav-links a:hover { color: #0066cc; }
        .nav-links a:not(:last-child)::after {
            content: "|"; margin-left: 28px; margin-right: 28px;
            color: #b0bec5; opacity: 0.6;
        }
        .container {
            max-width: 800px; margin: 120px auto 80px; padding: 0 40px;
        }
        .article-title {
            font-size: 36px; font-weight: 700; color: #0b2b44; margin-bottom: 12px;
        }
        .article-date { font-size: 14px; color: #8393a5; margin-bottom: 24px; }
        .article-body { font-size: 17px; color: #4a5c6c; line-height: 1.8; }
        .article-body p { margin-bottom: 16px; }
        footer {
            text-align: center; padding: 40px 20px;
            border-top: 1px solid #dce3eb; background: #fff;
        }
        footer p { color: #8393a5; font-size: 13px; }
    </style>
</head>
<body>
    <nav>
        <div class="nav-bottom">
            <a href="/home/" class="bottom-logo-link">
                <img src="/static/terralogo.png" alt="Logo" class="bottom-logo">
            </a>
            <a href="#" class="search-box">
                <span class="search-icon">🔍</span>
                <span>搜索</span>
            </a>
            <div class="nav-links">
                <a href="/products/">产品与服务</a>
                <a href="/about/">关于我们</a>
                <a href="/news/">新闻中心</a>
                <a href="/careers/">招贤纳士</a>
                <a href="/contact/">联系我们</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1 class="article-title">泰拉集团发布2025年度可持续发展报告</h1>
        <div class="article-date">2025年7月2日</div>
        <div class="article-body">
            <p>泰拉集团今日正式发布了《2025年度可持续发展报告》，全面阐述了集团在环境保护、社区共建及科研伦理方面的承诺与最新进展。报告显示，集团已提前实现2025年碳排放强度下降20%的目标。</p>
            <p>报告重点介绍了三个关键领域的成果：绿色采矿技术的推广使矿区水资源消耗降低了35%；“社区共建计划”累计投入超过2亿美元，用于改善诺文斯克地区的基础教育与医疗条件；内部伦理委员会全年审查并否决了12项存在潜在伦理争议的研究项目。</p>
            <p>集团首席执行官在报告致辞中强调：“科学的力量必须与责任同行。我们追求的不只是创新，更是对人类与地球的长期承诺。”</p>
        </div>
        <p style="margin-top: 40px;">
            <a href="/news/">← 返回新闻中心</a>
        </p>
    </div>

    <footer>
        <p>© 2026 Terra Group International. All rights reserved.</p>
    </footer>
</body>
</html>
    '''

# ========== 头条新闻网 ==========
@app.route('/news-portal/')
def news_portal():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>头条新闻网</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
            color: #1a2a3a;
        }
        .header {
            background: #ffffff;
            border-bottom: 1px solid #e0e7ef;
            padding: 12px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .logo {
            font-size: 28px;
            font-weight: 700;
            color: #cc0000;
            letter-spacing: 2px;
            margin-right: auto;
        }
        .search-area {
            display: flex;
            align-items: center;
            margin-right: 40px;
        }
        .search-input {
            width: 260px;                   /* 稍微加宽 */
            padding: 10px 16px;             /* 加大内边距 */
            border: 2px solid #cc0000;      /* 红色边框 */
            border-radius: 20px 0 0 20px;
            outline: none;
            font-size: 15px;
            transition: border-color 0.3s;
            height: 44px;                   /* 固定高度，与按钮对齐 */
        }
        .search-input:focus {
            border-color: #a30000;
        }
        .search-btn {
            padding: 10px 20px;             /* 与输入框等高 */
            background-color: #cc0000;
            color: white;
            border: 2px solid #cc0000;
            border-left: none;
            border-radius: 0 20px 20px 0;
            cursor: pointer;
            font-size: 15px;
            font-weight: 600;
            transition: background-color 0.3s;
            height: 44px;                   /* 固定高度对齐 */
            box-sizing: border-box;
        }
        .search-btn:hover {
            background-color: #a30000;
        }
        .nav-links {
            display: flex;
            gap: 30px;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: #cc0000; }
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }
        .headline {
            display: flex;
            gap: 30px;
            margin-bottom: 40px;
        }
        .headline-main {
            flex: 1;
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        .headline-main img {
            width: 100%;
            height: 350px;
            object-fit: cover;
        }
        .headline-text {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.8));
            padding: 40px 24px 24px;
            color: white;
        }
        .headline-text h2 {
            font-size: 32px;
            margin-bottom: 8px;
            font-weight: 700;
        }
        .headline-text p {
            font-size: 16px;
            opacity: 0.9;
        }
        .headline-side {
            width: 300px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .side-news {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .side-news h3 {
            font-size: 18px;
            margin-bottom: 6px;
            color: #0b2b44;
        }
        .side-news p {
            font-size: 14px;
            color: #5e6f82;
        }
        .section-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 20px;
            padding-left: 10px;
            border-left: 4px solid #cc0000;
        }
        .news-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 24px;
            margin-bottom: 40px;
        }
        .news-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(0,0,0,0.04);
            transition: transform 0.2s;
        }
        .news-card:hover { transform: translateY(-4px); }
        .news-card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        .news-card-content {
            padding: 16px;
        }
        .news-card-content h3 {
            font-size: 18px;
            margin-bottom: 8px;
            color: #0b2b44;
        }
        .news-card-content p {
            font-size: 14px;
            color: #5e6f82;
            line-height: 1.5;
        }
        footer {
            background: #fff;
            border-top: 1px solid #e0e7ef;
            text-align: center;
            padding: 20px;
            color: #8393a5;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">头条新闻网</div>
        <div class="search-area">
            <input type="text" class="search-input" placeholder="搜索新闻..." id="searchInput" onkeypress="if(event.key==='Enter')performSearch()">
            <button class="search-btn" onclick="performSearch()">搜索</button>
        </div>
        <div class="nav-links">
            <a href="#">国际</a>
            <a href="#">科技</a>
            <a href="#">财经</a>
            <a href="#">娱乐</a>
            <a href="#">体育</a>
        </div>
    </div>

    <div class="container">
        <!-- 头条新闻 -->
        <div class="headline">
            <div class="headline-main">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 400' fill='%23333'%3E%3Crect width='800' height='400' fill='%23444'/%3E%3Ctext x='50' y='220' font-size='24' fill='%23999'%3E头条新闻图片%3C/text%3E%3C/svg%3E" alt="头条">
                <div class="headline-text">
                    <h2>全球聚焦：2026 年科技峰会将在诺文斯克召开</h2>
                    <p>国际科技巨头齐聚，探讨人工智能、量子计算等前沿议题。</p>
                </div>
            </div>
            <div class="headline-side">
                <div class="side-news">
                    <h3>财经：全球股市震荡</h3>
                    <p>受国际局势影响，多国主要指数出现波动...</p>
                </div>
                <div class="side-news">
                    <h3>科技：新型电池突破</h3>
                    <p>续航能力提升50%，电动车行业迎来变革...</p>
                </div>
                <div class="side-news">
                    <h3>娱乐：年度大片定档</h3>
                    <p>科幻巨制《星辰坠落》将于暑期上映...</p>
                </div>
            </div>
        </div>

        <!-- 最新新闻 -->
        <div class="section-title">最新新闻</div>
        <div class="news-grid">
            <div class="news-card">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 200' fill='%23666'%3E%3Crect width='400' height='200' fill='%23666'/%3E%3Ctext x='30' y='110' fill='%23aaa' font-size='16'%3E新闻图片%3C/text%3E%3C/svg%3E" alt="">
                <div class="news-card-content">
                    <h3><a href="/news-portal/medical-accident/" style="color: inherit; text-decoration: none;">市中心医院发生严重医疗事故，多名患者受影响</a></h3>
                    <p>昨日晚间，市中心医院因设备故障导致多名重症患者治疗中断，卫生部门已介入调查。</p>
                </div>
            </div>
            <div class="news-card">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 200' fill='%23666'%3E%3Crect width='400' height='200' fill='%23666'/%3E%3Ctext x='30' y='110' fill='%23aaa' font-size='16'%3E新闻图片%3C/text%3E%3C/svg%3E" alt="">
                <div class="news-card-content">
                    <h3>诺文斯克经济特区建设加速</h3>
                    <p>基础设施投资增加，多个大型项目提前完工。</p>
                </div>
            </div>
            <div class="news-card">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 200' fill='%23666'%3E%3Crect width='400' height='200' fill='%23666'/%3E%3Ctext x='30' y='110' fill='%23aaa' font-size='16'%3E新闻图片%3C/text%3E%3C/svg%3E" alt="">
                <div class="news-card-content">
                    <h3>泰拉集团发布新研究：基因编辑新突破</h3>
                    <p>科学家成功培育出耐盐碱作物，有望缓解粮食危机。</p>
                </div>
            </div>
            <div class="news-card">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 200' fill='%23666'%3E%3Crect width='400' height='200' fill='%23666'/%3E%3Ctext x='30' y='110' fill='%23aaa' font-size='16'%3E新闻图片%3C/text%3E%3C/svg%3E" alt="">
                <div class="news-card-content">
                    <h3>太空探索：新望远镜传回首批图像</h3>
                    <p>观测到距离地球120亿光年的星系，引学界轰动。</p>
                </div>
            </div>
            <div class="news-card">
                <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 200' fill='%23666'%3E%3Crect width='400' height='200' fill='%23666'/%3E%3Ctext x='30' y='110' fill='%23aaa' font-size='16'%3E新闻图片%3C/text%3E%3C/svg%3E" alt="">
                <div class="news-card-content">
                    <h3>体育快讯：世界游泳锦标赛开幕</h3>
                    <p>中国队首日斩获两金，破亚洲纪录。</p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>© 2026 头条新闻网 | 传递最有价值的信息</p>
    </footer>

    <script>
        function performSearch() {
            const keyword = document.getElementById('searchInput').value.trim();
            if (keyword) {
                window.location.href = '/news-portal/search/?q=' + encodeURIComponent(keyword);
            } else {
                alert('请输入搜索关键词');
            }
        }
    </script>
</body>
</html>
    '''


# ========== 头条新闻网 - 医疗事故详情 ==========
@app.route('/news-portal/medical-accident/')
def news_medical_accident():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>市中心医院发生严重医疗事故 | 头条新闻网</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
            color: #1a2a3a;
        }
        .header {
            background: #ffffff;
            border-bottom: 1px solid #e0e7ef;
            padding: 12px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .logo {
            font-size: 28px;
            font-weight: 700;
            color: #cc0000;
            letter-spacing: 2px;
            margin-right: auto;
        }
        .search-area {
            display: flex;
            align-items: center;
            margin-right: 40px;
        }
        .search-input {
            width: 260px;
            padding: 10px 16px;
            border: 2px solid #cc0000;
            border-radius: 20px 0 0 20px;
            outline: none;
            font-size: 15px;
            transition: border-color 0.3s;
            height: 44px;
        }
        .search-input:focus {
            border-color: #a30000;
        }
        .search-btn {
            padding: 10px 20px;
            background-color: #cc0000;
            color: white;
            border: 2px solid #cc0000;
            border-left: none;
            border-radius: 0 20px 20px 0;
            cursor: pointer;
            font-size: 15px;
            font-weight: 600;
            transition: background-color 0.3s;
            height: 44px;
            box-sizing: border-box;
        }
        .search-btn:hover {
            background-color: #a30000;
        }
        .nav-links {
            display: flex;
            gap: 30px;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: #cc0000; }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.04);
            padding: 40px;
        }
        .article-title {
            font-size: 36px;
            font-weight: 700;
            color: #0b2b44;
            margin-bottom: 16px;
            line-height: 1.3;
        }
        .article-meta {
            font-size: 14px;
            color: #8393a5;
            margin-bottom: 30px;
            border-bottom: 1px solid #e0e7ef;
            padding-bottom: 15px;
        }
        .article-body {
            font-size: 17px;
            color: #333;
            line-height: 1.8;
        }
        .article-body p {
            margin-bottom: 20px;
        }
        .article-body strong {
            color: #cc0000;
        }
        .back-link {
            display: inline-block;
            margin-top: 30px;
            color: #cc0000;
            text-decoration: none;
            font-weight: 500;
            font-size: 16px;
        }
        .back-link:hover {
            text-decoration: underline;
        }
        footer {
            background: #fff;
            border-top: 1px solid #e0e7ef;
            text-align: center;
            padding: 20px;
            color: #8393a5;
            font-size: 13px;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">头条新闻网</div>
        <div class="search-area">
            <input type="text" class="search-input" placeholder="搜索新闻..." id="searchInput" onkeypress="if(event.key==='Enter')performSearch()">
            <button class="search-btn" onclick="performSearch()">搜索</button>
        </div>
        <div class="nav-links">
            <a href="#">国际</a>
            <a href="#">科技</a>
            <a href="#">财经</a>
            <a href="#">娱乐</a>
            <a href="#">体育</a>
        </div>
    </div>

    <div class="container">
        <h1 class="article-title">市中心医院发生严重医疗事故，多名患者受影响</h1>
        <div class="article-meta">
            <span>📅 2026年6月15日 22:30</span> | 
            <span>来源：头条新闻网社会频道</span> | 
            <span>记者：张明</span>
        </div>
        <div class="article-body">
            <p><strong>本网讯</strong> 昨日晚间，市中心医院重症监护室（ICU）发生一起严重医疗事故，因关键生命支持设备突发故障，导致至少5名正在接受治疗的重症患者被迫中断救治。事故发生后，院方紧急启动应急预案，但仍有3名患者状况不稳定，已转至邻近医院继续治疗。卫生部门已成立专项调查组，连夜进驻医院展开全面调查。</p>

            <p>据知情人士透露，故障设备为去年刚引进的“泰拉医疗科技”系列监护系统，该设备由<strong>泰拉集团</strong>下属子公司提供。事发时，设备突然黑屏，报警系统未能正常启动，值班医护人员虽立即进行人工干预，但仍造成了一段救治空窗期。</p>

            <p>“当时所有监护仪同时死机，我们完全不知道病人的生命体征数据。”一名不愿透露姓名的护士向记者描述了当时的混乱场面。另一位患者家属情绪激动地表示：“医院和厂商必须给个说法，这不是拿人命开玩笑吗？”</p>

            <p>泰拉医疗科技公司今早发布简短声明，称“对事件高度关注，已派遣技术团队协助调查”，但未就设备故障原因作出具体说明。值得注意的是，该公司近期在诺文斯克经济特区新落成的实验室正是专门从事医疗设备研发，而此次涉事的监护系统正是该实验室的首批产品之一。</p>

            <p>截至发稿时，市中心医院ICU仍处于部分关闭状态，卫生部门表示将在一周内公布初步调查结果。本报将持续关注此事进展。</p>
        </div>
        <a href="/news-portal/" class="back-link">← 返回新闻网首页</a>
    </div>

    <footer>
        <p>© 2026 头条新闻网 | 传递最有价值的信息</p>
    </footer>

    <script>
        function performSearch() {
            const keyword = document.getElementById('searchInput').value.trim();
            if (keyword) {
                window.location.href = '/news-portal/search/?q=' + encodeURIComponent(keyword);
            } else {
                alert('请输入搜索关键词');
            }
        }
    </script>
</body>
</html>
    '''

# ========== 头条新闻网 - 搜索结果页 ==========
@app.route('/news-portal/search/')
def news_portal_search():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>搜索结果 | 头条新闻网</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #f4f7fb;
            font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
            color: #1a2a3a;
        }
        .header {
            background: #ffffff;
            border-bottom: 1px solid #e0e7ef;
            padding: 12px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        .logo {
            font-size: 28px;
            font-weight: 700;
            color: #cc0000;
            letter-spacing: 2px;
            margin-right: auto;
        }
        .search-area {
            display: flex;
            align-items: center;
            margin-right: 40px;
        }
        .search-input {
            width: 260px;
            padding: 10px 16px;
            border: 2px solid #cc0000;
            border-radius: 20px 0 0 20px;
            outline: none;
            font-size: 15px;
            transition: border-color 0.3s;
            height: 44px;
        }
        .search-input:focus {
            border-color: #a30000;
        }
        .search-btn {
            padding: 10px 20px;
            background-color: #cc0000;
            color: white;
            border: 2px solid #cc0000;
            border-left: none;
            border-radius: 0 20px 20px 0;
            cursor: pointer;
            font-size: 15px;
            font-weight: 600;
            transition: background-color 0.3s;
            height: 44px;
            box-sizing: border-box;
        }
        .search-btn:hover {
            background-color: #a30000;
        }
        .nav-links {
            display: flex;
            gap: 30px;
        }
        .nav-links a {
            color: #4a5c6c;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
            transition: color 0.3s;
        }
        .nav-links a:hover { color: #cc0000; }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
        }
        .search-title {
            font-size: 24px;
            margin-bottom: 20px;
            color: #0b2b44;
        }
        .result-list {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .result-item {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .result-item h3 {
            font-size: 18px;
            margin-bottom: 8px;
            color: #0b2b44;
        }
        .result-item h3 a {
            color: inherit;
            text-decoration: none;
        }
        .result-item h3 a:hover {
            color: #cc0000;
        }
        .result-item p {
            font-size: 14px;
            color: #5e6f82;
            line-height: 1.5;
        }
        .no-result {
            text-align: center;
            padding: 60px 20px;
            color: #8393a5;
        }
        footer {
            background: #fff;
            border-top: 1px solid #e0e7ef;
            text-align: center;
            padding: 20px;
            color: #8393a5;
            font-size: 13px;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">头条新闻网</div>
        <div class="search-area">
            <input type="text" class="search-input" placeholder="搜索新闻..." id="searchInput" onkeypress="if(event.key==='Enter')performSearch()">
            <button class="search-btn" onclick="performSearch()">搜索</button>
        </div>
        <div class="nav-links">
            <a href="#">国际</a>
            <a href="#">科技</a>
            <a href="#">财经</a>
            <a href="#">娱乐</a>
            <a href="#">体育</a>
        </div>
    </div>

    <div class="container">
        <div class="search-title" id="searchTitle"></div>
        <div class="result-list" id="resultList"></div>
        <div class="no-result" id="noResult" style="display:none;">
            <p>😔 未找到相关新闻</p>
            <p style="margin-top:10px;">请尝试其他关键词</p>
        </div>
    </div>

    <footer>
        <p>© 2026 头条新闻网 | 传递最有价值的信息</p>
    </footer>

    <script>
        const keywordMap = {
            '市中心医院': {
                title: '市中心医院发生严重医疗事故，多名患者受影响',
                summary: '昨日晚间，市中心医院因设备故障导致多名重症患者治疗中断，卫生部门已介入调查。',
                url: '/news-portal/medical-accident/'
            }
        };

        function performSearch() {
            const keyword = document.getElementById('searchInput').value.trim();
            if (keyword) {
                window.location.href = '/news-portal/search/?q=' + encodeURIComponent(keyword);
            } else {
                alert('请输入搜索关键词');
            }
        }

        function loadSearchResults() {
            const params = new URLSearchParams(window.location.search);
            const query = params.get('q') || '';
            const searchTitle = document.getElementById('searchTitle');
            const resultList = document.getElementById('resultList');
            const noResult = document.getElementById('noResult');

            searchTitle.textContent = query ? `搜索结果：“${query}”` : '请输入搜索关键词';

            if (!query) {
                noResult.style.display = 'block';
                return;
            }

            const news = keywordMap[query];
            if (news) {
                resultList.innerHTML = `
                    <div class="result-item">
                        <h3><a href="${news.url}">${news.title}</a></h3>
                        <p>${news.summary}</p>
                    </div>`;
                noResult.style.display = 'none';
            } else {
                resultList.innerHTML = '';
                noResult.style.display = 'block';
            }
        }

        window.addEventListener('DOMContentLoaded', loadSearchResults);
    </script>
</body>
</html>
    '''

@app.route('/oracle/')
def oracle():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oracle · 地球仪</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #ffffff;
            background-image:
                linear-gradient(rgba(0, 0, 0, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 0, 0, 0.05) 1px, transparent 1px);
            background-size: 30px 30px;
            background-position: center;
            font-family: 'Segoe UI', 'PingFang SC', sans-serif;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }
        #container {
            position: fixed; top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: 1;
        }
        .input-panel {
            position: absolute; top: 30px; left: 30px;
            display: flex; flex-direction: column;
            align-items: flex-start;
            gap: 10px;
            z-index: 20;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(8px);
            padding: 10px 16px;
            border-radius: 12px;
            border: 1px solid rgba(0,0,0,0.1);
            box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        }
        .panel-logo {
            width: 300px;
            height: auto;
            margin-bottom: 5px;
        }
        .search-row {
            display: flex;
            align-items: center;
            gap: 10px;
            width: 100%;
        }
        .search-input {
            flex: 1;
            min-width: 0;
            padding: 8px 10px;
            border: 1px solid rgba(0,0,0,0.1);
            border-radius: 8px;
            background: rgba(255,255,255,0.9);
            font-size: 14px; color: #333;
            outline: none;
        }
        .search-input:focus {
            border-color: rgba(0,0,0,0.2);
            box-shadow: 0 0 0 2px rgba(0,102,204,0.15);
        }
        .confirm-btn {
            padding: 8px 16px;
            background: #0066cc; color: white;
            border: none; border-radius: 8px;
            cursor: pointer; font-size: 14px; font-weight: 500;
            transition: background 0.2s;
            white-space: nowrap;
        }
        .confirm-btn:hover { background: #0052a3; }

        .controls-panel {
            position: absolute; bottom: 40px; right: 30px;
            display: flex; gap: 12px; z-index: 20;
        }
        .control-btn {
            width: 48px; height: 36px;
            border-radius: 8px;
            border: 1px solid rgba(0,0,0,0.15);
            background: rgba(255,255,255,0.9);
            cursor: pointer;
            font-size: 18px;
            display: flex; align-items: center; justify-content: center;
            color: #333;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            transition: all 0.2s;
            backdrop-filter: blur(5px);
            outline: none;
        }
        .control-btn:hover {
            background: rgba(0,0,0,0.05);
            border-color: rgba(0,0,0,0.3);
        }
        .control-btn.active {
            background: #0066cc; color: white;
            border-color: #0066cc;
        }
        #playBtn span { position: relative; top: -1px; }
        #pauseBtn { font-size: 22px; }
        #pauseBtn span { position: relative; top: -3px; }

        .back-btn {
            position: absolute; bottom: 40px; right: 30px;
            width: 48px; height: 36px;
            border-radius: 8px;
            border: 1px solid rgba(0,0,0,0.15);
            background: rgba(255,255,255,0.9);
            cursor: pointer;
            font-size: 24px;
            display: none; align-items: center; justify-content: center;
            color: #333;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            z-index: 20;
        }
        .back-btn:hover { background: rgba(0,0,0,0.05); border-color: rgba(0,0,0,0.3); }
        .back-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            background: rgba(255,255,255,0.6);
        }

        .line-segment {
            position: absolute;
            background: #cc0000;
            pointer-events: none;
            z-index: 25;
            display: none;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .line-segment.visible { opacity: 1; }
        .line-slant { height: 2px; transform-origin: left center; }
        .line-h { height: 2px; }

        .info-box {
            position: absolute;
            padding: 20px;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            border: 1px solid rgba(0,0,0,0.08);
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
            font-size: 20px;
            color: #333;
            z-index: 26;
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            max-width: 400px;
            white-space: normal;
            text-align: left;
            line-height: 1.6;
        }
        .info-box.visible { opacity: 1; }
    </style>
</head>
<body>
    <div id="container"></div>

    <div class="input-panel">
        <img src="/static/oracle_logo.png" alt="Oracle Logo" class="panel-logo">
        <div class="search-row">
            <input type="text" id="searchInput" class="search-input" placeholder="输入地点，如：北京">
            <button class="confirm-btn" id="confirmBtn">确认</button>
        </div>
    </div>

    <div class="controls-panel" id="rotateControls">
        <button class="control-btn active" id="playBtn" onclick="window.startRotation()"><span>▶︎</span></button>
        <button class="control-btn" id="pauseBtn" onclick="window.stopRotation()"><span>⏸︎</span></button>
    </div>
    <button class="back-btn" id="backBtn" disabled>↩️</button>

    <div class="line-segment line-slant" id="lineSlant"></div>
    <div class="line-segment line-h" id="lineH"></div>
    <div class="info-box" id="infoBox"></div>

    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
            }
        }
    </script>
    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

        const container = document.getElementById('container');
        const scene = new THREE.Scene();
        scene.background = null;

        const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
        camera.position.set(0, 0, 8);

        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.setClearColor(0x000000, 0);
        container.appendChild(renderer.domElement);

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.rotateSpeed = 0.8;
        controls.zoomSpeed = 1.2;
        controls.enablePan = false;
        controls.minDistance = 4;
        controls.maxDistance = 15;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 0.08;

        // 灯光
        const ambientLight = new THREE.AmbientLight(0xffffff, 1.6);
        scene.add(ambientLight);
        const sunLight = new THREE.DirectionalLight(0xffffff, 1.4);
        sunLight.position.set(5, 3, 5);
        scene.add(sunLight);
        const fillLight = new THREE.DirectionalLight(0xffffff, 0.6);
        fillLight.position.set(-5, 0, -5);
        scene.add(fillLight);

        // 地球
        const geometry = new THREE.SphereGeometry(3, 64, 64);
        const textureLoader = new THREE.TextureLoader();
        const earthTextureUrl = '/static/oracle.jpg';
        const material = new THREE.MeshStandardMaterial({
            map: textureLoader.load(earthTextureUrl),
            roughness: 0.6,
            metalness: 0.0,
            color: 0xffffff,
        });
        const earth = new THREE.Mesh(geometry, material);
        scene.add(earth);

        // 标记组
        const markerGroup = new THREE.Group();
        markerGroup.visible = false;
        earth.add(markerGroup);

        const markerCoreGeo = new THREE.SphereGeometry(0.025, 16, 16);
        const markerCoreMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
        const markerCore = new THREE.Mesh(markerCoreGeo, markerCoreMat);
        markerGroup.add(markerCore);

        const glowGeo = new THREE.SphereGeometry(0.05, 16, 16);
        const glowMat = new THREE.MeshBasicMaterial({
            color: 0xff3333,
            transparent: true,
            opacity: 0.4,
        });
        const glowSphere = new THREE.Mesh(glowGeo, glowMat);
        markerGroup.add(glowSphere);

        // 动画循环
        function animate() {
            requestAnimationFrame(animate);
            if (markerGroup.visible) {
                const scale = 1 + Math.sin(Date.now() * 0.005) * 0.05;
                glowSphere.scale.setScalar(scale);
            }
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        });

        // ===================== 交互元素 =====================
        const searchInput = document.getElementById('searchInput');
        const confirmBtn = document.getElementById('confirmBtn');
        const playBtn = document.getElementById('playBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const backBtn = document.getElementById('backBtn');
        const rotateControls = document.getElementById('rotateControls');

        const lineSlant = document.getElementById('lineSlant');
        const lineH = document.getElementById('lineH');
        const infoBox = document.getElementById('infoBox');

        // 地点数据
        const locationData = {
            '北京': {
                lat: 39.9,
                lon: 116.4,
                desc: '北京，中华人民共和国的首都，拥有三千多年的建城史。故宫、长城、天坛等世界遗产屹立于此，古老与现代在这里交融。'
            },
            '伦敦': {
                lat: 51.5,
                lon: -0.1,
                desc: '伦敦，英国首都，全球金融中心之一。泰晤士河穿城而过，大本钟、伦敦塔桥和白金汉宫是这座城市的标志。'
            },
            '莫斯科': {
                lat: 55.75,
                lon: 37.6,
                desc: '莫斯科，俄罗斯联邦首都，政治与经济中心。红场、克里姆林宫和圣瓦西里大教堂展现出浓厚的历史底蕴。'
            },
            '悉尼': {
                lat: -33.9,
                lon: 151.2,
                desc: '悉尼，澳大利亚最大的城市，以悉尼歌剧院和海港大桥闻名于世。阳光、沙滩与多元文化构成了独特的城市魅力。'
            }
        };

        // 经纬度 -> 局部坐标
        function latLonToLocal(latDeg, lonDeg) {
            const lat = latDeg * Math.PI / 180;
            const lon = -lonDeg * Math.PI / 180;
            const R = 3;
            const y = R * Math.sin(lat);
            const r = R * Math.cos(lat);
            const x = r * Math.cos(lon);
            const z = r * Math.sin(lon);
            return new THREE.Vector3(x, y, z);
        }

        // 仅缩放距离（不改变视线方向）
        function zoomToDistance(targetDistance, duration, callback) {
            const startPos = camera.position.clone();
            const origin = new THREE.Vector3(0, 0, 0);
            const startDir = startPos.clone().normalize();
            const startDist = startPos.length();
            const startTime = performance.now();

            function step(now) {
                const elapsed = now - startTime;
                const t = Math.min(elapsed / duration, 1.0);
                const ease = 1 - Math.pow(1 - t, 3);
                const currentDist = startDist + (targetDistance - startDist) * ease;
                camera.position.copy(startDir.clone().multiplyScalar(currentDist));
                controls.target.copy(origin);
                controls.update();
                if (t < 1) {
                    requestAnimationFrame(step);
                } else {
                    camera.position.copy(startDir.clone().multiplyScalar(targetDistance));
                    controls.target.copy(origin);
                    if (callback) callback();
                }
            }
            requestAnimationFrame(step);
        }

        // 同步旋转+拉近
        function animateToTarget(targetRotY, posLocal, finalDistance, duration, callback) {
            const startRotY = earth.rotation.y;
            const startCamPos = camera.position.clone();
            const startTarget = controls.target.clone();
            const startTime = performance.now();

            const finalWorldPos = posLocal.clone().applyAxisAngle(new THREE.Vector3(0, 1, 0), targetRotY);
            const finalNormal = finalWorldPos.clone().normalize();
            const finalCamPos = finalWorldPos.clone().add(finalNormal.clone().multiplyScalar(finalDistance));

            function step(now) {
                const elapsed = now - startTime;
                const t = Math.min(elapsed / duration, 1.0);
                const ease = 1 - Math.pow(1 - t, 3);
                earth.rotation.y = startRotY + (targetRotY - startRotY) * ease;

                const currentWorld = posLocal.clone().applyAxisAngle(new THREE.Vector3(0, 1, 0), earth.rotation.y);
                const normal = currentWorld.clone().normalize();
                const currentCamPos = currentWorld.clone().add(normal.clone().multiplyScalar(finalDistance));
                const currentTarget = currentWorld.clone();

                camera.position.lerpVectors(startCamPos, currentCamPos, ease);
                controls.target.lerpVectors(startTarget, currentTarget, ease);
                controls.update();

                if (t < 1) {
                    requestAnimationFrame(step);
                } else {
                    earth.rotation.y = targetRotY;
                    camera.position.copy(finalCamPos);
                    controls.target.copy(finalWorldPos);
                    if (callback) callback();
                }
            }
            requestAnimationFrame(step);
        }

        // 平移相机（向右平移）
        function panCameraRight(offsetX, duration, callback) {
            const startPos = camera.position.clone();
            const startTarget = controls.target.clone();
            const startTime = performance.now();

            function step(now) {
                const elapsed = now - startTime;
                const t = Math.min(elapsed / duration, 1.0);
                const ease = 1 - Math.pow(1 - t, 3);
                camera.position.x = startPos.x + offsetX * ease;
                controls.target.x = startTarget.x + offsetX * ease;
                controls.update();
                if (t < 1) {
                    requestAnimationFrame(step);
                } else {
                    camera.position.x = startPos.x + offsetX;
                    controls.target.x = startTarget.x + offsetX;
                    if (callback) callback();
                }
            }
            requestAnimationFrame(step);
        }

        // 标记弹性入场
        function animateMarkerEntry(callback) {
            const startTime = performance.now();
            function step(now) {
                const elapsed = now - startTime;
                const t = Math.min(elapsed / 500, 1.0);
                const ease = 1 - Math.pow(1 - t, 3);
                markerGroup.scale.setScalar(ease);
                if (t < 1) {
                    requestAnimationFrame(step);
                } else {
                    markerGroup.scale.setScalar(1.0);
                    if (callback) callback();
                }
            }
            markerGroup.scale.setScalar(0);
            requestAnimationFrame(step);
        }

        // 复位视角
        function resetView(duration, callback) {
            const startPos = camera.position.clone();
            const startTarget = controls.target.clone();
            const startRotY = earth.rotation.y;
            const endPos = new THREE.Vector3(0, 0, 8);
            const endTarget = new THREE.Vector3(0, 0, 0);
            const endRotY = 0;
            const startTime = performance.now();

            function step(now) {
                const elapsed = now - startTime;
                const t = Math.min(elapsed / duration, 1.0);
                const ease = 1 - Math.pow(1 - t, 3);
                camera.position.lerpVectors(startPos, endPos, ease);
                controls.target.lerpVectors(startTarget, endTarget, ease);
                earth.rotation.y = startRotY + (endRotY - startRotY) * ease;
                controls.update();
                if (t < 1) {
                    requestAnimationFrame(step);
                } else {
                    camera.position.copy(endPos);
                    controls.target.copy(endTarget);
                    earth.rotation.y = endRotY;
                    if (callback) callback();
                }
            }
            requestAnimationFrame(step);
        }

        // 显示折线与文字框
        function showConnectorAndInfo() {
            const worldPos = markerCore.getWorldPosition(new THREE.Vector3());
            const screenPos = worldPos.clone().project(camera);
            const sx = (screenPos.x * 0.5 + 0.5) * window.innerWidth;
            const sy = (screenPos.y * -0.5 + 0.5) * window.innerHeight;

            infoBox.style.display = 'block';
            infoBox.style.visibility = 'hidden';
            const boxHeight = infoBox.offsetHeight;
            infoBox.style.visibility = '';

            // 可调参数
            const offsetX = 650;
            const slantDx = 80;
            const slantDy = 40;
            const textVerticalOffset = 0;

            const turnX = sx + slantDx;
            const turnY = sy - slantDy;
            const infoX = sx + offsetX;
            const infoY = turnY - boxHeight / 2 + textVerticalOffset;

            // 斜线
            const dx = turnX - sx;
            const dy = turnY - sy;
            const slantLength = Math.sqrt(dx * dx + dy * dy);
            const angle = Math.atan2(dy, dx) * (180 / Math.PI);
            lineSlant.style.left = sx + 'px';
            lineSlant.style.top = sy + 'px';
            lineSlant.style.width = slantLength + 'px';
            lineSlant.style.transform = `rotate(${angle}deg)`;
            lineSlant.style.display = 'block';
            lineSlant.classList.add('visible');

            // 水平线
            lineH.style.left = turnX + 'px';
            lineH.style.top = turnY + 'px';
            lineH.style.width = (infoX - turnX) + 'px';
            lineH.style.display = 'block';
            lineH.classList.add('visible');

            infoBox.style.left = infoX + 'px';
            infoBox.style.top = infoY + 'px';
            infoBox.style.display = 'block';
            infoBox.classList.add('visible');
        }

        // 隐藏折线与文字框
        function hideConnectorAndInfo() {
            lineSlant.classList.remove('visible');
            lineH.classList.remove('visible');
            infoBox.classList.remove('visible');
            setTimeout(() => {
                if (!lineSlant.classList.contains('visible')) lineSlant.style.display = 'none';
                if (!lineH.classList.contains('visible')) lineH.style.display = 'none';
                if (!infoBox.classList.contains('visible')) infoBox.style.display = 'none';
            }, 300);
        }

        // 执行定位的核心函数
        function applyLocation(cityName) {
            const data = locationData[cityName];
            if (!data) return;

            const posLocal = latLonToLocal(data.lat, data.lon);
            const targetRotY = -Math.atan2(posLocal.x, posLocal.z);

            markerGroup.position.copy(posLocal);
            markerGroup.visible = false;

            controls.autoRotate = false;
            controls.enableRotate = false;
            controls.enableZoom = false;
            controls.minDistance = 0;
            rotateControls.style.display = 'none';
            backBtn.style.display = 'flex';
            backBtn.disabled = true;

            const finalZoom = 2.8;

            hideConnectorAndInfo();
            infoBox.textContent = data.desc;

            zoomToDistance(8, 800, () => {
                animateToTarget(targetRotY, posLocal, finalZoom, 1200, () => {
                    markerGroup.visible = true;
                    animateMarkerEntry(() => {
                        panCameraRight(1, 800, () => {
                            showConnectorAndInfo();
                            setTimeout(() => {
                                backBtn.disabled = false;
                            }, 500);
                        });
                    });
                });
            });
        }

        // 确认按钮事件
        confirmBtn.addEventListener('click', () => {
            const query = searchInput.value.trim();
            if (!query) {
                alert('请输入地点名称');
                return;
            }
            if (locationData[query]) {
                applyLocation(query);
            } else {
                alert('请检查输入的内容！');
            }
        });

        // 回车触发确认
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') confirmBtn.click();
        });

        // 返回按钮
        backBtn.addEventListener('click', () => {
            if (backBtn.disabled) return;
            backBtn.disabled = true;

            controls.enableRotate = true;
            controls.enableZoom = true;
            controls.minDistance = 4;
            controls.autoRotate = true;
            playBtn.classList.add('active');
            pauseBtn.classList.remove('active');

            markerGroup.visible = false;
            hideConnectorAndInfo();

            // 注意：这里不再立即显示 rotateControls，而是在动画完成后显示
            resetView(1200, () => {
                backBtn.style.display = 'none';
                backBtn.disabled = false;
                rotateControls.style.display = 'flex';  // 动画完成后才显示播放暂停按钮
            });
        });

        window.startRotation = function() {
            controls.autoRotate = true;
            playBtn.classList.add('active');
            pauseBtn.classList.remove('active');
        };
        window.stopRotation = function() {
            controls.autoRotate = false;
            pauseBtn.classList.add('active');
            playBtn.classList.remove('active');
        };
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)