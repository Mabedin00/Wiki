# UNTESTED
# Make sure you guys's variable names sync with these
# Change something if it's wrong/incompatible, but make a note

from flask import Flask, render_template, request, redirect, url_for, flash

@app.route('/')
def main():
    # form for add page
    # form for go to page
    # list of pages
    return render_template('index.html')

@app.route('/add')
def add():           # args is for get, form is for post. I think get should work? But not sure
    addToDB(request.args.get('page'), request.args.get('text'))
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
