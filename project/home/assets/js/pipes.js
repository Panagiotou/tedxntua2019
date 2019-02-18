const seconds = 4;
const start_delay = 0.3;
const transition = "ease-in";

function polylineToPath() {
        var polylines = document.querySelectorAll('polyline');
        var maxlen = -1;
        for (i = 0; i < polylines.length; ++i) {
          var svgNS = polylines[i].ownerSVGElement.namespaceURI;
          var path = document.createElementNS(svgNS, 'path');
          var coords = polylines[i].getAttribute('points');
          path.setAttribute('d', 'M' + coords);
          path.setAttribute('id', 'p');
          //path.setAttribute('stroke-width', polylines[i].getAttribute('stroke-width'));
          path.setAttribute('stroke-width', 0.5);
          path.setAttribute('stroke',  "black");
          path.setAttribute('fill', polylines[i].getAttribute('fill'));
          path.setAttribute('fill-opacity', "0");
          var len = path.getTotalLength();
          if(len > maxlen){
            maxlen = len;
          }
          path.style.strokeDashoffset = len;
          path.style.strokeDasharray = len + ',' + len;
          //polylines[i].parentNode.appendChild(path);
          //polylines[i].parentNode.remove(polylines[i]);
          polylines[i].parentNode.replaceChild(path, polylines[i]);
        }

        var polygons = document.querySelectorAll('polygon');
        for (i = 0; i < polygons.length; ++i) {
          var svgNS = polygons[i].ownerSVGElement.namespaceURI;
          var path = document.createElementNS(svgNS, 'path');
          var coords = polygons[i].getAttribute('points');
          path.setAttribute('d', 'M' + coords);
          path.setAttribute('id', 'p');
          path.setAttribute('stroke-width', 0.5);
          path.setAttribute('stroke',  "black");
          path.setAttribute('fill', polygons[i].getAttribute('fill'));
          path.setAttribute('fill-opacity', "0");
          var len = path.getTotalLength();
          if(len > maxlen){
            maxlen = len;
          }
          path.style.strokeDashoffset = len;
          path.style.strokeDasharray = len + ',' + len;
          //polylines[i].parentNode.appendChild(path);
          //polylines[i].parentNode.remove(polylines[i]);
          polygons[i].parentNode.replaceChild(path, polygons[i]);
        }
        setTimeout(function(){
          animate(maxlen);
        }, start_delay*1000);
  }

  function animate(len) {
    var length = len;
    var paths = document.querySelectorAll('path');
    for (i = 0; i < paths.length; ++i) {
      var path = paths[i];
      // Clear any previous transition
      path.style.transition = path.style.WebkitTransition =
        'none';
      // Set up the starting positions
      path.style.strokeDasharray = length + ' ' + length;
      path.style.strokeDashoffset = length;
      // Trigger a layout so styles are calculated & the browser
      // picks up the starting position before animating
      path.getBoundingClientRect();
      // Define our transition
      path.style.transition = path.style.WebkitTransition =
        'stroke-dashoffset '+ seconds + 's ' + transition;
      // Go!
      path.style.strokeDashoffset = '0';
    }
    animateopacity();
  }

  function appear(elm, i, step, speed){
    var t_o;
    //initial opacity
    i = i || 0;
    //opacity increment
    step = step || 5;
    //time waited between two opacity increments in msec
    speed = speed || 50;

    t_o = setInterval(function(){
        //get opacity in decimals
        var opacity = i / 100;
        //set the next opacity step
        if(i>0.5){
          i = i +2*step;
        }
        else{
          i = i + step;
        }
        if(opacity > 1 || opacity < 0){
            clearInterval(t_o);
            //if 1-opaque or 0-transparent, stop
            return;
        }
        //modern browsers
        elm.style['fill-opacity'] = opacity;
        //older IE
        elm.style.filter = 'alpha(fill-opacity=' + opacity*100 + ')';
    }, speed);
  }

  function animateopacity(){
    setTimeout(function(){
      var paths = document.querySelectorAll('path');
      for (i = 0; i < paths.length; ++i) {
        /*if(paths[i].getAttribute('fill') == "#F69891"){
          appear(paths[i], 0, 2, 50);
        }
        */
        appear(paths[i], 0, 2, 50);
      }
    }, seconds*1000/2);
  }
  polylineToPath();
