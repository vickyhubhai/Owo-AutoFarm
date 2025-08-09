# TerrorBhai OWO Auto Farm Bot

## Deploying to Render

1. **Fork or upload this repository to your own GitHub.**
2. **Create a new Worker Service on Render:**
   - Connect your GitHub repo.
   - Set the build command to `pip install -r requirements.txt`.
   - Set the start command to `python main.py`.
3. **Set the `TOKEN` environment variable** in the Render dashboard (do not use `.env` on Render).
4. **(Optional)**: Set `autoDeploy` to `false` in `render.yaml` if you want to manually control deployments.

### Environment Variables
- `TOKEN`: Your Discord account token (keep this secret!).

### Notes
- This bot uses `discord.py-self` (selfbotting is against Discord ToS; use at your own risk).
- The bot will not work unless the `TOKEN` is set as an environment variable on Render.

---

A powerful Discord self-bot for automating OwO Bot farming, created by Vicky (TerrorBhai).

## Features
- Automated farming for OwO commands: `owoh`, `hunt`, `battle`, `sell`, `flip`, `cash`, and `pray`
- Human-like random delays and intervals
- Command usage statistics (`>stats`)
- Start/stop automation with commands
- Easy setup with `.env` token file
- Self-bot: runs on your own Discord account

## Usage
1. **Install Python 3.8–3.12** and required libraries:
   ```sh
   pip install -r requirements.txt
   ```
2. **Set your Discord token** in a `.env` file:
   ```env
   TOKEN="YOUR_DISCORD_TOKEN_HERE"
   ```
3. **Run the bot:**
   ```sh
   python main.py
   ```
4. **Commands:**
   - `>autoOwO` — Start auto farming
   - `>stopautoOwO` — Stop auto farming
   - `>banbypass` — Anti-ban farming mode
   - `>help` — Show help
   - `>stats` — Show farming statistics

## Disclaimer
- This is a self-bot and violates Discord ToS. Use at your own risk.
- For educational purposes only.

## Credits
- Developed by Vicky (TerrorBhai)
- Based on the original OwO Auto Farm script
