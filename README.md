# chatbots
## Archetectures for 'chatbots'
```bash
chatbots/
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
└── app.py
```
## Clone and begin developing
```bash
# Navigate to your desired parent directory (e.g., your Projects folder)
cd ~/Projects

# Create a directory named "chatbots"
mkdir chatbots

# Change into the newly created directory
cd chatbots

# Clone the repository into the current directory
git clone https://github.com/Will-Langhart/chatbots.git .

# (Optional) Create a virtual environment for your project
python3 -m venv venv

# (Optional) Activate the virtual environment
source venv/bin/activate

# (Optional) Install the required dependencies
pip install -r requirements.txt
```
To run your Flask app, try the following steps:
	1.	Ensure your virtual environment is active.
(It looks like it is, as your prompt shows (venv).)
	2.	Set the Flask app environment variable (if needed):
 ```bash
export FLASK_APP=app.py
```
  3. Run the Flask application.
You can either run it using the built-in Flask CLI:
 ```bash
flask run
```
or run it directly with Python (if your app.py has the appropriate main block):
 ```bash
python app.py
 ```
