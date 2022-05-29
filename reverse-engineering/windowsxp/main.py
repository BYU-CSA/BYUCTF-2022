from jinja2 import Template
from flask import Flask, render_template, request, send_file
def main():
    app = Flask(__name__)

    @app.route('/')
    def home():
        print('getting template!')
        return render_template('index.html')

    @app.route('/js/challenge.js')
    def get_flexbox():
        return render_template('challenge.js')

    @app.route('/images/<image>')
    def get_image(image):
        print(request.args)
        if request.args.get('flag') == 'steve is so cool':
            print('sending flag!')
            return send_file('images/flag.png', mimetype='image/gif')
        return send_file('images/normal.png', mimetype='image/gif')

    app.run(debug=False, host='0.0.0.0', port=40016)
    
if __name__ == '__main__':
    main()
