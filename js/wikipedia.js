
 


function getwiki(pageid){
     var httpRequest, key = "oCdV3MjLj1mshtyIXwBVzBqRKtY9p1XJNiajsn1vsCETYVLwK3";
   var url = "https://community-wikipedia.p.mashape.com/api.php?format=json&action=query&prop=extracts&pageids="+ pageid + "&redirects=true";
   return new Promise(function(resolve, reject) {
       if(window.XMLHttpRequest) { // mozilla, safari,...
           httpRequest = new XMLHttpRequest();
       } else if(window.ActiveXObject) {
           httpRequest = ("Microsoft.XMLHTTP");
       }
       httpRequest.open('GET', url);
       httpRequest.setRequestHeader("X-Mashape-Key", key);
       httpRequest.onload = function() {
           if(httpRequest.readyState === 4 && httpRequest.status === 200) {
               var response = JSON.parse(httpRequest.responseText);
               console.log(response['query']['pages'][pageid])
           }
       };
       httpRequest.send();
   });
    
    
}


function init(){
    console.log(document.getElementById('getteam'))
//    document.getElementById('getteam').addEventListener("click", function(){
//        getwiki('Arsenal_F.C')
//    })
} 
// var displayItems = function(response) {
//    'use strict';
//    var i,
//        newlist = document.createElement('UL'),
//        div = document.getElementById('suggestions'),
//        newitem = '',
//        text = '',
//        link = '';
//    response.forEach(function(item) {
//        text = document.createTextNode(item);
//        newitem = document.createElement('li');
//        link = document.createElement('a');
//        link.href = "http://en.wikipedia.org/wiki/" + item.replace(/ /g, "_");
//        link.appendChild(text);
//        newitem.appendChild(link);
//        newlist.appendChild(newitem);
//    });
//    div.appendChild(newlist);
// };
 
window.onload = init();