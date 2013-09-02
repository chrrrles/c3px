;(function($){var ls=window.localStorage;var supported=(ls&&'getItem'in ls&&typeof window.JSON!=='undefined');$.totalStorage=function(key,value,options){return $.totalStorage.impl.init(key,value);}
$.totalStorage.setItem=function(key,value){return $.totalStorage.impl.setItem(key,value);}
$.totalStorage.getItem=function(key){return $.totalStorage.impl.getItem(key);}
$.totalStorage.getAll=function(){return $.totalStorage.impl.getAll();}
$.totalStorage.deleteItem=function(key){return $.totalStorage.impl.deleteItem(key);}
$.totalStorage.impl={init:function(key,value){if(typeof value!='undefined'){return this.setItem(key,value);}else{return this.getItem(key);}},setItem:function(key,value){if(!supported){try{$.cookie(key,value);return value;}catch(e){}}
var saver=JSON.stringify(value);try{ls.setItem(key,saver);}catch(e){return null;}
return this.parseResult(saver);},getItem:function(key){var value=null;if(!supported){try{return this.parseResult($.cookie(key));}catch(e){return null;}}
try{value=ls.getItem(key);}catch(e){}
return this.parseResult(value);},deleteItem:function(key){if(!supported){try{$.cookie(key,null);return true;}catch(e){return false;}}
try{ls.removeItem(key);}catch(e){return false;}
return true;},getAll:function(){var items=new Array();if(!supported){try{var pairs=document.cookie.split(";");for(var i=0;i<pairs.length;i++){var pair=pairs[i].split('=');var key=pair[0];items.push({key:key,value:this.parseResult($.cookie(key))});}}catch(e){return null;}}else{for(var i in ls){if(i.length){try{items.push({key:i,value:this.parseResult(ls.getItem(i))});}catch(e){}}}}
return items;},parseResult:function(res){var ret;try{ret=JSON.parse(res);if(ret=='true'){ret=true;}
if(ret=='false'){ret=false;}
if(parseFloat(ret)==ret&&typeof ret!="object"){ret=parseFloat(ret);}}catch(e){}
return ret;}}})(jQuery);