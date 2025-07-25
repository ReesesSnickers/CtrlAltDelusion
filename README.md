# CtrlAltDelusion

This is not your average Discord bot. Well actually, it is but that is besides the point. Add some flair to your channel with handlebar ai generated completions. Having a bad day but don't know how to complete it? Just add {{Value}} to your message and let CtrlAltDelusion pick it up from there.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `OPENAI_API_KEY` - Your personal OpenAI API Key. Don't have a OpenAI API Key? Navigate to [OpenAI](https://platform.openai.com/) and set up your account today!

- `DISCORD_BOT_TOKEN` - Your personal bot token from Discord. Don't have a Discord bot token? Navigate to the [Discord developer portal](https://discord.com/developers) and get started today!

- `APP_URL` - http://localhost:5000

- `APP_ENV` - local

## Run Locally

### Prerequisites

### Dependency Requirements
1. You will need a OpenAI API token to run this project. Don't have a OpenAI API Key? Navigate to [OpenAI](https://platform.openai.com/) and set up your account today!
2. You will need to set up a Discord bot and obtain a API key with the following permissions and settings:

- Server Members Intent
- Message Content Intent

### Python Requirements
1. Python 3.13
2. Install local certificates:
```bash
/Applications/Python\ 3.13/Install\ Certificates.command
```

### Node.js Requirements
1. Node.js (for semantic-release)
2. Install semantic-release globally:
```bash
npm install -g semantic-release
```

### Local

1. Clone the project

```bash
  git clone https://github.com/ReesesSnickers/CtrlAltDelusion.git
```

2. Go to the project directory

```bash
  cd CtrlAltDelusion
```

3. Install dependencies

```bash
  pip3 install -r /path/to/requirements.txt
```

4. Create a .env file at the root of the project and add the appropriate environmental variables

5. Start the server

```bash
  python3 -m src.bot.main 
```
OR

```bash
python3 src/bot/main.py
```

## Useage

Any time a user in your channel makes a statement using `{{}}`, the bot will interpret the content and generate a statement to replace the `{{}}` within the statement that was provided.

_Example_:

_Input: "well {{military dark humor}}."_

_Output: "well the coffee is a lie._

## Run Locally

CtrlAltDelusion is currently set up to be deployed on [Render](https://dashboard.render.com/) as a Webservice.

## Committing using symantic release

Symantic release requires commit messages to be formatted in a particular way. Please see below around these requirements:

feat: message - New feature (minor version bump)
fix: message - Bug fix (patch version bump)
BREAKING CHANGE: message - Breaking API change (major version bump)
chore: message - Maintenance changes (no version bump)
docs: message - Documentation only (no version bump)
style: message - Code style changes (no version bump)
refactor: message - Code refactoring (no version bump)
perf: message - Performance improvements (no version bump)
test: message - Adding tests (no version bump)

## Contributors

- [ReesesSnickers](https://github.com/ReesesSnickers)
