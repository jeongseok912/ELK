#from route.elf_test_route import elk_test
#from flask import Flask, Blueprint
from flask import Flask, render_template, flash, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = '1234'


#app.register_blueprint(elk_test)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run()
    