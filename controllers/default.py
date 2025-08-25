# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
# Fichier : applications/yourapp/controllers/default.py

def figmatoliveai():
    """
    Cette fonction gère le formulaire d'inscription personnalisé
    pour la liste d'attente.
    """
    # 1. Création de l'objet SQLFORM
    form = SQLFORM(db.waitlist, fields=['email'])

    # 2. Personnalisation des widgets pour correspondre à votre HTML
    
    # Personnalisation du champ de saisie email
    form.custom.widget.email['_placeholder'] = 'your.email@company.com'
    form.custom.widget.email['_aria-label'] = 'Email address'
    # Note : Les classes CSS de votre exemple ne sont pas présentes ici, 
    # mais vous pourriez les ajouter avec `_class` si nécessaire.
    
    # Personnalisation du bouton de soumission
    form.custom.submit['_class'] = 'ui primary button'
    form.custom.submit['_value'] = 'Notify Me at Launch'


    # 3. Traitement du formulaire
    if form.process().accepted:
        response.flash = T('Thank you for joining the waitlist!')
    elif form.errors:
        response.flash = T('Please correct the errors below.')

    # 4. On passe le formulaire personnalisé à la vue
    return dict(form=form)

def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
