  const seconds = 3;
  const transition = "linear";
  const max_lines = 50;
function animate_paths() {
          var paths = document.querySelectorAll('path');
          var TotalLengths = new Array(max_lines).fill(0); // TotalLength of line
          var allLines = 0;
          var groups = new Array(max_lines).fill(0); // keeps number of groups[line] = # of groups in line
          for (i = 0; i < paths.length; ++i) {
            if(paths[i].getAttribute('fill') !="#FFFFFF"){
              var gr = paths[i].getAttribute('g')
              var li = paths[i].getAttribute('l');
              if(gr > groups[li]){
                groups[li] = gr;
              }
              if(li > allLines ){
                allLines  = li;
              }
              paths[i].setAttribute('fill-opacity', "0");
              var len = paths[i].getTotalLength();
              paths[i].style.strokeDashoffset = len;
              paths[i].style.strokeDasharray = len + ',' + len;
              TotalLengths[li] += len;
            }
          }
          // Set transition delay for each path
          for(line=0; line <=allLines ; line++ ){
            var ttw = 0;
            for (i = 0; i <=groups[line]; ++i) {
              path_group = document.querySelectorAll(`[g="${i}"][l="${line}"]`);
              for (j = 0; j < path_group.length; ++j) {
                mylength = path_group[j].getTotalLength();
                time_to_excecute = (mylength/TotalLengths[line]);
                path_group[j].style['transition-delay'] = ttw*seconds + "s";
                console.log(`Path g= ${i} l= ${line} waits ${ttw*seconds}`)
              }
              ttw += time_to_excecute;
            }
          }
          animate(TotalLengths);
    }

    function animate(TotalLengths) {
      var paths = document.querySelectorAll('path');
      for (i = 0; i < paths.length; ++i) {
          var length = paths[i].getTotalLength();
          // Set up the starting positions
          paths[i].style.strokeDasharray = length + ' ' + length;
          paths[i].style.strokeDashoffset = length;
          // Trigger a layout so styles are calculated & the browser
          // picks up the starting position before animating
          paths[i].getBoundingClientRect();
          // Define our transition
          var li = paths[i].getAttribute('l');
          var total = TotalLengths[li]; // Get TotalLength of current paths, line
          time_to_excecute = (length/total)*seconds; // paths animation duration
          paths[i].style['transition-property'] = 'stroke-dashoffset';
          paths[i].style['transition-duration'] = time_to_excecute + "s";
          paths[i].style['transition-timing-function'] = transition;
          // Go!
          paths[i].style.strokeDashoffset = '0';
        }
    }
    animate_paths();
