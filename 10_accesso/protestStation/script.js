/* If you're feeling fancy you can add interactivity 
    to your site with Javascript */

// prints "hi" in the browser's dev tools console
console.log("hi");

// document.addEventListener('DOMContentLoaded', function() {
//     let elems = document.querySelectorAll('.autocomplete');
//     let instances = M.Autocomplete.init(elems, options);
//   });

// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.materialboxed');
//     var instances = M.Materialbox.init(elems, inDuration);
//   });

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems, options);
  });