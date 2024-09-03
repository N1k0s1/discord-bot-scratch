## Self Hosting Instructions

### Prerequisites
1. **Python**: Ensure you have Python 3.8 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Discord Bot Token**: You need a bot token from the Discord Developer Portal. Create a new application and bot to get this token.

### Instructions

1. **Clone or Download the Bot Code**:
   - Clone the repository or download the bot code to your local machine.

2. **Install Required Libraries**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the bot code is located.
   - Install the required libraries using pip:
     ```sh
     pip install discord.py
     ```

3. **Set Up Your Bot Token**:
   - Open the `main.py` file.
   - Replace `'secrettokenhere!'` with your actual bot token:
     ```python
     bot.run('your_actual_bot_token_here')
     ```

5. **Run the Bot**:
   - In the terminal or command prompt, navigate to the directory containing `main.py`
   - Run the bot using Python:
     ```sh
     python main.py
     ```

6. **Verify the Bot is Running**:
   - You should see a message in the terminal indicating that the bot has logged in.
   - Go to your Discord server and test the commands:
     - Use `/hello` to get a "Hello!" response.
     - Use `/sync` to sync commands.
     - Use `/goodbye` to get a "Goodbye!" response.
     - Use the user command to greet a member.
