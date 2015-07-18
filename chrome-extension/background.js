chrome.runtime.onInstalled.addListener(function() {
  var context = "image";
  var title = "LinkedIn Image Search";
  var id = chrome.contextMenus.create({"title": title, "contexts":[context],
                                         "id": "context" + context, "onclick": onClickHandler});  
});

// add click event
//chrome.contextMenus.onClicked.addListener(onClickHandler);

// The onClicked callback function.
var onClickHandler = function(e) {
  var url = encodeURI(e.srcUrl);  
  console.log(url);
  window.open('https://proj-nishantgill.c9.io/down?url='+url, '_blank');
};