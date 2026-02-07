from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Guest in the Universe</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 { color: #ffd700; text-align: center; }
        .subtitle { text-align: center; opacity: 0.8; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .stat-card {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        .number { font-size: 2em; font-weight: bold; }
        .label { opacity: 0.7; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌌 Guest in the Universe</h1>
        <p class="subtitle">Exploring the vast cosmos of web development</p>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">∞</div>
                <div class="label">Possibilities</div>
            </div>
            <div class="stat-card">
                <div class="number">1</div>
                <div class="label">Journey</div>
            </div>
            <div class="stat-card">
                <div class="number">2024</div>
                <div class="label">Launch Year</div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 40px;">
            <p>Welcome to your corner of the universe!</p>
            <p style="opacity: 0.7;">Built with Flask, Docker, and Ansible</p>
        </div>
    </div>
</body>
</html>
    ''')

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'guestintheuniverse'}

@app.route('/api/stats')
def api_stats():
    return {
        'app': 'Guest in the Universe',
        'version': '1.0.0',
        'status': 'running',
        'tech': ['Flask', 'Docker', 'Nginx', 'Ansible']
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
