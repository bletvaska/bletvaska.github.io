
// http://stackoverflow.com/questions/610406/javascript-equivalent-to-printf-string-format
// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}



function date_time(){
    var months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'Jully', 'August', 'September', 'October', 'November', 'December');
    var days = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday');

    var now = new Date();

    var year = now.getFullYear();
    var month = now.getMonth();
    var dom = now.getDate();
    var dow = now.getDay();
    var hour = now.getHours();
    var min = now.getMinutes();
    var sec = now.getSeconds();

    $("#dtStamp").text(now/1);
    $("#dtUStamp").text(Math.floor(now/1000));

    $('#now').text(now);

    //setTimeout('date_time("'+idStamp+'","'+idUStamp+'","'+idFormatted+'")','1000');
    setTimeout('date_time()','500');

var dt = `struct dt { 
    int sec;
    int min;
    int hour;
    int dom;
    int month;
    int year;
    int dow;
};

struct dt now = {
    .sec   = {0},
    .min   = {1},
    .hour  = {2},
    .dom   = {3},
    .month = {4}, // {5}
    .year  = {6},
    .dow   = {7} // {8}
};`.format(sec, min, hour, dom, month+1, months[month], year, dow, days[dow]);

    $("#struct-dt").text(dt);
    
    if(typeof hljs !== 'undefined'){
        $("#struct-dt").each(function(i, block) {
            hljs.highlightBlock(block);
          });
    }

    return true;
}




function getArrayWith(length, number){
    // populate array with random numbers
    var array = [];
    for( i = 0; i < length; i++ ){
        random = 0;
        do{
            random = Math.floor((Math.random()*20)+1);
        }while( array.indexOf(random) != -1 );

        array.push( random );
    }

    // check if there is number (from function param) in the array
    if( array.indexOf(number) == -1 ){
        array[ Math.floor((Math.random()*length))] = number;
    }

    return array;
}



window.addEventListener('load', function(event){
    /*
    $("#countdown").countdown("2017/11/8 19:00:00", function(event) {
        $(this).text(
            event.strftime('%D days %H:%M:%S')
        );
        $(this).css({
            "font-family": "courier",
            "font-weight": "bolder"
        });
    });
    */

    // More info about config & dependencies:
    // - https://github.com/hakimel/reveal.js#configuration
    // - https://github.com/hakimel/reveal.js#dependencies
    //Reveal.initialize({
        //dependencies: [
            //{ src: 'plugin/markdown/marked.js' },
            //{ src: 'plugin/markdown/markdown.js' },
            //{ src: 'plugin/notes/notes.js', async: true },
            //{ src: 'plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } }
        //]
    //});

    date_time();


    // set games
    var linearSearchArray = getArrayWith(7, 7);
    var binarySearchArray = getArrayWith(7, 7);
    binarySearchArray.sort(function(a,b){return a-b});

    // write it to the console (just for sure)
    console.log( linearSearchArray);
    console.log( binarySearchArray);

    $('#linear-search .button').click(function(){
        $(this).text( linearSearchArray[ $(this).index() ]);
    });

    $('#binary-search .button').click(function(){
        $(this).text( binarySearchArray[ $(this).index() ]);
    });
});
