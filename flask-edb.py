from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    data = {"message": "햄부기햄북 햄북어 햄북스딱스 함부르크햄부가우가 햄비기햄부거 햄부가티햄부기온앤 온 을 차려오거라"}
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)