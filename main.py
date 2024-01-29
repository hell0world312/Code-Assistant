from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "" #put token here


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    
    message = "You are Dimension, one of the best programmers out there who has a lot of experience in the field and can do anything from writing, reviewing and fixing code. Make sure to keep your answers short and concise. Here is my prompt: " + request.json.get("message")
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

