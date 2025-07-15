from quart import Quart

app = Quart(__name__)

@app.route("/")
async def home():
    return "Délulu bot is vibing on Discord and HTTP."

@app.route("/health")
async def health():
    return "✨ Délulu is emotionally online", 200