import bottle
import ephem

import pprint


"""
Static routes
"""
@bottle.route('/js/<filename>')
def static_js(filename):
    return bottle.static_file(filename, root='./static/js')

@bottle.route('/css/<filename>')
def static_css(filename):
    return bottle.static_file(filename, root='./static/css')

@bottle.route('/img/<filename>')
def static_img(filename):
    return bottle.static_file(filename, root='./static/img')

@bottle.route('/fonts/<filename>')
def static_fonts(filename):
    return bottle.static_file(filename, root='./static/fonts')


"""
Index
"""
@bottle.route('/')
def index():
    # Default find for current location. For now, make this Richardson
    lon = -96.743857
    lat = 32.950962
    location = (lon, lat)

    observer = ephem.Observer()
    observer.lon = lon
    observer.lat = lat

    moon = ephem.Moon()
    moon.compute(observer)

    '''
    yh = ephem.readdb("C/2002 Y1 (Juels-Holvorcem),e,103.7816," +
            "166.2194,128.8232,242.5695,0.0002609,0.99705756,0.0000," +
            "04/13.2508/2003,2000,g  6.5,4.0")
    yh.compute('2003/4/11')
    print(yh.name) >>> C/2002 Y1 (Juels-Holvorcem)
    print("%s %s" % (yh.ra, yh.dec)) >>> 0:22:44.58 26:49:48.1
    print("%s %s" % (ephem.constellation(yh), yh.mag)) >>> ('And', 'Andromeda') 5.96
    '''

    test_message = 'Just beginning work...'
    return bottle.template(
        'templates/index',
        test_message=test_message,
        location=location
    )


"""
Run
"""
bottle.debug(True)
bottle.run(reloader=True)

