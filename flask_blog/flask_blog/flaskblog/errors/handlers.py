from flask import Blueprint,render_template

errors=Blueprint('errors', __name__)
#app_errorhandler(for error handler for the whole application)
#errorhandler(for error handling in this blueprint)
#


@errors.app_errorhandler(404)# 404 Error:(not found)
def error_404(errors):
	return render_template('errors/404.html'),404


errors.app_errorhandler(403)#403 Forbidden
def error_403(errors):
	return render_template('errors/403.html'),403


errors.app_errorhandler(500)#500 Internal Server Error(problem with the web server)
def error_500(errors):
	return render_template('errors/500.html'),500






