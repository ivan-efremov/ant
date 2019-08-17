from xml.etree.ElementTree import XMLParser

class DocElemet:
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):
        print tag
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        pass

parser = XMLParser(target=MaxDepth(), encoding='UTF-8')
exampleXml = """ \
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> \
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" xmlns:og="http://opengraphprotocol.org/schema/" itemscope itemtype="http://schema.org/Article" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:fb="http://ogp.me/ns/fb#"><!-- Обявление стандарта. Не убирать! -->

<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# article: http://ogp.me/ns/article#">

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="description" content="Самые свежие новости России, мира, СНГ и регионов РФ. Фото и видео. Актуальные материалы. Политика. Экономика. Общество. Происшествия. Культура. Звезды." />
<meta name="RATING" content="General" />
<title>Мисс купальник &quot;КП&quot;</title>


<link rel="icon" href="http://www.kp.ru/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="http://www.kp.ru/favicon.ico" type="image/x-icon" />

<link href="/css/odkl_share.css" rel="stylesheet" />

<!-- Стили расположены в 3х файлах. Первый для всех браузеров, кроме IE. Второй только для IE 8. Третий переопределяет стили для IE 6-7 -->
<link href="/css/common.css" rel="stylesheet" type="text/css" />
<link href="/css/comments.css" rel="stylesheet" type="text/css" />
<link href="/css/poll.css?v1" rel="stylesheet" type="text/css" />
<link href="/css/header-footer.css?v1" rel="stylesheet" type="text/css" />
<link href="/css/button.css" rel='stylesheet' type='text/css' />
<link href="/css/kp-share.css" rel='stylesheet' type='text/css' />
<link href="/css/col.css" rel="stylesheet" type="text/css" />
<link href="/css/contest.css" rel='stylesheet' type='text/css' />

<!--[if (gte IE 8) & (lte IE 9)]>
<link href="/css/ie8and9.css" rel="stylesheet" type="text/css" />
<![endif]-->

<!--[if lt IE 8]>
<link href="/css/ie_old.css" rel="stylesheet" type="text/css" />
<![endif]-->

<!--[if !IE]><!-->
<script>if(/*@cc_on!@*/false){document.documentElement.className+=' ie10';}</script>
<!--<![endif]-->
<link href="/css/ie_new.css" rel="stylesheet" type="text/css" />


<!-- Конец объявления стилей -->
   
   <script type="text/javascript"  src="/_js_out/prototype.js"></script><!--1.6.1.0-->
   <script type="text/javascript"  src="/_js_out/scriptaculous.js"></script><!--1.8.2-->
   <script type="text/javascript" src="/_js_out/jquery.min.js"></script><!--1.9.1-->
   <script type="text/javascript" src="/_js_out/jquery-ui.js"></script><!--1.9.2-->
   <script type="text/javascript" src="http://api-maps.yandex.ru/2.0.17/?load=package.full&lang=ru-RU" id="yandexmaps_script"></script>
   <script type="text/javascript"  src="/_js/jquery.jcarousel.min.js"></script>
   <script type="text/javascript"  src="/_js/jquery.mousewheel.js"></script>
   <script type="text/javascript">
      $.noConflict();
      KPjQuery = jQuery.noConflict();
   </script>

<script type="text/javascript" src="/_js/jquery.jscrollpane.min.new.js"></script>
<script type="text/javascript">
$(function(){
  $('.scroll-pane').jScrollPane();
});
</script>

   <script type="text/javascript" language="javascript" src="/_js/flowplayer-3.2.8.min.js"></script>
   <script type="text/javascript" language="javascript" src="/_js/flowplayer.ipad-3.2.1.min.js"></script>
   <script type="text/javascript" language="javascript" src="/_js/flowplayer.embed-3.0.3.min.js"></script>

   <script type="text/javascript" language="javascript" src="/_js/jwplayer.min.js"></script>

   <script type="text/javascript" src="/_js/swfobject.js"></script>

   <!--<script type="text/javascript" src="http://my.kp.ru/login/view.do?fmt=js&userpicSize=b28"></script>-->
   
   <script type="text/javascript" src="/_js/kp.js?ts=1404916115"> </script>
   <script type="text/javascript" src="/_js/carousel.js"></script>
   <script type="text/javascript" src="/_js/rtools.js"></script>

<!-- Для кнопки Мне нравится! соц. сети ВКонтакте!! ПОТОМ ВЫПИЛИТЬ В КОНЕЦ-->
    <script async type="text/javascript"
            src="http://userapi.com/js/api/openapi.js?31"
            onload='(function(){
                VK.init({apiId: 2353840, onlyWidgets: true});
                var e = document.createElement("script");
                e.src = "http://vk.com/js/api/share.js?11";
                e.charset="utf-8";
                e.type="text/javascript";
                document.getElementsByTagName("head")[0].appendChild(e); 
            })();'>
    </script>
<!-- Для кнопки Поделиться! соц. сети ВКонтакте, конец -->


<script type="text/javascript" src="/_js/button.js" charset="utf-8"></script>
<script type="text/javascript" src="/_js/kp-share.js" charset="utf-8"></script>


                        <style>
#uslotitem16873 .all_block-title { background: url("http://www.kp.ru/f/160/banner_img/72/68/16872.jpg") no-repeat scroll left bottom rgba(0, 0, 0, 0) }
</style>

<script type='text/javascript'>
var crtg_nid="2044";
var crtg_cookiename="crt_kpru";
var crtg_varname="crtg_content";
function crtg_getCookie(c_name){ var i,x,y,ARRCookies=document.cookie.split(";");for(i=0;i<ARRCookies.length;i++){x=ARRCookies[i].substr(0,ARRCookies[i].indexOf("="));y=ARRCookies[i].substr(ARRCookies[i].indexOf("=")+1);x=x.replace(/^\s+|\s+$/g,"");if(x==c_name){return unescape(y);}}return'';}
var crtg_content = crtg_getCookie(crtg_cookiename);var crtg_rnd=Math.floor(Math.random()*99999999999);
var crtg_url=location.protocol+'//rtax.criteo.com/delivery/rta/rta.js?netId='+escape(crtg_nid);crtg_url+='&cookieName='+escape(crtg_cookiename);crtg_url+='&rnd='+crtg_rnd;crtg_url+='&varName=' + escape(crtg_varname);
var crtg_script=document.createElement('script');crtg_script.type='text/javascript';crtg_script.src=crtg_url;crtg_script.async=true;
if(document.getElementsByTagName("head").length>0)document.getElementsByTagName("head")[0].appendChild(crtg_script);else if(document.getElementsByTagName("body").length>0)document.getElementsByTagName("body")[0].appendChild(crtg_script);</script>
<script type="text/javascript" src="http://www.kp.ru/regions/adv/library/adfox.asyn.code.ver3.js"> </script>
<script type="text/javascript" src="http://www.kp.ru/regions/msk/adriver/adriver.core.2.js"></script>
<meta  name="adriverDefaults"content="sid:51864, bt:52"/> 
<meta  name="adriverOptions"content="autoLoad:0"/>
<script  type="text/javascript">new adriver.Plugin.require("onScroll.adriver");</script>
                       
<script type="text/javascript">
var kpVideoAdvertSettings = {
  "plugins": {
    "/_swf/jwplayer/ova-jw.swf": {
      "ads": {
        "skipAd": {
          "enabled": true,
          "html": "<p>Пропустить</p>",
          "region": {
            "id": "my-new-skip-ad-button",
            "verticalAlign": 3,
            "horizontalAlign": 3,
            "backgroundColor": "#FF3300",
            "opacity": 0.8,
            "borderRadius": 15,
            "padding": "0 1 1 13",
            "width": 100,
            "height": 20
          },
          "parseWrappedAdTags": true,
        },
        "notice": {
          "message": "<p class=\"smalltext\" align=\"right\"> До конца рекламы осталось _countdown секунд</p>",
        },
        "clickSign": {
          "html": "<p class=\"smalltext\" align=\"center\">Нажмите для получения информации</p>"
        },
        "schedule": [
          {
            "position": "pre-roll",
            "tag": "http://ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&bn=1&target=top&bt=61&pz=2&rnd=__random-number__"
          }
        ]
      },
            "debug": {
                "debugger": "firebug",
                "levels": "fatal, config, vast_template"
            }
    }
  }
}
</script>






<!-- og-tags для соцсетей -->
  <meta name="mrc__share_title" content="Мисс купальник &quot;КП&quot;">
  <meta property="og:title" content="Мисс купальник &quot;КП&quot;" />
  <meta itemprop="name" content="Мисс купальник &quot;КП&quot;">
  <meta property="og:type" content="article" />
  <meta property="og:url" content="http://www.kp.ru/daily/forumcontest/photo/113571/?geo=1&view=desktop?view=desktop" />
  <meta property="og:site_name" content="КП" />
  <meta property="fb:app_id" content="191944177588942" />
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@onlinekpru">
  <meta name="twitter:url" content="http://www.kp.ru/daily/forumcontest/photo/113571/?geo=1&view=desktop?view=desktop">
  <meta name="twitter:title" content="Мисс купальник &quot;КП&quot;">
  <meta name="twitter:image" content="http://www.kp.ru/f/3/image/87/66/1736687.jpg">
  <link rel="image_src" href="http://s2.stc.all.kpcdn.net/f/3/image/87/66/1736687.jpg" />
  <meta property="og:image" content="http://www.kp.ru/f/3/image/87/66/1736687.jpg" />
  <meta itemprop="image" content="http://www.kp.ru/f/3/image/87/66/1736687.jpg">
  <meta name="mrc__share_description" content="Наши читательницы - самые красивые и стильные! Участвуйте в конкурсе! 
">
  <meta property="og:description" content="Наши читательницы - самые красивые и стильные! Участвуйте в конкурсе! 
" />
  <meta itemprop="description" content="Наши читательницы - самые красивые и стильные! Участвуйте в конкурсе! 
">
  <meta name="twitter:description" content="Наши читательницы - самые красивые и стильные! Участвуйте в конкурсе! 
">

<!-- #PARTNER_HEAD_TAGS# -->

</head>



  <body>
                        
<script language="JavaScript" type="text/javascript" src="//js.revsci.net/gateway/gw.js?csid=F09828&auto=t&bpid=kpru"></script>
<!-- VDNA Audience Analytics Tag -->
<script>
    (function(){
        var b, a;
        b=document.createElement("script");
        b.src="//a1.vdna-assets.com/analytics.js";
        b.async=true;
        a=document.getElementsByTagName("head")[0];
        a.insertBefore(b,a.firstChild);
        this.VDNA=this.VDNA||{};
        this.VDNA.queue=this.VDNA.queue||[];
    }());

    VDNA.queue.push({apiKey : "kp.ru", method : "reportPageView"});
</script>
<!-- tns-counter.ru --> 
<script language="JavaScript" type="text/javascript"> 
  var img = new Image();
  img.src = 'http://www.tns-counter.ru/V13a***R>' + document.referrer.replace(/\*/g,'%2a') + '*kp_ru/ru/UTF-8/tmsec=kp_other/' + Math.round(Math.random() * 1000000000);
</script> 
<noscript> 
  <img src="http://www.tns-counter.ru/V13a****kp_ru/ru/UTF-8/tmsec=kp_other/" width="1" height="1" alt="">
</noscript> 
<!--/ tns-counter.ru -->
<!-- Kavanga.AdEngine START -->
<!-- Газета "Комсомольская правда" - последние новости России. -->
<!-- ZeroPixel -->
<script language="JavaScript">
<!--
  var kref = '';
  try {kref = escape(document.referrer);} catch(e){};
  var d = document, b = document.body;
  var img = d.createElement('IMG');
  with(img.style){position = 'absolute'; width = '0px'; height = '0px';}
  img.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'b.kavanga.ru/exp?sid=1223&bt=3&bn=1&ct=8&prr=' + kref + '&rnd=' + Math.round(Math.random()*1000000);
  b.insertBefore(img, b.firstChild);
//-->
</script>
<noscript><img src="b.kavanga.ru/exp?sid=1223&bt=3&bn=1&ct=8" border=0 width=1 height=1></noscript>
<!-- Kavanga.AdEngine END -->
<script type='text/javascript' src='http://www.kp.ru/regions/msk/adwolf/adwolf.js'></script>

<div id="placeholderIdAdwolf40x200"></div>
<!-- tns-counter.ru -->
<script language="JavaScript">
  var img = new Image();
  img.src = 'http://www.tns-counter.ru/V13a***R>' + document.referrer.replace(/\*/g,'%2a') + '*kp_ru/ru/CP1251/tmsec=kp_miss-style/';
</script>
<noscript>
  <img src="http://www.tns-counter.ru/V13a****kp_ru/ru/CP1251/tmsec=kp_miss-style/" width="1" height="1" alt="" />
</noscript>
<!--/ tns-counter.ru -->

<!--LiveInternet counter--><script type="text/javascript"><!--
new Image().src = "//counter.yadro.ru/hit;kp/msk?r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";h"+escape(document.title.substring(0,80))+
";"+Math.random();//--></script><!--/LiveInternet-->
<div id="uslotitem1836"><script type="text/javascript">
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    /* First Call */
    ga('create', 'UA-23870775-1','auto');
    ga('require','displayfeatures');
    ga('send','pageview');
    /* Second Call */
    ga('create', 'UA-5200037-1', 'auto', {'name': 'newTracker'});
    ga('newTracker.require','displayfeatures');
    ga('newTracker.send', 'pageview');
</script>
</div>

<!-- Yandex.Metrika counter -->
<script type="text/javascript">
(function (d, w, c) {
    (w[c] = w[c] || []).push(function() {
        try {
            w.yaCounter1051362 = new Ya.Metrika({id:1051362, enableAll: true, trackHash:true, webvisor:true});
        } catch(e) {}
    });
    
    var n = d.getElementsByTagName("script")[0],
        s = d.createElement("script"),
        f = function () { n.parentNode.insertBefore(s, n); };
    s.type = "text/javascript";
    s.async = true;
    s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f);
    } else { f(); }
})(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="//mc.yandex.ru/watch/1051362" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->





<div class="all_page-bg">
<!-- ВЕРХНЯЯ ЧАСТЬ САЙТА (НАЧАЛО) -->

                        <div class="topline" id="сatfish" style="margin-bottom: 0px; "><!--  AdRiver code START. Type:extension Site: kp.ru SZ: second PZ: 1 BN: 4 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L+=escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="margin: 0 auto; width: 1030px; overflow: hidden;"><div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div></div>');_();ar_cn++;
})('http://ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=second&bn=4&target=top&bt=43&pz=1&tail256=');
</script>
<!--  AdRiver code END  --></div>






<div class="body_branding">


<script type="text/javascript">
KPjQuery(document).ready(function() {
  if ( KPjQuery('#сatfish').length == 1 ) {
    if ( KPjQuery('#сatfish #ad_ph_1').css('display') == 'block') { 
      KPjQuery("#fixedBox").css("margin-top","27px");
      }
  }

  KPjQuery(window).scroll(function() {
    if ( KPjQuery('#сatfish').length == 1 ) {
      if ( KPjQuery('#сatfish #ad_ph_1').css('display') == 'block') { 
        var x = KPjQuery(window).scrollTop();
        var y = 27;
        if ( x < y ) {
          KPjQuery("#fixedBox").css("margin-top",(y-x)+"px");
        } else {
          KPjQuery("#fixedBox").css("margin-top","0");
        }
      }
    }
  });
});
</script> 


<div class="all_user-panel" id="fixedBox" style="margin-top: 0px;">
  <div id='top-link' style="display:none">
    <a href="#top" onclick="ga('send', 'event', 'Upbutton', 'Scroll');">наверх</a>
  </div> 
  <div id="region-sel" class="all_region-sel">

    <a class="link active" id="toggle-link">Москва</a>
    <!--noindex-->
    <div class="region-menu" id="region-menu">
      <ul class="region-opt">
        <li class="pb"><a class="link" href="http://abakan.kp.ru" rel="nofollow">Абакан</a></li>
        <li><a class="link" href="http://alt.kp.ru" rel="nofollow">Барнаул</a></li>
        <li><a class="link" href="http://bel.kp.ru" rel="nofollow">Белгород</a></li>
        <li><a class="link" href="http://amur.kp.ru" rel="nofollow">Благовещенск</a></li>
        <li class="pb"><a class="link" href="http://bryansk.kp.ru" rel="nofollow">Брянск</a></li>
        <li><a class="link" href="http://dv.kp.ru" rel="nofollow">Владивосток</a></li>
        <li><a class="link" href="http://vladimir.kp.ru" rel="nofollow">Владимир</a></li>
        <li><a class="link" href="http://volgograd.kp.ru" rel="nofollow">Волгоград</a></li>
        <li><a class="link" href="http://vologda.kp.ru" rel="nofollow">Вологда</a></li>
        <li class="pb"><a class="link" href="http://vrn.kp.ru" rel="nofollow">Воронеж</a></li>
        <li class="pb"><a class="link" href="http://ural.kp.ru" rel="nofollow">Екатеринбург</a></li>
        <li><a class="link" href="http://izh.kp.ru" rel="nofollow">Ижевск</a></li>
        <li class="pb"><a class="link" href="http://irk.kp.ru" rel="nofollow">Иркутск</a></li>
        <li><a class="link" href="http://kazan.kp.ru" rel="nofollow">Казань</a></li>
        <li><a class="link" href="http://kaliningrad.kp.ru" rel="nofollow">Калининград</a></li>
        <li><a class="link" href="http://kem.kp.ru" rel="nofollow">Кемерово</a></li>
        <li><a class="link" href="http://kirov.kp.ru" rel="nofollow">Киров</a></li>
        <li><a class="link" href="http://kuban.kp.ru" rel="nofollow">Краснодар</a></li>
        <li><a class="link" href="http://krsk.kp.ru" rel="nofollow">Красноярск</a></li>
        <li><a class="link" href="http://crimea.kp.ru" rel="nofollow">Крым</a></li>
        <li><a class="link" href="http://kursk.kp.ru" rel="nofollow">Курск</a></li>
      </ul>
      <ul class="region-opt">
        <li class="pb"><a class="link" href="http://lipetsk.kp.ru" rel="nofollow">Липецк</a></li>
        <li><a class="curr">Москва</a></li>
        <li class="pb"><a class="link" href="http://murmansk.kp.ru" rel="nofollow">Мурманск</a></li>
        <li><a class="link" href="http://nnov.kp.ru" rel="nofollow">Нижний Новгород</a></li>
        <li class="pb"><a class="link" href="http://nsk.kp.ru" rel="nofollow">Новосибирск</a></li>
        <li><a class="link" href="http://omsk.kp.ru" rel="nofollow">Омск</a></li>
        <li><a class="link" href="http://orel.kp.ru" rel="nofollow">Орел</a></li>
      </ul>
      <ul class="region-opt">
        <li><a class="link" href="http://penza.kp.ru" rel="nofollow">Пенза</a></li>
        <li><a class="link" href="http://perm.kp.ru" rel="nofollow">Пермь</a></li>
        <li class="pb"><a class="link" href="http://pskov.kp.ru" rel="nofollow">Псков</a></li>
        <li><a class="link" href="http://rostov.kp.ru" rel="nofollow">Ростов-на-Дону</a></li>
        <li class="pb"><a class="link" href="http://ryazan.kp.ru" rel="nofollow">Рязань</a></li>
        <li><a class="link" href="http://samara.kp.ru" rel="nofollow">Самара</a></li>
        <li><a class="link" href="http://spb.kp.ru" rel="nofollow">Санкт-Петербург</a></li>
        <li><a class="link" href="http://saratov.kp.ru" rel="nofollow">Саратов</a></li>
        <li><a class="link" href="http://smol.kp.ru" rel="nofollow">Смоленск</a></li>
        <li><a class="link" href="http://stav.kp.ru" rel="nofollow">Ставрополь</a></li>
        <li class="pb"><a class="link" href="http://komi.kp.ru" rel="nofollow">Сыктывкар</a></li>
        <li><a class="link" href="http://tambov.kp.ru" rel="nofollow">Тамбов</a></li>
        <li><a class="link" href="http://tver.kp.ru" rel="nofollow">Тверь</a></li>
        <li><a class="link" href="http://tomsk.kp.ru" rel="nofollow">Томск</a></li>
        <li><a class="link" href="http://tula.kp.ru" rel="nofollow">Тула</a></li>
        <li><a class="link" href="http://tumen.kp.ru" rel="nofollow">Тюмень</a></li>
      </ul>
      <ul class="region-opt">
        <li><a class="link" href="http://ul.kp.ru" rel="nofollow">Ульяновск</a></li>
        <li class="pb"><a class="link" href="http://ufa.kp.ru" rel="nofollow">Уфа</a></li>
        <li class="pb"><a class="link" href="http://hab.kp.ru" rel="nofollow">Хабаровск</a></li>
        <li><a class="link" href="http://chel.kp.ru" rel="nofollow">Челябинск</a></li>
        <li class="pb"><a class="link" href="http://chita.kp.ru" rel="nofollow">Чита</a></li>
        <li class="hr2"><a class="link" href="http://yar.kp.ru" rel="nofollow">Ярославль</a></li>
        <li><a class="link" href="http://balkans.kp.ru" rel="nofollow">Балканы</a></li>
        <li><a class="link" href="http://kp.by" rel="nofollow">Беларусь</a></li>
        <li><a class="link" href="http://kp.kg" rel="nofollow">Бишкек</a></li>
        <li><a class="link" href="http://cyprus.kp.ru" rel="nofollow">Кипр</a></li>
        <li><a class="link" href="http://kp.md" rel="nofollow">Молдова</a></li>
        <li><a class="link" href="http://kompravda.eu" rel="nofollow">Северная Европа</a></li>
      </ul>
    </div>
    <!--/noindex-->
  </div>

<!-- Выбор региона, число и погода (начало) -->
  <!-- Число (начало) -->
  <div class="date">Сегодня <strong>14 Августа</strong></div>
<!-- Число (конец) -->

        <a href="/webcams/" class="webcam">Погода за окном</a>
<!-- Виджет погоды (начало) -->
  <!-- Погода (начало) -->
<p class='weather day cloud-small'>26&degC</p> 
<!-- Погода (конец) -->


<!-- Виджет погоды (конец) -->





<!-- Выбор региона, число и погода (конец) -->

<!-- #SOCNET_TOP_BEGIN# -->
<div class="user-div">
  <div id="login-conteiner" style='display:none;'>
    <div class="regi-button"><a href="http://my.kp.ru/register.do" class="button" onclick="MYKP_open_register_popup(); return false;"></a></div>
    <div class="login-button">
      <a href="http://my.kp.ru/login.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Feuromaidan%3Fgeo%3D72" class="button" onclick="MYKP_open_login_popup(); return false;"></a>
      <div id="loginDIV"></div>
    </div>
    <div class="clear"></div>
    <div></div>
  </div>
  <div id="user-panel" style="display:none;">
  <div class="drop-down">
    <span class="button" id="top-drop"></span>
    <div class="nastroiki-dropdown">
      <span class="top"></span>
      <ul>
        <li>
          <a href="http://www.my.kp.ru/community/all.do">Cообщества</a><span></span>
        </li>
        <li>
          <a href="http://www.my.kp.ru/profile/edit-form.do">Анкета</a><span></span>
        </li>
        <li class="polosa-bottom">
          <a href="http://www.my.kp.ru/profile/setupinfo.do">Настройки</a><span></span>
        </li>
                <!--li class="polosa-bottom fon">
                    <a href="http://www.kp.ru/swad/">Быстрый сайт</a><span></span>
                </li--> 
        <li class="polosa-top last">
          <a href="javascript:void(0);" onclick="LogOut(); return false;">Выйти</a><span></span>
        </li>
      </ul>
    </div>
  </div>


<div class="name" id="user_name"></div>
<div class="img" id="user_avatar"></div>

<!-- #JEWEL_PANEL_BEGIN# -->
<div class="pictogr">
    <a href="http://my.kp.ru/profile/friends.do?method=list" id="jewel_friend" class="friend-none"></a>
    <a href="http://my.kp.ru/message.do?id=<!-- #USER_ID-->" id="jewel_message" class="message-none"></a>
    <div class="new-none-div">
        <a href="http://my.kp.ru/community/list.do" id="jewel_new" class="new-none my-kp-informer"></a>
        <div class="all_user-panel-informer" id="informer">
            <div class="wrapInformer" id="informer-container">
            </div>
            <div class="allNotices"><a href="http://my.kp.ru/community/list.do">Все уведомления</a></div>
        </div>
    </div>


  <div class="raketa-drop-down no-use" id="user-raketa"  style='display:none;'   class="raketa-drop-down" >
    <ul id="raketa_menu">
          <li><a href="/swad/">Быстрый сайт</a></li>
          <li class="active" onclick="SwitchSWAD('on');" id="switch_swad_on">Подключено</li>
          <li class="none-active" onclick="SwitchSWAD('off');" id="switch_swad_off">Отключить</li>
        </ul>
  </div>  

  <div class="raketa-popup-ins" id="raketa-popup-ins" style="display:none;">
    <h6>Добро пожаловать!</h6>
    <p>Что бы сайт стал еще лучше мы скрыли рекламу. <br />Здесь вы можете включить или отключить рекламу.</p>
    <a href="#" onclick="$('raketa-popup-ins').fade({ duration: 1.5}); $('raketa_menu').appear({ duration: 1.5 }); return false;">Скрыть подсказку</a>
  </div>

</div>



<!-- #JEWEL_PANEL_END# -->
<div class="clear"></div>
</div>
</div>
<script async type="text/javascript" src="/_js/apollo.js?ts=1398156665"></script>
<script type="text/javascript">
    var informer_show = 0;

    
  KPjQuery('.my-kp-informer').on('click',function(obj){
        obj.stopPropagation();
        if(!informer_show) {
            var container = KPjQuery('#informer-container');

            if(container.length > 0) {
                KPjQuery('body').one('click', function(e){
                    KPjQuery('#informer').addClass('hideDropDown');
                    KPjQuery('#informer').removeClass('dropDown');
                    informer_show = 0;
                });    
            }
            

        KPjQuery.ajax(
            {
                url: '/_ajax/profile_informer?key='+ApolloApi.getUserInfo().sosh_o,
                type: 'GET',
                timeout: 15000,
                cache: false,
                dataType: 'json',
                beforeSend: function() {
                    container.html('<div class="ajax-loader" style="text-align: center; margin: 10px;"><img src="http://s3.stc.all.kpcdn.net/images/ajax-loader.gif" alt="Идет загрузка приложения..."></div>');
                },
                success: function(response) {

                    if(response.errorCode == 0) {
                        container.empty();
                        var i = 0;
                        var new_count = 0;
                        for(; i < response.result.length; i++) {

                            var elem = KPjQuery('<a>', {
                                class: response.result[i].readed ? 'noticeBlock' : 'noticeBlock notRead',
                                title: response.result[i].readed ? 'Прочитанное уведомление' : 'Непрочитанное уведомление',
                                href: response.result[i].url,
                                id: 'noticeBlock_'+response.result[i].id
                            });
                            elem.data({id_read: response.result[i].id});

                            if(!response.result[i].readed) {
                                new_count++;
                                // need send message - message is read!
                                elem.on('click',function(e){
                                    var target = KPjQuery(this);
                                    var data = 'key=' + ApolloApi.getUserInfo().sosh_o + '&ids=' + target.data('id_read');
                                    KPjQuery.ajax(
                                    {
                                        url: '/_ajax/profile_informer?ts=' + (new Date()).getTime(),
                                        type: 'POST',
                                        timeout: 5000,
                                        cache: false,
                                        dataType: 'json',
                                        'data': data,
                                        success: function() {
                                            window.location.href = target.attr('href');
                                        },
                                        error: function() {
                                            window.location.href = target.attr('href');
                                        }
                                    });
                                    return false;
                                });
                            }

                            elem.html('<img src="' + response.result[i].image + '"/><span class="p">' + response.result[i].text + '</span>');
                            container.append(elem);

                        }
                        // not be found notices
                        if( i==0 ) {
                            container.html('<p class="center">У вас нет уведомлений.</p>');
                        }
                        else if(new_count > 0){
                            KPjQuery('#jewel_new').addClass('new').removeClass('new-none').html('<span>' + new_count + '</span>');
                        }
                    }

                }
            });
            KPjQuery('#informer').addClass('dropDown');
            KPjQuery('#informer').removeClass('hideDropDown');
            informer_show = 1;
        }
        else {
            KPjQuery('#informer').addClass('hideDropDown');
            KPjQuery('#informer').removeClass('dropDown');
            informer_show = 0;
        }
    
    return false;
  });
</script>

<!-- #SOCNET_TOP_END# -->
</div>






<div class="topuslot">
<!-- #PARTNER_SLOT_0# -->
                        <script type="text/javascript" language="JavaScript">
                                                                                                                //name: KP.ru Prequal Tag MR
                                                                                                                //created: 02/20/2014 07:12
                                                                                                                var cb = new Date().getTime();
                                                                                                                var asiPqTag = false;
                                                                                                                try {
                                                                                                                                document.write("<sc" + "ript type='text/javascript' language='JavaScript' src='//pq-direct.revsci.net/pql?placementIdList=9xp9Ue,vNqc18,8xE1yP,LtkfNO,qoekJZ,LtkfNO&cb=" + cb + "'></sc" + "ript>");
                                                                                                                } catch(err) { }
                                                                                                                </script>


<script type="text/javascript" language="JavaScript">
        if (typeof asiPlacements != "undefined") { for(var p in asiPlacements) {
          window["ASPQ_"+p]=(asiPlacements[p].default)?"PQ_"+p+"=T":""; }
        }
      </script>
      <script type="text/javascript">
        var custom = function (s){
          var ar_s = 0;
          if (typeof s !== 'undefined' && s.length) {
            ar_s=(s.indexOf('T')+1)?1:0
          }
          return ar_s;
        }
      </script>
<!--  AdRiver code START. Type:AjaxJS Site: kp.ru SZ: reklama PZ: 1 BN: 7 -->
<div id="adriver_banner_333443659"></div>

<script type="text/javascript">
new adriver("adriver_banner_333443659", {sid:51864, bt:52, sz:'reklama', bn:7, pz:1});
</script>

<!--  AdRiver code END  -->
<!--  AdRiver code START. Type:extension Site: kp.ru SZ: second PZ: 1 BN: 3 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L='' + ('https:' == document.location.protocol ? 'https:' : 'http:') + ''+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div>');_();ar_cn++;
})('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=second&bn=3&target=top&bt=43&pz=1&tail256=');
</script>
<!--  AdRiver code END  -->





</div>

<div class="all_header ptichka">
     <!-- Большой баннер -->
                             <div id="uni_slot_1" class="uslot_banner restrict_height all_banner-top" style="display:block;clear:both;">
    <div id="uslotitem5933" class="lazyload_ad"><!--noindex-->
<style>
.mynew1{
text-align:center !important;
}
.mynew1 div{
margin:0px auto;
}
  </style> 
<div class="mynew1">
<script type="text/javascript">
 /* custom params */
         var ar_custom = [];
         ar_custom[1] = custom(window.ASPQ_9xp9Ue);
/* end of custom params */
 
 ar_custom.getStd = function(){for(var i=0,j,s=[];i<this.length;i++){if(this[i])s.push((!j?(j=1,i+'='):'')+escape(this[i]));else j=0}return s.length?'&custom='+s.join(';'):''};
 var bannerExtensionFirst = (function(L){
    if(typeof(ar_cn)=="undefined")ar_cn=1;
    var W=window,D=document,E=D.documentElement,T=0,N=ar_cn,P=0,C=D.compatMode=="CSS1Compat",
      X='<scr'+'ipt type="text/javascript">var ar_bnum='+N+';setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e)}},3000);',
      Y='<\/sc'+'ript><sc'+'ript type="text/javascript" src="'+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999)+ar_custom.getStd()+'"><\/sc'+'ript>';
    function G(){if(T++<100){var o=D.getElementById('ar_container_'+N);if(o){try{var d=o.contentDocument||(W.ActiveXObject&&W.frames['ar_container_'+N].document);if(d){d.write(X+Y)}else setTimeout(arguments.callee,100)}catch(e){try{o.src = "javascript:{document.write('"+X+'document.domain="'+D.domain+'";'+Y+"')}";return}catch(E){}}}else setTimeout(arguments.callee,100)}}
    D.write('<div style="visibility:hidden;height:0px;width:1px;position:absolute;"><iframe id="ar_container_'+ar_cn+'"><\/iframe><\/div><div id="ad_ph_'+ar_cn+'" style="display:none;"><\/div>');ar_cn++;return G;
  })('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=second&bn=1&target=top&bt=43&keyword='+encodeURIComponent(crtg_content)+'&pz=1&tail256=');
  
</script>


<div id="adriver_banner_106190822"></div>
 <script type="text/javascript">
         var bannerFirst = new adriver("adriver_banner_106190822", {sid:51864, bt:52, sz:'reklama', bn:1, pz:1});
         bannerFirst.onLoadComplete(function(){
                 if (this.reply.adid == 0){
                         bannerExtensionFirst();
                 }
         });
 </script>

</div>
<!--/noindex--></div>
</div>





     <!-- & /_inc/cache/test.html, delta => 5*60 & -->
  
  <div class="row1">
     <!-- Логотип (начало) -->
     <div class="logo"><a href="/"><strong>Новости</strong></a></div>

     <!-- Логотип (конец) -->
     
     <a href="mailto:kp@kp.ru" class="mailto">связь с редакцией</a>
     
     <!-- Глобальный поиск (начало) -->
       <div class="search">
    <div id="search-inset0">
            <div class="all_search-inp">
     <form action="/search/" id="cse-search-box">
        <input type="hidden" name="cx" value="partner-pub-7127235648224767:8g2twv-uz6i" />
        <input type="hidden" name="cof" value="FORID:11" />
        <input type="hidden" name="ie" value="utf-8" />
        <input type="text" class="inp_text" name="q" value="" class="inp_text"/>
        <input type="submit" id="bsearch" name="sa" class="inp_subm" value="" />
     </form>
    </div>
<script type="text/javascript" async src="http://www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=ru"></script> 
    </div>
  </div>
     <!-- Глобальный поиск (конец) -->
  </div>
</div>
<!-- ВЕРХНЯЯ ЧАСТЬ САЙТА (КОНЕЦ) -->

  <!-- Главное меню -->
<div class="all_nav">
  <ul class="mobile"><li><a href="http://www.kp.ru/daily/00000/529958/">RSS</a></li><li><a href="http://pda.kp.ru/">PDA</a></li><li><a href="http://www.kp.ru/mobile/pages/ipad">IPAD</a></li><li id="pop-up-mobile-hover"><span>MOBILE</span><ul><li><a href="http://www.kp.ru/mobile/pages/iphone">iPhone</a></li><li><a href="http://www.kp.ru/mobile/pages/android">Android</a></li></ul></li><li><a href="http://www.kp.ru/mobile/pages/ebooks/">ЭЛЕКТРОКНИГИ</a></li></ul>

    <!--a href="/comments/kp" class="a-all-comments">свежие комментарии</a-->
    <strong><a href="http://www.kp.ru/gazeta/" rel="canonical" class="new-num">Читай свежий номер</a><span class="new-num-date">14 Августа № 91.4</span></strong>

    <!-- Соц. сети -->
    <noindex><ul class="seti"><li class="mm"><a rel="nofollow" target="_blank" href="http://my.mail.ru/community/onlinekp.ru/"></a></li><li class="st"><a rel="nofollow" target="_blank" href="http://statigr.am/onlinekp"></a></li><li class="gp"><a rel="nofollow" target="_blank" href="https://plus.google.com/u/0/112261544981697332354/posts"></a></li><li class="fb"><a rel="nofollow" target="_blank" href="http://www.facebook.com/pages/Komsomolskaa-pravda/369256943469?ref=mf"></a></li><li class="od"><a rel="nofollow" target="_blank" href="http://www.odnoklassniki.ru/kpru"></a></li><li class="tw"><a rel="nofollow" target="_blank" href="http://www.twitter.com/onlinekpru/"></a></li><li class="vk"><a rel="nofollow" target="_blank" href="http://vkontakte.ru/club15722194"></a></li></ul></noindex>

    <!-- Верхнее меню ИД КП -->
  <ul class="top">
    <li class="photo"><a href="/photo/">Фото</a></li>
    <li class="video"><a href="/video/">Видео</a></li>
    <li><a href="/handbook">КП-Справочник</a></li>
    <li><a href="http://www.kp.ru/about/">Все о КП</a></li>
    <li><a href="/daily/friday/">Еженедельник</a></li>
    <!--noindex--><li><a href="http://tv.kp.ru/" rel="nofollow">Телеканал КП</a></li><!--/noindex-->
    <li><a href="/radio/">Радио КП</a></li>
    <li><a href="http://kp.ru/go/http://advert.kp.ru/kr/">Реклама</a></li>
    <li><a href="/daily/collections/">Коллекции КП</a></li>
    <li><a href="/action">Акции КП</a></li>
    <li><a href="/daily/press/">Пресс-центр</a></li>
  </ul>
    <!-- Спецразделы -->
  <ul class="spec-rubric">
    <li class="red"><a href="/daily/sanctions/" >Торговая война с Россией</a></li>
    <li class=""><a href="/daily/26225.5/3108302/" >Спецкор</a></li>
    <li class="blue"><a href="/daily/tourism-krim/" >#КрымНаш</a></li>
    <li class="light-blue"><a href="/daily/euromaidan" >Украина</a></li>
    <li class="red"><a href="http://www.kp.ru/daily/bam2014/?view=desktop" >БАМ</a></li>
    <li class="green"><a href="/daily/mydacha" >Дача</a></li>
    <li class="red"><a href="/daily/potrebit/" >Клуб потребителей</a></li>
    <li class="yellow"><a href="/daily/afisha/" >Афиша</a></li>
    <li class="light-blue"><a href="/daily/shkola/" >Снова в школу</a></li>
    <li class="black"><a href="/daily/allcolumn/" >Колумнисты</a></li>
    <li class="red"><a href="/daily/infographics/rabota_ru" >Работа</a></li>
    <li class="green"><a href="/region/1" >Москва</a></li>
  </ul>
<!-- Нижнее главное меню -->
  <ul class="rubric">



                <li><a title="Новости 24" onclick="ga('send', 'event', 'Header', 'Online');" href="/online/">Новости</a></li>

                <li><a title="Спорт" onclick="ga('send', 'event', 'Header', 'Sport');" href="/sport">Спорт</a></li>

                <li><a title="Политика" onclick="ga('send', 'event', 'Header', 'Politics');" href="/politics">Политика</a></li>

                <li><a title="Экономика" onclick="ga('send', 'event', 'Header', 'Economics');" href="/economics">Экономика</a></li>

                <li><a title="Общество" onclick="ga('send', 'event', 'Header', 'Society');" href="/society">Общество</a></li>

                <li><a title="Происшествия" onclick="ga('send', 'event', 'Header', 'Incidents');" href="/incidents">Происшествия</a></li>

                <li><a title="Звезды" onclick="ga('send', 'event', 'Header', 'Stars');" href="/stars">Звезды</a></li>

                <li><a title="Наука" onclick="ga('send', 'event', 'Header', 'Science');" href="/daily/science/">Наука</a></li>

                <li><a title="Авто" onclick="ga('send', 'event', 'Header', 'Auto');" href="/auto">Авто</a></li>

                <li><a title="Дом. Семья" onclick="ga('send', 'event', 'Header', 'Special');" href="/special">Дом. Семья</a></li>

                <li><a title="Здоровье" onclick="ga('send', 'event', 'Header', 'Health');" href="/daily/health">Здоровье</a></li>
  </ul>
</div>
<!-- % $ENV{REQUEST_URI} % -->





<!-- Div центровки страницы (начало) -->
<div class="all_page">

<!-- СТРАНИЦА НОВОСТЕЙ (НАЧАЛО) -->
<div class="pc_content">

  <div class="pc_title-section">
      <h1><a href="/contest/?view=desktop" style="color:#40454C;">Фотоконкурсы</a></h1>
    </div>
                            


    <!-- ЛЕВАЯ КОЛОНКА 680 (начало) -->
    <div class="pc_leftcol">


  <!-- Информация вверху (начало) -->
        <div class="pc_date"><a href="http://www.kp.ru/contest/?view=desktop">Фотоконкурсы</a> | <a href="/contest/miss-stile-2010/?view=desktop"><strong>Мисс купальник "КП"</strong></a> 30.08.2012</div>
        
        
<!-- Навигация (начало) -->
<div class="pc_navigation">
<ul>
    <li class="next"><a href="/daily/forumcontest/photo/113536/?view=desktop">Следующая</a> &raquo;</li>

  <li class="prev">&laquo; <a href="/daily/forumcontest/photo/113596/?view=desktop">Предыдущая</a></li>
</ul>
<div class="clear"></div>
</div>
<!-- Навигация (конец) -->

        
        <div class="pc_name">Мария Бурлакова
    </div>
        <div class="pc_city">Магнитогорск</div>
        <!-- Информация вверху (конец) -->

        <!-- Персональное большое фото (начало) -->
        <div class="pc_big_photo"><img src="http://s4.stc.all.kpcdn.net/f/3/image/87/66/1736687.jpg" alt="Мария Бурлакова" /></div>
        <!-- Персональное большое фото (конец) -->

      <!-- О себе (начало) -->
        <div class="pc_about">
            <div class="tit">О себе:</div>

            <div class="txt">
                23 года

Очень любит танцы, открывает свою студию модной одежды.

Комментирует имидж-консультант Елена ГОНЧАРОВА:

- Желтый цвет и платье макси - это, конечно, модные хиты прошедшего лета. Но вот все это вместе с татуировкой и особенно с этими красными туфлями выглядит странно. Можно, конечно, представить, что это что-то, навеянное фильмами Тарантино, -  «Убить Билла» или «Криминальное чтиво»... Ведь по общему типажу Мария даже чем-то похожа на Уму Турман... Но все же для жизни образ этот слишком странный и эпатажный. Не могу себе представить, где бы, кроме сценария гротескной комедии, этот образ выглядел бы уместно. Удачи в конкурсе!

Фото Евгения ЧУФАРОВА.
            </div>
        </div>
        <!-- О себе (конец) -->

        <!-- Проголосовать (начало) -->
        <div class="pc_vote">
    
    <div class="pc_msg" id="vote_msg"></div>

    <form method="post" name="vote_form" id="vote_form">
        <table>
        <tr>

            <td>
                <div class="pc_vote-rcol">
                    <div class="button" onClick="voteContest('vote_msg', '113571');" title="Проголосовать"></div>
                    </form>
                    <div class="txt">всего голосов: <span id="vote_total">253</span></div>
                </div>
            </td>
        </tr>
        </table>

            
        <div class="clear"></div>

    <div class="like-text"><span></span>Поделитесь своей фотографией с друзьями, пусть голосуют!  
    </div>



    <div class="a_diffusion">
  <div class="center">
    <div class="left">
      <noindex>
      <br>
        <div class="yashare-auto-init" data-yashareLink="" data-yashareTitle="" data-yashareDescription="" data-yashareQuickServices="facebook,twitter,odnoklassniki,gplus,vkontakte,moimir" data-yashareTheme="counter" data-yashareType="big" style="display: inline-block;"></div>
        <div class="my-kp" style="display: inline-block;">
<a href="http://my.kp.ru/login.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop" class="my_kp_bkm" id="http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop" title="%D0%9C%D0%B8%D1%81%D1%81%20%D0%BA%D1%83%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%20%22%D0%9A%D0%9F%22"><img src="http://s5.stc.all.kpcdn.net/images/my_kp/kp-icon.png" border="0" alt="Добавить в избранное" title="Добавить в избранное"></a>
<script>InitMyKpBookmark();</script>


        </div>
            </noindex>
    </div>

    <div class="clear"></div>
  </div>


</div>
        <div class="clear"></div>

  </div>
  <div id="vote_preloader" class="preloader" style="display:none;"><img src="http://s1.stc.all.kpcdn.net/images/preloaders/190x10_horizontal.gif" alt="Загружается..." /></div>
        <!-- Проголосовать (конец) -->

<!-- КОММЕНТАРИИ (НАЧАЛО) -->
  

    <script>
        function hide_complaint_form() {
            KPjQuery('#popup-background, #popup-complaint-form').fadeOut(600);
            return false;
        }

        function complaint_comment(comment_id) {
            var userData;
            if(typeof(ApolloApi) !== 'undefined' && ApolloApi.getUserInfo()) {
                userData = ApolloApi.getUserInfo();
                KPjQuery('#complaint-key').attr('value', userData.sosh_o);
                KPjQuery('#complaint-comment-id').attr('value',comment_id);
                KPjQuery('#complaint-user-id').attr('value', userData.id);
                KPjQuery('#complaint-user-type').attr('value', userData.user_type);

                switch(userData.user_type) {
                    case 'journalist':
                    case 'star':
                    case 'expert':

                        KPjQuery.ajax(
                            {
                                url: '/_ajax/complaint_comment/'+comment_id,
                                type: 'post',
                                data: 'cause_id=0&key='+userData.sosh_o+'&user_id='+userData.id+'&user_type='+userData.user_type, 
                                cache: false,
                                dataType: 'json',
                                beforeSend: function() {
                                    KPjQuery('#comment-'+comment_id).animate({opacity: 0.2},1000);
                                },
                                error: function() {
                                    KPjQuery('#comment-'+comment_id).css({opacity: 1});
                                },
                                success: function(response) {

                                    if(response.errorCode == 0 && response.showComment == 0) {
                                        //hide comment
                                        KPjQuery('#comment-'+comment_id).fadeOut(400);
                                    }
                                }
                            }
                        );
                        break;

                    case 'user':
                    case 'web_journalist':

                    default:
                        KPjQuery('#popup-complaint-form').attr('action', '/_ajax/complaint_comment/'+comment_id);

                        KPjQuery('#popup-background, #popup-complaint-form').fadeIn(600);
                        
                        break;
                    
                }
                return false;
            }
            return true;
        }

        function submit_complaint() {
            
            var comment_id = KPjQuery('#complaint-comment-id').attr('value');
            KPjQuery.ajax(
                {
                    url: KPjQuery('#popup-complaint-form').attr('action'),
                    data: KPjQuery('#popup-complaint-form').serialize(),
                    type: 'POST',
                    timeout: 15000,
                    cache: false,
                    dataType: 'json',
                    success: function(response) {

                        if(response.errorCode == 0 && response.showComment == 0) {
                            //hide comment
                            KPjQuery('#comment-'+comment_id).fadeOut(400);
                        }
                    }
                }
            );
            
            KPjQuery('#popup-background, #popup-complaint-form').fadeOut(400);
        }
    </script>

    <form class="all_alert-popup" id="popup-complaint-form" style="display: none;" onsubmit="submit_complaint(); return false;">
        <input type="hidden" name="key" value="" id="complaint-key"/>
        <input type="hidden" name="comment_id" value="" id="complaint-comment-id"/>
        <input type="hidden" name="user_id" value="" id="complaint-user-id"/>
        <input type="hidden" name="user_type" value="" id="complaint-user-type"/>
        <div class="popup-title">Пожаловаться на комментарий</div>
        <p class="p-popup-text">Выберите причину для жалобы</p>
        <input type="radio" name="cause_id" id="cause1" class="inp-rad" value="0" /><label for="cause1" class="label-rad">Пропаганда войны, призыв к разжиганию национальной, расовой или религиозной ненависти и вражды</label>
        <input type="radio" name="cause_id" id="cause2" class="inp-rad" value="1" /><label for="cause2" class="label-rad">Нарушение авторских прав</label>
        <input type="radio" name="cause_id" id="cause3" class="inp-rad" value="2" /><label for="cause3" class="label-rad">Материалы порнографического характера</label>
        <input type="radio" name="cause_id" id="cause4" class="inp-rad" value="3" /><label for="cause4" class="label-rad">Оскорбление других пользователей</label>
        <input type="radio" name="cause_id" id="cause5" class="inp-rad" value="4" /><label for="cause5" class="label-rad">Другая причина</label>
        <div class="ta"><textarea name="cause_text"></textarea></div> 
        <p class="p-popup-text">Читать <a href="/regions/msk/socnet/eula.html">Пользовательское соглашение</a> и <a href="/regions/msk/socnet/pd.html">Политику по защите персональных данных</a></p>
        <p class="p-popup-text">Если после публикации вы перестанете видеть данный комментарий, то это значит что ваша жалоба не одинока: мы скрываем проблемный материал.</a></p>
        <div class="kp_popup_buttons">
            <button class="popup-button-left" onclick="return hide_complaint_form()"><span>Отмена</span></button>
            <button class="popup-button-right" type="submit"><span>Отправить</span></button>
        </div>
    </form>
    <div class="flr-popup-background" id="popup-background" style="display: none;" onclick="hide_complaint_form()"></div>


  <!--noindex-->
  <div class="all_comments">
    <div class="txt-num">
      <a name="comment"></a>
      Комментировать
      <span id="cm-count-bottom" class="count-comments bottom">
        <span>43</span>
      </span>
    </div>
    <button id="btn-0" style="display:none;" class="all_button-comments" onclick="toggleFormCmt(0, 72, 113571, 0); return false;">
      <span>Комментировать</span>
    </button>
    <div id="form_0">
      <div id="cm-result"></div>
      


<script>

var CommentsObj = {
  auth_form_flag: false,
    current: 0,
    classId: 72,
    objectId: 113571,
    regionId: 0
};

function toggleFormCmt( CommentID, cId, oId, rId, parentId ) {
    currWrpFrm = KPjQuery( '#form_' + CommentsObj.current );
    nextWrpFrm = KPjQuery( '#form_' + CommentID );
        
    KPjQuery('#cm-result').html('');
    if (!currWrpFrm || !nextWrpFrm) { return; }
        
    currBtn = KPjQuery( '#btn-' + CommentsObj.current );
    nextBtn = KPjQuery( '#btn-' + CommentID );

    if ( nextBtn ) { nextBtn.hide(); }
    if ( currBtn ) { currBtn.show(); }

    currWrpFrm.hide();
    nextWrpFrm.html(currWrpFrm.html());
    currWrpFrm.html('');

    var comment_to = KPjQuery('#cm-to');
    comment_to.attr('value', CommentID);
    
    if (CommentID == 1) { comment_to.attr('value', 0); }

    if (( CommentID == 0 ) || ( CommentID == 1 )) {
        KPjQuery( '#cm-submit' ).html('Комментировать');
    } else {
        KPjQuery( '#cm-submit' ).html('Ответить');
    }
    nextWrpFrm.show();
    
    CommentsObj.classId = cId;
    CommentsObj.objectId = oId;
    CommentsObj.regionId = rId;
    

    KPjQuery('#cm-region').attr('value', CommentsObj.regionId);
    KPjQuery('#cm-form').attr('action',"/_ajax/add_comment/" + CommentsObj.classId + "/" + CommentsObj.objectId + "/" + (parentId ? parentId : CommentID)).show();

    CommentsObj.current = CommentID;
}



</script>
<form class="all_add-comment cm_anonymous" id="cm-form" action="/_ajax/add_comment/72/113571/0" method="POST" onsubmit="add_comment(); return false;">
    <input type="hidden" id="cm-region" name="object_region" value="0" />
    <input type="hidden" id="cm-key" name="key" value="" />
    <input type="hidden" id="cm-to" name="to" value="0" />
    <input type="hidden" id="cm-user-id" name="user_id" value="" />
    <input type="hidden" id="cm-guest-auto-name" name="guest_auto_name" value="" />
    <input type="hidden" id="cm-guest-mode" name="anonymous" value="1" />
    <input type="hidden" id="cm-show-url" name="answer_url" value="" />
    <input type="hidden" name="redirect" value="http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop" />
    <div class="titl">
        Оставить комментарий
        <div class="a"><span class="text-decoration">О модерации</span>
            <div class="all_popup-moderatione">
                <h5>Уважаемые читатели!</h5>
                <p>Ваши сообщения будут опубликованы только после проверки их модератором. Модерация осуществляется круглосуточно без выходных.</p>
                <p><strong>Комментарии могут быть опубликованы, если они не содержат:</strong>
                <br />&mdash; Призывов к насилию, межнациональной розни и прочим нарушениям закона
                <br />&mdash; Оскорбление или уничижение России, ее символов и первых лиц.
                <br />&mdash; Ненормативной лексики
                <br />&mdash; Личных оскорблений или проявлений неуважения в адрес авторов материала, других посетителей форума, иных лиц, а также «Комсомольской правды»
                <br />&mdash; Ссылок на какие-либо страницы в интернете
                <br />&mdash; Рекламы товаров или услуг, адресов или телефонов и т.п.</p>
                <p>Администрация сайта оставляет за собой право удалять любые сообщения с форума без объяснения причин. Администрация сайта не несет ответственности за содержание сообщений. Мнение автора сообщения может не совпадать с мнением редакции.</p>
                <div class="corner"></div>
            </div>
        </div>
    </div>
    <ul class="guest-right">
        <li class="txt">Как пользователь социальной сети</li>
        <li class="kp"><a href="http://my.kp.ru/login.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop" onclick="MYKP_open_login_popup(); return false;"></a></li>
        <li class="fb"><a href="http://my.kp.ru/login/facebook.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
        <li class="tw"><a href="http://my.kp.ru/login/twitter.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
        <li class="mm"><a href="http://my.kp.ru/login/mailru.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
        <li class="vk"><a href="http://my.kp.ru/login/vkontakte.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
        <li class="od"><a href="http://my.kp.ru/login/odkl.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
    </ul>
    <div class="user-right" style="display: none;">
        <span class="other-name">Оставить комментарий под другим именем</span>
        <ul>
            <li class="anonym" id="authorized_anon_post" style="display: none"><a href="#" onclick="return changeTypeForm('anonymous')"></a></li>
            <li class="kp"><a href="http://my.kp.ru/login.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop"></a></li>
            <li class="fb"><a href="http://my.kp.ru/login/facebook.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
            <li class="tw"><a href="http://my.kp.ru/login/twitter.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
            <li class="mm"><a href="http://my.kp.ru/login/mailru.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
            <li class="vk"><a href="http://my.kp.ru/login/vkontakte.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
            <li class="od"><a href="http://my.kp.ru/login/odkl.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop&fmt=xml&fromSite=my.kp.ru"></a></li>
        </ul>
        <div class="all_popup-moderatione"><p>Как пользователь любимой соцсети</p><div class="corner"></div></div>
    </div>
    <div class="guest-left" style="display: none;">
        <input id="cm-guest-name" type="text" name="guest_name" value="Ваше имя" onfocus="if(this.value=='Ваше имя'){this.value=''}" onblur="if(this.value==''){this.value='Ваше имя'}" />
        <span class="name" id="cm-guest-display-auto-name">Гость</span>
    </div>
    <div class="user-left" style="display: none;">
        <a href="#" id="cm-user-profile">
            <img src="http://s2.stc.all.kpcdn.net/regions/msk/_img/all_add-comment-img.jpg" alt="" id="cm-user-image" />
            <span class="name" id="cm-user-name"></span>
            <!-- <span class="status" id="cm-user-type">первопроходец</span> -->
        </a>
        <div class="all_popup-moderatione"><p>Ваша персональная страничка на KP.RU</p><div class="corner"></div></div>
    </div>
  <div id="only_auth">Теперь для комментирования материалов на сайте KP.RU необходимо авторизоваться. Для этого просто нажмите на значок любой социальной сети (Одноклассники, ВКонтакте и т.д), где у вас есть страница. </div>
    <textarea name="text" id="cm-text"  style="display: none;" onblur="if(this.value==''){this.value='Ваше сообщение';}" onfocus="if(this.value=='Ваше сообщение'){this.value='';};" onkeyup="max_count(); return false;" onchange="max_count();">Ваше сообщение</textarea>
    <button type="submit" id="submit_comment"  style="display: none;"><span id="cm-submit">Комментировать</span></button>
    <input type="hidden" name="kp_coords" id="kp_coords" value=""/>
    <input type="hidden" name="kp_city" id="kp_city" value=""/>
    <input type="hidden" name="kp_city2" id="kp_city2" value=""/>
    <!-- <div type="text" name="kp_city2" id="kp_city2" value=""/></div> -->
    <!-- <a href="#" class="how">Как получить свою персональную страничку на KP.RU?</a> -->
    <div class="ost"  style="display: none;">Осталось символов - <strong id="cm-words-count-1">2000</strong></div>
</form>
<div id="cm-preloader" class="preloader" style="display:none;"><img alt="Отправляем..." src="http://s3.stc.all.kpcdn.net/images/preloaders/190x10_horizontal.gif"></div>

<script>
    function add_comment() {

      push_geo();

        var form = KPjQuery('#cm-form');

        var name = KPjQuery('#cm-guest-name');
        if(name.attr('value') == 'Ваше имя')
            name.attr('value', '');
        var text = KPjQuery('#cm-text');
        if(text.attr('value') == 'Ваше сообщение')
            text.attr('value','');

        KPjQuery.ajax({
                url: form.attr('action'),
                type: 'post',
                data: form.serialize(),
                cache: false,
                dataType: 'html',
                beforeSend: function() {
                    KPjQuery('#cm-submit').attr('disabled', true);
                    KPjQuery('#cm-form').hide();
                    KPjQuery('#cm-preloader').show();
                },
                error: function() {
                    KPjQuery('#cm-submit').attr('disabled', false);
                    KPjQuery('#cm-preloader').hide();
                    KPjQuery('#cm-result').text('Ошибка соединения');
                },
                success: function(response) {
                    KPjQuery('#cm-text').attr('value', 'Ваше сообщение');
                    max_count();
                    KPjQuery('#cm-submit').attr('disabled', false);
                    KPjQuery('#cm-preloader').hide();
                    KPjQuery('#cm-result').html(response);
                }
            }
        );

        return false;
    }

    KPjQuery(document).ready(function() {
        // подцепляем нормальные ссылки для кнопок залогинивания
        KPjQuery('.my-kp-login').each(function(index, elem){
            elem.href = 'http://my.kp.ru/login.do?returnUrl=http%3A%2F%2Fwww.kp.ru%2Fdaily%2Fforumcontest%2Fphoto%2F113571%2F%3Fgeo%3D1%26view%3Ddesktop';
        });
    });

  function push_geo() {
      if(navigator.geolocation) {
        var obj=document.getElementById("kp_coords");
        obj.value = [ymaps.geolocation.longitude, ymaps.geolocation.latitude];
        var city=document.getElementById("kp_city");
        city.value = ymaps.geolocation.city;
        var coords = [ymaps.geolocation.latitude, ymaps.geolocation.longitude];
        ymaps.geocode(coords).then(function (res) {
          var names = [];
          res.geoObjects.each(function (obj) {
            names.push(obj.properties.get('name'));
          });
          var city2=document.getElementById("kp_city2");
          city2.value = [names[0], names[1], names[2], names[3], names[4], names[5], names[6]].reverse().join(' ');
        });
      } else {
        console.log("Geolocation API не поддерживается");
      }
  }

    function changeTypeForm(type) {
        container = document.getElementById('cm-form');
        // нечего делать на не существующей форме
        if(!container)
            return;

        var guest_auto_name = readCookie('guest_user_name');
        if (!guest_auto_name) {
            // для анонимного пользователя присвоим имя по умолчанию
            var host = window.location.host.replace(/.*\.([-a-z0-9]*)\.(\w*)$/,".$1.$2");
            if(!/^\./.test(host)) {
                host = "." + host;
            }
            guest_auto_name = 'Гость №' + Math.floor(Math.random()*10000);
            createCookie('guest_user_name', guest_auto_name, 4*30, host);
        }

        switch(type) {
            case 'anonymous':
                container.className = 'all_add-comment cm_anonymous';
                document.getElementById('cm-guest-auto-name').value = guest_auto_name;
                document.getElementById('cm-guest-display-auto-name').innerHTML = guest_auto_name;
                document.getElementById('cm-user-id').value='';
                document.getElementById('cm-user-name').innerHTML='';
                // document.getElementById('cm-user-type').innerHTML='';
                document.getElementById('cm-user-image').src='/regions/msk/_img/all_add-comment-img.jpg';
                document.getElementById('cm-user-profile').href='#';
                document.getElementById('cm-key').value='';
                document.getElementById('cm-guest-mode').value = 1;

              break;

          case 'no_anon_comments':
            container.className = 'all_add-comment cm_anonymous no_anon_comments';

            document.getElementById('cm-user-id').value='';
            document.getElementById('cm-user-name').innerHTML='';

            document.getElementById('cm-user-profile').href='#';
            document.getElementById('cm-key').value='';
            document.getElementById('cm-guest-mode').value = 1;

            document.getElementById("cm-text").parentNode.removeChild(document.getElementById("cm-text"));
            document.getElementsByClassName("ost")[0].parentNode.removeChild(document.getElementsByClassName("ost")[0]);
            document.getElementById("submit_comment").parentNode.removeChild(document.getElementById("submit_comment"));


            break;

          case 'authorized':
            var info = ApolloApi.getUserInfo();
                container.className='all_add-comment cm_authenticated';
//                document.getElementById('cm-user-id').value=info.id;
                document.getElementById('cm-user-name').innerHTML=info.name;
            KPjQuery('div.all_comments #cm-user-id').val(info.id);
                
                // switch(info.user_type) {
                //     case 'user': 
                //         document.getElementById('cm-user-type').innerHTML='id';
                //         break;
                //     case 'journalist':
                //         document.getElementById('cm-user-type').innerHTML='журналист';
                //         break;
                // }
                document.getElementById('cm-user-image').src=info.userpic.b28;
                document.getElementById('cm-user-profile').href=info.userUrl;
                document.getElementById('cm-key').value=info.sosh_o;
                document.getElementById('cm-guest-mode').value = 0;

            if (CommentsObj.auth_form_flag == true) {
              document.getElementById('cm-form').className='all_add-comment cm_authenticated comments_off';
            } else {
              document.getElementById('cm-form').className='all_add-comment cm_authenticated comments_on';
            }

                break;  
        }
        return false;
    }

    function max_count() {
        var text    = document.getElementById('cm-text');
        var max1    = document.getElementById('cm-words-count-1');
        var max;
        var limit   = 2000;
        
        max = text.value.length;
        if (max < limit) {
            max1.style.color = 'green';
            max1.innerHTML = (limit - max);
        } else {
            max1.style.color = 'red';
            max1.innerHTML = (limit - max);
            
        }
    }

//    if (typeof(ApolloApi) !== 'undefined') {
//
//        if(!ApolloApi.getUserInfo()) {
//
//          // если не залогинен
//          if (CommentsObj.auth_form_flag === true) {
//            alert('comments_allowed');
//            changeTypeForm('comments_allowed');
//          } else {
//            alert('anonymous');
//            changeTypeForm('anonymous');
//          }
//
//        } else {
//
//          alert('authorized');
//          changeTypeForm('authorized');
//
//        }
//    }

        
</script>


    </div>
    

<div class="all_pagination">
    <ul id="comments_paginator">

    
<li class="select"><a href="/daily/forumcontest/photo/113571/?view=desktop#comment">2</a></li>

    
<li><a href="/daily/forumcontest/photo/113571/?view=desktop&cp=0#comment">1</a></li>

    
<li class="next"><a href="/daily/forumcontest/photo/113571/?view=desktop&cp=0#comment">вперёд</a></li>

  </ul>
</div>
    







    <div>
      <div id="comments_messages_container_preloader" class="preloader" style=" display:none;">
        <img src="http://s4.stc.all.kpcdn.net/images/preloaders/64x64_round.gif" alt="Загружается..." />
      </div>
      <div id="comments_messages_container"></div>
      <script type="text/javascript"><!--
        KPjQuery('#comments_messages_container').html('<ul><li id="comment-14291258" class="anonymous" style=""><div class="status-div"><div class="top"><div class="description"></div><span class="name">Mari</span></div><div class="txt"><span class="date">04.06.2014, 23:08</span><p style="">Девушка очень яркая, красивая со своим стилем!!!!!фотограф сделал акцент сильный в цветах!!!!но в целом очень сексуально и стильно!!!!!</p></div></div><div class="all_comments-element-vote"><button id="btn-14291258" class="reply" href="#" onclick="toggleFormCmt(14291258, 72, 113571, 0); return false;">Ответить</button><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'14291258\');" title="Пожаловаться"></a></div><div id="form_14291258"></div><ul></ul></li><li id="comment-10269120" class="anonymous" style=""><div class="status-div"><div class="top"><div class="description"></div><span class="name">Гость №9416</span></div><div class="txt"><span class="date">14.04.2013, 12:49</span><p style="">Кто автор этого фото &laquo;шедевра&raquo;? Полная безвкусица&hellip; Изуродовали девушку кошмарным балахоном и &laquo;утюгами&raquo; на ногах&hellip; Фотографа фтопку.</p></div></div><div class="all_comments-element-vote"><button id="btn-10269120" class="reply" href="#" onclick="toggleFormCmt(10269120, 72, 113571, 0); return false;">Ответить</button><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'10269120\');" title="Пожаловаться"></a></div><div id="form_10269120"></div><ul></ul></li><li id="comment-9443499" class="anonymous" style=""><div class="status-div"><div class="top"><div class="description"></div><span class="name">Ценитель</span></div><div class="txt"><span class="date">25.01.2013, 7:16</span><p style="">Вижу красавицу. Но слишком много фотошопа.. Жаль.</p></div></div><div class="all_comments-element-vote"><button id="btn-9443499" class="reply" href="#" onclick="toggleFormCmt(9443499, 72, 113571, 0); return false;">Ответить</button><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'9443499\');" title="Пожаловаться"></a></div><div id="form_9443499"></div><ul><li id="comment-9449665" class="anonymous" style=""><div class="status-div"><div class="top"><div class="description"></div><span class="name">Ценителю от&nbsp;ценительницы</span></div><div class="txt"><span class="date">25.01.2013, 17:42</span><p style="">Очень красивая девушка! Красивое платье! Не нравятся слишком тяжелые и&nbsp;массивные туфли и&nbsp;ужасная татуировка! Что касается фотошопа&hellip; Не знаю&hellip; Об этом фотографе я говорю хорошо или&nbsp;ничего! Я очень уважаю Евгения!</p></div></div><div class="all_comments-element-vote"><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'9449665\');" title="Пожаловаться"></a></div><div id="form_9449665"></div></li></ul></li><li id="comment-8780440" class="anonymous" style=""><div class="status-div"><div class="top"><div class="description"></div><span class="name">Гость №8685</span></div><div class="txt"><span class="date">08.11.2012, 18:05</span><p style="">Красавица!!! Какая там Ума Турман&hellip; Мария в&nbsp;1000 раз лучше!!! Фотографу респект!</p></div></div><div class="all_comments-element-vote"><button id="btn-8780440" class="reply" href="#" onclick="toggleFormCmt(8780440, 72, 113571, 0); return false;">Ответить</button><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'8780440\');" title="Пожаловаться"></a></div><div id="form_8780440"></div><ul></ul></li><li id="comment-8583828" class="user" style=""><div class="status-div"><a href="http://my.kp.ru/main.do?id=p1344499" class="avatar"><img src="http://my.kp.ru/image/gA/AA/AA/AU/plgo/ZG/Q5/Zd/ng/oN/I$.jpg_s50.jpg"></a><div class="top"><div class="description"></div><a href="http://my.kp.ru/main.do?id=p1344499" class="name">Ромон Николаевич ВЫШИБАЛА</a></div><div class="txt"><span class="date">15.10.2012, 18:24</span><p style="">класс без&nbsp;слов&hellip;</p></div></div><div class="all_comments-element-vote"><button id="btn-8583828" class="reply" href="#" onclick="toggleFormCmt(8583828, 72, 113571, 0); return false;">Ответить</button><a href="http://my.kp.ru/login.do" class="all_wall-element-dismiss my-kp-login" onclick="return complaint_comment(\'8583828\');" title="Пожаловаться"></a></div><div id="form_8583828"></div><ul></ul></li></ul>');
      //--></script>
    </div>
    

<div class="all_pagination">
    <ul id="comments_paginator2">

    
<li class="select"><a href="/daily/forumcontest/photo/113571/?view=desktop#comment">2</a></li>

    
<li><a href="/daily/forumcontest/photo/113571/?view=desktop&cp=0#comment">1</a></li>

    
<li class="next"><a href="/daily/forumcontest/photo/113571/?view=desktop&cp=0#comment">вперёд</a></li>

  </ul>
</div>
    








    </div>
    <!--/noindex-->
<!-- КОММЕНТАРИИ (КОНЕЦ) -->

    <button id="btn-1" class="all_button-comments" onclick="toggleFormCmt(1, 72, 113571, 0); return false;">
      <span>Комментировать</span>
    </button>
        <div id="form_1"></div>















<div class="clear"></div>
<div style="padding-top: 10px;">
                            


</div>

  </div>
    <!-- ЛЕВАЯ КОЛОНКА 680 (конец) -->


  <!-- ПРАВАЯ КОЛОНКА 300 (начало) -->
<div class="all_rightcol">
                            <div id="uni_slot_2" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem5995" class="lazyload_ad"><!--noindex-->
<div align=center>
<script type="text/javascript">
 /* custom params */
         var ar_custom = [];
         ar_custom[1] = custom(window.ASPQ_qoekJZ);
/* end of custom params */
 
 ar_custom.getStd = function(){for(var i=0,j,s=[];i<this.length;i++){if(this[i])s.push((!j?(j=1,i+'='):'')+escape(this[i]));else j=0}return s.length?'&custom='+s.join(';'):''};
 var bannerExtensionSecond = (function(L){
    if(typeof(ar_cn)=="undefined")ar_cn=1;
    var W=window,D=document,E=D.documentElement,T=0,N=ar_cn,P=0,C=D.compatMode=="CSS1Compat",
      X='<scr'+'ipt type="text/javascript">var ar_bnum='+N+';setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e)}},3000);',
      Y='<\/sc'+'ript><sc'+'ript type="text/javascript" src="'+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999)+ar_custom.getStd()+'"><\/sc'+'ript>';
    function G(){if(T++<100){var o=D.getElementById('ar_container_'+N);if(o){try{var d=o.contentDocument||(W.ActiveXObject&&W.frames['ar_container_'+N].document);if(d){d.write(X+Y)}else setTimeout(arguments.callee,100)}catch(e){try{o.src = "javascript:{document.write('"+X+'document.domain="'+D.domain+'";'+Y+"')}";return}catch(E){}}}else setTimeout(arguments.callee,100)}}
    D.write('<div style="visibility:hidden;height:0px;width:1px;position:absolute;"><iframe id="ar_container_'+ar_cn+'"><\/iframe><\/div><div id="ad_ph_'+ar_cn+'" style="display:none;"><\/div>');ar_cn++;return G;
  })('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=second&bn=2&target=top&bt=43&keyword='+encodeURIComponent(crtg_content)+'&pz=1&tail256=');
  
</script>

<div id="adriver_banner_310018681"></div>
 <script type="text/javascript">
         var bannerSecond = new adriver("adriver_banner_310018681", {sid:51864, bt:52, sz:'reklama', bn:2, pz:1});
         bannerSecond.onLoadComplete(function(){
                 if (this.reply.adid == 0){
                         bannerExtensionSecond();
                 }
         });
 </script>
</div>

<!--  AdRiver code START. Type:AjaxJS Site: Sovsport PZ: 3 BN: 2 -->
<div id="adriver_banner_1130900216"></div>

<script type="text/javascript">
new adriver("adriver_banner_1130900216", {sid:41610, bt:52, bn:2, pz:3});
</script>

<!--  AdRiver code END  -->
<!--/noindex--></div>
<div id="uslotitem14718" class="lazyload_ad"><!--noindex-->
<!--  AdRiver code START. Type:extension Site: kp.ru PZ: 2 BN: 5 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L='' + ('https:' == document.location.protocol ? 'https:' : 'http:') + ''+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div>');_();ar_cn++;
})('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&bn=5&target=top&bt=43&pz=2&tail256=');
</script>



<!--  AdRiver code END  -->

<!--  AdRiver code START. Type:extension Site: kp.ru PZ: 1 BN: 9 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L='' + ('https:' == document.location.protocol ? 'https:' : 'http:') + ''+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div>');_();ar_cn++;
})('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&bn=9&target=top&bt=43&pz=1&tail256=');
</script>
<!--  AdRiver code END  -->
<!--/noindex--></div>
</div>





                            <div id="uni_slot_201" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem9082" class="lazyload_ad"><!--noindex-->
<script type="text/javascript">
KPjQuery(document).ready(function() {
  KPjQuery( "#tabs" ).tabs({ show: { effect: "fadeIn", duration: 600 } });
});
var kpga_events = {
  FacebookWidget:0, 
  TwitterWidget:0, 
  VKWidget:0, 
  OdnoklassnikiWidget:0,
  chk: function(name) {
    var me = this;
    if(!me[name]) {
      me[name] = 1;
      _gaq.push(['_trackEvent', 'SocialWidget', name]);
    }
  }
}
</script>
<div class="all_partners all_partners-margintop">
<link type="text/css" rel="stylesheet" href="/css/tabs.css" rel="nofollow" media="all">
<div id="tabs" class="tabset">
  <ul class="tabset_tabs">
    <li>
      <a href="#tabs-2" rel="nofollow" onclick="kpga_events.chk('FacebookWidget')">
        <img src="http://s5.stc.all.kpcdn.net/images/tabs/facebook2_icon.jpg" border="0" />
      </a>
    </li><li>
      <a href="#tabs-3" rel="nofollow" onclick="kpga_events.chk('TwitterWidget')">
        <img src="http://s1.stc.all.kpcdn.net/images/tabs/twitter2_icon.jpg" border="0" />
      </a>
    </li><li id="kp_vkontakte">
      <a href="#tabs-4" rel="nofollow" onclick="kpga_events.chk('VKWidget')">
        <img src="http://s2.stc.all.kpcdn.net/images/tabs/vkontakte2_icon.jpg" border="0" />
      </a>
    </li><li id="kp_od">
      <a href="#tabs-5" rel="nofollow" onclick="kpga_events.chk('OdnoklassnikiWidget')">
        <img src="http://s3.stc.all.kpcdn.net/f/3/image/51/27/2242751.png" border="0" width="27px" />
      </a>
    </li>
  </ul>
  <div class="tabset_content_container">
    <div id="tabs-2" class="tabset_content">
      <iframe src="http://www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Fwww.facebook.com%2Fonlinekpru&amp;width=285&amp;colorscheme=light&amp;show_faces=true&amp;stream=false&amp;header=false&amp;height=210" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:285px; height:210px;" allowTransparency="true"></iframe>
    </div>
    <div id="tabs-3" class="tabset_content" style="display:none">
      <a class="twitter-timeline" height="225" data-dnt="true" href="https://twitter.com/search?q=onlinekpru" rel="nofollow" data-widget-id="370463552194093056" data-chrome="nofooter transparent noscrollbar" data-screen-name="onlinekpru" data-show-replies="false">Твиты о "onlinekpru"</a>
      <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
    </div>
    <div id="tabs-4" class="tabset_content" style="display:none">
      <script type="text/javascript" src="//vk.com/js/api/openapi.js?82"></script>
      <!-- VK Widget -->
      <div id="vk_groups"></div>
      <script type="text/javascript">
        VK.Widgets.Group("vk_groups", {mode: 0, width: "285", height: "210"}, 15722194);
      </script>
    </div>
    <div id="tabs-5" class="tabset_content" style="display:none">
      <div id="ok_group_widget"></div>
      <script type="text/javascript">
!function (d, id, did, st) {
  var js = d.createElement("script");
  js.src = "http://connect.ok.ru/connect.js";
  js.onload = js.onreadystatechange = function () {
    if (!this.readyState || this.readyState == "loaded" || this.readyState == "complete") {
      if (!this.executed) {
        this.executed = true;
        setTimeout(function () {
          OK.CONNECT.insertGroupWidget(id,did,st);
        }, 0);
      }
    }
  }
  d.documentElement.appendChild(js);
}(document,"ok_group_widget","50657161838784","{width:290,height:230}");
      </script>
      </div>
    </div>
  </div>
</div>
<!--/noindex--></div>
</div>





                            <div id="uni_slot_202" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem5954" class="lazyload_ad"><div class='all_bblock'><h5 class='black'>Новости сми</h5><div class='all_bblock-ins'>
<!--noindex-->
<div id="smi2adblock_59338"><a href="http://smi2.ru/" rel="nofollow">Новости СМИ2</a></div>

<script type="text/javascript" charset="windows-1251">

  (function() {

    var sc = document.createElement('script'); sc.type = 'text/javascript'; sc.async = true;

    sc.src = 'http://js.smi2.ru/data/js/59338.js'; sc.charset = 'windows-1251';

    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sc, s);

  }());

</script>
<!--/noindex-->
</div></div></div>
</div>





                            <div id="uni_slot_105" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem6600" class="lazyload_ad"><!--noindex-->
<!--  AdRiver code START. Type:extension Site: kp.ru SZ: valio2010 PZ: 1 BN: 5 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L+=escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div>');_();ar_cn++;
})('http://ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=valio2010&bn=5&target=top&bt=43&pz=1&tail256=');
</script>
<!--  AdRiver code END  -->
<!--/noindex--></div>
</div>




 
                            <div id="uni_slot_203" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <!--noindex-->
<div id="uslotitem15456"><div style="text-align: left;" class="all_block leopard">
  <div class="all_block-title">
    <div class="all_block-title-lbg">
      <div class="all_block-title-rbg"><a href="/daily/leopard/" rel="nofollow">Земля леопарда</a></div>
    </div>
  </div>
  <div class="clear"></div>
        <div class="all_block-ins">
                <ul>
      <li class="first">
        <div class="img"><a href="/daily/26260/3139084/" rel="nofollow"><img alt="Прибавление в пятнистом семействе" src="http://s4.stc.all.kpcdn.net/f/12/image/77/60/7126077.jpg"></a></div>
        <div class="txt">
          <h5><a href="/daily/26260/3139084/" rel="nofollow">Прибавление в пятнистом семействе</a></h5>
          <p><a href="/daily/26260/3139084/" rel="nofollow">Мы следим за судьбой леопарденка, которого выкормила овчарка</a></p>
        </div>
        <div class="clear"></div>
      </li>
      <li class="">
        <div class="img"><a href="/daily/26260/3139083/" rel="nofollow"><img alt="Снова счастливы вместе" src="http://s5.stc.all.kpcdn.net/f/12/image/72/60/7126072.jpg"></a></div>
        <div class="txt">
          <h5><a href="/daily/26260/3139083/" rel="nofollow">Снова счастливы вместе</a></h5>
          <p><a href="/daily/26260/3139083/" rel="nofollow">В новом эпизоде таежного сериала «Пятнистая семейка-2» мама Кедровка находит  котенка, считавшегося погибшим</a></p>
        </div>
        <div class="clear"></div>
      </li>
      <li class="last">
        <div class="img"><a href="/daily/26260/3139082/" rel="nofollow"><img alt="60 минут наедине с хищником: «Киса, если ты меня съешь, кто тебя защищать будет?»" src="http://s1.stc.all.kpcdn.net/f/12/image/67/60/7126067.jpg"></a></div>
        <div class="txt">
          <h5><a href="/daily/26260/3139082/" rel="nofollow">60 минут наедине с хищником: «Киса, если ты меня съешь, кто тебя защищать будет?»</a></h5>
          <p><a href="/daily/26260/3139082/" rel="nofollow">Легендарный приморский ученый несколько раз встречался с хищниками в тайге один на один</a></p>
        </div>
        <div class="clear"></div>
      </li>
                </ul>
        </div>
</div>
</div>

<!--/noindex-->
</div>





                            <div id="uni_slot_204" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem5759" class="lazyload_ad"><div class='all_bblock'><h5 class='black'>Новости сми</h5><div class='all_bblock-ins'>
<!--noindex-->
<div id="smi_teaser_2390">
    <center><a href="http://24smi.org" rel="nofollow">Новости 24СМИ</a></center>
    </div>
<!--/noindex-->
</div></div></div>
<div id="uslotitem17431" class="lazyload_ad"><div class='all_bblock'><h5 class='black'>Новости сми</h5><div class='all_bblock-ins'>
<!--noindex-->
<script src='http://partner.mediametrics.ru/inject/inject.js' type='text/javascript' id='MediaMetricsInject' data-width='300' data-height='300' data-rows='4' data-inline='' data-logo='true' data-font='small' data-fontfamily='arial' data-border='' data-borderwidth='1' data-alignment='vertical' data-site='mmet/kp_ru' data-hash='bef1307d7dcec9f1f4d94166e244501f'> </script>
<!--/noindex-->
</div></div></div>
</div>





                            <div id="uni_slot_3" class="uslot_banner all_banner-rbig" style="display:block;clear:both;">
    <div id="uslotitem14922" class="lazyload_ad"><!--noindex-->
<div id="CNM1121" style="text-align:center;display:none" ><a href="http://www.novostimira.com.ua" rel="nofollow" id="CNM1121t" style="display:none" target="_blank"><strong>Новости</strong></a></div>

<script type="text/javascript">
    var el = document.getElementById('CNM1121');
    if (el) {
        if (document.getElementById('CNM1121t').style.display == 'none') {
            document.getElementById('CNM1121t').style.display = '';
            var dateNM = new Date();
            var t = Math.floor(dateNM.getTime()/(1000*600));
            var NMces=document.createElement('script');
            NMces.type = 'text/javascript';
            NMces.charset = 'UTF-8';
            NMces.src='http://c.novostimira.biz/l/1121?v='+t;
            el.parentNode.appendChild(NMces);
        }
    }
</script>
<br>

<!--/noindex--></div>
<div id="uslotitem12298" class="lazyload_ad"><!--noindex-->
<br>
<div id="smi2adblock_72479"><a href="http://smi2.ru/" rel="nofollow">Новости СМИ2</a></div>
<script type="text/javascript" charset="utf-8">
  (function() {
    var sc = document.createElement('script'); sc.type = 'text/javascript'; sc.async = true;
    sc.src = 'http://js.smi2.ru/data/js/72479.js'; sc.charset = 'utf-8';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sc, s);
  }());
</script>
<!--/noindex--></div>
<div id="uslotitem14389" class="lazyload_ad"><!--noindex-->
<div id="DIV_KP_17" style="text-align:left;"></div>
<script charset="windows-1251" type="text/javascript" src="http://www.adv.kp.ru/show.cgi?adp=17&div=DIV_KP_17"></script>
<!--/noindex--></div>
</div>





                            




                            


                            <div id="uni_slot_4" class="uslot_banner" style="display:block;clear:both;">
    <div id="uslotitem17168" class="lazyload_ad"><!--noindex-->

<style> div#ttarget_div{ background-color:#ffffff; border-width:0px; border-color:#e7e7e7; border-style: solid; width: 298px; } div#ttarget_div div{ background-color:#ffffff; border-width:1px; border-color:#e7e7e7; border-style: solid; width:298px; display: inline-block; text-align:left; padding-top: 15px; padding-right: 0px; } div#ttarget_div div a{ color:#40454C; font-size:12px; font-family: Tahoma; text-decoration: none; } div#ttarget_div img { float: left; width: 70px; padding-right:10px; padding-left:10px; padding-bottom:15px; } div#ttarget_title { float: left; height: 20px; } #ttarget_title { float: left; width: auto; height: auto; color: white; padding: 3px 9px 3px 9px; font-size: 15px; font-weight: bold; letter-spacing: 0.6pt; text-transform: uppercase; font-family: Tahoma, Geneva, Arial, Helvetica, sans-serif; background: #788F88; background: -webkit-gradient(linear, left top, left bottom, color-stop(0, #788F88), color-stop(0.7, #5C646D)); background: -moz-linear-gradient(center top, #788F88 0%, #5C646D 70%); background: -webkit-linear-gradient(top, #788F88 0%, #5C646D 70%); background: -o-linear-gradient(top, #788F88 0%, #5C646D 70%); background: linear-gradient(top, #788F88 0%, #5C646D 70%); background: -ms-linear-gradient(top, #788F88 0%, #5C646D 70%); -pie-background: linear-gradient(#788F88, #5C646D); text-shadow: 1px 2px 3px #383D43; } </style> 

<div id="ttarget_title">Новости Ttarget</div> <div id="ttarget_div" data-width="240" data-height="300"></div>  <script type="text/javascript"> var tt = document.createElement('script'); tt.type = 'text/javascript'; tt.async = true; tt.src = 'http://tt.ttarget.ru/s/tt.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(tt, s); </script>
<!--/noindex--></div>
<div id="uslotitem15858" class="lazyload_ad"><!--noindex-->
<div align=center>
<!--  AdRiver code START. Type:poster Site: kp.ru SZ: realty PZ: 3 BN: 7 -->
<script type="text/javascript">
function adriverPoster(L){
    if(typeof(ar_cn)=="undefined")ar_cn=1;
    var W=window,D=document,E=D.documentElement,T=0,N=ar_cn,P=0,C=D.compatMode=="CSS1Compat",
        X='<scr'+'ipt type="text/javascript">var ar_bnum='+N+';setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e)}},3000);',
        Y='<\/sc'+'ript><sc'+'ript type="text/javascript" src="' + ('https:' == document.location.protocol ? 'https:' : 'http:') + ''+L+'&tail256='+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999)+'"><\/sc'+'ript>';
    function G(){if(T++<100){var ph=document.getElementById('ad_ph_'+N);if (ph){var c=ph.previousSibling;c.innerHTML='<iframe id="ar_container_'+N+'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe>'}else{setTimeout(arguments.callee,100);return}var o=D.getElementById('ar_container_'+N);if(o){try{var d=o.contentDocument||(W.ActiveXObject&&W.frames['ar_container_'+N].document);if(d){d.write(X+Y)}else setTimeout(arguments.callee,100)}catch(e){try{o.src = "javascript:{document.write('"+X+'document.domain="'+D.domain+'";'+Y+"')}";return}catch(E){}}}else setTimeout(arguments.callee,100)}}
    function A(e,t,f){if(e.addEventListener)e.addEventListener(t,f,false);else if(e.attachEvent)e.attachEvent('on'+t,f)}
    function R(e,t,f){if(e.removeEventListener)e.removeEventListener(t,f,false);else if(e.detachEvent)e.detachEvent('on'+t,f)}
    function S(){var ch=self.innerHeight||C&&E.clientHeight||D.body.clientHeight,st=self.pageYOffset||C&&E.scrollTop||D.body.scrollTop;if(P>=st&&st+ch>=P){R(W,'scroll',S);G()}}
    A(W,'load',function(){var o=D.getElementById('ad_ph_'+N);if(o){while(o.offsetParent){P+=o.offsetTop;o=o.offsetParent}A(W,'scroll',S);S()}});
    D.write('<div style="position:absolute;visibility:hidden;height:0px;"><\/div><div id="ad_ph_'+N+'"><\/div>');
    ar_cn++;
}
adriverPoster('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=realty&bn=7&target=top&bt=49&pz=3');
</script>
<!--  AdRiver code END  -->



</div>

<!--/noindex--></div>
</div>





    <!--<div class="none">&nbsp;&nbsp;&nbsp;<br />&nbsp;</div>-->
    <!--</div>-->
    <!-- ПРАВАЯ КОЛОНКА 300 (конец) -->
</div>
<div class="clear"></div>



  <div class="clear"></div>

  </div>
  <!-- СТРАНИЦА НОВОСТЕЙ (КОНЕЦ) -->

  </div>
<!-- Div центровки страницы (конец) -->


  <!-- /_inc/bottom.html:1|0|www.kp.ru -->
<div class="all_footer">
    <!-- Левая колонка -->
    <div class="leftcol">
  <p class="archive"><a class="logo" href="/">&nbsp;</a><a href="/arch/">Архив номеров</a>&nbsp;|&nbsp;<a href="/subscribe/">Подписка</a></p>
  <!--Виджет архива номеров-->
  <div id="calendar">
  <p class="month"><input type="button" class="prev" value="&lt;&lt;" /><strong> Август 2014 </strong><input type="button" class="next" value="&gt;&gt;" style="visibility:hidden;" /></p>
  <p class="th"><em>пн</em><em>вт</em><em>ср</em><em>чт</em><em>пт</em><em>сб</em><em>вс</em></p>
<div class="m7_y2014"><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><a href='/gazeta/2014/08/01/'>1</a><em>2</em><em>3</em><a href='/gazeta/2014/08/04/'>4</a><a href='/gazeta/2014/08/05/'>5</a><a href='/gazeta/2014/08/06/'>6</a><a href='/gazeta/2014/08/07/'>7</a><a href='/gazeta/2014/08/08/'>8</a><a href='/gazeta/2014/08/09/'>9</a><em>10</em><a href='/gazeta/2014/08/11/'>11</a><a href='/gazeta/2014/08/12/'>12</a><a href='/gazeta/2014/08/13/'>13</a><a href='/gazeta/2014/08/14/'>14</a><em>15</em><em>16</em><em>17</em><em>18</em><em>19</em><em>20</em><em>21</em><em>22</em><em>23</em><em>24</em><em>25</em><em>26</em><em>27</em><em>28</em><em>29</em><em>30</em><em>31</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em></div><div class="m6_y2014" style="display:none;"><em>&nbsp;</em><a href='/gazeta/2014/07/01/'>1</a><a href='/gazeta/2014/07/02/'>2</a><a href='/gazeta/2014/07/03/'>3</a><a href='/gazeta/2014/07/04/'>4</a><a href='/gazeta/2014/07/05/'>5</a><em>6</em><a href='/gazeta/2014/07/07/'>7</a><a href='/gazeta/2014/07/08/'>8</a><a href='/gazeta/2014/07/09/'>9</a><a href='/gazeta/2014/07/10/'>10</a><a href='/gazeta/2014/07/11/'>11</a><a href='/gazeta/2014/07/12/'>12</a><em>13</em><a href='/gazeta/2014/07/14/'>14</a><a href='/gazeta/2014/07/15/'>15</a><a href='/gazeta/2014/07/16/'>16</a><a href='/gazeta/2014/07/17/'>17</a><a href='/gazeta/2014/07/18/'>18</a><em>19</em><em>20</em><a href='/gazeta/2014/07/21/'>21</a><a href='/gazeta/2014/07/22/'>22</a><a href='/gazeta/2014/07/23/'>23</a><a href='/gazeta/2014/07/24/'>24</a><a href='/gazeta/2014/07/25/'>25</a><a href='/gazeta/2014/07/26/'>26</a><em>27</em><a href='/gazeta/2014/07/28/'>28</a><a href='/gazeta/2014/07/29/'>29</a><a href='/gazeta/2014/07/30/'>30</a><a href='/gazeta/2014/07/31/'>31</a><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em></div><div class="m5_y2014" style="display:none;"><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>1</em><a href='/gazeta/2014/06/02/'>2</a><a href='/gazeta/2014/06/03/'>3</a><a href='/gazeta/2014/06/04/'>4</a><a href='/gazeta/2014/06/05/'>5</a><a href='/gazeta/2014/06/06/'>6</a><a href='/gazeta/2014/06/07/'>7</a><em>8</em><a href='/gazeta/2014/06/09/'>9</a><a href='/gazeta/2014/06/10/'>10</a><a href='/gazeta/2014/06/11/'>11</a><em>12</em><em>13</em><em>14</em><em>15</em><a href='/gazeta/2014/06/16/'>16</a><a href='/gazeta/2014/06/17/'>17</a><a href='/gazeta/2014/06/18/'>18</a><a href='/gazeta/2014/06/19/'>19</a><a href='/gazeta/2014/06/20/'>20</a><a href='/gazeta/2014/06/21/'>21</a><em>22</em><a href='/gazeta/2014/06/23/'>23</a><a href='/gazeta/2014/06/24/'>24</a><a href='/gazeta/2014/06/25/'>25</a><a href='/gazeta/2014/06/26/'>26</a><a href='/gazeta/2014/06/27/'>27</a><a href='/gazeta/2014/06/28/'>28</a><em>29</em><a href='/gazeta/2014/06/30/'>30</a><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em></div><div class="m4_y2014" style="display:none;"><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>1</em><em>2</em><em>3</em><em>4</em><a href='/gazeta/2014/05/05/'>5</a><a href='/gazeta/2014/05/06/'>6</a><a href='/gazeta/2014/05/07/'>7</a><a href='/gazeta/2014/05/08/'>8</a><em>9</em><em>10</em><em>11</em><a href='/gazeta/2014/05/12/'>12</a><a href='/gazeta/2014/05/13/'>13</a><a href='/gazeta/2014/05/14/'>14</a><a href='/gazeta/2014/05/15/'>15</a><a href='/gazeta/2014/05/16/'>16</a><a href='/gazeta/2014/05/17/'>17</a><em>18</em><a href='/gazeta/2014/05/19/'>19</a><a href='/gazeta/2014/05/20/'>20</a><a href='/gazeta/2014/05/21/'>21</a><a href='/gazeta/2014/05/22/'>22</a><a href='/gazeta/2014/05/23/'>23</a><a href='/gazeta/2014/05/24/'>24</a><em>25</em><a href='/gazeta/2014/05/26/'>26</a><a href='/gazeta/2014/05/27/'>27</a><a href='/gazeta/2014/05/28/'>28</a><a href='/gazeta/2014/05/29/'>29</a><a href='/gazeta/2014/05/30/'>30</a><a href='/gazeta/2014/05/31/'>31</a><em>&nbsp;</em></div><div class="m3_y2014" style="display:none;"><em>&nbsp;</em><a href='/gazeta/2014/04/01/'>1</a><a href='/gazeta/2014/04/02/'>2</a><a href='/gazeta/2014/04/03/'>3</a><a href='/gazeta/2014/04/04/'>4</a><a href='/gazeta/2014/04/05/'>5</a><em>6</em><a href='/gazeta/2014/04/07/'>7</a><a href='/gazeta/2014/04/08/'>8</a><a href='/gazeta/2014/04/09/'>9</a><a href='/gazeta/2014/04/10/'>10</a><a href='/gazeta/2014/04/11/'>11</a><a href='/gazeta/2014/04/12/'>12</a><em>13</em><a href='/gazeta/2014/04/14/'>14</a><a href='/gazeta/2014/04/15/'>15</a><a href='/gazeta/2014/04/16/'>16</a><a href='/gazeta/2014/04/17/'>17</a><a href='/gazeta/2014/04/18/'>18</a><a href='/gazeta/2014/04/19/'>19</a><em>20</em><a href='/gazeta/2014/04/21/'>21</a><a href='/gazeta/2014/04/22/'>22</a><a href='/gazeta/2014/04/23/'>23</a><a href='/gazeta/2014/04/24/'>24</a><a href='/gazeta/2014/04/25/'>25</a><a href='/gazeta/2014/04/26/'>26</a><em>27</em><a href='/gazeta/2014/04/28/'>28</a><a href='/gazeta/2014/04/29/'>29</a><a href='/gazeta/2014/04/30/'>30</a><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em></div><div class="m2_y2014" style="display:none;"><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><a href='/gazeta/2014/03/01/'>1</a><em>2</em><a href='/gazeta/2014/03/03/'>3</a><a href='/gazeta/2014/03/04/'>4</a><a href='/gazeta/2014/03/05/'>5</a><a href='/gazeta/2014/03/06/'>6</a><a href='/gazeta/2014/03/07/'>7</a><em>8</em><em>9</em><em>10</em><a href='/gazeta/2014/03/11/'>11</a><a href='/gazeta/2014/03/12/'>12</a><a href='/gazeta/2014/03/13/'>13</a><a href='/gazeta/2014/03/14/'>14</a><a href='/gazeta/2014/03/15/'>15</a><em>16</em><a href='/gazeta/2014/03/17/'>17</a><a href='/gazeta/2014/03/18/'>18</a><a href='/gazeta/2014/03/19/'>19</a><a href='/gazeta/2014/03/20/'>20</a><a href='/gazeta/2014/03/21/'>21</a><a href='/gazeta/2014/03/22/'>22</a><em>23</em><a href='/gazeta/2014/03/24/'>24</a><a href='/gazeta/2014/03/25/'>25</a><a href='/gazeta/2014/03/26/'>26</a><a href='/gazeta/2014/03/27/'>27</a><a href='/gazeta/2014/03/28/'>28</a><a href='/gazeta/2014/03/29/'>29</a><em>30</em><a href='/gazeta/2014/03/31/'>31</a><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em><em>&nbsp;</em></div>
</div>

  <noindex>
    <ul class="seti">
      <li class="first">Комсомолка<br /> в социальных сетях:</li>
      <li><a rel="nofollow" href="http://my.mail.ru/community/onlinekp.ru/" target="_blank"><img src="http://s2.stc.all.kpcdn.net/f/191/sn_logo/05/03/305.png" alt="Мой Мир КП Central" /></a></li>
      <li><a rel="nofollow" href="http://statigr.am/onlinekp" target="_blank"><img src="http://s3.stc.all.kpcdn.net/f/191/sn_logo/43/01/143.png" alt="instagr.am" /></a></li>
      <li><a rel="nofollow" href="https://plus.google.com/u/0/112261544981697332354/posts" target="_blank"><img src="http://s4.stc.all.kpcdn.net/f/191/sn_logo/42/01/142.png" alt="Google Plus" /></a></li>
      <li><a rel="nofollow" href="http://www.facebook.com/pages/Komsomolskaa-pravda/369256943469?ref=mf" target="_blank"><img src="http://s5.stc.all.kpcdn.net/f/191/sn_logo/11/00/11.png" alt="facebook Komsomolskaa-pravda" /></a></li>
      <li><a rel="nofollow" href="http://www.odnoklassniki.ru/kpru" target="_blank"><img src="http://s1.stc.all.kpcdn.net/f/191/sn_logo/14/00/14.png" alt="odnoklassniki group kpru" /></a></li>
      <li><a rel="nofollow" href="http://www.twitter.com/onlinekpru/" target="_blank"><img src="http://s2.stc.all.kpcdn.net/f/191/sn_logo/30/00/30.png" alt="twitter onlinekpru" /></a></li>
      <li><a rel="nofollow" href="http://vkontakte.ru/club15722194" target="_blank"><img src="http://s3.stc.all.kpcdn.net/f/191/sn_logo/13/00/13.png" alt="vkontakte club15722194" /></a></li>
    </ul>
  </noindex>
  <p class="contacts">Как с нами связаться:<br /><a href="/daily/scheme/">Схема проезда</a><br /><a href="mailto:kp@kp.ru">Читателям</a></p>
  <div class="age">возрастная категория сайта <span class="num">18+</span></div>
</div>


    <!-- Правая колонка -->
    <!-- Правая колонка (начало) -->
<div class="rightcol">
    <ul class="topmenu">
        <li><a href="/handbook">КП-Справочник</a></li>
        <li><a href="http://www.kp.ru/about/">Все о КП</a></li>
        <li><a href="/daily/friday/">Еженедельник</a></li>
        <!--noindex--><li><a href="http://tv.kp.ru/" rel="nofollow">Телеканал КП</a></li><!--/noindex-->
        <li><a href="/radio/">Радио КП</a></li>
        <li><a href="http://kp.ru/go/http://advert.kp.ru/kr/">Реклама</a></li>
        <li><a href="/daily/collections/">Коллекции КП</a></li>
        <li><a href="/action">Акции КП</a></li>
        <li><a href="/daily/press/">Пресс-центр</a></li>
    </ul>
    <ul class="tabs">
        <li><a title="Новости 24" href="/online/">Новости</a></li>
        <li><a title="Спорт" href="/sport">Спорт</a></li>
        <li><a title="Политика" href="/politics">Политика</a></li>
        <li><a title="Экономика" href="/economics">Экономика</a></li>
        <li><a title="Общество" href="/society">Общество</a></li>
        <li><a title="Происшествия" href="/incidents">Происшествия</a></li>
        <li><a title="Звезды" href="/stars">Звезды</a></li>
        <li><a title="Наука" href="/daily/science/">Наука</a></li>
        <li><a title="Авто" href="/auto">Авто</a></li>
        <li><a title="Дом. Семья" href="/special">Дом. Семья</a></li>
    </ul>
                <div class="editorial">
                <p>УЧРЕДИТЕЛЬ И РЕДАКЦИЯ: <strong>ЗАО «ИД «Комсомольская правда».</strong></p>

                <p>Сетевое издание (сайт) зарегистрировано Роскомнадзором, свидетельство Эл№ФC77-50166 от 15 июня 2012.</p>
                <p>Главный редактор - Сунгоркин В.Н.</p>
                <p>Шеф-редактор сайта - Носова О.В.</p>
                <p>Сообщения и комментарии читателей сайта размещаются без предварительного редактирования. Редакция оставляет за собой право удалить их с сайта или отредактировать, если указанные сообщения и комментарии являются злоупотреблением свободой массовой информации или нарушением иных требований закона.</p>
            </div>
            <div class="copyright">
                <p><strong>© ЗАО ИД «Комсомольская правда», 2014.</strong></p>
                 125993, Москва, Старый Петровско-Разумовский проезд, 1/23, стр. 1. Тел. +7 (495) 777-02-82.<br />
                <p>Исключительные права на материалы, размещённые на интернет-сайте <a href="http://www.kp.ru/">www.kp.ru</a>, в соответствии с законодательством Российской Федерации об охране результатов интеллектуальной деятельности принадлежат ЗАО "Издательский дом "Комсомольская правда", и не подлежат использованию другими лицами в какой бы то ни было форме без письменного разрешения правообладателя.<br />Приобретение авторских прав: <a href="mailto:kp@kp.ru">kp@kp.ru</a><br />Для читателей. Нам важно ваше мнение: (495)777-02-82, 8-800-200-0057 (бесплатно для жителей РФ).</p>
            </div>

    <ul class="last-news">
        <li><a href="/">Новости</a></li>
        <li><a href="/">Последние новости</a></li>
        <li><a href="/">Новости шоу-бузнеса</a></li>
        <li><a href="/">Бизнес новости</a></li>
        <li><a href="/">Новости дня</a></li>
        <li><a href="/">Новости России</a></li>
        <li><a href="/">Новости Украины</a></li>
        <li><a href="/">Новости мира</a></li>
        <li><a href="http://www.kp.ru/guide/">Гид</a></li>
    </ul>

    <ul class="regions-news">
        <li>Новости в регионах:</li>
        <li><a class="s_follow" href="http://msk.kp.ru">Москва</a></li>
        <li><a class="s_follow" href="http://abakan.kp.ru">Абакан</a></li>
        <li><a class="s_follow" href="http://alt.kp.ru">Барнаул</a></li>
        <li><a class="s_follow" href="http://bel.kp.ru">Белгород</a></li>
        <li><a class="s_follow" href="http://amur.kp.ru">Благовещенск</a></li>
        <li><a class="s_follow" href="http://bryansk.kp.ru">Брянск</a></li>
        <li><a class="s_follow" href="http://dv.kp.ru">Владивосток</a></li>
        <li><a class="s_follow" href="http://vladimir.kp.ru">Владимир</a></li>
        <li><a class="s_follow" href="http://volgograd.kp.ru">Волгоград</a></li>
        <li><a class="s_follow" href="http://vologda.kp.ru">Вологда</a></li>
        <li><a class="s_follow" href="http://vrn.kp.ru">Воронеж</a></li>
        <li><a class="s_follow" href="http://ural.kp.ru">Екатеринбург</a></li>
        <li><a class="s_follow" href="http://izh.kp.ru">Ижевск</a></li>
        <li><a class="s_follow" href="http://irk.kp.ru">Иркутск</a></li>
        <li><a class="s_follow" href="http://kazan.kp.ru">Казань</a></li>
        <li><a class="s_follow" href="http://kaliningrad.kp.ru">Калининград</a></li>
        <li><a class="s_follow" href="http://kem.kp.ru">Кемерово</a></li>
        <li><a class="s_follow" href="http://kirov.kp.ru">Киров</a></li>
        <li><a class="s_follow" href="http://kuban.kp.ru">Краснодар</a></li>
        <li><a class="s_follow" href="http://krsk.kp.ru">Красноярск</a></li>
        <li><a class="s_follow" href="http://crimea.kp.ru">Крым</a></li>
        <li><a class="s_follow" href="http://kursk.kp.ru">Курск</a></li>
        <li><a class="s_follow" href="http://lipetsk.kp.ru">Липецк</a></li>
        <li><a class="s_follow" href="http://murmansk.kp.ru">Мурманск</a></li>
        <li><a class="s_follow" href="http://nnov.kp.ru">Нижний Новгород</a></li>
        <li><a class="s_follow" href="http://nsk.kp.ru">Новосибирск</a></li>
        <li><a class="s_follow" href="http://omsk.kp.ru">Омск</a></li>
        <li><a class="s_follow" href="http://orel.kp.ru">Орел</a></li>
        <li><a class="s_follow" href="http://penza.kp.ru">Пенза</a></li>
        <li><a class="s_follow" href="http://perm.kp.ru">Пермь</a></li>
        <li><a class="s_follow" href="http://pskov.kp.ru">Псков</a></li>
        <li><a class="s_follow" href="http://rostov.kp.ru">Ростов-на-Дону</a></li>
        <li><a class="s_follow" href="http://ryazan.kp.ru">Рязань</a></li>
        <li><a class="s_follow" href="http://samara.kp.ru">Самара</a></li>
        <li><a class="s_follow" href="http://spb.kp.ru">Санкт-Петербург</a></li>
        <li><a class="s_follow" href="http://saratov.kp.ru">Саратов</a></li>
        <li><a class="s_follow" href="http://smol.kp.ru">Смоленск</a></li>
        <li><a class="s_follow" href="http://stav.kp.ru">Ставрополь</a></li>
        <li><a class="s_follow" href="http://komi.kp.ru">Сыктывкар</a></li>
        <li><a class="s_follow" href="http://tambov.kp.ru">Тамбов</a></li>
        <li><a class="s_follow" href="http://tver.kp.ru">Тверь</a></li>
        <li><a class="s_follow" href="http://tomsk.kp.ru">Томск</a></li>
        <li><a class="s_follow" href="http://tula.kp.ru">Тула</a></li>
        <li><a class="s_follow" href="http://tumen.kp.ru">Тюмень</a></li>
        <li><a class="s_follow" href="http://ul.kp.ru">Ульяновск</a></li>
        <li><a class="s_follow" href="http://ufa.kp.ru">Уфа</a></li>
        <li><a class="s_follow" href="http://hab.kp.ru">Хабаровск</a></li>
        <li><a class="s_follow" href="http://chel.kp.ru">Челябинск</a></li>
        <li><a class="s_follow" href="http://chita.kp.ru">Чита</a></li>
        <li><a class="s_follow" href="http://yar.kp.ru">Ярославль</a></li>
    </ul>

    <!--noindex-->
    <ul class="abroad-news">
        <li>Новости за рубежом:</li>
        <li><a rel="nofollow" href="http://balkans.kp.ru">Балканы</a></li>
        <li><a rel="nofollow" href="http://kp.by">Беларусь</a></li>
        <li><a rel="nofollow" href="http://kp.kg">Бишкек</a></li>
        <li><a rel="nofollow" href="http://cyprus.kp.ru">Кипр</a></li>
        <li><a rel="nofollow" href="http://kp.md">Молдова</a></li>
        <li><a rel="nofollow" href="http://kompravda.eu">Северная Европа</a></li>
    </ul>
    <!--/noindex-->
</div>
<!-- Правая колонка (конец) -->


    <!-- Счетчики -->
    <div class="counters" id="bottom_counters">
                                <!--noindex-->
<!--bigmir)net TOP 100 Part 1-->
<div style="float:left; width:94px; height:35px;">
<script type="text/javascript" language="javascript"><!--
bmN=navigator,bmD=document,bmD.cookie='b=b',i=0,bs=[],bm={o:1,v:92303,s:92303,t:6,c:bmD.cookie?1:0,n:Math.round((Math.random()* 1000000)),w:0};
for(var f=self;f!=f.parent;f=f.parent)bm.w++;
try{if(bmN.plugins&&bmN.mimeTypes.length&&(x=bmN.plugins['Shockwave Flash']))bm.m=parseInt(x.description.replace(/([a-zA-Z]|\s)+/,''));
else for(var f=3;f<20;f++)if(eval('new ActiveXObject("ShockwaveFlash.ShockwaveFlash.'+f+'")'))bm.m=f}catch(e){;}
try{bm.y=bmN.javaEnabled()?1:0}catch(e){;}
try{bmS=screen;bm.v^=bm.d=bmS.colorDepth||bmS.pixelDepth;bm.v^=bm.r=bmS.width}catch(e){;}
r=bmD.referrer.replace(/^w+:\/\//,'');if(r&&r.split('/')[0]!=window.location.host){bm.f=escape(r).slice(0,400).slice(0,400);bm.v^=r.length}
bm.v^=window.location.href.length;for(var x in bm) if(/^[ovstcnwmydrf]$/.test(x)) bs[i++]=x+bm[x];
bmD.write('<sc'+'ript type="text/javascript" language="javascript" src="http://c.bigmir.net/?'+bs.join('&')+'"></sc'+'ript>');
//-->
</script>
<noscript><img src="http://c.bigmir.net/?v92303&s92303&t6" width="0" height="0" alt="" title="" border="0" /></noscript>
<!--bigmir)net TOP 100 Part 1-->
<!--bigmir)net TOP 100 Part 2-->
<script type="text/javascript" language="javascript"><!--
function BM_Draw(oBM_STAT){
document.write('<table cellpadding="0" cellspacing="0" border="1"><tr><td><div style="margin:0px;padding:0px;font-size:1px;width:88px;"><div style="background:url(\'http://i.bigmir.net/cnt/samples/diagonal/b58_top.gif\') no-repeat bottom;"> </div><div style="font:10px Tahoma;background:url(\'http://i.bigmir.net/cnt/samples/diagonal/b58_center.gif\');"><div style="text-align:center;"><a href="http://www.bigmir.net/" rel="nofollow" target="_blank" style="color:#0000ab;text-decoration:none;font:10px Tahoma;">bigmir<span style="color:#ff0000;">)</span>net</a></div><div style="margin-top:3px;padding: 0px 6px 0px 6px;color:#003596;"><div style="float:left;font:10px Tahoma;">'+oBM_STAT.hosts+'</div><div style="float:right;font:10px Tahoma;">'+oBM_STAT.hits+'</div></div><br clear="all"/></div><div style="background:url(\'http://i.bigmir.net/cnt/samples/diagonal/b58_bottom.gif\') no-repeat top;"> </div></div></td></tr></table>');
}
//-->
</script>
<script type="text/javascript" language="javascript" src="http://c.bigmir.net/?s92303&t0&l1&o1"></script>
<noscript>
<a href="http://www.bigmir.net/" rel="nofollow" target="_blank"><img src="http://c.bigmir.net/?v92303&s92303&t2&l1" width="88" height="31" alt="bigmir)net TOP 100" title="bigmir)net TOP 100" border="0" /></a>
</noscript>
</div>
<!--bigmir)net TOP 100 Part 2-->
<!--/noindex-->






<!--noindex-->
<div id="top100counter" style="display:inline;"></div>
<script type="text/javascript">
var _top100q = _top100q || [];

_top100q.push(["setAccount", "17841"]);
_top100q.push(["trackPageviewByLogo", document.getElementById("top100counter")]);

(function(){
 var top100 = document.createElement("script"); top100.type = "text/javascript";
 top100.async = true;
 top100.src = ("https:" == document.location.protocol ? "https:" : "http:") + "//st.top100.ru/pack/pack.min.js";
 var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(top100, s);
})();
</script>
<!--/noindex-->
<!--noindex-->
<!--LiveInternet logo--><a href="http://www.liveinternet.ru/click;kp" rel="nofollow"
target="_blank"><img src="//counter.yadro.ru/logo;kp?21.6"
title="LiveInternet: показано число просмотров за 24 часа, посетителей за 24 часа и за сегодня"
alt="" border="0" width="88" height="31"/></a><!--/LiveInternet-->
<!--/noindex-->

<!--noindex-->
<!-- Yandex.Metrika informer -->
<a href="http://metrika.yandex.ru/stat/?id=1051362&amp;from=informer"
target="_blank" rel="nofollow"><img src="//bs.yandex.ru/informer/1051362/3_0_FFFFFFFF_FFFFFFFF_0_pageviews"
style="width:88px; height:31px; border:0;" alt="Яндекс.Метрика" title="Яндекс.Метрика: данные за сегодня (просмотры, визиты и уникальные посетители)" onclick="try{Ya.Metrika.informer({i:this,id:1051362,type:0,lang:'ru'});return false}catch(e){}"/></a>
<!-- /Yandex.Metrika informer -->
<!--/noindex-->





    <div style="float: right; margin-right: 30px; width: 140px;">
      <a href="http://www.rambler.ru" title="Партнер «Рамблера»" style="color:#555555;" class="s_follow">Партнер «Рамблера»</a>
        </div>
    </div>
</div>
                        


<script charset="windows-1251" type="text/javascript" src="http://www.smi.ru/show.cgi?adp=5060&div=DIV_SMI_5060"></script>

<script type="text/JavaScript" encoding="utf8">
        (function() {
        var sm = document.createElement("script");
        sm.type = "text/javascript";
        sm.async = true;
        sm.src = "http://jsn.24smi.org/9/9/2390.js";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(sm, s);})();
    </script>
    
 <!-- pered </body> --> <script type="text/javascript"> var MarketGidDate = new Date(); document.write('<scr'+'ipt type="text/javascript" ' +'src="//jsn.marketgid.com/k/p/kp.ru.4421.js?t='+MarketGidDate.getYear()+MarketGidDate.getMonth()+MarketGidDate.getDay()+MarketGidDate.getHours() + '" charset="windows-1251" ></scr'+'ipt>'); </script>


<script charset="windows-1251" type="text/javascript" src="http://www.smi.ru/show.cgi?adp=4723&div=DIV_SMI_4723"></script>

<script charset="windows-1251" type="text/javascript" src="http://www.nnn.ru/show.cgi?adp=32087&div=DIV_NNN_32087"></script>





                        <!--  AdRiver code START. Type:extension Site: kp.ru SZ: second PZ: 3 BN: 19 -->
<script type="text/javascript">
(function(L){if(typeof(ar_cn)=="undefined")ar_cn=1;
var S='setTimeout(function(e){if(!self.CgiHref){document.close();e=parent.document.getElementById("ar_container_"+ar_bnum);e.parentNode.removeChild(e);}},3000);',
    j=' type="text/javascript"',t=0,D=document,n=ar_cn;L='' + ('https:' == document.location.protocol ? 'https:' : 'http:') + ''+L+escape(D.referrer||'unknown')+'&rnd='+Math.round(Math.random()*999999999);
function _(){if(t++<100){var F=D.getElementById('ar_container_'+n);
    if(F){try{var d=F.contentDocument||(window.ActiveXObject&&window.frames['ar_container_'+n].document);
    if(d){d.write('<sc'+'ript'+j+'>var ar_bnum='+n+';'+S+'<\/sc'+'ript><sc'+'ript'+j+' src="'+L+'"><\/sc'+'ript>');t=0}
    else setTimeout(_,100);}catch(e){try{F.src="javascript:{document.write('<sc'+'ript"+j+">var ar_bnum="+n+"; document.domain=\""
    +D.domain+"\";"+S+"<\/sc'+'ript>');document.write('<sc'+'ript"+j+" src=\""+L+"\"><\/sc'+'ript>');}";return}catch(E){}}}else setTimeout(_,100);}}
D.write('<div style="visibility:hidden;height:0px;left:-1000px;position:absolute;"><iframe id="ar_container_'+ar_cn
    +'" width=1 height=1 marginwidth=0 marginheight=0 scrolling=no frameborder=0><\/iframe><\/div><div id="ad_ph_'+ar_cn
    +'" style="display:none;"><\/div>');_();ar_cn++;
})('//ad.adriver.ru/cgi-bin/erle.cgi?sid=51864&sz=second&bn=19&target=blank&bt=43&pz=3&tail256=');
</script>
<!--  AdRiver code END  -->
<div id="AdwolfBanner40x200_915159" ></div>
<!--AdWolf Asynchronous Code Start -->
<script type="text/javascript" >
new Adwolf({
    placeholderId: 'AdwolfBanner40x200_915159',
    width: 40,
    height: 200,
    link: 'http://a.adwolf.ru/prepareCode?p1=cec&p2=cd&pct=a&plp=a&pli=a&pop=a&pr='}, {puids:{}}, {paps:{pap1:'center_left'}}, {mechanics:2});
</script>
<!--AdWolf Asynchronous Code End -->
<!--  AdRiver code START. Type:AjaxJS Site: kp.ru SZ: second PZ: 3 BN: 2 -->

<div id="adriver_banner_1424280189"></div>

<script type="text/javascript">
new adriver("adriver_banner_1424280189", {sid:51864, bt:52, sz:'second', bn:2, pz:3});
</script>

<!--  AdRiver code END  -->
<!--  AdRiver code START. Type:AjaxJS Site: kp.ru PZ: 3 BN: 8 -->
<div id="adriver_banner_1088294394"></div>

<script type="text/javascript">
new adriver("adriver_banner_1088294394", {sid:51864, bt:52, bn:8, pz:3});
</script>

<!--  AdRiver code END  -->






<!-- Подключаемые js библиотеки -->
<script type="text/javascript" src="/_js/slider.js"></script>
<script type="text/javascript" src="/_js/livepipe.js"></script>
<script type="text/javascript" src="/_js/scrollbar.js"></script>
<script type="text/javascript" src="http://my.kp.ru/js/kp/login.js"></script>
<!--<script type="text/javascript" src="/_js/apollo.js?ts=1398156646"></script>-->

<!-- Для кнопки КЛАСС! соц. сети Однокласники, аналогично старому сайту -->
<script src="http://stg.odnoklassniki.ru/share/odkl_share.js" async type="text/javascript" onload='(function(){ODKL.init();})();' ></script>
<!-- Для кнопки КЛАСС! соц. сети Однокласники, конец -->


<!-- Для шаринга в Twitter ( JS-API asynchronously + GA.tracking ) -->
<script type="text/javascript" async
    onload="(function(){
  var twitterWidgets = document.createElement('script');
  twitterWidgets.type = 'text/javascript';
  twitterWidgets.async = true;
  twitterWidgets.src = 'http://platform.twitter.com/widgets.js';
  twitterWidgets.onload = _ga.trackTwitter;
  document.getElementsByTagName('head')[0].appendChild(twitterWidgets);
    })();"
   src="/_js/trackSocial.js">
</script>

<!-- Для шаринга в Twitter, конец -->

<!-- Для шаринга в Мой Мир -->
<script async src="http://cdn.connect.mail.ru/js/loader.js" type="text/javascript" charset="UTF-8"></script>
<!-- Для шаринга в Мой Мир, конец -->


<!-- Для кнопки +1 в Google -->
<script async type="text/javascript" src="https://apis.google.com/js/plusone.js">
  {lang: 'ru'}
</script>
<!-- Для кнопки +1 в Google, конец  -->

<!-- Для раздела Видео 
    <script type="text/javascript" language="javascript" src="/_js/flowplayer-3.2.6.min.js"></script>
    <script type="text/javascript" language="javascript" src="/_js/flowplayer.ipad-3.2.1.min.js"></script>
    <script type="text/javascript" language="javascript" src="/_js/flowplayer.embed-3.0.3.min.js"></script>
 Для раздела Видео, конец -->

<!-- Конец Подключаемые js библиотеки -->

</div>

<script type="text/javascript" src="/_js/region-menu.js" charset="utf-8"></script>
</body>
</html>"""
parser.feed(exampleXml.decode('utf-8').encode("ascii", errors="ignore"))
parser.close()
