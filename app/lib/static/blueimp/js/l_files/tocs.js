$(document).ready(function(){$('#catAbb, input.min, input.max').prop('disabled',false);var modeToShow=checkCookie()||'list';var $body=$('body');var isMapMode=$body.hasClass('map');if(isMapMode){modeToShow='map';}
if(modeToShow=='show'){modeToShow='pic';}
var viewMode=function(mode){if(mode==='map'){if(!isMapMode){$('#zoomtoposting').val('');$('#usemapcheck input').prop('checked',true);$('#searchform').submit();}}else{setImgCookie(mode);if(isMapMode){$('#usemapcheck input').prop('checked',false);$('#searchform').submit();return;}
$body.removeClass('list pic grid').addClass(mode);if(mode=='list'){$('p.row').show();}else if(mode=='pic'){$('p.row').show();addFloater();populateImageSpans('50x50c');$('p.row .i:not(:has(img))').addClass('empty').attr('title','no image');}else if(mode=='grid'){removeFloater();populateImageSpans('300x300');$('p.row .i:not(:has(img))').addClass('empty').attr('title','no image');}}};var addFloater=function(){var $floater=$('#floater');var $payload=$floater.find('img.payload');var visible=false;if(!$body.hasClass('mobile')){$('.i').on('mouseover',function(){var imgID=$(this).data('id');if(imgID){$floater.show();$payload.attr('src',imgURL(imgID,'300x300'))
.on('load',function(){$('#floater').addClass('f');});visible=true;}})
.on('mouseout',function(){$floater.hide().removeClass('f');$payload.attr('src','');visible=false;})
.on('mousemove',function(e){if(visible){$('#floater').css({'left':e.pageX+15+'px','top':e.pageY+15+'px'});}});}}
var removeFloater=function(){$('.i').off();$('#floater').hide();}
viewMode(modeToShow);if($.fn.DefaultValue){$('input.min').DefaultValue('min');$('input.max').DefaultValue('max');$('#query').DefaultValue('search');}
$('#catAbb').change(function(){$('#searchform').submit();});$('#nh').hide().removeAttr('disabled');newSel=$('#nh').clone();newSel.find('#all').remove();$('#nh').replaceWith(newSel);$('#hoodtogon, #hoodtitle').show();$('#hoodtitle').click(function(e){e.preventDefault;toggleHoods();});countHoods();$body.click(function(e){if(!$(e.target).parents('#hoodpicker').length){$('#hoodtogon').show();$('#hoodtogoff').hide();$('#nh').slideUp(100);}});$('#satabs a').click(function(e){e.preventDefault();var f=$('#searchform');var t=f.attr('action').match(/\/search\/.../);var s=getSubarea($(this).attr('href'));if(s){t=t+"/"+s;}
f.attr('action',t);$('select#nh').prop('disabled',true);f.submit();});$("a.gc,#searchlegend a").click(function(e){e.preventDefault();flipCatAndSubmit($(this).data('cat'));});$('#'+modeToShow+'view').addClass('down');if($('div.container').html()){$('#toc_rows blockquote').first().hide();}
var $modeButtons=$('.modebtns button');$modeButtons.on('click',function(e){var $this=$(this);if($this.hasClass('down')){return;}
e.preventDefault();var newMode=$this.attr('id').replace('view','');$modeButtons.removeClass('down');$this.addClass('down');viewMode(newMode);});$('span.itemsfound').prependTo('div.container');$('a.maptag').click(function(){var mapTagPostingID=$(this).data('pid');$('#usemapcheck input').prop('checked',true);$('#zoomtoposting').val(mapTagPostingID);$('#searchform').submit();});});function toggleHoods(){$('#hoodtogon, #hoodtogoff').toggle();$('#nh').slideToggle(100);$('select#nh').toChecklist({addScrollBar:false,showSelectedItems:true,submitDataAsArray:false});$('#nh').click(countHoods);countHoods();}
function countHoods(){$('span#hoodcount').text($('#nh :checked').length||$('#nh :selected').length||'all');}
function setImgCookie(val,time){var date=new Date();time=time||date.getTime();date.setTime(time+(365*24*60*60*1000));document.cookie="cl_img="+val+"; expires=0; path=/";document.cookie="cl_img="+val+"; expires="+date.toGMTString()+"; path=/; domain=craigslist.org";}
var imgNewToOldSizes={'50x50c':'thumb/','300x300':'medium/','600x450':''};function imgURL(img_id,size){if(img_id.indexOf(':')==-1){return imageHost+'/'+imgNewToOldSizes[size]+img_id;}
return imageHost+'/'+img_id.substr(2)+'_'+size+'.jpg';}
function populateImageSpans(size){size=size||'50x50c';$('.i').each(function(){var img_id=$(this).data('id');if(img_id){$(this).html('<img alt="" src="'+imgURL(img_id,size)+'">');}});}
function getSubarea(url){var match=url.match(/\/search\/...\/(...)/);if(match){return match[1];}
match=url.match(/\/(...)\/...\//);if(match){return match[1];}}
function checkCookie(){var C=document.cookie.split(/\s*;\s*/);for(i=0;i<C.length;i++){var c=C[i];if(c.indexOf('cl_img=')===0)return c.substring(7);}
return null;}
function flipCatAndSubmit(cat){$('#searchform').find('#catAbb').val(cat).end().submit();}
