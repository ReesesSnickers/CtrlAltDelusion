# CtrlAltDelusion

This is not your average Discord bot. Well actually, it is but that is besides the point. Add some flair to your channel with handlebar ai generated completions. Having a bad day but don't know how to complete it? Just add {{Value}} to your message and let CtrlAltDelusion pick it up from there.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `OPENAI_API_KEY` - Your personal OpenAI API Key. Don't have a OpenAI API Key? Navigate to [OpenAI](https://platform.openai.com/) and set up your account today!

- `DISCORD_BOT_TOKEN` - Your personal bot token from Discord. Don't have a Discord bot token? Navigate to the [Discord developer portal](https://discord.com/developers) and get started today!

## Run Locally

### Prerequisites

1. You will need a OpenAI API token to run this project. Don't have a OpenAI API Key? Navigate to [OpenAI](https://platform.openai.com/) and set up your account today!
2. You will need to set up a Discord bot and obtain a API key with the following permissions and settings:

- Server Members Intent
- Message Content Intent

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

4. Create a .env file at the root of the project and add the appropriate environemental variables

5. Start the server

```bash
  python3 main.py
```

## Useage

Any time a user in your channel makes a statment using `{{}}`, the bot will interpret the content and generate a statement to replace the `{{}}` within the statement that was provided.

_Example_:

_Input: "well {{military dark humor}}."_

_Output: "well the coffee is a lie._

## Run Locally

CtrlAltDelusion is currently set up to be deployed on [Render](https://dashboard.render.com/) as a Webservice.

## Contributors

- [ReesesSnickers](https://github.com/ReesesSnickers)
