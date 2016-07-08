const APPID = "3718d7f90e7b081ca8f46aa4305c05ea";
const QUERY = "http://api.openweathermap.org/data/2.5/weather";

$(document).ready(function(){
    console.log('here we go');
    $('button#search').on('click', function(){
        var location = $('input#location').val();
        console.log('searching ' + location);

        // get data
        $.get(QUERY, {APPID: APPID, q: location, units: 'metric'})
            .done(function(data){
                console.log('super');
                console.log(data);
            })
            .fail(function(data){
                alert('Error occurred');
                console.log('we have some problem');
                console.log(data);
            });

    });
});
