$(document).ready(function(){var tocStarSelector='.row .star,.postingtitle .star,#mapcontainer .star';var $tocStars;var listBits=parseString($.totalStorage('cl_fav'));var listToken=listBits[0]||newToken();var favlist=listBits[1];(function(){if(window.expFaves){var expFavList=window.expFaves.split(',');for(var i=0;i<expFavList.length;i++){delete favlist[expFavList[i]];}
syncState();}
var mine=$.totalStorage('cl_fav');var page=unescape($.urlParam('fl'));if(mine!==page){var myBits=parseString(mine);var pageBits=parseString(page);if(pageBits[0]!==myBits[0]){$('.sharedFavList').show();}else{$('.oldFavList').show();}}})();function parseString(raw){var list={};var token;if(raw&&(raw.length>5)){raw=Base64.decode(raw);var testtoken=raw.match(/^(.+):/);if(testtoken!==null){token=testtoken[1];raw=raw.replace(/^.+:/,'');}
if(raw.length>0){var bits=raw.split(',');var base=bits.shift();list[base]=1;for(var i=bits.length-1;i>=0;--i){list[parseInt(base)+parseInt(bits[i])]=1;};}}
return[token,list];}
function newToken(){return Math.random().toString(36).substring(5);}
function favListString(){var base=0;var bits=[];var list=Object.keys(favlist).sort();var len=list.length;var toPush;for(i=0;i<len;i++){if(isNaN(list[i]))continue;if(base===0){base=list[i];toPush=base;}else{toPush=list[i]-base;}
bits.push(toPush);}
return Base64.encode(listToken+":"+bits.join(','));}
function toggleFav($t){var pid=pID||$t.data('pid');if($t.hasClass('fav')){delete favlist[pid];}else{if(Object.keys(favlist).length>=200){alert("Sorry, there is currently a limit of 200 concurrent favorites");return;}
favlist[pid]=1;}
$t.toggleClass('fav');syncState();}
function initStars(){var useStarHint=typeof starHint!=='undefined';$tocStars=$(tocStarSelector);if(!CL.browser.localStorageAvailable){$tocStars.hide();return;}else{$tocStars.addClass('v');if(useStarHint){$tocStars.attr('title',starHint);}}
$tocStars.each(function(){var $this=$(this);var pid=pID||$this.parents('p.row').data('pid');$this.toggleClass('fav',favlist[pid]===1).data('pid',pid);});$('h4 .star').off('click.star').on('click.star',function(){if($(this).hasClass('fav')){$tocStars.click();}else{$tocStars.not(".fav").click();}});$tocStars.off('click.star').on('click.star',function(){toggleFav($(this));});$('h4 button.delfaves').off('click.star').on('click.star',function(){favlist={};syncState();});syncState();}
function updateFavCount(){var fav_list_length=Object.keys(favlist).length;$('#favorites .n').text(fav_list_length);$('#favorites').toggle(!!(window.location.href.match(/\/favorites/)||fav_list_length!==0));$favlink=$('#favorites a');if(fav_list_length>0){$favlink.removeClass('off').attr('href','/favorites?fl='+favListString());}else{$favlink.addClass('off').attr('href','#');}}
function updateHeaderStar(){var countAllFavs=$('.row .star.fav').length;var $headerStar=$('h4 .star');if($tocStars.length===countAllFavs){$headerStar.removeClass('half').addClass('fav');}else if(countAllFavs===0){$headerStar.removeClass('fav half');}else{$headerStar.removeClass('fav').addClass('half');}}
function syncState(){$.totalStorage('cl_fav',favListString());updateFavCount();updateHeaderStar();}
initStars();CL.extend('favorites',{init:initStars,sync:syncState});});