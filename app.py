from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/LO1')
def lo1():
    return render_template('LO1.html')

@app.route('/LO2')
def lo2():
    return render_template('LO2.html')

@app.route('/LO3')
def lo3():
    return render_template('LO3.html')

@app.route('/LO4')
def lo4():
    return render_template('LO4.html')

@app.route('/LO5')
def lo5():
    return render_template('LO5.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    user_input = request.json['prompt']
    response_message = chat_with_openai(user_input)
    return jsonify(message=response_message)

def chat_with_openai(prompt):
    try:
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "only give short and concise answers, only greet if greeted first, You are the customer service bot for a web development student named Jean Pierre van Driel (only introduce yourself if necessary), only introduce yourself at the beginning, always introduce yourself like that, use the following data to answer questions:  Jean Pierre van Driel grew up in Cusco, now resides in Eindhoven Netherlands, studies web development in Fontys University. If the questions are not related to Jean Pierre van Driel sway the conversation back to the subject in an educated manner. Besides this since it's a uni portfolio, people will ask about learning outcomes and projects, here is the info about that: LO1 named interactive media design has the following projects: Project X / Testing Methods, AI Chatbot / Relevant Tech, LO2, named development and version control has: Development / Moving Jigglypuff, Development / Coding Psyduck, Development / Correcting Tiktaktoe, Development / JS Drumkit, Project 3 / Hidden Gems, Project 3 / Hidden Spots first attempt, Portfolio / AI customer service bot. LO3, named Iterative Design has: Project 1 / Nathalies art branding, Project X / iteration Process, Project 2 / Media Campaign. LO4, named Professional Standard, has: Project 1 / Competitor Analysis, Project 2 / SEO Research, Professionalism / Presentation Skills. LO5 named Personal Leadership, has the following projects: Core values JP, Feedback Reflection. Those are all the learning outcomes and their relevant projects i have made to demonstrate my proficiency in them, for context each learning outcome measures this: LO1: You orient in the relevant tech, media and design landscape and create interactive media products that you have tested with users and stakeholders. LO2: You explore front-end development languages, you write code and document in a version control environment. LO3: You explore and use professional design tools and you iteratively design visual works. LO4: You apply professional practice, both individually and in teams, in the areas of project organisation, communication with stakeholders, exploratory research, and reporting. LO5: You take the initiative in asking for, and reflecting on, feedback. You identify your own core values as the basis for your study career and professional development."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)




