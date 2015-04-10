from bottle import route, run, template, debug, view, static_file, request


"""
Static routes
"""
@route('/js/<filename>')
def static_js(filename):
    return static_file(filename, root='./static/js')

@route('/css/<filename>')
def static_css(filename):
    return static_file(filename, root='./static/css')

@route('/img/<filename>')
def static_img(filename):
    return static_file(filename, root='./static/img')

@route('/fonts/<filename>')
def static_fonts(filename):
    return static_file(filename, root='./static/fonts')


"""
Index
"""
@route('/')
def index():
    test_message = 'Just beginning work...'
    return template('templates/index', test_message=test_message)


"""
Run
"""
debug(True)
run(reloader=True)

