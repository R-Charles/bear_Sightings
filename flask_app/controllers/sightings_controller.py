from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.sighting_model import Sighting
from flask_app.models.user_model import User

#move this sighting to controller from from users_controller
# @app.route( '/' )
# def display_sightings():
#     # if 'email' not in session:
#     #     return redirect( 'login.html' )

#     list_sightings = Sighting.get_all_with_users()    #Grab all the recipes
#     print(list_sightings)
#     return render_template( 'sightings.html', list_sightings = list_sightings )

@app.route('/sightings')
def show_all():
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "email" : session['email']

    }
    loggedin_user=User.get_one_to_validate_email(data)
    print(loggedin_user)
    sightings=Sighting.get_one_with_user(data)
    sightings_list = Sighting.get_all_with_users()
    return render_template('sightings.html', sightings_list = sightings_list, loggedin_user = loggedin_user )

@app.route( '/sightings/new' )
def display_create_sighting():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "sightings.html" )

@app.route( '/sightings/create', methods = ['POST'] )
def create_sighting():
    if Sighting.validate_sighting( request.form ) == False:  #validate fields
        return redirect( '/sightings/new' )

    data = {
        **request.form,
        "user_id" : session['user_id']
    }

    Sighting.create( data )
    return redirect( '/' )

@app.route( '/sightings/<int:id>' )
def display_one( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_sighting = Sighting.get_one_with_user( data )
    return render_template( "sightings.html", current_sighting = current_sighting )

@app.route( '/sightings/<int:id>/update' )
def display_update_sighting( id ):
    if 'email' not in session:
        return redirect( '/' )
    data = {
        "id" : id
    }
    current_sighting = Sighting.get_one_with_user( data )
    return render_template( "update_sightings.html", current_sighting = current_sighting )


@app.route( '/sightings/update/<int:id>', methods = ['POST'] )
def update_sighting( id ):
    if Sighting.validate_sighting( request.form ) == False:  #validate fields
        return redirect( f'/sightings  /{id}/update' )
    # return redirect( '/sightings ' )
    sighting_data = {
        **request.form,
        "id": id,
    }
    Sighting.update_one( sighting_data)
    return redirect( '/sightings   ' )

@app.route( '/sightings/<int:id>/delete' )
def delete_sighting( id ):
    print('hello')
    data = {
        "id" : id 
    }
    Sighting.delete_one( data )
    return redirect( '/sightings' )

    #if validation goes through, create recipe
    #redirect to /recipes
