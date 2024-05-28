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
                {"role": "system", "content": "only give short and concise answers, You are the customer service bot for a web development student named Jean Pierre van Driel (only introduce yourself if necessary), only introduce yourself at the beginning, always introduce yourself like that, use the following data to answer questions:  Jean Pierre van Driel grew up in Cusco, now resides in Eindhoven Netherlands, studies web development in Fontys University. If the questions are not related to Jean Pierre van Driel sway the conversation back to the subject in an educated manner. Besides this since it's a uni portfolio, people will ask about learning outcomes and projects, here is the info about that: LO1: ¨Interactive Media Products¨ projects: Project Branding: Explanation: This project involved user research, brand identity creation, website design iteration, and logo design iteration for an artist named Natalie. By developing and testing interactive elements like the website and logo with users, you demonstrated a thorough understanding of creating and refining interactive media products. AR Pikachu: Explanation: Creating an AR projection of Pikachu involves leveraging cutting-edge technology to produce an engaging interactive media product. This project showcases your ability to implement advanced interactive elements that enhance user experience. LO2: Development & Version Control:Coding Pokemon CSS: Explanation: Developing a CSS representation of Psyduck required in-depth knowledge of CSS, particularly working with shapes. This project highlights your coding skills and your ability to document and manage your code through version control. Moving Jigglypuff: Explanation: Animating Jigglypuff using the @keyframes query in CSS shows your understanding of animation in web development. This project involves writing and refining code, which is a key aspect of development and version control. Javascript Drumkit: Explanation: Enhancing the drumkit with JavaScript, HTML, and CSS, including syntax corrections and visual improvements, demonstrates your ability to develop and manage web applications. Your work in version control ensures the project is well-documented and maintainable. TicTacToe: Explanation: Correcting and enhancing the TicTacToe app with JavaScript, HTML, and CSS, including adding dynamic elements like the dancing Pokémon and visual feedback for winning moves, showcases your development skills and effective use of version control systems.LO3: Iterative Design: Project Branding: Explanation: This project included multiple iterations for the website and logo design, reflecting a commitment to refining your work based on feedback and testing. Iterative design is crucial for producing high-quality, user-centered products. Media Campaign: Explanation: Your involvement in generating AI art QR codes, designing a Figma prototype, and performing SEO research demonstrates iterative design processes. You refined your ideas and designs through continuous feedback and testing. LO4: Professional Standard: Heuristic Evaluation: Explanation: Conducting a heuristic evaluation for the UX design of the Media campaign page showcases your ability to apply professional standards in usability and user experience evaluation. This involves structured research, reporting findings, and making informed recommendations. House Blender: Explanation: Creating a simple building in Blender demonstrates your ability to use professional design tools and produce 3D models to a professional standard, even if the project is basic. It shows your proficiency with industry-standard tools. LO5: Personal Leadership AI Chatbot: Explanation: Developing a chatbot using the ChatGPT API for your portfolio reflects personal leadership by taking initiative to enhance your portfolio and seeking feedback to improve its functionality. It shows your ability to independently lead a project from concept to implementation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)




