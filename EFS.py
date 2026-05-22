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

# ========== 游戏入口（网站首页） ==========
@app.route('/')
def game_entry():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>逃离石家庄 - 网页解谜游戏</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            width: 100vw; height: 100vh;
            background: #0a0f0f;
            font-family: 'PingFang SC', 'Microsoft YaHei', 'Segoe UI', sans-serif;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .fog-container {
            position: absolute; top: 0; left: 0;
            width: 100%; height: 100%;
            background: radial-gradient(ellipse at 20% 50%, #1b2b2b 0%, #0a0f0f 70%);
            z-index: 0;
        }
        .fog-layer {
            position: absolute; top: 0; left: 0;
            width: 200%; height: 200%;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" opacity="0.08"><filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/></filter><rect width="800" height="600" filter="url(%23noise)"/></svg>');
            animation: fogMove 60s linear infinite;
            pointer-events: none;
        }
        @keyframes fogMove {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-50%, -50%); }
        }
        .main-card {
            position: relative; z-index: 10;
            text-align: center; padding: 60px 50px;
            background: rgba(10,15,15,0.75);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.7);
            max-width: 600px; width: 90%;
        }
        .game-title {
            font-size: clamp(42px, 10vw, 72px); font-weight: 900;
            letter-spacing: 8px; color: #e6e9e8;
            text-shadow: 0 0 20px rgba(100,180,160,0.5);
            margin-bottom: 20px; line-height: 1.2;
        }
        .subtitle {
            font-size: 16px; letter-spacing: 10px;
            color: #667a74; text-transform: uppercase;
            margin-bottom: 40px;
        }
        .intro-text {
            color: #a3b9b0; font-size: 17px; line-height: 1.8;
            margin-bottom: 45px; max-width: 480px;
            margin-left: auto; margin-right: auto;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }
        .start-btn {
            display: inline-block; padding: 16px 48px;
            background: transparent; border: 2px solid #4a8c7c;
            color: #cfe6db; font-size: 20px; font-weight: 600;
            letter-spacing: 5px; text-decoration: none;
            border-radius: 4px; transition: all 0.3s ease;
            cursor: pointer; position: relative; overflow: hidden;
        }
        .start-btn:hover {
            background: #4a8c7c; color: #fff;
            box-shadow: 0 0 30px rgba(74,140,124,0.5);
            border-color: #5faa97;
        }
        .start-btn::before {
            content: ''; position: absolute; top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        .start-btn:hover::before { left: 100%; }
        .version {
            position: absolute; bottom: 25px; right: 30px;
            color: #3a514b; font-size: 13px;
            letter-spacing: 2px; z-index: 20;
        }
    </style>
</head>
<body>
    <div class="fog-container"><div class="fog-layer"></div></div>
    <div class="main-card">
        <h1 class="game-title">逃离石家庄</h1>
        <div class="subtitle">ESCAPE FROM SHIJIAZHUANG</div>
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

        /* 窗口样式 */
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
            background: #ffffff;
            color: #333;
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
        .window-content {
            flex: 1; overflow: hidden;
            background: white;
        }

        /* 逃离塔科夫加载/警告样式 */
        .tarkov-loading {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            height: 100%; gap: 20px;
        }
        .tarkov-spinner {
            width: 48px; height: 48px;
            border: 5px solid #ddd;
            border-top: 5px solid #0066cc;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        .tarkov-warning {
            display: none; flex-direction: column; align-items: center; justify-content: center;
            height: 100%; gap: 20px;
        }
        .tarkov-warning .icon { font-size: 48px; }
        .tarkov-warning .text {
            font-size: 20px; font-weight: bold; color: #c00;
            text-align: center; line-height: 1.5;
        }
        .tarkov-warning button {
            padding: 8px 24px; font-size: 16px; cursor: pointer;
            background: #0066cc; color: white; border: none; border-radius: 4px;
        }

        /* 记事本样式 */
        .notepad-menubar {
            display: flex;
            background: #f0f0f0;
            border-bottom: 1px solid #ccc;
            padding: 2px 0;
        }
        .notepad-menubar span {
            padding: 4px 12px;
            font-size: 13px;
            cursor: default;
        }
        .notepad-menubar span:hover { background: #d0d0d0; }
        .notepad-textarea {
            flex: 1;
            padding: 4px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 14px;
            border: none; outline: none; resize: none;
            width: 100%; height: 100%;
            background: white; color: #333;
            cursor: text; user-select: text;
        }
        .notepad-statusbar {
            display: flex;
            justify-content: space-between;
            padding: 4px 10px;
            background: #f0f0f0;
            border-top: 1px solid #ccc;
            font-size: 12px; color: #666;
        }

        /* 浏览器内部样式 */
        .browser-toolbar {
            display: flex; align-items: center; padding: 6px 10px;
            background: #f1f3f4; border-bottom: 1px solid #ddd;
        }
        .browser-url {
            flex: 1; padding: 6px 10px; border: 1px solid #ccc;
            border-radius: 4px; font-size: 14px;
        }
        .browser-go-btn {
            margin-left: 8px; padding: 6px 16px;
            background: #0066cc; color: white; border: none;
            border-radius: 4px; cursor: pointer; font-size: 14px;
        }
        .browser-view {
            flex: 1; background: #fff;
            display: flex; align-items: center; justify-content: center;
        }

        /* 调整手柄 */
        .resize-handle {
            position: absolute; z-index: 10; background: transparent;
        }
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
        <div class="desktop-icon" onclick="openWindow('computer')">
            <img src="/static/desktop-mycomputer.ico" alt="此电脑">
            <span>此电脑</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('recycle')">
            <img src="/static/desktop-recyclebin.ico" alt="回收站">
            <span>回收站</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('browser')">
            <img src="/static/desktop-chrome.ico" alt="浏览器">
            <span>浏览器</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('notepad')">
            <img src="/static/desktop-notepad.ico" alt="记事本">
            <span>记事本</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('tarkov')">
            <img src="/static/desktop-EscapeFromTarkov.ico" alt="逃离塔科夫">
            <span>逃离塔科夫</span>
        </div>
    </div>

    <!-- 此电脑窗口 -->
    <div class="window" id="computer-window">
        <div class="window-titlebar">
            <span class="window-title">此电脑</span>
            <div class="window-controls">
                <button onclick="minimizeWindow('computer')">─</button>
                <button onclick="closeWindow('computer')">✕</button>
            </div>
        </div>
        <div class="window-content">
            <p style="padding:20px;">📁 本地磁盘 (C:)</p>
            <p style="padding:0 20px;">📁 文档</p>
            <p style="padding:0 20px;">📁 图片</p>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 回收站窗口 -->
    <div class="window" id="recycle-window">
        <div class="window-titlebar">
            <span class="window-title">回收站</span>
            <div class="window-controls">
                <button onclick="minimizeWindow('recycle')">─</button>
                <button onclick="closeWindow('recycle')">✕</button>
            </div>
        </div>
        <div class="window-content"><p style="padding:20px;color:#666;">回收站是空的。</p></div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 浏览器窗口 -->
    <div class="window" id="browser-window" style="width:900px; height:600px;">
        <div class="window-titlebar">
            <span class="window-title">浏览器</span>
            <div class="window-controls">
                <button onclick="minimizeWindow('browser')">─</button>
                <button onclick="closeWindow('browser')">✕</button>
            </div>
        </div>
        <div class="window-content" style="display:flex; flex-direction:column;">
            <div class="browser-toolbar">
                <input type="text" class="browser-url" id="browser-url" placeholder="输入网址..." onkeypress="if(event.key==='Enter')navigateBrowser()">
                <button class="browser-go-btn" onclick="navigateBrowser()">转到</button>
            </div>
            <div class="browser-view" id="browser-view">
                <div style="text-align:center;color:#999;">
                    <div style="font-size:48px;margin-bottom:20px;">🔍</div>
                    <div style="font-size:16px;">请在地址栏输入网址以访问</div>
                </div>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 记事本窗口 -->
    <div class="window" id="notepad-window" style="width:600px; height:450px;">
        <div class="window-titlebar">
            <span class="window-title">记事本</span>
            <div class="window-controls">
                <button onclick="minimizeWindow('notepad')">─</button>
                <button onclick="closeWindow('notepad')">✕</button>
            </div>
        </div>
        <div class="window-content" style="display:flex; flex-direction:column;">
            <div class="notepad-menubar">
                <span>文件(F)</span>
                <span>编辑(E)</span>
                <span>格式(O)</span>
                <span>查看(V)</span>
                <span>帮助(H)</span>
            </div>
            <textarea class="notepad-textarea" readonly>http://www.terragroup.com</textarea>
            <div class="notepad-statusbar">
                <span>第1行, 第1列</span>
                <span>100%</span>
            </div>
        </div>
        <div class="resize-handle top"></div><div class="resize-handle bottom"></div><div class="resize-handle left"></div><div class="resize-handle right"></div>
        <div class="resize-handle top-left"></div><div class="resize-handle top-right"></div><div class="resize-handle bottom-left"></div><div class="resize-handle bottom-right"></div>
    </div>
    <!-- 逃离塔科夫窗口 -->
    <div class="window" id="tarkov-window" style="width:400px; height:300px;">
        <div class="window-titlebar">
            <span class="window-title">逃离塔科夫</span>
            <div class="window-controls">
                <button onclick="closeWindow('tarkov')">✕</button>
            </div>
        </div>
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

    <div class="taskbar">
        <button class="start-btn">
            <img src="/static/desktop-windows.png" alt="开始">
        </button>
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

        const iconMap = {
            computer: '/static/desktop-mycomputer.ico',
            recycle: '/static/desktop-recyclebin.ico',
            browser: '/static/desktop-chrome.ico',
            notepad: '/static/desktop-notepad.ico',
            tarkov: '/static/desktop-EscapeFromTarkov.ico'
        };

        const VALID_URLS = [
            'http://www.terragroup.com',
            'https://www.terragroup.com',
            'www.terragroup.com'
        ];

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

        function resetBrowser() {
            const view = document.getElementById('browser-view');
            if (view) {
                view.innerHTML = `
                    <div style="text-align:center;color:#999;">
                        <div style="font-size:48px;margin-bottom:20px;">🔍</div>
                        <div style="font-size:16px;">请在地址栏输入网址以访问</div>
                    </div>`;
            }
            const urlInput = document.getElementById('browser-url');
            if (urlInput) urlInput.value = '';
        }

        function navigateBrowser() {
            const urlInput = document.getElementById('browser-url');
            const view = document.getElementById('browser-view');
            if (!urlInput || !view) return;
            const input = urlInput.value.trim();
            if (VALID_URLS.includes(input)) {
                window.open('/home/', '_blank');
                view.innerHTML = `
                    <div style="text-align:center;color:#0066cc;">
                        <div style="font-size:48px;margin-bottom:20px;">🚀</div>
                        <div style="font-size:16px;">正在跳转到 ${input} ...</div>
                    </div>`;
            } else {
                view.innerHTML = `
                    <div style="text-align:center;color:#c00;">
                        <div style="font-size:48px;margin-bottom:20px;">⚠️</div>
                        <div style="font-size:16px;">无法访问该网页</div>
                        <div style="font-size:13px;color:#666;margin-top:10px;">请检查网址是否正确</div>
                    </div>`;
            }
        }

        function updateTaskbarActive() {
            for (const [name, icon] of Object.entries(activeWindows)) {
                if (name === currentFocus) {
                    icon.classList.add('active');
                } else {
                    icon.classList.remove('active');
                }
            }
        }

        function openWindow(name) {
            if (name === 'tarkov') {
                const win = document.getElementById('tarkov-window');
                if (!win) return;
                if (win.style.display === 'flex') {
                    focusWindow('tarkov');
                    return;
                }
                const loadingDiv = document.getElementById('tarkov-loading');
                const warningDiv = document.getElementById('tarkov-warning');
                if (loadingDiv) loadingDiv.style.display = 'flex';
                if (warningDiv) warningDiv.style.display = 'none';
                win.style.display = 'flex';
                win.style.zIndex = ++zIndexCounter;
                if (!win.style.left || win.style.left === '') {
                    win.style.left = (100 + Math.random() * 200) + 'px';
                    win.style.top = (50 + Math.random() * 150) + 'px';
                }
                createTaskbarIcon('tarkov');
                focusWindow('tarkov');
                if (tarkovTimer) clearTimeout(tarkovTimer);
                tarkovTimer = setTimeout(() => {
                    if (loadingDiv) loadingDiv.style.display = 'none';
                    if (warningDiv) warningDiv.style.display = 'flex';
                }, 5000);   // 改为5秒
                return;
            }

            const win = document.getElementById(name + '-window');
            if (!win) return;
            if (win.style.display === 'flex') {
                focusWindow(name);
                return;
            }
            win.style.display = 'flex';
            win.style.zIndex = ++zIndexCounter;
            if (!win.style.left || win.style.left === '') {
                win.style.left = (100 + Math.random() * 200) + 'px';
                win.style.top = (50 + Math.random() * 150) + 'px';
            }
            if (name === 'browser') resetBrowser();

            createTaskbarIcon(name);
            focusWindow(name);
        }

        function focusWindow(name) {
            const win = document.getElementById(name + '-window');
            if (win && win.style.display === 'flex') {
                win.style.zIndex = ++zIndexCounter;
            }
            if (currentFocus !== name) {
                currentFocus = name;
                updateTaskbarActive();
            }
        }

        function minimizeWindow(name) {
            document.getElementById(name + '-window').style.display = 'none';
            if (currentFocus === name) {
                currentFocus = null;
                updateTaskbarActive();
            }
        }

        function closeWindow(name) {
            document.getElementById(name + '-window').style.display = 'none';
            if (activeWindows[name]) {
                activeWindows[name].remove();
                delete activeWindows[name];
            }
            if (currentFocus === name) {
                currentFocus = null;
                updateTaskbarActive();
            }
            if (name === 'tarkov' && tarkovTimer) {
                clearTimeout(tarkovTimer);
                tarkovTimer = null;
            }
        }

        // 拖动窗口
        document.querySelectorAll('.window').forEach(win => {
            const titlebar = win.querySelector('.window-titlebar');
            let offsetX, offsetY, isDragging = false;
            titlebar.addEventListener('mousedown', (e) => {
                isDragging = true;
                const winId = win.id.replace('-window', '');
                focusWindow(winId);
                win.style.zIndex = ++zIndexCounter;
                offsetX = e.clientX - win.offsetLeft;
                offsetY = e.clientY - win.offsetTop;
                document.addEventListener('mousemove', onMouseMove);
                document.addEventListener('mouseup', onMouseUp);
            });
            function onMouseMove(e) { if (!isDragging) return; win.style.left = (e.clientX - offsetX) + 'px'; win.style.top = (e.clientY - offsetY) + 'px'; }
            function onMouseUp() { isDragging = false; document.removeEventListener('mousemove', onMouseMove); document.removeEventListener('mouseup', onMouseUp); }
            win.addEventListener('mousedown', (e) => {
                if (e.target.closest('.resize-handle')) return;
                const winId = win.id.replace('-window', '');
                focusWindow(winId);
            });
        });

        // 窗口大小调整
        document.querySelectorAll('.resize-handle').forEach(handle => {
            const win = handle.closest('.window');
            handle.addEventListener('mousedown', (e) => {
                e.stopPropagation();
                e.preventDefault();
                const startX = e.clientX;
                const startY = e.clientY;
                const startLeft = win.offsetLeft;
                const startTop = win.offsetTop;
                const startWidth = win.offsetWidth;
                const startHeight = win.offsetHeight;
                const handleClass = handle.className;

                function onResizeMove(e) {
                    const dx = e.clientX - startX;
                    const dy = e.clientY - startY;
                    let newWidth = startWidth;
                    let newHeight = startHeight;
                    let newLeft = startLeft;
                    let newTop = startTop;

                    if (handleClass.includes('right'))  newWidth  = Math.max(300, startWidth + dx);
                    if (handleClass.includes('left'))   { newWidth  = Math.max(300, startWidth - dx); newLeft = startLeft + dx; }
                    if (handleClass.includes('bottom')) newHeight = Math.max(200, startHeight + dy);
                    if (handleClass.includes('top'))    { newHeight = Math.max(200, startHeight - dy); newTop = startTop + dy; }

                    win.style.width = newWidth + 'px';
                    win.style.height = newHeight + 'px';
                    if (handleClass.includes('left') || handleClass.includes('right')) win.style.left = newLeft + 'px';
                    if (handleClass.includes('top') || handleClass.includes('bottom')) win.style.top = newTop + 'px';
                }

                function onResizeUp() {
                    document.removeEventListener('mousemove', onResizeMove);
                    document.removeEventListener('mouseup', onResizeUp);
                }

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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)