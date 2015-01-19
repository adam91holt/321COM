/**
 * Created with 321COM Task4-5.
 * User: adam91holt
 * Date: 2014-11-20
 * Time: 01:35 PM
 * To change this template use Tools | Templates.
 */

function getLoc(lon,lat,id) {
    function initialize() {
        var mapProp = {
            center: new google.maps.LatLng(lat, lon),
            zoom: 12,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById(id), mapProp);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat, lon),
            map: map,
            title: 'Sent Here!'
        });
    }  
    document.getElementById(id).style.display = 'block';
    initialize()
}
