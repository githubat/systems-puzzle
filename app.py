import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    results = []

    head = '<head> <style> table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } \
            td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style> </head>'
 
    qry = db_session.query(Items)
    results = qry.all()

    ret = '<html>{:s}<body><table>{:s}</table></body></html>'.format( head,
          ''.join( [ '<tr><th>{:s}</th><th>{:s}</th><th>{:s}</th><th>{:s}</th></tr>'.format(x.name, str(x.quantity), x.description, str(x.date_added) ) for x in results ] ) )

    return str( ret )
  

if __name__ == '__main__':
    app.run(host='0.0.0.0')
