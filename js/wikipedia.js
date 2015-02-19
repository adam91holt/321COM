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
               var div = document.getElementById('wikiInfo')
               div.innerHTML = response['query']['pages'][pageid]['extract']
           }
       };
       httpRequest.send();
   });  
}