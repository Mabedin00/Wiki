# NOT COMPLETE, UNTESTED
# import stuff

@app.route('/')
def main():
    # form for add page
    # form for go to page
    # list of pages
    # return render template of landing page

@app.route('/add')
def add():           # not sure if form syntax is correct
    addToDB(request.form.get('page'), request.form.get('text'))
    flash("Your page has been successfully added to wiki!") # include page name in message later
    return redirect(url_for('/'))

@app.route('/page')
def displayPage():
    return render_template('page.html',
                           page = request.form.get('page'),
                           text = getText(request.form.get('page'))
                                  # the right text, based off of page
                           )
                           # keep in mind these are different forms
