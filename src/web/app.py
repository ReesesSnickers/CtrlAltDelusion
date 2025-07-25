from quart import Quart
import os
from hypercorn.asyncio import serve
from hypercorn.config import Config

app = Quart(__name__)

@app.route('/')
async def home():
    return {'status': 'healthy', 'message': 'Délulu bot is vibing on Discord and HTTP.'}

@app.route('/health')
async def health():
    return {'status': 'ok', "message": '✨ Délulu is emotionally online'}

async def run_task(host="0.0.0.0", port=5000):
    config = Config()
    config.bind = [f"{host}:{port}"]
    await serve(app, config)
    
# Add run_task to app
app.run_task = run_task

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)