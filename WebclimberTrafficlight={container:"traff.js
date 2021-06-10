WebclimberTrafficlight = {
    container: 'trafficlightContainer',
    insertTrafficlight: function(e) {
        e && e.html && (document.getElementById(e.container).innerHTML = e.html)
    },
    loadTrafficlight: function(e, t, i, r, c) {
        if (!e || !t) return !1;
        r || (r = ''), c || (c = ''), i ? WebclimberTrafficlight.container = i : i = WebclimberTrafficlight.container;
        let n = document.createElement('script');
        n.setAttribute('src', 'https://' + e + '.webclimber.de/de/trafficlight?callback=WebclimberTrafficlight.insertTrafficlight&key=' + t + '&hid=' + e + '&container=' + i + '&type=' + r + '&area=' + c), n.setAttribute('id', 'jsonp' + i), document.getElementsByTagName('head')[0].appendChild(n)
    }
};