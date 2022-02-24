# Tracker Descriptions

The technical and policy review information below was recorded on the date observed and does not necessarily include all information used to determine proper classification. Classifications are subject to review and change. Concerns or requests for review can be emailed to support@disconnect.me.

- [Adabra](#Adabra)
- [Adbot](#Adbot)
- [Adbrain](#Adbrain)
- [AdCash](#AdCash)
- [AdGainerSolutions](#AdGainerSolutions)
- [Adjust](#Adjust)
- [AdMaven](#AdMaven)
- [Admicro](#Admicro)
- [Adnium](#Adnium)
- [Adobe](#Adobe)
- [AdScore](#AdScore)
- [Adstune](#Adstune)
- [AdxSpace](#AdxSpace)
- [AdYouLike](#AdYouLike)
- [AivaLabs](#AivaLabs)
- [a.js](#a.js)
- [Albacross](#Albacross)
- [AppCast](#AppCast)
- [AuditedMedia](#AuditedMedia)
- [Augur](#Augur)
- [AvantLink](#AvantLink)
- [Awin](#Awin)
- [Azet](#Azet)
- [BetssonPalantir](#BetssonPalantir)
- [BigClick](#BigClick)
- [Bisnode](#Bisnode)
- [BitMedia](#BitMedia)
- [BlueCava](#BlueCava)
- [BlueKai](#BlueKai)
- [BoostBox](#BoostBox)
- [Bouncex](#Bouncex)
- [Brandcrumb](#Brandcrumb)
- [BreakTime](#BreakTime)
- [BrightEdge](#BrightEdge)
- [C3-Metrics](#C3-Metrics)
- [CallSource](#CallSource)
- [CartsGuru](#CartsGuru)
- [CashBeet](#CashBeet)
- [Choozle](#Choozle)
- [ClearLink](#ClearLink)
- [Clickayab](#Clickayab)
- [ClickFrog](#ClickFrog)
- [ClickGuard](#ClickGuard)
- [Clixtell](#Clixtell)
- [Cloudflare](#Cloudflare)
- [CoinHive](#CoinHive)
- [CoinPot](#CoinPot)
- [ConversantMedia](#ConversantMedia)
- [CryptoLoot](#CryptoLoot)
- [DoubleVerify](#DoubleVerify)
- [Drawbridge](#Drawbridge)
- [ECSAnalytics](#ECSAnalytics)
- [EroAdvertising](#EroAdvertising)
- [Experian](#Experian)
- [EyeNewton](#EyeNewton)
- [eyeReturn-Marketing](#eyeReturn-Marketing)
- [Facebook](#Facebook)
- [Fanplayr](#Fanplayr)
- [Fiksu](#Fiksu)
- [Flocktory](#Flocktory)
- [Foresee](#Foresee)
- [Friends2Follow](#Friends2Follow)
- [FuelX](#FuelX)
- [Gleam](#Gleam)
- [Google](#Google)
- [GrapheneMedia](#GrapheneMedia)
- [Gridcash](#Gridcash)
- [HilltopAds](#HilltopAds)
- [HotelChamp](#HotelChamp)
- [HotMart](#HotMart)
- [ie8eamus](#ie8eamus)
- [iMedia](#iMedia)
- [Infolinks](#Infolinks)
- [iShumei](#iShumei)
- [IslayTech](#IslayTech)
- [ismatlab.com](#ismatlab.com)
- [Itch](#Itch)
- [JSE](#JSE)
- [justuno](#justuno)
- [KISSmetrics](#KISSmetrics)
- [Kitewheel](#Kitewheel)
- [Konduto](#Konduto)
- [LeadsHub](#LeadsHub)
- [LiveRamp](#LiveRamp)
- [Lotame](#Lotame)
- [lptracker](#lptracker)
- [MaxMind](#MaxMind)
- [MediaMath](#MediaMath)
- [Mercadopago](#Mercadopago)
- [MinerAlt](#MinerAlt)
- [Minescripts](#Minescripts)
- [MineXMR](#MineXMR)
- [Mobials](#Mobials)
- [Mystighty](#Mystighty)
- [Negishim](#Negishim)
- [NeroHut](#NeroHut)
- [OneAd](#OneAd)
- [OnlineMetrix](#OnlineMetrix)
- [OpenX](#OpenX)
- [Origo](#Origo)
- [PartyPoker](#PartyPoker)
- [Paypal](#Paypal)
- [PerimeterX](#PerimeterX)
- [PinPoll](#PinPoll)
- [Polen](#Polen)
- [PPCProtect](#PPCProtect)
- [PrismApp](#PrismApp)
- [PrometheusIntelligenceTechnology](#PrometheusIntelligenceTechnology)
- [Protected-Media](#Protected-Media)
- [Provers](#Provers)
- [Psonstrentie](#Psonstrentie)
- [RazorPay](#RazorPay)
- [Rollick](#Rollick)
- [RoqAd](#RoqAd)
- [Salesforce](#Salesforce)
- [SAP](#SAP)
- [Semantiqo](#Semantiqo)
- [SendPulse](#SendPulse)
- [Shixiseng](#Shixiseng)
- [SiftScience](#SiftScience)
- [SmarterClick](#SmarterClick)
- [SmartyAds](#SmartyAds)
- [Smi](#Smi)
- [Socital](#Socital)
- [SpareChange](#SpareChange)
- [SteelHouse](#SteelHouse)
- [Storeland](#Storeland)
- [Stripchat](#Stripchat)
- [Tapad](#Tapad)
- [TechSolutions](#TechSolutions)
- [The-Trade-Desk](#The-Trade-Desk)
- [Trendemon](#Trendemon)
- [Unknown2mdnsys](#Unknown2mdnsys)
- [Upland](#Upland)
- [VerticalHealth](#VerticalHealth)
- [Vtex](#Vtex)
- [Warumbistdusoarm](#Warumbistdusoarm)
- [Webmecanik](#Webmecanik)
- [Webmine](#Webmine)
- [WideOrbit](#WideOrbit)
- [Yieldmo](#Yieldmo)
- [ZafulAffiliate](#ZafulAffiliate)
- [Zefir](#Zefir)
- [Zip](#Zip)
## Adabra
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://track.adabra.com/sbn_fingerprint.v1.16.47.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        this.options = this.extend(t, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };
```
2. Sends computed fingerprint back to server
```
Request URL: https://track.adabra.com/log?tit=www.gioiapura.it%2FOfferte%20su%20Orologi%20e%20Gioielli%20delle%20Migliori%20Marche%3A%20gioielleria%20online%20Gioiapura&_viewts=1553539057&pguri=https%3A%2F%2Fwww.gioiapura.it%2F&_usrc=7431f35392f1f144&_usrccts=1553539050&fp2=********&idp=110&pgty=101&az=RV&ec_lng=it&cli_ctlg=32&sl_qty=1&idrcctx=1350&__adbraud=110||115,129,594,596,1897,1936,1939,3441,3572|ca310d19-1405-4ca7-a9a9-5fe87a521194|374,381,421,1080,1199,1268,1281
```
[Go back to top](#tracker-descriptions)

## Adbot
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://learning.adbot.tw/js/fingerprint2.min.js?_=1549428431957`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var Fingerprint2 = function(options) {
        if (!(this instanceof Fingerprint2)) {
            return new Fingerprint2(options)
        }
        var defaultOptions = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: true,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(options, defaultOptions);
        this.nativeForEach = Array.prototype.forEach;
        this.nativeMap = Array.prototype.map
    };
```
[Go back to top](#tracker-descriptions)

## Adbrain
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review

Adbrain's Privacy Policy States: 

`https://www.thetradedesk.com/general/privacy`

>Our AdBrain product, which is part of our Platform, uses data to produce a mapping of devices that might be related to each other, meaning that they might be used by the same person or by people within the same household. This helps advertisers better target and measure their campaigns, as well as limiting the number of times the same person or household sees an ad. 

>Cross device graphing: We may use data and algorithms to associate devices that might be related to each other, such as devices used by the same person or in the same household. 

>Some of the ways the Platform collects data include: using cookies and pixels 

>The Platform processes data both on our behalf and on behalf of clients and partners for advertising purposes such as: associating devices that might be related to each other

Adbrain's website states: 

`www.adbrain.com`

>Retargeting: Turn on cross-device targeting to reach your audience everywhere — from desktop computers and mobile devices to in-app, mobile web, and across browsers.

>Adbrain empowers you to solve for this fragmentation by unifying varied quality data sources so that you can focus on targeting the person, not just their device. 

>Adbrain uses machine learning algorithms to contextualize unstructured data points across devices, people, and households – achieving both broad coverage and a clear view of your target audience’s behavior. With a multidimensional approach to identity, it’s easier than ever to compare patterns across people, places, and things. 


[Go back to top](#tracker-descriptions)

## AdCash
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ufpcdn.com/cdn-cgi/bm/cv/2172558837/api.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "40px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Wfu\",179,115]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"b@)b@\",118,160]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "100px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"fW(i\",147,287]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"qGb))\",165,130]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## AdGainerSolutions
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://adgainersolutions.com/adgainer/tracking/fp.min.js?v=201708290`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(e) {
        var t = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i]
        };
        this.options = this.extend(e, t), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server
```
    (new Fingerprint2).get(function(n, r) {
        if (i = i + "&device_id=" + n + "&t=" + (new Date).getTime(), "undefined" != typeof ga && ga(function() {
                i = i + "&ga_client_id=" + ga.getAll()[0].get("clientId") + "&ga_tracking_id=" + Object.keys(gaData)[0]
            }), "undefined" != typeof vis_data)
            for (var o in vis_data) i = i + "&vwo_" + o + "=" + vis_data[o];
        var s = function(e) {
            for (var t = [], i = 0; i < e.scripts.length; i++) t.push('<script type="text/javascript" async src="' + e.scripts[i].script + '" />');
            jQuery("#tagManager_DIV").html(t.join(""))
        };
        if (window.XDomainRequest) {
            var l = new XDomainRequest;
            l.open("get", e + "incomingdata/tagManager?campaign_id=" + t + "&vars=" + i + "&referrer=" + a), l.send(), l.onload = function() {
                var e = $.parseJSON(l.responseText);
                null != e && void 0 !== e && s(e)
            }
        } else jQuery.support.cors = !0, jQuery.post(e + "incomingdata/tagManager", {
            campaign_id: t,
            vars: i,
            referrer: a
        }, s, "json")
    })

```
[Go back to top](#tracker-descriptions)

## Adjust
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Adjust's privacy policy States:

`https://www.adjust.com/terms/privacy-policy/`

>Processing of data through the Adjust Technology: We provide mobile analytics and attribution services to mobile app providers (our “Customers”). In connection with these services, we may process certain data from the users of these mobile apps (collectively the “End User” or “You”), as further described hereafter. 
Our SDK and APIs (collectively the “Adjust technology”) may process some of the following data from You as the End User: 
>- hashed IP address 
>- Mobile identifiers such as the ID for Advertising for iOS (IDFA), Google Advertising ID or similar mobile identifiers 
>-  Installation and first opening of an app on Your mobile device 
>-  Your interactions within an app (e.g. in-app purchases, registration) 
>-  Information regarding which advertisements You have seen or clicked on 
>-  For the Unbotify/Fraud product additionally: sensory data including touch events, counting text changes, accelerometer, gyroscope, battery, light sensor, device hardware specifications and operating system version

Adjust's website states: 

`https://www.adjust.com/product-updates/web-sdk-and-cross-device-tracking-measurement-beyond-the-app/`

>We’re happy to announce enhanced support for cross-device tracking features, strengthening our offering of measurement beyond the app. In combination with Adjust’s mobile SDK, cross-device tracking has been made possible and enables our clients to fill in the gaps with their overall marketing efforts.  
  
>Adjust’s Web SDK allows clients to track installs, sessions and events that occur in web apps, or on a web page, enabling marketers to track a campaign from the first ad view to a landing page, and then to events - whether they occur on desktop or the mobile web.  
  
>Moving towards to cross-device tracking - Now, in combination with Adjust’s mobile SDK, our clients have the ability to implement cross-device tracking via their own BI system. Cross-device tracking works by matching activity across different devices to the same user who performs them by utilizing shared identifiers, such as sign-in data, that are in use on each user’s device.


[Go back to top](#tracker-descriptions)

## AdMaven
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://d2fbkzyicji7c4.cloudfront.net/?zkbfd=691740`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            wa.T(va, function() {
                try {
                    var a = new window.Fingerprint2.FP2Options;
                    a.exclude.PixelRatio = !0;
                    a.exclude.AdBlock = !0;
                    a.extendedJsFonts = !0;
                    (new window.Fingerprint2(a)).get()
                } catch (b) {
                    J(B.m,
                        "fp2: " + b)
                }
            })

```
[Go back to top](#tracker-descriptions)

## Admicro
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
1. admicro fingerprints by using several fingerprinting techniques like canvas/font and webrtc
```
window.IP_ADDRESS = {}; localIP = []; i = 0; (function (b) {
            try {
                var d = function (d) { var c = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/.exec(d); null != c && (d = c[1]); void 0 === a[d] && b(d); a[d] = !0 }, a = {}; var c = window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection; if (!c) { var p = iframe.contentWindow; c = p.RTCPeerConnection || p.mozRTCPeerConnection || p.webkitRTCPeerConnection } var l = new c({ iceServers: [{ urls: "stun:stun.services.mozilla.com" }] }, { optional: [{ RtpDataChannels: !0 }] });
                l.onicecandidate = function (a) { a.candidate && d(a.candidate.candidate) }; l.createDataChannel(""); l.createOffer(function (a) { l.setLocalDescription(a, function () { }, function () { }) }, function () { }); setTimeout(function () { l.localDescription.sdp.split("\n").forEach(function (a) { 0 === a.indexOf("a=candidate:") && d(a) }) }, 1E3)
            } catch (q) { console.log("ERROR" + q.message) }
        }
```
```
c.prototype.getCanvas = function () {
        try {
            var b = document.createElement("canvas"), d = b.getContext("2d"); d.textBaseline = "top"; d.font =
                "14px 'Arial'"; d.textBaseline = "alphabetic"; d.fillStyle = "#f60"; d.fillRect(125, 1, 62, 20); d.fillStyle = "#069"; d.fillText("http://admicro.vn/", 2, 15); d.fillStyle = "rgba(102, 204, 0, 0.7)"; d.fillText("http://admicro.vn/", 4, 17); return this.md5(b.toDataURL())
        } catch (a) { return "Unknown" }
    }
```
[Go back to top](#tracker-descriptions)

## Adnium
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://a.montwam.top/static?r=1847068&id=665&pid=18&sid=36&tid=1&w=300&h=250`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        this.options = this.extend(t, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };


```
2. Sends computed fingerprint back to server
```
        a = {
            pre: function() {
                return e.adnLoaded = o.def(e.adnLoaded) ? [] : e.adnLoaded, -1 !== e.adnLoaded.indexOf(n.zone) ? !1 : (e.adnLoaded.push(n.zone), !0)
            },
            init: function() {
                return n.parent = o.isParent(), n.script = t.getElementById("adn-" + n.zone), null !== n.script && o.visible(n.script) ? this.frame() : !1
            },
            src: function() {
                var e = n.host + "/loader?a=" + n.zone,
                    t = o.url(!0),
                    a = encodeURIComponent(o.title()),
                    r = ["v=2", "t=" + n.type, "s=" + n.site, "p=" + n.pub, "if=" + n.parent, "fp=" + n.print, "adb=" + i.getAdBlock()];
                return 0 !== t.length && r.push("url=" + t), 0 !== a.length && r.push("title=" + a), n.extra.forEach(function(e) {
                    var t = o.safe(e);
                    t = t && 0 !== t.length ? r.push(t) : ""
                }), e += "&" + r.join("&")
            },
            frame: function() {
                var e = n.script.parentNode,
                    i = t.createElement("iframe");
                if (null === e) return !1;
                if (i.src = this.src(), i.width = n.width, i.height = n.height, i.scrolling = "no", i.style.cssText = "border:0;display:block;", i.sandbox = "allow-popups allow-scripts allow-same-origin allow-forms", i.setAttribute("data-zone", n.zone), "SCRIPT" === n.script.nodeName) {
                    for (var o = e.childNodes, a = 0; a < o.length; a++) "SCRIPT" === o[a].nodeName && -1 !== o[a].innerHTML.indexOf("adn") && -1 !== o[a].innerHTML.indexOf("id=" + n.zone) && e.removeChild(o[a]);
                    try {
                        e.removeChild(t.currentScript)
                    } catch (r) {}
                    return e.appendChild(i), !1
                }
                n.script.appendChild(i)
            }
        };

```

[Go back to top](#tracker-descriptions)

## Adobe
This service has been classified as `Email`, `Content`, `Advertising`, `EmailStrict` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Adobe's privacy policy States:

`https://www.adobe.com/privacy/cookies.html`

>Technologies similar to cookies - There are other technologies that can be used for similar purposes, such as HTML5 Local Storage and local shared objects (LSOs). LSOs are used by the authors of files that are read by Adobe® Flash® Player and the websites hosting those files (learn more about Flash Player and LSOs). We may use HTML5 Local Storage, LSOs, and similar technologies for authenticating you, keeping track of information you have provided to us, and remembering your preferences (see bullet points above). When you are using an Adobe application offline, we may store information related to how you used that website on your device and then transfer it to our servers the next time you connect online to our service. 
  
>Web beacons and embedded scripts - Web beacons and embedded scripts are other technologies that we use in our websites, as well as in some of our emails and ads. Web beacons (or “tags”) are bits of programming code included in web pages, emails, and ads that notify Adobe (or the companies that help us run our business) when those web pages, emails, or ads have been viewed or clicked on. Embedded scripts are bits of programming code included within some of our web pages that measure how you use those web pages, such as which links you click. We use this information to improve our websites, tailor our websites to your likely interests, conduct market research, and for anti-fraud monitoring purposes. 

Adobe's website states: 

`https://docs.adobe.com/content/help/en/device-co-op/using/about/overview.html`

>The Experience Cloud Device Co-op empowers participating brands to recognize their consumers so they can deliver more personalized experiences across devices and apps at massive scale…The Device Co-op allows participants to provide their consumers with a better, more consistent content experience as they migrate across devices. It does this by establishing links between a group of devices used by unknown consumers. This technology helps marketers understand and respond to consumer behaviors across devices.  

>Retargeting Across Devices: Reach your consumers via the power of retargeting unlocked across the mobiles, tablets, browsers, and other devices they use everyday. Advertising is dramatically more effective if you can stay front of mind, and cross device retargeting allows your brand to do exactly that.


[Go back to top](#tracker-descriptions)

## AdScore
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
```
        k = function() {
            try {
                var c = A(),
                    d = document.createElement("canvas");
                d.width = 200;
                d.height = 200;
                var b = d.getContext("2d");
                b.beginPath();
                b.rect(0, 0, 200, 200);
                b.fillStyle = "black";
                b.fill();
                var g = d.toDataURL();
                b.beginPath();
                b.rect(0, 0, 200, 200);
                b.fillStyle = "white";
                b.fill();
                var e = d.toDataURL(),
                    p = b.createLinearGradient(0, 0, 200, 0);
                p.addColorStop(0, "blue");
                p.addColorStop(1, "white");
                b.fillStyle = p;
                b.fillRect(0, 0, 200, 200);
                b.rotate(1 * Math.PI / 180);
                b.font = "14px 'Arial'";
                b.textBaseline = "alphabetic";
                b.fillStyle = "#f60";
                b.fillRect(0, 15, 200, 15);
                b.beginPath();
                b.moveTo(0, 0);
                b.quadraticCurveTo(50, 150, 180, 180);
                b.bezierCurveTo(190, -40, 100, 50, 100, 50);
                b.lineTo(30, 10);
                b.lineWidth = 1;
                b.strokeStyle = "#222222";
                b.stroke();
                b.fillStyle = "#069";
                b.fillText("mmiillII,)#!>\u26c4\u26c7\u12b9\u102a\u07f7\u058e\u17d8",
                    2, 15);
                b.fillStyle = "rgba(102,204,0,0.7)";
                b.fillText("mmiillII,)#!>\u26c4\u26c7\u12b9\u102a\u07f7\u058e\u17d8", 4, 17);
                p = d.toDataURL();
                A();
                f = A() - c;
                A();
                p = B(p.substr(p.length - 100));
                bt = B(g.substr(g.length - 100) + e.substr(e.length - 100)).substr(0, 8);
                A();
                c = [];
                c.push(bt);
                c.push(p);
                c.push("");
                c.push("");
                return c
            } catch (G) {
                return ""
            }
        }();
```
[Go back to top](#tracker-descriptions)

## Adstune
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://adstune.com/cdn-cgi/bm/cv/2172558837/api.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "100px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"&M\",90,155]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\":F\\\\\\\\$\",53,78]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"-<E\",179,179]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## AdxSpace
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.00px.net/static/space.min.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "13pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Sphinx of black quartz, judge my vow 🐼😄\",2,20]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.23456789)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Sphinx of black quartz, judge my vow 🐼😄\",4,22]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,125,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(125,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## AdYouLike
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.pulpix.com/static/pulpix.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
("Fingerprint2", this, function() {
        "use strict";
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            var r = {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            };
            this.options = this.extend(t, r), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
{
                    key: "_computeTrackingEvent",
                    value: function(e, r) {
                        r.name = e;
                        var o = new A(r),
                            a = Object.assign({
                                timestamp: (new Date).toISOString(),
                                ab_test: t.chosenVariations,
                                visitor_id: l.visitorId,
                                session_id: l.sessionId,
                                visitor_fingerprint: l.visitorFingerprint,
                                visitor_random_id: l.visitorRandomId,
                                document_referrer: window.document.referrer || void 0,
                                device_orientation: p(),
                                has_adblock: i(),
                                is_tab_active: n.isTabActive(),
                                is_visitor_active: f(),
                                device_type: n.isMobile() ? "mobile" : "desktop",
                                canonical_url: n.getCanonicalUrl()
                            }, n.removeUndefinedKeys(o));
                        return new s(a)
                    }
                }

```

[Go back to top](#tracker-descriptions)

## AivaLabs
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://aivalabs.com/cta/?identity=QtBHuIKbz7dQys5LY2dm0u4SiTppOAeMefE/JyIcTGlKg1zbgwTL.&shop=g-floor.myshopify.com`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
                function a() {
                    e.printInfo("Socket connected");
                    var t = this;
                    (new Fingerprint2).get(function(e, a) {
                        t.emit("connected", {
                            clientEmail: Aiva.ExportData.clientEmail,
                            fingerprint: e,
                            currentSite: window.location.href,
                            timezone: Aiva.ExportData.timezone
                        })
                    })
                }

```
2. Sends computed fingerprint back to server
```
this.sendAnalytics = function(n) {
            var r = t.getIdentityString(n),
                i = t.getAnalytics(r);
            if (!a.isBot() && !Aiva.ExportData.isPreview) {
                var r = t.getIdentityString(n),
                    s = t.numberOfTiles(n),
                    i = t.getAnalytics(r),
                    o = Aiva.Parameters.Socket;
                Aiva.Constants.DebugMode && e.printInfo(i.data), o.emit("analytics", i.data, s)
            }
        }

```

[Go back to top](#tracker-descriptions)

## a.js
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Observered on: http://telecomsource.net
- CPU utilization
    - Baseline load: 515.77%
    - Cryptomining script blocked: 14.21%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://telecomsource.net",
        "isBlockingMiners": false,
        "miners": [
            "zymerget.bid"
        ],
        "miner_requests": [
            "https://zymerget.bid/004U7k/WyJOaWNvbGw4MDMiLDQsMC40LDAsIjEwMCUiXQ.xab7rZEvIDAC1wkHggEujSmVWlg.empty.html",
            "https://zymerget.bid/004U7k/WyJOaWNvbGw4MDMiLDQsMC40LDAsIjEwMCUiXQ.xab7rZEvIDAC1wkHggEujSmVWlg.min.js",
            "https://zymerget.bid/004U7k/w.js"
        ],
        "run_stats": {
            "cpu": 515.7668845315904,
            "memory": "650.8 MB"
        },
        "workers_created": [
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae",
            "blob:https://zymerget.bid/41cbf39d-34eb-4514-aa6a-e1f6359aa5ae"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://telecomsource.net",
        "isBlockingMiners": true,
        "miners": [
            "zymerget.bid"
        ],
        "miner_requests": [
            "https://zymerget.bid/004U7k/WyJOaWNvbGw4MDMiLDQsMC40LDAsIjEwMCUiXQ.xab7rZEvIDAC1wkHggEujSmVWlg.empty.html"
        ],
        "run_stats": {
            "cpu": 14.214015151515152,
            "memory": "456.6 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## Albacross
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Albacross’ privacy policy states:

`https://albacross.com/privacy-policy/`

>The data processed is the IP-address from which you visited our customer´s website, and technical information that enables us to tell different visitors apart that are originating from the same IP-address (cookies). In some cases, the IP-address and the company it is matched with may constitute personal data – for instance when it comes to sole traders – as it would allow for the identification of the visitor.

[Go back to top](#tracker-descriptions)

## AppCast
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Appcast’s privacy policy states:  
`https://www.appcast.io/privacy-policy/`  
 
>To provide the Service, we collect certain information from job applicants using automated means, such as cookies and web beacons, when they click on an Appcast-sponsored job ad at third party websites… 
> 
>The information we collect in this manner includes IP address, browser type, device type, operating system, referring URLs, dates and times of site visits, and predictive demographic information… 
> 
>We may also enable third parties to use cookies, web beacons, and ID syncing to collect information when you click on an Appcast-powered job ad at third party websites." 

[Go back to top](#tracker-descriptions)

## AuditedMedia
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Policy Review
1. https://auditedmedia.com/ 
### Technical Review
1. Script uses canvas/font to fingerprint users and sends calculated fingerprint id and other properties back to Audited Media
```
10: [function(g, u, p) {
        (function() {
            var d = g("../lib_managed/lodash");
            g("./helpers");
            var b = g("murmurhash").v3
              , c = g("browser-cookie-lite")
              , a = "undefined" !== typeof p ? p : this
              , l = window
              , h = navigator
              , q = screen
              , u = document;
            a.hasSessionStorage = function() {
                try {
                    return !!l.sessionStorage
                } catch (f) {
                    return !0
                }
            }
            ;
            a.hasLocalStorage = function() {
                try {
                    return !!l.localStorage
                } catch (f) {
                    return !0
                }
            }
            ;
            a.localStorageAccessible = function() {
                if (!a.hasLocalStorage())
                    return !1;
                try {
                    return l.localStorage.setItem("modernizr", "modernizr"),
                    l.localStorage.removeItem("modernizr"),
                    !0
                } catch (f) {
                    return !1
                }
            }
            ;
            a.hasCookies = function(a) {
                a = a || "testcookie";
                return d.isUndefined(h.cookieEnabled) ? (c.cookie(a, "1"),
                "1" === c.cookie(a) ? "1" : "0") : h.cookieEnabled ? "1" : "0"
            }
            ;
            a.isCanvasSupported = function() {
                var a = document.createElement("canvas");
                return !(!a.getContext || !a.getContext("2d"))
            }
            ;
            a.getCanvasFp = function() {
                var a = []
                  , c = document.createElement("canvas");
                c.width = 2E3;
                c.height = 200;
                c.style.display = "inline";
                var b = c.getContext("2d");
                b.rect(0, 0, 10, 10);
                b.rect(2, 2, 6, 6);
                a.push("canvas winding:" + (!1 === b.isPointInPath(5, 5, "evenodd") ? "yes" : "no"));
                b.textBaseline = "alphabetic";
                b.fillStyle = "#f60";
                b.fillRect(125, 1, 62, 20);
                b.fillStyle = "#069";
                b.fillText("Cwm fjordbank glyphs vext quiz, \ud83d\ude03", 2, 15);
                b.fillStyle = "rgba(102, 204, 0, 0.7)";
                b.font = "18pt Arial";
                b.fillText("Cwm fjordbank glyphs vext quiz, \ud83d\ude03", 4, 45);
                b.globalCompositeOperation = "multiply";
                b.fillStyle = "rgb(255,0,255)";
                b.beginPath();
                b.arc(50, 50, 50, 0, 2 * Math.PI, !0);
                b.closePath();
                b.fill();
                b.fillStyle = "rgb(0,255,255)";
                b.beginPath();
                b.arc(100, 50, 50, 0, 2 * Math.PI, !0);
                b.closePath();
                b.fill();
                b.fillStyle = "rgb(255,255,0)";
                b.beginPath();
                b.arc(75, 100, 50, 0, 2 * Math.PI, !0);
                b.closePath();
                b.fill();
                b.fillStyle = "rgb(255,0,255)";
                b.arc(75, 75, 75, 0, 2 * Math.PI, !0);
                b.arc(75, 75, 25, 0, 2 * Math.PI, !0);
                b.fill("evenodd");
                a.push("canvas fp:" + c.toDataURL());
                return a.join("~")
            }
            ;
            a.detectSignature = function(f) {
                var d = a.isCanvasSupported() ? a.getCanvasFp() : ""
                  , m = "" != c.cookie("__utma") ? c.cookie("__utma") : c.cookie("_ga");
                d = [h.userAgent, [q.height, q.width, q.colorDepth].join("x"), (new Date).getTimezoneOffset(), a.hasSessionStorage(), a.hasLocalStorage(), d, m];
                m = [];
                if (h.plugins)
                    for (var l = 0; l < h.plugins.length; l++) {
                        for (var g = [], p = 0; p < h.plugins[l].length; p++)
                            g.push([h.plugins[l][p].type, h.plugins[l][p].suffixes]);
                        m.push([h.plugins[l].name + "::" + h.plugins[l].description, g.join("~")])
                    }
                return b(d.join("###") + "###" + m.sort().join(";"), f)
            }
            ;
            a.detectTimezone = function() {
                return ""
            }
            ;
            a.detectViewport = function() {
                var a = l
                  , b = "inner";
                "innerWidth"in l || (b = "client",
                a = u.documentElement || u.body);
                return a[b + "Width"] + "x" + a[b + "Height"]
            }
            ;
            a.detectDocumentSize = function() {
                var a = u.documentElement
                  , b = Math.max(a.clientWidth, a.offsetWidth, a.scrollWidth);
                a = Math.max(a.clientHeight, a.offsetHeight, a.scrollHeight);
                return isNaN(b) || isNaN(a) ? "" : b + "x" + a
            }
            ;
            a.detectBrowserFeatures = function(b) {
                var f, m = {
                    pdf: "application/pdf",
                    qt: "video/quicktime",
                    realp: "audio/x-pn-realaudio-plugin",
                    wma: "application/x-mplayer2",
                    dir: "application/x-director",
                    fla: "application/x-shockwave-flash",
                    java: "application/x-java-vm",
                    gears: "application/x-googlegears",
                    ag: "application/x-silverlight"
                }, g = {};
                if (h.mimeTypes && h.mimeTypes.length)
                    for (f in m)
                        if (Object.prototype.hasOwnProperty.call(m, f)) {
                            var p = h.mimeTypes[m[f]];
                            g[f] = p && p.enabledPlugin ? "1" : "0"
                        }
                g.inpriv = "" != c.cookie("privAu") ? c.cookie("privAu") : 0;
                g.abd = "" != c.cookie("abdAu") ? c.cookie("abdAu") : 0;
                "unknown" !== typeof h.javaEnabled && !d.isUndefined(h.javaEnabled) && h.javaEnabled() && (g.java = "1");
                d.isFunction(l.GearsFactory) && (g.gears = "1");
                g.res = q.width + "x" + q.height;
                g.cd = q.colorDepth;
                g.cookie = a.hasCookies(b);
                return g
            }
        }
        )()
    }
```
[Go back to top](#tracker-descriptions)

## Augur
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Policy Review
1. Augur claims that they track users via devices, not through cookies. - `https://www.mediapost.com/publications/article/166916/bluecava-touts-device-fingerprinting.html`

> A set of APIs and tools that instantly enables businesses to recognize devices, and consumers across devices. - `https://www.augur.io/#landingPage`

> Cookie-less tracking - Instead of cookies (which cause mis-attribution), Augur uses CAKE, a multi-layer recognition architecture.

2. Augur claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://www.augur.io/privacypolicy`

> To deliver the Augur Services, our software collects, organizes, and uses Non-PII. This information includes, the date and time of visits to a Client Property, browser information (e.g., browser type, font signature), operating system information (e.g. screen resolution), IP addresses, non-precise geographic information ( e.g. time zone, city, state, country), battery level, and user agent


[Go back to top](#tracker-descriptions)

## AvantLink
This service has been classified as `Analytics`, `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Avantlink's Privacy Policy States:

`https://www.avantlink.com/privacy-policy/`

>In connection with use of our Network, and the availability of links through our Network, we may automatically collect information such as a device’s IP address or mobile device ID, browsing activity and similar information which indicates how a user has interacted with our Network, Affiliates or Merchants.

Avantlink's website states:

`http://blog.avantlink.com/arches/`

>Advanced Tracking:
>- Cross-Device 
>- More Attribution Roles for AvantMetrics 
>-  Additional Insight into the Customer’s Path to Purchase

[Go back to top](#tracker-descriptions)

## Awin
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Awin's privacy policy States:

`https://www.awin.com/us/privacy#how-do-we-collect-data-from-end-users`

>How do we collect data from end users? 
>- Fingerprinting: This is a method by which Awin can uniquely identify a device by considering certain attributes of the browser or the device (incl. screen size/resolution and user configurations).

[Go back to top](#tracker-descriptions)

## Azet
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://rsz.sk/delivery/sd3.php`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
function getFp() {
    akFp = getCk('OAFP'); if (akFp === '' && typeof Fingerprint2 !== 'undefined') { new Fingerprint2().get(function (result) { setCk('OAFP', result, 1); akFp = result; var akFpImg = new Image(1, 1); akFpImg.style.display = 'none'; akFpImg.src = '//rsz.sk/delivery/sd3.php?fp=' + akFp; document.body.appendChild(akFpImg); /*console.log('akFpNew', akFp);*/ }); } else { /*console.log('akFpOld', akFp);*/ }
    var akImg = new Image(1, 1); akImg.style.display = 'none'; akImg.src = 'https://azetklik.sk/delivery/v2/set?id=5fdf6dd9302cf57f609d6be26de85107&fp=' + akFp; document.body.appendChild(akImg);
}

```
[Go back to top](#tracker-descriptions)

## BetssonPalantir
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://amonsul.betssonpalantir.com/amonsul-receiver.js?v=1540819800000`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            var t = {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            };
```
2. Sends computed fingerprint back to server
```
   function __AmonsulSender(e) {
    function t() {
        return location.protocol == "https:"
    }

    function n() {
        return t() ? "https://" + e : "http://" + e
    }

    function r(e) {
        var t = s("__amonsulfp");
        !t || t == undefined ? (new Fingerprint2).get(function(t) {
            o("__amonsulfp", t, 7300), e(t)
        }) : e(t)
    }

    function i() {
        var e = s("__amonsulid");
        if (!e || e == undefined) e = Math.uuid();
        return o("__amonsulid", e, 7300), e
    }

    function s(e) {
        var t = e + "=",
            n = document.cookie.split(";");
        for (var r = 0; r < n.length; r++) {
            var i = n[r];
            while (i.charAt(0) == " ") i = i.substring(1);
            if (i.indexOf(t) == 0) return i.substring(t.length, i.length)
        }
        return ""
    }

    function o(e, t, n) {
        var r = new Date;
        n = n || 365, r.setTime(r.getTime() + n * 24 * 60 * 60 * 1e3);
        var i = "expires=" + r.toUTCString();
        document.cookie = e + "=" + t + "; " + i
    }

    function u(e) {
        var t = e || {};
        t.uuid = i();
        var n, r = new Date,
            s = Math.round(r.getTime() / 1e3),
            o = "&r=" + String(Math.random()).slice(2, 8) + "&h=" + r.getHours() + "&m=" + r.getMinutes() + "&s=" + r.getSeconds() + "&_idts=" + s;
        o += "&fp=" + encodeURIComponent(e.fingerprint);
        for (n in t) Object.prototype.hasOwnProperty.call(t, n) && !a(t[n]) && (o += "&" + n + "=" + t[n]);
        return o
    }

    function a(e) {
        return e == null || e.length === 0
    }

    function f(e, t, n) {
        var r = window.XMLHttpRequest ? new window.XMLHttpRequest : window.ActiveXObject ? new window.ActiveXObject("Microsoft.XMLHTTP") : null;
        r.open("POST", e, !0), r.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"), r.onreadystatechange = function() {
            4 == r.readyState && (typeof n == "function" && n(req), r = null)
        }, r.send(t)
    }

    function l(e, t, n, r, s, o) {
        return "ec=" + encodeURIComponent(n) + "&ea=" + encodeURIComponent(r) + "&el=" + encodeURIComponent(s) + "&uid=" + encodeURIComponent(e) + "&vid=" + encodeURIComponent(i()) + "&fp=" + encodeURIComponent(t) + "&data=" + encodeURIComponent(o)
    }
    var e = e || "";
    this.getVersion = function() {
        return "0.1-pre"
    }, this.logEventMessage = function(e, t, i, s, o) {
        r(function(r) {
            var u = l(e, r, t, i, s, o);
            f(n() + "/event", u)
        })
    }, this.logRawMessage = function(e) {
        r(function(t) {
            e.fingerprint = t;
            var r = u(e);
            f(n() + "/track", r)
        })
    }, this.getTrackingInfo = function(e) {
        r(function(t) {
            var n = {};
            n.fingerprint = t, n.amonsulid = i(), e(n)
        });
        return
    }
}
```

[Go back to top](#tracker-descriptions)

## BigClick
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://bgclck.me/lhzbsrfkjf/js/545?r=&3845`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        function initFingerprint() {
            Fingerprint2.get(function(e) {
                fingerprint_hash = Fingerprint2.x64hash128(e.map(function(e) {
                    return e.value
                }).join(), 31);
                var t = {};
                for (i = 0; i < e.length; i++) {
                    var r = e[i].key;
                    "canvas" !== r && "webgl" !== r && (null != lies[r] && (lies[r].value = e[i].value - 0), t[r] = e[i].value)
                }
                fingerprint_json = JSON.stringify(t)
            })
        }
        hasFingerprint() && window.requestIdleCallback ? requestIdleCallback(initFingerprint) : hasFingerprint() && setTimeout(initFingerprint, 500)

```
2. Sends computed fingerprint back to server
```
            var _ = new("onload" in new XMLHttpRequest ? XMLHttpRequest : XDomainRequest),
                u = "keys=" + encodeURIComponent(e.join("|||"));
            "" !== fingerprint_hash && (u = u + "&fingerprint_hash=" + encodeURIComponent(fingerprint_hash) + "&fingerprint_json=" + encodeURIComponent(fingerprint_json)), _.open("POST", url + "/view", !0), _.setRequestHeader("Content-type", "application/x-www-form-urlencoded"), _.send(u)

```

[Go back to top](#tracker-descriptions)

## Bisnode
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Bisnode’s privacy policy states: 
 
`https://www.bisnode.com/privacy/personal_data/data-we-collect/`
 
What data do we collect about you? 
 
>•Consumer interest and buying behavior. Statistical variables 

>•Electronic localization data. GPS location, mobile phone 

>•Electronic identification data. IP-address and cookies from your visits to our sites

[Go back to top](#tracker-descriptions)

## BitMedia
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ad.bitmedia.io/js/adbybm.js/5b58f88917356f00108024d8`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        getCanvasFp: function() {
            var e = document.createElement("canvas"),
                t = e.getContext("2d"),
                o = "Cwm fjordbank glyphs vext quiz, https://github.com/valve á½ ";
            return t.textBaseline = "top", t.font = "70px 'Arial'", t.textBaseline = "alphabetic", t.fillStyle = "#f60", t.fillRect(125, 1, 62, 20), t.fillStyle = "#069", t.fillText(o, 2, 15), t.fillStyle = "rgba(102, 204, 0, 0.7)", t.fillText(o, 4, 17), e.toDataURL()
        },

```
2. Sends computed fingerprint back to server
```
        s = function(e) {
            var t = e.displayHost + "p/" + e.adBlockId + "/?source=" + encodeURIComponent(e.sourceURL) + "&ref=" + encodeURIComponent(e.sourceRef) + "&ent=" + bmblocks.idEntropy + "&we=" + bmblocks.we + "&fid=" + bmblocks.fid + "&fidnoua=" + bmblocks.fidnoua + "&impid=" + bmblocks.impUuid + "&ua=" + encodeURIComponent(e.userAgent) + "&sig=0x00000&blocksubid=" + e.blockSubId,
                o = bmblocks[e.adBlockId][e.blockSubId],
                n = document.getElementsByClassName(e.blockClass)[o];
            if (function(e) {
                    for (var t = e.getBoundingClientRect(), o = t.left; o < t.right; o += 15)
                        for (var n = t.top; n < t.bottom; n += 15) {
                            var i = document.elementFromPoint(o, n);
                            if (null != i && i != e) return !0
                        }
                    return !1
                }(n)) {
                var i = e.displayHost + "pb/" + e.publId + "/" + e.adBlockId + "?type=overlapping&fid=" + bmblocks.fid + "&fidnoua=" + bmblocks.fidnoua + "&ref=" + encodeURIComponent(e.sourceRef) + "&impid=" + bmblocks.impUuid;
                p(i)
            }
            var a = document.createElement("iframe");
            a.setAttribute("src", t), a.setAttribute("class", e.iframeClass), a.setAttribute("scrolling", "no"), a.style.border = "none", a.style.width = n.style.width, a.style.height = n.style.height, e.adWidth = n.style.width, e.adHeight = n.style.height, n.appendChild(a)
        }

```

[Go back to top](#tracker-descriptions)

## BlueCava
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Policy Review
1. BlueCava says that the newest version of its device-fingerprinting technology doesn't require installing cookies on users' computers. Instead, the company recognizes the unique characteristics of users' computers and then compiles information about those people's Web-surfing activity. - `https://www.mediapost.com/publications/article/166916/bluecava-touts-device-fingerprinting.html`

> Says David Norris, CEO of BlueCava, “Once we’ve identified a device, we can provide information about that device’s history so a business can decide how it wants to interact.” - `https://www.clickz.com/device-fingerprinting-firm-bluecava-makes-tracking-opt-outs-easier/46797/`

> You can reset the advertising ID we generate when we recognize your device. This will unlink your device from any of the data that has been accumulated and assigned to that ID. The effect is the same as if you had just gotten a new computer or phone. To reset your advertising ID click the button to the right. Note, that if you reset your advertising ID we will automatically apply the opt-out setting from the old ID to the new one when we create the new one, so if you have opted out above you won’t have to do that again. - `https://bluecava.com/`

2. Bluecava privacy policy states they use cookieless tracking and specifically states they profile installed fonts and "various other properties of a Screen" - `https://bluecava.com/privacy-policy`

> Qualia’s Platform enables our Clients to recognize Screens when their Users visit Sites. In order to do this, we collect information about User’s computers, mobile devices, tablets, and game consoles (“Screens”). The type of information collected via the Platform includes the type of Screen, IP address, browser version, time zone, the fonts installed, browser plug-ins and various other properties of a Screen. Qualia does not collect PII in connection with the Platform.
### Technical Review
1. Script uses canvas/font fingerprinting to fingerprint users

```
    test : function(name) {
      this.h.appendChild(this.d);
      /** @type {!Array} */
      var style = [];
      return style.name = this.s.style.fontFamily = name, style.width = this.s.offsetWidth, style.height = this.s.offsetHeight, this.h.removeChild(this.d), name = name.toLowerCase(), "serif" == name ? style.found = true : style.found = style.width != this.defaultWidth || style.height != this.defaultHeight, style;
    },
    getFontList : function(fonts) {
      this.init();
      /** @type {!Array} */
      var list = [];
      /** @type {number} */
      i = 0;
      for (; i < fonts.length; ++i) {
        if (this.test(fonts[i]).found) {
          list.push(i);
        }
      }
      return list;
    }
```

2. Script probes device properties to attempt to fingerprint users

```
    var init = function(stop) {
      if (c$jscomp$0.config.F.PDF) {
        set(c$jscomp$0.m.PDF);
      }
      if (c$jscomp$0.config.F.Ajax) {
        set(c$jscomp$0.m.Ajax);
      }
      if (c$jscomp$0.config.F.CPU) {
        set(c$jscomp$0.m.CPU);
      }
      if (c$jscomp$0.config.F.Timezone) {
        set(c$jscomp$0.m.Timezone);
      }
      if (c$jscomp$0.config.F.Gears) {
        set(c$jscomp$0.m.Gears);
      }
      if (c$jscomp$0.config.F.Languages) {
        set(c$jscomp$0.m.Languages);
      }
      if (c$jscomp$0.config.F.Plugins) {
        set(c$jscomp$0.m.Plugins);
      }
      if (c$jscomp$0.config.F.General) {
        set(c$jscomp$0.m.General);
      }
      if (c$jscomp$0.config.F.JSEngine) {
        set(c$jscomp$0.m.JSEngine);
      }
      if (c$jscomp$0.config.F.PDFReader) {
        set(c$jscomp$0.m.PDFReader);
      }
      if (c$jscomp$0.config.F.Silverlight) {
        set(c$jscomp$0.m.Silverlight);
      }
      if (c$jscomp$0.config.F.DotNet) {
        set(c$jscomp$0.m.DotNet);
      }
      if (c$jscomp$0.config.F.Display) {
        set(c$jscomp$0.m.Display);
      }
      if (c$jscomp$0.config.F.Fonts) {
        set(c$jscomp$0.m.Fonts);
      }
      if (c$jscomp$0.config.F.Fonts && c$jscomp$0.config.F.Flash) {
        c$jscomp$0.m.Flash(b, function() {
          stop();
        });
      } else {
        stop();
      }
```
[Go back to top](#tracker-descriptions)

## BlueKai
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Oracle's privacy policy states:

`https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html`

>Oracle can process information about you: 
>- For online interest-based advertising delivered through Oracle Data Cloud partners that display online advertising to you on behalf of Oracle Data Cloud customers…
>- via a connected device (due to an association between your IP address and device identifier)…
>- For linking Profiles and Interest Segments to enable Oracle Marketing & Data Cloud customers and partners to connect your Interest Segments across the various browsers and/or devices you may use. 

>Cookies and similar technologies (e.g., pixels tags and device identifiers) are used by Oracle and our advertising technology partners to recognize you and/or your device(s) on, off and across different services and devices

>Online information about you for linkage purposes (cross device/cross-context technology) is retained for up to 12 months.

Oracle’s website states:

`https://www.oracle.com/data-cloud/products/data-management-platform/cross-device.html`

>Visualize and Plan Campaigns Across Devices: The Oracle Data Management Platform’s Audience Builder puts the power of the Oracle ID Graph in the hands of marketers. The Audience Builder allows marketers to visualize linkages and build audiences across devices. With enhanced audience segmentation and delivery, Oracle DMP users now have even more options to define exactly who they want to analyze and target by selecting the device ID from the environment from which the data was collected. 

>- Analyze data across devices: define exactly who to target by the device ID source 
>- Match Devices to Consumers 
>- Map Consumer Purchase Path to Device: And deliver a consistent message across multiple devices


[Go back to top](#tracker-descriptions)

## BoostBox
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
```
      keys = this.userAgentKey(keys);
      keys = this.languageKey(keys);
      keys = this.colorDepthKey(keys);
      keys = this.deviceMemoryKey(keys);
      keys = this.pixelRatioKey(keys);
      keys = this.hardwareConcurrencyKey(keys);
      keys = this.screenResolutionKey(keys);
      keys = this.availableScreenResolutionKey(keys);
      keys = this.timezoneOffsetKey(keys);
      keys = this.sessionStorageKey(keys);
      keys = this.localStorageKey(keys);
      keys = this.indexedDbKey(keys);
      keys = this.addBehaviorKey(keys);
      keys = this.openDatabaseKey(keys);
      keys = this.cpuClassKey(keys);
      keys = this.platformKey(keys);
      keys = this.doNotTrackKey(keys);
      keys = this.pluginsKey(keys);
      keys = this.canvasKey(keys);
      keys = this.webglKey(keys);
      keys = this.webglVendorAndRendererKey(keys);
      keys = this.adBlockKey(keys);
      keys = this.hasLiedLanguagesKey(keys);
      keys = this.hasLiedResolutionKey(keys);
      keys = this.hasLiedOsKey(keys);
      keys = this.hasLiedBrowserKey(keys);
      keys = this.touchSupportKey(keys);
      keys = this.customEntropyFunction(keys);
```

```
    ge : function(value) {
      /** @type {string} */
      var ret = "";
      (new Fingerprint2({
        excludeDeviceMemory : true,
        excludeJsFonts : true,
        excludeFlashFonts : true,
        detectScreenOrientation : false,
        preprocessor : function(css, type) {
          return "user_agent" === css ? parse() : type;
        }
      })).get(function(a, canCreateDiscussions) {
        ret = $Flab.sha256.hxd(a);
      });
      return ret;
    }
```
[Go back to top](#tracker-descriptions)

## Bouncex
This service has been classified as `Advertising`, `EmailStrict` and `FingerprintingInvasive` for the following reasons:
### Policy Review
Bouncex's privacy policy States:

`https://www.bouncex.com/privacy/`

>As directed by our Clients, we process information such as hashed email addresses, cookie IDs, mobile advertising o/s IDs and other pseudonymous identifiers. We use this information to help us understand whether two devices are likely to be used by the same User or household. For example, where a User opens an email and we are able to place a cookie on that User’s browser, we may be to determine that this was the same User that had recently visited and logged into our Client’s website. Once we’ve established that linkage, we may use the information across Clients to enable Clients to onboard demographic data and other data onto profiles linked to those pseudonymous identifiers. This technology enables us to identify browsers and devices over time and across different websites via the Identify Platform. We also may enable Clients to leverage those pseudonymous identifiers to purchase advertising on digital media platforms. We are careful to segregate this data to ensure that neither Bounce Exchange nor our Clients are permitted to use information collected across non-affiliated Client sites and apps to personally identify and/or re-identify individual Users.  
  
>Our Platforms and our Services may utilize tracking technologies such as pixel tags, HTML5 cookies, HTTP cookies, web beacons, statistical identifiers, and mobile o/s advertising identifiers such as Apple’s IDFA, the Android Advertising ID and other pseudonymous information. Statistical identifiers are created when our systems read pseudonymous information about your computer or device, including the user agent, IP address, and the browser and operating system of your computer and device. Statistical identifiers enable our systems to determine within a reasonable level of certainty that they are encountering the same computer or device, including in environments where third-party cookies are not supported.

BounceX's website states: 

`https://www.bouncex.com/` (1)  

>Market to people, not cookies. Today’s consumer expects more than yesterday’s tech. Use BounceX to accurately recognize and market to the actual person behind every visit in real-time. (1)  

>We Know Your Users - Our proprietary tech identifies 40% of your anonymous traffic (on average) across all of their devices and sessions. (1)  

'https://www.bouncex.com/thinktank/publisherid/' (2)

>To truly “identify” a visitor, you need a first-party link to a device that can survive across browsers and sessions. That link will allow you to remember each visit the device makes to your site, thereby building an accurate view of the visitor’s affinities. To do this, bounceX’s identification product capitalizes on the massive network of websites that we serve. (2)

### Technical Review
Script: `https://assets.bounceexchange.com/assets/smart-tag/versioned/ijs_all_modules_cjs_min_ab1b3652f02ee26ed4e57a5cb243129f.js`
1. Script accesses several Javascript API calls known to invasively fingerprint users. Some examples (APIs captured using [OpenWPM](https://github.com/mozilla/OpenWPM)):
```json
{
  "top_level_url": "https://www.sears.com/",
  "script_url": "https://assets.bounceexchange.com/assets/smart-tag/versioned/ijs_all_modules_cjs_min_ab1b3652f02ee26ed4e57a5cb243129f.js",
  "script_line": "1",
  "symbol": "window.navigator.doNotTrack",
  "arguments": null,
  "value": "unspecified"
}
```
```json
{
  "top_level_url": "https://www.sears.com/",
  "script_url": "https://assets.bounceexchange.com/assets/smart-tag/versioned/ijs_all_modules_cjs_min_ab1b3652f02ee26ed4e57a5cb243129f.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "https://www.sears.com/",
  "script_url": "https://assets.bounceexchange.com/assets/smart-tag/versioned/ijs_all_modules_cjs_min_ab1b3652f02ee26ed4e57a5cb243129f.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "https://www.sears.com/",
  "script_url": "https://assets.bounceexchange.com/assets/smart-tag/versioned/ijs_all_modules_cjs_min_ab1b3652f02ee26ed4e57a5cb243129f.js",
  "script_line": "1",
  "symbol": "RTCPeerConnection.setLocalDescription",
  "arguments": "[\"{\\\"type\\\":\\\"offer\\\",\\\"sdp\\\":\\\"v=0\\\\r\\\\no=mozilla...THIS_IS_SDPARTA-78.0.1 XXXXX 0 IN IP4 0.0.0.0\\\\r\\\\ns=-\\\\r\\\\nt=0 0\\\\r\\\\na=fingerprint:sha-256 XXXXX\\\\r\\\\na=group:BUNDLE 0\\\\r\\\\na=ice-options:trickle\\\\r\\\\na=msid-semantic:WMS *\\\\r\\\\nm=application 9 UDP/DTLS/SCTP webrtc-datachannel\\\\r\\\\nc=IN IP4 0.0.0.0\\\\r\\\\na=sendrecv\\\\r\\\\na=ice-pwd:XXXXX\\\\r\\\\na=ice-ufrag:XXXXX\\\\r\\\\na=mid:0\\\\r\\\\na=setup:actpass\\\\r\\\\na=sctp-port:5000\\\\r\\\\na=max-message-size:1073741823\\\\r\\\\n\\\"}\"]",
  "value": ""
}
```
[Go back to top](#tracker-descriptions)

## Brandcrumb
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://static.brandcrumb.com/bc.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var b = function(a) {
            if (!(this instanceof b)) return new b(a);
            var c = {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            };
            this.options = this.extend(a, c), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server:
```
e.prototype.getFingerprint = function() {
        var a = this,
            b = new Fingerprint2;
        b.get(function(b, c) {
            var d = {};
            for (var e in c) d[c[e].key] = c[e].value;
            var h = {
                fingerprint: b,
                user_agent: d.user_agent,
                user_agent_hash: g(d, "user_agent"),
                regular_plugins: d.regular_plugins,
                regular_plugins_hash: g(d, "regular_plugins"),
                available_resolution_hash: g(d, "available_resolution"),
                has_lied_languages_hash: g(d, "has_lied_languages"),
                webgl_hash: g(d, "webgl"),
                canvas_hash: g(d, "canvas"),
                pixel_ratio_hash: g(d, "pixel_ratio"),
                canvas_webgl_hash: g(f(d, "canvas"), "webgl")
            };
            a.sendPixel(a.getUrl("dharma"), h)
        })
    }

```

[Go back to top](#tracker-descriptions)

## BreakTime
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://a.breaktime.com.tw/js/au.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
            key: "getBaseData",
            value: function() {
                return {
                    session_id: this.sessionId,
                    fp: this.fingerprint,
                    txn_id: this.txnId,
                    txn_id2: this.txnId2,
                    url: this.url,
                    url_canonical: this.urlCanonical,
                    url_og: this.urlOg,
                    url_pageid: this.urlPageId,
                    referrer: this.referrer,
                    device_type: this.deviceType,
                    spj: this.partnerIdList.join()
                }
            }


```

[Go back to top](#tracker-descriptions)

## BrightEdge
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.b0e8.com/conv_v3.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var audioTimeoutId$jscomp$0 = setTimeout(function() {
       console.warn('Audio fingerprint timed out. Please report bug at https://github.com/Valve/fingerprintjs2 with your user agent: "' + navigator.userAgent + '".');
       /**
        * @return {undefined}
        */
       context$jscomp$0.oncomplete = function() {
       };
       /** @type {null} */
       context$jscomp$0 = null;
       return done$jscomp$1("audioTimeout");
     }

```
2. Fingerprint is then sent to to BrightEdge:
```
 var _bright3 = new Object({
   C_NAME : "BE_CLA3",
   BE_URL : "a.b0e8.com/brightedge3.php",
   BE_SURL : "a.b0e8.com/brightedge3.php",
   IX_CONTENTS_HOSTNAME : "ix-contents.brightedge.com",
   IX_CONTENTS_STAGING_HOSTNAME : "ixl-nginx1-001.gcp.staging.brightedge.com",
   IX_STAGING_EXTERNAL_HOSTNAMES : /(ix-testing.brightedge.com)|(valuemyweb.com)/g,
   IX_STAGING_INTERNAL_HOSTNAMES : /(-staging.brightedge.com)/g,
   IX_TRUNCATE_HEADLINE_CHAR_COUNT : 100,
   IX_TRUNCATE_DESC_CHAR_COUNT : 200,
   TIMEOUT : 100 * 12 * 31 * 24 * 60 * 60 * 1E3,
   S_TIMEOUT : 30 * 60 * 1E3,
   VERSION : "3.39",

```

[Go back to top](#tracker-descriptions)

## C3 Metrics
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Policy Review
1. C3 Metrics claims that can universally track users with their fingerprinting technology - `https://c3metrics.com/privacy/`

> Tracking: Universal Identifier with fingerprinting technology unifies the consumer journey into a private & secure infrastructure.

> Data Unification: Distribute attribution credit algorithmically with the Attribution Data Cloud’s constantly updating machine learning.
### Technical Review
1. C3 Metrics appears to be heavily based on an open source fingerprinting library: `https://github.com/Valve/fingerprintjs2`. It probes difference device properties to fingerprint users
```
            getPixelRatio: function() {
                return window[_0x4dfd("0x118")] || ""
            },
            screenResolutionKey: function(d) {
                return this[_0x4dfd("0xec")][_0x4dfd("0x119")] ? d : this[_0x4dfd("0x11a")](d)
            },
            getScreenResolution: function(d) {
                var x;
                return x = this[_0x4dfd("0xec")][_0x4dfd("0x11b")] && window[_0x4dfd("0x110")][_0x4dfd("0x73")] > window[_0x4dfd("0x110")].width ? [window.screen[_0x4dfd("0x73")], window[_0x4dfd("0x110")][_0x4dfd("0x72")]] : [window[_0x4dfd("0x110")][_0x4dfd("0x72")], window[_0x4dfd("0x110")][_0x4dfd("0x73")]],
                d[_0x4dfd("0x108")]({
                    key: _0x4dfd("0x11c"),
                    value: x
                }),
                d
            },
            availableScreenResolutionKey: function(d) {
                return this[_0x4dfd("0xec")][_0x4dfd("0x11d")] ? d : this.getAvailableScreenResolution(d)
            },
            getAvailableScreenResolution: function(d) {
                var x;
                return window[_0x4dfd("0x110")][_0x4dfd("0x11e")] && window[_0x4dfd("0x110")].availHeight && (x = this[_0x4dfd("0xec")].detectScreenOrientation ? window[_0x4dfd("0x110")][_0x4dfd("0x11f")] > window[_0x4dfd("0x110")][_0x4dfd("0x11e")] ? [window.screen[_0x4dfd("0x11f")], window[_0x4dfd("0x110")][_0x4dfd("0x11e")]] : [window[_0x4dfd("0x110")][_0x4dfd("0x11e")], window[_0x4dfd("0x110")][_0x4dfd("0x11f")]] : [window[_0x4dfd("0x110")][_0x4dfd("0x11f")], window[_0x4dfd("0x110")][_0x4dfd("0x11e")]]),
                void 0 !== x && d.addPreprocessedComponent({
                    key: _0x4dfd("0x120"),
                    value: x
                }),
                d
            },
            timezoneOffsetKey: function(d) {
                return this[_0x4dfd("0xec")][_0x4dfd("0x121")] || d.addPreprocessedComponent({
                    key: _0x4dfd("0x122"),
                    value: (new Date)[_0x4dfd("0x123")]()
                }),
                d
            }
```


[Go back to top](#tracker-descriptions)

## CallSource
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ai.leadtrackingdata.com/ai.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
we = [{
                key: "userAgent",
                getData: p
            }, {
                key: "language",
                getData: v
            }, {
                key: "colorDepth",
                getData: h
            }, {
                key: "deviceMemory",
                getData: _
            }, {
                key: "pixelRatio",
                getData: g
            }, {
                key: "hardwareConcurrency",
                getData: Y
            }, {
                key: "screenResolution",
                getData: y
            }, {
                key: "availableScreenResolution",
                getData: x
            }, {
                key: "timezoneOffset",
                getData: k
            }, {
                key: "timezone",
                getData: T
            }, {
                key: "sessionStorage",
                getData: C
            }, {
                key: "localStorage",
                getData: S
            }, {
                key: "indexedDb",
                getData: E
            }, {
                key: "addBehavior",
                getData: A
            }, {
                key: "openDatabase",
                getData: N
            }, {
                key: "cpuClass",
                getData: L
            }, {
                key: "platform",
                getData: D
            }, {
                key: "doNotTrack",
                getData: O
            }, {
                key: "plugins",
                getData: G
            }, {
                key: "canvas",
                getData: M
            }, {
                key: "webgl",
                getData: F
            }, {
                key: "webglVendorAndRenderer",
                getData: I
            }, {
                key: "adBlock",
                getData: q
            }, {
                key: "hasLiedLanguages",
                getData: P
            }, {
                key: "hasLiedResolution",
                getData: B
            }, {
                key: "hasLiedOs",
                getData: R
            }, {
                key: "hasLiedBrowser",
                getData: j
            }, {
                key: "touchSupport",
                getData: z
            }, {
                key: "fonts",
                getData: H,
                pauseBefore: !0
            }, {
                key: "fontsFlash",
                getData: V,
                pauseBefore: !0
            }, {
                key: "audio",
                getData: f
            }, {
                key: "enumerateDevices",
                getData: s
            }]

```
[Go back to top](#tracker-descriptions)

## CartsGuru
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://tracker-client.carts.guru/dist/shopify-client.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
window.Fingerprint2 = ((i = function i(e) {
            if (!(this instanceof i)) return new i(e);
            this.options = this.extend(e, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        }

```
2. Sends computed fingerprint back to server
```
var b = {
            version: "1.0.0",
            xhrTimeout: parseInt("5000"),
            trkUrl: "https://tracker.carts.guru/",
            trkClientUrl: "https://tracker-client.carts.guru/",
            trkDomain: "tracker.carts.guru",
            trkPrefix: "trkcg_",
            SOURCE_TYPE: JSON.parse('{"Ads":"ads","Direct":"direct","Organic":"organic","Referral":"referral"}'),
            CART_SOURCE_TYPE: JSON.parse('{"FBM":1,"CI":2}'),
            organicSources: JSON.parse('["aol.com","ask.com","bing.com","google.com","google.com.ua","yahoo.com","search.yahoo.com","mamma.com","naver.com","lycos.com","hotbot.com","bbc.com","eniro.se","dotdash.com","about.com","aol.com","ask.com","globososo.com","go.mail.ru","rambler.ru","tut.by"]'),
            ACTIVITY_TYPES: JSON.parse('{"event":1,"action":2,"fbm":3}'),
            ACTIVITIES: {
                events: ["visit", "quit"],
                actions: ["click", "cartAdd", "cartRemove", "cartUpdate", "cartCheckout", "cartContinue", "cartPopup", "OpenCartDiv", "confirmOptIn"],
                fbm: ["confirmOptIn", "optIn", "optOut", "MessengerCheckboxUserConfirmation"],
                specials: ["set", "unset", "delete"]
            },
            EVENTS: {
                pageView: 1,
                productView: 2,
                cartView: 3,
                cartCreate: 4,
                cartUpdate: 5,
                checkoutView: 6
            },
            PAGE_ROUTES: {
                root: "index",
                home: "home",
                collections: "collection",
                products: "product",
                cart: "cart",
                search: "search"
            }
        }

                    C.makeRequest("check-user-ref", {
                        siteId: this.model.siteId,
                        fingerprint: this.model.fingerprint,
                        fingerprintId: this.model.fingerprintId,
                        cg_accountid: this.model.cg_accountid
                    }, function(e, t) {
                        if (e) return console.warn(e);
                        t.user_ref ? (o.userRef = t.user_ref, o.setUserRef(t.user_ref)) : sessionStorage.setItem("cgCheckedUserRef", "true"), i(t)
                    })

```

[Go back to top](#tracker-descriptions)

## CashBeet
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Raw log: 
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://ilkxeber.info/",
        "isBlockingMiners": false,
        "miners": [
            "cashbeet.com"
        ],
        "miner_requests": [
            "http://cashbeet.com/8252605565b09521.3.n.2.2.l50.js",
            "https://cashbeet.com/7c93027c-4137-4ad3-a911-53fc51a6ab42/iframe.html"
        ],
        "run_stats": {
            "cpu": 41.32903225806452,
            "memory": "568.7 MB"
        },
        "workers_created": []
    },
    "WhenBlocked": {
        "test_webpage": "http://ilkxeber.info/",
        "isBlockingMiners": true,
        "miners": [
            "cashbeet.com"
        ],
        "miner_requests": [
            "http://cashbeet.com/8252605565b09521.3.n.2.2.l50.js"
        ],
        "run_stats": {
            "cpu": 17.823802294197034,
            "memory": "486.4 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## Choozle
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Choozle’s privacy policy states: 

`https://choozle.com/privacy-policy/`

>Automatically collected information: To make our Site and Services more useful to you, our servers (which may be hosted by a third-party service provider) may collect information from you, including browser type, operating system, Internet Protocol (IP) address (a number that is automatically assigned to your computer when you use the Internet, which may vary from session to session), domain name, precise location data and/or a date and time stamp for your visit. We also use Cookies (as defined below) and navigational data to gather information regarding the date and time of your visit … We also could use data from mobile applications, including advertising IDs and mobile device IDs. 

>Information collected through our service: Our service allows our clients to collect information about their current or potential customers using cookies, pixel tags, web beacons, web bugs, televisions or OTT devices, and other collection technologies. While we do not collect this information on our site, we want you to be aware of how our services can be used to collect your information using publically available data and other collection technologies...We also source matched or linked data that enables our clients to pseudonymously match users across channels.


Choozle’s website states: 

`https://choozle.com/features/` 

>Launch highly-targeted campaigns with custom audiences created from first or third-party data. You can also target specific locations or based on web content and page categories. 

>- Third-party Data: 60+ data providers, purchase history targeting, behavioral targeting, psychographics targeting,
>- Location and Content: Geolocation Targeting, IP Address Targeting, Contextual Targeting, Keyword Targeting, Postal code Targeting
>- Other Targeting: Cross-Device Targeting

[Go back to top](#tracker-descriptions)

## ClearLink
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://mapi.clearlink.com/js/cl-track.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
("Fingerprint2", this, function() {
            "use strict";
            var e = function(t) {
                if (!(this instanceof e)) return new e(t);
                var n = {
                    swfContainerId: "fingerprintjs2",
                    swfPath: "flash/compiled/FontList.swf",
                    detectScreenOrientation: !0,
                    sortPluginsFor: [/palemoon/i],
                    userDefinedFonts: []
                };
                this.options = this.extend(t, n), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
            };
            return e.prototype = {
                extend: function(e, t) {
                    if (null == e) return t;
                    for (var n in e) null != e[n] && t[n] !== e[n] && (t[n] = e[n]);
                    return t
                },
                get: function(e) {
                    var t = [];
                    t = this.userAgentKey(t), t = this.languageKey(t), t = this.colorDepthKey(t), t = this.pixelRatioKey(t), t = this.hardwareConcurrencyKey(t), t = this.screenResolutionKey(t), t = this.availableScreenResolutionKey(t), t = this.timezoneOffsetKey(t), t = this.sessionStorageKey(t), t = this.localStorageKey(t), t = this.indexedDbKey(t), t = this.addBehaviorKey(t), t = this.openDatabaseKey(t), t = this.cpuClassKey(t), t = this.platformKey(t), t = this.doNotTrackKey(t), t = this.pluginsKey(t), t = this.canvasKey(t), t = this.webglKey(t), t = this.adBlockKey(t), t = this.hasLiedLanguagesKey(t), t = this.hasLiedResolutionKey(t), t = this.hasLiedOsKey(t), t = this.hasLiedBrowserKey(t), t = this.touchSupportKey(t), t = this.customEntropyFunction(t);
                    var n = this;
                    this.fontsKey(t, function(t) {
                        var r = [];
                        n.each(t, function(e) {
                            var t = e.value;
                            "undefined" != typeof e.value.join && (t = e.value.join(";")), r.push(t)
                        });
                        var i = n.x64hash128(r.join("~~~"), 31);
                        return e(i, t)
                    })
                }

```
2. Sends computed fingerprint back to server
```
function c(e, t, n, r, i) {
                n && (e.push(["setCustomVariable", 1, "PromoCode", n, "visit"]), i.promoCode = n), t && (e.push(["setCustomVariable", 2, "RequestID", t, "visit"]), i.requestId = t), r = r || i && i.fingerprint, r && (e.push(["setCustomVariable", 3, "Fingerprint", r, "visit"]), e.push(["setUserId", r]), i.fingerprint = r, h(r, t))
            }

            function d() {
                var e = o();
                c(n._paq, e, a(), !1, n.piwikData), _paq.push(["trackPageView"]), h(n.piwikData && n.piwikData.fingerprint, e)
            }

            function h(e, t) {
                if (t && e) {
                    var n = w.getMapiUrl() + ("/cpr/external/request/" + t);
                    T.putJSON(n, {
                        data: {
                            request: {
                                fingerprint: {
                                    fingerprint: e,
                                    request_id: t
                                }
                            }
                        }
                    })
                }
            }
```

[Go back to top](#tracker-descriptions)

## Clickayab
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://supplier.clickyab.com/api/multi.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

```
swfContainerId:"fingerprintjs2"
```
[Go back to top](#tracker-descriptions)

## ClickFrog
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://franecki.net/js/lib.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(e) {
        var t = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i]
        };
        this.options = this.extend(e, t), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };


```
2. Sends computed fingerprint to various endpoints:
```
    _match: function() {
        var m = ["quitzon.net", "bashirian.biz", "franecki.net", "buckridge.link", "0qq20ey4fo5veh0t.wisokykulas.bid"],
            i = 0,
            l = m.length,
            r;
        for (; i < l; i++) {
            var p = "//" + m[i] + "/r/?auid=" + AMSP._dmp.adwuid + "&p=" + AMSP._dmp.adwuid;
            try {
                window.XDomainRequest ? (r = new XDomainRequest) : (r = window.XMLHttpRequest ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP")), r.timeout = 1e3, r.withCredentials = true, r.open("GET", p, !0), r.send()
            } catch (er) {}
        }
    }

```
[Go back to top](#tracker-descriptions)

## ClickGuard
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://io.clickguard.com/s/cHJvdGVjdG9y/KsNIeBlt`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        var i = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(t, i), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server
```
    var qs = function(v) {
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i = 0; i < vars.length; i++) {
            var pair = vars[i].split("=");
            if (pair[0] == v) {
                return pair[1];
            }
        }
        return (false);
    };
    var z = window[atob('YXRvYg==')];
    var r = function(i, f, e) {
        if (!window.sessionStorage.gclid && qs('gclid')) {
            window.sessionStorage.gclid = qs('gclid');
        }
        if (!window.sessionStorage.sid) {
            window.sessionStorage.sid = window.btoa(new Date().getTime());
        }
        if (!window.localStorage.did) {
            window.localStorage.did = window.btoa(new Date().getTime());
        }
        var d = {
            t: 1553717499121,
            s: window.sessionStorage.sid,
            ss: new Date().getTime(),
            u: window.location.href,
            r: decodeURI(document.referrer),
            gclid: qs('gclid'),
            d: window.localStorage.did,
            i: i,
            f: f,
            e: e
        };
        var x = new XMLHttpRequest();
        x.open("POST", z("aHR0cHM6Ly9pby5jbGlja2d1YXJkLmNvbTo0NDMvci9jSEp2ZEdWamRHOXkvS3NOSWVCbHQ="), !0);
        x.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        x.send(JSON.stringify(d));

```

[Go back to top](#tracker-descriptions)

## Clixtell
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://app.clixtell.com/scripts/latest.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var _0x677fx7 = function(_0x677fx8) {
        var _0x677fx9 = {
            swfContainerId: 'fingerprintjs2',
            swfPath: 'flash/compiled/FontList.swf',
            detectScreenOrientation: true,
            sortPluginsFor: [/palemoon/i]
        };
        this['options'] = this['extend'](_0x677fx8, _0x677fx9);
        this['nativeForEach'] = Array['prototype']['forEach'];
        this['nativeMap'] = Array['prototype']['map']
    };

```
2. Sends computed fingerprint back to server
```
function n(t) {
            var n = "",
                i = c("utm_source"),
                o = c("utm_medium");
            n = "xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                var t = 16 * Math.random() | 0,
                    n = "x" == e ? t : 3 & t | 8;
                return n.toString(16)
            }), window.clixTellClickID = n, null !== c("gclid") && (n = c("gclid")), window.clixTellFCID = n;
            var a = document.referrer;
            window.location.href.indexOf("snippet-asset") > -1 && (a = "");
            var s = {
                    referrer: a,
                    DeviceId: t,
                    sessionId: r,
                    source: i,
                    medium: o,
                    keywords: e(),
                    gclid: c("gclid"),
                    campaign: c("utm_campaign"),
                    clickid: n
                },
                l = document.location.protocol;
            "http" == l && "https" == l || (l = "https:");
            var x = new XMLHttpRequest;
            x.onreadystatechange = function() {
                if (x.readyState == XMLHttpRequest.DONE && "true" == x.responseText) {
                    var e = document.createElement("script");
                    e.async = !0, e.type = "text/javascript";
                    var t = l + "//app.clixtell.com/scripts/recorder.js";
                    e.src = t;
                    var n = document.head;
                    n.appendChild(e)
                }
            }, x.open("POST", l + "//tracker.clixtell.com/track", !0), x.setRequestHeader("Content-Type", "application/json;charset=UTF-8"), x.send(JSON.stringify(s))
        }

```
[Go back to top](#tracker-descriptions)

## Cloudflare
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://assets.hcaptcha.com/c/7f492a3/hsw.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "#000000", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "get"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"❤️🤪🎉👋\",50,70]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "#000000", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "get"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"❤️🤪🎉👋\",50,70]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## CoinHive
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://coinhive.com` describes its service as a javascript crypto miner.

> Coinhive offers a JavaScript miner for the Monero Blockchain (Why Monero?) that you can embed in your website
### Technical Review
Coinhive has been identified using the following domains:
- coinhive.com
- coin-hive.com
- cnhv.co
- authedmine.com
- wsservices.org

1. Script contains an implementation of the cryptonight hash algorithm

```
var CryptonightWASMWrapper = function() {
  this.ctx = _cryptonight_create();
  /** @type {number} */
  this.throttleWait = 0;
  /** @type {number} */
  this.throttledStart = 0;
  /** @type {number} */
  this.throttledHashes = 0;
  this.workThrottledBound = this.workThrottled.bind(this);
  /** @type {null} */
  this.currentJob = null;
  /** @type {!Uint8Array} */
  this.target = new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255]);
  var inputs = Module.HEAPU8.buffer;
  /** @type {!Uint8Array} */
  this.input = new Uint8Array(inputs, Module._malloc(84), 84);
  /** @type {!Uint8Array} */
  this.output = new Uint8Array(inputs, Module._malloc(32), 32);
  self.postMessage("ready");
  self.onmessage = this.onMessage.bind(this);
};
```

2. Network traffic shows script submitting hashes

```
up: {"type":"submit","params":{"version":7,"job_id":"448165886709466","nonce":"0bf389de","result":"eefccc790cd55f37715d07ffedd97652737eff274c747795e4c66f2da81ad100"}}

down: {"type":"hash_accepted","params":{"hashes":256}}
```
[Go back to top](#tracker-descriptions)

## CoinPot
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
CoinPot has been identified using the following domains:
- coinpot.co

Observered on: http://sarzaminhayedoor.ir
- CPU utilization
    - Baseline load: 387.84%
    - Cryptomining script blocked: 19.32%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://sarzaminhayedoor.ir",
        "isBlockingMiners": false,
        "miners": [
            "coinpot.co",
            "coinhive.com"
        ],
        "miner_requests": [
            "https://coinpot.co/mine/dogecoin/?ref=561D40CFB1AC&mode=widget",
            "https://coinpot.co/css/core?v=Q7AbQW6bSB8k9oEdpwQ88CIOTScjp-DY4u2i45CPiTo1",
            "https://coinpot.co/css/mine?v=EMuRUrCvQojGTBslF-qKPUnQZDlLJgZutm2V221SDRk1",
            "https://coinpot.co/js/core?v=njVP3ZVyl6pV9piAzCamowq5KrVFrtkqPStsvdPAPdY1",
            "https://coinpot.co/js/site?v=_T5qLblY4DhVBtQklVQp3qBV0ShJcWi61ps4pQ6uW541",
            "https://coinhive.com/lib/coinhive.min.js?v8",
            "https://coinpot.co/js/mine?v=OuPG9LnHSWrT0DKH26bbgtl7DAysUL68GA18XX9HhMA1",
            "https://coinpot.co/api/transactions/service.svc/GetMiningSummary",
            "https://coinpot.co/img/coin/dogecoin/icon.png",
            "https://www.google-analytics.com/r/collect?v=1&_v=j72&a=413559415&t=pageview&_s=1&dl=https%3A%2F%2Fcoinpot.co%2Fmine%2Fdogecoin%2F%3Fref%3D561D40CFB1AC%26mode%3Dwidget&dr=http%3A%2F%2Fsarzaminhayedoor.ir%2F&ul=en-us&de=UTF-8&dt=CoinPot%20%7C%20Cryptocurrency%20microwallet&sd=24-bit&sr=1680x1050&vp=&je=0&_u=IEBAAEAB~&jid=6086565&gjid=1862641903&cid=1835399174.1543466248&tid=UA-49827542-11&_gid=1320420632.1543466248&_r=1&z=976113981",
            "https://coinpot.co/api/transactions/service.svc/ProcessMining"
        ],
        "run_stats": {
            "cpu": 387.8432295932296,
            "memory": "687 MB"
        },
        "workers_created": [
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff",
            "blob:https://coinpot.co/954f0c63-fd55-4fc7-898c-b5e2a53036ff"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://sarzaminhayedoor.ir",
        "isBlockingMiners": true,
        "miners": [
            "coinpot.co"
        ],
        "miner_requests": [
            "https://coinpot.co/mine/dogecoin/?ref=561D40CFB1AC&mode=widget"
        ],
        "run_stats": {
            "cpu": 19.322393822393824,
            "memory": "575 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## ConversantMedia
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Conversant's privacy policy States:

`https://www.conversantmedia.com/legal/privacy`

>We may use technologies such as cookies, log files, pixel tags or other similar technologies to collect Non-PII about the browser or device you are using, including browsing activity, online transactions, and IP addresses. We may also receive similar Non-PII from third parties, which may additionally include the types of programming you view on your television…All Non-PII received and collected by Conversant from the various sources may be combined and used to provide you relevant advertising, and for other purposes as determined by Conversant.  
  
>We also may use Internet browsing, cross-mobile application browsing and online purchase data associated with a user, on a Non-PII level, across multiple devices to develop a predictive statistical user profile of the end user's needs and interests for the purpose of sending them relevant advertisements on multiple browsers and devices. This is called cross-device IBA. We may also use this cross-device functionality for the purpose of more accurately paying third-parties affiliate commissions, as described in the paragraph directly above.

Conversant's website states: 
`https://www.conversantmedia.com/case-studies/cross-device-remarketing` (1)  

>Conversant cross-device remarketing consistently reaches site visitors across all their devices—mobile, tablet and desktop. (1)  

`https://www.conversantmedia.eu/solutions/media-solutions/media-platform` (2)

>Whether you choose a mobile-only or integrated multi-device campaign, you’ll benefit from the insights that come from our incredibly rich cross-device consumer profiles. Our profiles encompass browsing, interaction, shopping and purchase data as well as mobile-specific insights like device and location. With superior cross-device mapping and a potential reach of 90+ percent of both iOS and Android, we offer an unparalleled opportunity to reach and message consumers across channels and on virtually any device they choose. In fact, we have full SDK integration with more than 20,000 apps. Conversant's cross-device solutions deliver more than three times the engagement and five times the conversions of single device programmes. From standard banners to rich, interactive full-screen executions, we offer an incredibly broad creative suite to accommodate virtually any marketing goal or metric. (2)


[Go back to top](#tracker-descriptions)

## CryptoLoot
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://cryptoloot.com` describes its service as a javascript crypto miner.

> Crypto-Loot offers a Browser based web miner for the Monero Blockchain
### Technical Review
1. Script contains an implementation of the cryptonight hash algorithm

```
function _0x45bcc2() {
  var w = new Worker(CRLT["CRYPTONIGHT_WORKER_BLOB"]);
  _0x293514[_0x57ed("0x4b")](w);
  w["onmessage"] = _0x5a4854;
  setTimeout(function() {
    _0xe5c8f6(w);
  }, 2E3);
}
```
[Go back to top](#tracker-descriptions)

## DoubleVerify
This service has been classified as `Analytics` and `FingerprintingGeneral` for the following reasons:
### Policy Review
DoubleVerify's Privacy Policy States: 

`https://doubleverify.com/privacy-policy/`

> Categories of data and personal information collected by the DoubleVerify Services:  
>> Digital environment attributes – The type of connected device the advertisement is being delivered to: mobile, desktop, connected TV or other device, the browser type and version used to render the page where the ad appears and the operating system are collected to determine what version of our code would properly run in that environment and to properly measure if the advertisement had the chance to become viewable on the screen according to industry standards which vary between environments.  
>> Viewability attributes – The location of the ad on the page, the size of the ad, the size of the screen, the size of the viewport, the tab focus status, the browser focus status, the time duration the ad was in the viewable part of the webpage and the scroll position of the webpage are collected to determine and report to our customers if the advertisement had the chance to become viewable on the screen.  
>> Exposure and engagement attributes – Data that shows if the ad was clicked, resized, skipped, muted, paused, rotated, hovered or changed volume is collected to help our customers measure the performance of the advertisement, the advertising campaign or the media property. The data is not tied back to any personally identifiable information.  

> Categories of data and personal information collected by the DoubleVerify Services solely for fraud prevention and geo compliance purposes:  
>> Device identifiers and attributes – IP address, user agent, advertising ID, and user ID, in order to analyze whether the device is participating in a fraudulent scheme.  
>> IP addresses are collected to extract geolocation information.


[Go back to top](#tracker-descriptions)

## Drawbridge
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Drawbridge/Linkedin’s privacy policy states:

`https://www.linkedin.com/legal/privacy-policy`

>We use cookies and similar technologies (e.g., pixels and ad tags) to collect data (e.g., device IDs) to recognize you and your device(s) on, off and across different services and devices where you have engaged with our Services. We also allow some others to use cookies as described in our Cookie Policy. If you are outside the Designated Countries, we also collect (or rely on others who collect) information about your device where you have not engaged with our Services (e.g., ad ID, IP address, operating system and browser information) so we can provide our Members with relevant ads and better understand their effectiveness.

>Your Device and Location: When you visit or leave our Services (including some plugins and our cookies or similar technology on the sites of others), we receive the URL of both the site you came from and the one you go to and the time of your visit. We also get information about your network and device (e.g., IP address, proxy server, operating system, web browser and add-ons, device identifier and features, cookie IDs and/or ISP, or your mobile carrier). If you use our Services from a mobile device, that device will send us data about your location based on your phone settings.

[Go back to top](#tracker-descriptions)

## ECSAnalytics
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://common.ecsanalytics.com/js/vendor/fp.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(e) {
        var t = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i]
        };
        this.options = this.extend(e, t), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };
```
2. Sends computed fingerprint back to server
```
Request URL: https://mittmedia.ecsanalytics.com/analytics/p.gif?r=ex&cid=REMOVED&d=lt.se&jid=REMOVED&vid=f2qwg0&eid=REMOVED&v=1.7.0
```
[Go back to top](#tracker-descriptions)

## EroAdvertising
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://go.ero-advertising.com/loadeactrl.go?pid=71279&siteid=111148&spaceid=3830036`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
Andale|innerHTML|Rounded|Bitstream|Antiqua|Book|Vera|fontSize|span|setTimeout|swf_fonts|valid|monospace|sans|getElementsByTagName|72px|mmmmmmmmmmlli|excludeDoNotTrack|navigator_platform|compiled|colorDepth|color_depth|excludeColorDepth|excludeScreenResolution|excludeAvailableScreenResolution|excludeTimezoneOffset|available_resolution|fingerprintjs2|FontList||swf|user_agent|get|excludeUserAgent|excludeLanguage|userLanguage|palemoon|systemLanguage|browserLanguage|timezone_offset|Date|excludeOpenDatabase|add_behavior|addBehavior|excludeAddBehavior|openDatabase|open_database|excludePlatform|cpu_class|excludeCpuClass|indexed_db|excludeIndexedDB|while|session_storage|getTimezoneOffset|Infinity|s|local_storage

```
2. Sends computed fingerprint back to server
```
    cg: function(ab) {
        var fprint = eaCtrl.getStorage('fprint');
        if (fprint == null || fprint == '') {
            var options = {
                cj: true
            };
            var fp = new fp2(options);
            fp.get(function(result) {
                eaCtrl.setStorage('fprint', result, (24 * 60 * 30));
                eaCtrl.f_print = result;
                ab()
            })
        } else {
            eaCtrl.f_print = fprint;
            ab()
        }
    },

eaCtrl.connectors = {
    1: {
        isproxy: 0,
        type: "url",
        url: "//go.ero-advertising.com/eactrl.go",
        "isfailed": 0
    }
};


```

[Go back to top](#tracker-descriptions)

## Experian
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Experian's privacy policy States:

`https://www.experian.co.uk/legal/privacy-statement`

>Information specific to Aperture Data Studio and the SaaS Self Service Portal: Whenever a visitor visits our services, we may collect information from such visitor regarding his or her use of that website or application, such as pages visited, links clicked, non-sensitive text entered, and mouse movements, as well as information more commonly collected such as his/her IP address, referring URL, browser, operating system, cookie information, CSS animations and dynamic content (“Visitors’ Information“). Visitors’ Information, in the aggregate, may be considered as Personal Information as it may be linked to a user identifier or may include Personal Information. Visitors’ Information may include: User unique ID (stored in a cookie for tracking and may be stored on our servers), Visitors’ clicks/touches on elements, changes to input field (like text fields, CSS selector or timestamp), elements and session meta-data, input on fields, system errors, window size and changes to size, User agent (browser, device), mouse position, page snapshot, whether a user clicked on a play or pause button of a video, and other events (scrolling, focusing, hiding pages etc.). Such information may identify the visitor. We use IP addresses to determine End Users’ geolocation (country and city in which you are located) which allows us to block recordings for certain End Users. 


Experian's website states:
`https://www.experian.co.uk/business/marketing/multi-channel-marketing/campaign-personalisation/index` (1)

>By consistently applying data across and the entire customer journey, you’ll offer more personalised experiences so your customers feel understood and engaged.  Experian has the data, media partners, advertising services and analytical capabilities to help you create targeted campaigns and seamless experiences. (1)

`https://www.experian.co.uk/business/data-management/single-customer-view/index` (2)

>Our approach focuses on the data and provides a methodology that will consolidate, clean, fix, link, harmonise, and enrich with additional customer insights across all data assets within a business.
>- Investigate- Extract data from systems across your organisation, consolidate it, and assess its accuracy and completeness as the first step to cleansing and validating.
>- Assess- Consolidate and profile the data so you can assess potential strengths and weaknesses within it, in the context of business priorities.
>- Improve- Bring consistency to the way your data is formatted, ensure your customer data is accurate, and fill the gaps using our unique range of reference data including location and socio-demographic data sets.
>- Control - Compare records, identify and harmonise duplicates, create a golden nominal and give each individual a unique identification number and ensure you can maintain an up-to-date and accurate view over time. (2) 


[Go back to top](#tracker-descriptions)

## EyeNewton
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
`https://eyenewton.ru/docs/privacy_policy.pdf`
PRIVACY POLICY NOT RELEVANT AND "PROCESSING OF PERSONAL DATA" SECTION ONLY APPLIES TO CONSENT

[Go back to top](#tracker-descriptions)

## eyeReturn Marketing
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Policy Review
1. Eyereturn claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://eyereturnmarketing.com/privacy/`

> Statistical IDs are created via an algorithm using non-personally identifiable and pseudonymous information about a computer or device. The information used may include the operating system, user-agent string, Web browser, approximate location, installed fonts, and similar information. This information makes your computer or device distinct enough for our systems to determine within a reasonable probability that they are encountering the same computer or device. These IDs are not used to target advertisements, and are only used for campaign analytics and reporting purposes

[Go back to top](#tracker-descriptions)

## Facebook
This service has been classified as `Social`, `Content`, `Disconnect`, `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Facebook's Privacy Policy States:  
  
`https://www.facebook.com/policies/cookies` (1)
  
>Cookies are used to store and receive identifiers and other information on computers, phones, and other devices. Other technologies, including data we store on your web browser or device, identifiers associated with your device, and other software, are used for similar purposes. In this policy, we refer to all of these technologies as “cookies.”  (1)
  
>Cookies help us serve and measure ads across different browsers and devices used by the same person.  (1)
  
>We also use cookies to help you opt out of seeing ads from Facebook based on your activity on third-party websites.  (1)
  
>We may place cookies on your computer or device, and receive information stored in cookies, when you use or visit: Websites and apps provided by other companies that use the Facebook Products, including companies that incorporate the Facebook Technologies into their websites and apps. Facebook uses cookies and receives information when you visit those sites and apps, including device information and information about your activity, without any further action from you. This occurs whether or not you have a Facebook account or are logged in.  (1)

`https://m.facebook.com/policy.php` (2)

>Device Information: As described below, we collect information from and about the computers, phones, connected TVs and other web-connected devices you use that integrate with our Products, and we combine this information across different devices you use. For example, we use information collected about your use of our Products on your phone to better personalize the content (including ads) or features you see when you use our Products on another device, such as your laptop or tablet, or to measure whether you took an action in response to an ad we showed you on your phone on a different device. (2)  
>  
>Information we obtain from these devices includes:
>-   Device attributes: information such as the operating system, hardware and software versions, battery level, signal strength, available storage space, browser type, app and file names and types, and plugins.
>-   Device operations: information about operations and behaviors performed on the device, such as whether a window is foregrounded or backgrounded, or mouse movements (which can help distinguish humans from bots).
>-   Identifiers: unique identifiers, device IDs, and other identifiers, such as from games, apps or accounts you use, and Family Device IDs (or other identifiers unique to Facebook Company Products associated with the same device or account).
>-   Device signals: Bluetooth signals, and information about nearby Wi-Fi access points, beacons, and cell towers.
>-   Data from device settings: information you allow us to receive through device settings you turn on, such as access to your GPS location, camera or photos.
>-   Network and connections: information such as the name of your mobile operator or ISP, language, time zone, mobile phone number, IP address, connection speed and, in some cases, information about other devices that are nearby or on your network (2)

Facebook's Website States:  
  
`https://www.facebook.com/business/news/cross-device-measurement`
  
>Today we’re launching cross-device reporting for Facebook ads, enabling advertisers to see for the first time how people are moving between devices — across mobile apps and the web — before they convert.  
  
>With the new cross-device report, advertisers are now able to view the devices on which people see ads and the devices on which conversions subsequently occur. For instance, a marketer can view the number of customers that clicked an ad on an iPhone but then later converted on desktop, or the number of people that saw an ad on desktop but then converted on an Android tablet.  
  
>Josh McFarland, CEO of TellApart, a Facebook Preferred Marketing Developer, adds: “Tracking click and conversion data deterministically across devices has confirmed what we know to be true: mobile ads drive commerce everywhere. This new reporting from Facebook has been a game-changer in our ability to help clients like Neiman Marcus and Sur La Table correctly value and invest in their mobile ads efforts.”

[Go back to top](#tracker-descriptions)

## Fanplayr
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Fanplayr’s privacy policy states: 
 
`https://fanplayr.com/files/en/Fanplayr-Privacy-Policy-May-2018.pdf`
 
>Passively Collected Information 
>•Automatically Collected Information. When You use the Services, some information is also automatically collected, such as Your Internet Protocol (IP) address, Your operating system, the browser type, the address of a referring Web site and Your activity on the Services. 
>•"Cookies" and Clear Gif Information. We may automatically collect certain information using "cookies" or clear gifs. Cookies are small data files that are stored on a User's hard drive at the request of a Web Site to enable such Web site to recognize Users who have previously visited them and retain certain information such as user preferences and history. If we combine cookies with or link them to any personally identifiable information, we would treat this information as Personal Data. Clear gifs are small, invisible graphic images that may be used by the Services or in emails relating to the Services to collect certain information and monitor user activity on the Services and may be combined with Your IP address or other information that we have gathered with respect to a User's use of the Services 
>•We use analytics tools to track how You get to Web Sites and to understand how You use the WebSites after You arrive."

[Go back to top](#tracker-descriptions)

## Fiksu
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Fiksu's privacy policy States:

`https://fiksu.com/privacy-policy`

>Marketing Service of FiksuDSP - When you click on a Client ad or application link delivered by FiksuDSP, FiksuDSP servers may receive and store an advertising identifier ("Advertising ID") or device identifier ("Device ID"), either of them is a pseudonymous number that is associated with your mobile or CTV device. FiksuDSP cannot use the Advertising/Device ID to identify you personally, but it does enable us to deliver relevant advertising to each mobile or CTV device. In addition to the Advertising/Device ID, we collect information about the kind of mobile/CTV device you use (e.g., iPhone, Samsung, Roku etc.), the operating system for your mobile device (e.g., Android, iOS, Fire OS etc.), IP address, websites you may be visiting, content that you may be watching through video streaming CTV/OTT applications, the applications you download from Clients of FiksuDSP, when, how, and how often you use those applications.  
  
>We use your device's Advertising/Device ID and other information about Client applications you download to help our Clients understand which ads are most effective at generating downloads of our Client's applications or at achieving other goals defined by Client. We also use your Advertising/Device ID and the information associated with your device Advertising/Device ID over time (e.g., the applications you download, when and how you use those applications, and any publisher-provided demographic data) to enhance our services and to select FiksuDSP' Client ads that are most likely to be of interest to you.

Fiksu's website states: 

`https://fiksu.com/products/DSP/retargeting/` (1)

>Single-pixel cross-device targeting: Fiksu is the only company who can do this with one pixel. (1)

`https://fiksu.com/#home-scroll-learn-more` (2)  

>Looking to raise your brand’s profile with ads cross-platform? Or maybe you want to retarget lapsed customers that haven’t made a purchase in a while? Fiksu’s unique combination of aggregated user data and audience-building tools allows us to address brands’ biggest marketing challenges, reaching audiences on mobile and CTV/OTT. (2)  


[Go back to top](#tracker-descriptions)

## Flocktory
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Flocktory's privacy policy States:

`https://www.flocktory.com/en/data_privacy/`

>As a Flocktory client, you are a Data Controller and Flocktory is acting as your Data Processor for your users’ data. Flocktory collects and processes data of website visitors and their usage of the website with the purpose of:
>-   Analysis and profiling of data subjects
>-   Fulfilling its contractual obligations with its clients for services that improve the user experience on the client website.
>-   Improve our own website experience and services
>-   Electronic direct marketing


>Data that Flocktory collects may include:
>-   Online identifiers (cookies, device, browser information)
>-   Geographic location (country, region, city)
>-   Data about social media accounts
>-   Data about purchases
>-   Data about visited pages
>-   Data about membership / registration status

Flocktory's website states:

`https://www.flocktory.com/en/about-us/`

>Our solutions come as a complete platform which addresses the entire customer journey and use newest technology and communication channels.

'https://www.flocktory.com/en/platform/'

>Flocktory tracks millions of data points every single day and combines user behavior and customer shopping history with strong cohort analysis and predictive algorithms to support and automate your business decisions


[Go back to top](#tracker-descriptions)

## Foresee
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Policy Review
1. Answers Cloud Services uses the Foresee SDK (subsidiary of Answers Cloud Services) to provide a variety of services including fingerprinting. Their developer documentation includes definitions of their cookie passed parameters, including fingerprint:
> Fingerprint (fp) - Anonymous identifier for site visitor, used for cookieless tracking in 19.4.0+.
### Technical Review
1. Script uses canvas to perform font fingerprinting and calculate other properties
```
  var Binder = function(bridge) {
    /** @type {string} */
    this.browser = bridge;
    /** @type {string} */
    this.sig = "not detected";
    this.ready = new self.FSEvent;
    this._detect();
  };
  /**
   * @return {undefined}
   */
  Binder.prototype._detect = function() {
    var value;
    var iterator = _.proxy(function(obj) {
      /** @type {string} */
      this.sig = obj;
      this.ready.fire(obj);
    }, this);
    /** @type {!Array} */
    var textBuffer = [];
    /** @type {!Navigator} */
    var n = navigator;
    var browser = this.browser;
    if (win != win.top) {
      /** @type {(Array<string>|null)} */
      var quoteMatch = location.search.match(/uid=([\d\w]*)/i);
      if (quoteMatch && quoteMatch[1]) {
        /** @type {string} */
        value = quoteMatch[1];
      }
    }
    if (!(value && "not detected" != value || !browser.supportsLocalStorage)) {
      value = localStorage.getItem("_fsPRINT_");
    }
    if (!value) {
      textBuffer = self.trim(navigator.userAgent.replace(/[0-9\.\/\\\(\);_\-]*/gi, "")).split(" ");
      textBuffer.push(n.language || "");
      textBuffer.push(n.hardwareConcurrency || "");
      textBuffer.push(n.platform || "");
      textBuffer.push(n.vendor || "");
      textBuffer.push(n.appName || "");
      textBuffer.push(n.maxTouchPoints || "");
      textBuffer.push(n.doNotTrack || "false");
      textBuffer.push(browser.os.name || "false");
      textBuffer.push(browser.os.version || "false");
      textBuffer.push(this._getCanvasPrint());
      value = self.md5(textBuffer.join(""));
      this.sig = value;
      if (browser.supportsLocalStorage) {
        localStorage.setItem("_fsPRINT_", value);
      }
    }
    _.nextTick(function() {
      iterator(value);
    });
  };
  /**
   * @return {?}
   */
  Binder.prototype._getCanvasPrint = function() {
    try {
      /** @type {!Element} */
      var canvasDrawBG = document.createElement("canvas");
      var ctx = canvasDrawBG.getContext("2d");
      /** @type {string} */
      var tempPathText = "ForeSee,CloudUser <canvas> 1.0";
      return canvasDrawBG.width = 250, canvasDrawBG.height = 30, ctx.textBaseline = "top", ctx.font = "14px 'Arial'", ctx.textBaseline = "alphabetic", ctx.fillStyle = "#f60", ctx.fillRect(125, 1, 62, 20), ctx.fillStyle = "#069", ctx.fillText(tempPathText, 2, 15), ctx.fillStyle = "rgba(102, 204, 0, 0.7)", ctx.fillText(tempPathText, 4, 17), canvasDrawBG.toDataURL();
    } catch (t) {
      return "nocanvas";
    }
  };
  /** @type {function(string): undefined} */
  self.Fingerprint = Binder;
```

[Go back to top](#tracker-descriptions)

## Friends2Follow
This service has been classified as `Analytics`, `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://assets-us-u11ncmyydwz.stackpathdns.com/sites/all/modules/friends2follow/dist/friends2follow_socialstack.min.js?v=201902040`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var a = function(a) {
        var b = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(a, b), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server:
```
            addHoneyTracking: function() {
                var b = a(this);
                b.find(".socialstack-item").each(function() {
                    var b = a(this),
                        c = b.find("div.header a.username"),
                        d = Drupal.settings.baseURL + Drupal.settings.basePath + "f2fh.php?fi=" + Drupal.settings.f2f_widget_settings.fingerprint,
                        e = a.getQueryString.click;
                    "undefined" != typeof e && (clickMaco = decodeURIComponent(e), a.validateURL(clickMaco) && (d = decodeURIComponent(e) + encodeURIComponent(d))), a('<a href="' + d + '" class="hp" target="_blank">' + c.text() + "</a>").appendTo(b)
                })
            }

```

[Go back to top](#tracker-descriptions)

## FuelX
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.fuelx.com/js/fp2.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            audio: {
                timeout: 1e3,
                excludeIOS11: !0
            },
            fonts: {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                userDefinedFonts: [],
                extendedJsFonts: !1
            },
            screen: {
                detectScreenOrientation: !0
            },
            plugins: {
                sortPluginsFor: [/palemoon/i],
                excludeIE: !1
            },

```
2. Sends computed fingerprint back to server
```
Request URL: https://fsr3.fuel451.com/ids?browserId=REMOVED&fxidhash=REMOVED&bid=QwxV275UK6v5YQgGE2henQ%3D%3D&fxndid=&fxuuid=&lts=Tue%20Mar%2026%202019%2021%3A08%3A06%20GMT-0700%20(Pacific%20Daylight%20Time)&ga=&oid=&cb=fuelxP.setFXCookies&fxt=true
```

[Go back to top](#tracker-descriptions)

## Gleam
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://js.gleam.io/assets/w-a08f4344eff99f85d18b1274a8789282a47d9e81d80d2fec172019c7e5fab781.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
/*
* Fingerprintjs2 2.0.5 - Modern & flexible browser fingerprint library v2
* https://github.com/Valve/fingerprintjs2
* Copyright (c) 2015 Valentin Vasilyev (valentin.vasilyev@outlook.com)
* Licensed under the MIT (http://www.opensource.org/licenses/mit-license.php) license.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED. IN NO EVENT SHALL VALENTIN VASILYEV BE LIABLE FOR ANY
* DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
* (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
* ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
* (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
* THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

```
2. Fingerprint is then stored to be transmitted with subsequent requests
```
if (!$scope.revealed() && !$scope.isLoading) return $scope.isLoading = !0, $http({
                    url: "/" + campaignService.campaign.key + "/" + this.entry_method.id + "/claim",
                    params: {
                        fingerprint: fingerprintService.hash($scope.fingerprint)
                    }
                })
```

[Go back to top](#tracker-descriptions)

## Google
This service has been classified as `Email`, `Social`, `Content`, `Analytics`, `Disconnect`, `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Google's Privacy Policy States: 

`https://policies.google.com/privacy`

>We collect information about your activity in our services…The activity information we collect may include: Activity on third-party sites and apps that use our services.

>We use various technologies to collect and store information, including cookies, pixel tags, local storage, such as browser web storage or application data caches, databases, and server logs. 

>We use automated systems that analyze your content to provide you with things like customized search results, personalized ads, or other features tailored to how you use our services...We also use algorithms to recognize patterns in data. We may combine the information we collect among our services and across your devices for the purposes described above. When you’re not signed in to a Google Account, we store the information we collect with unique identifiers tied to the browser, application, or device you’re using. This helps us do things like maintain your language preferences across browsing sessions. 

>Categories of personal information we collect: Internet, network, and other activity information such as: views and interactions with content and ads; information about the interaction of your apps, browsers, and devices with our services (like IP address, crash reports, and system activity); and activity on third-party sites and apps that use our services. 

>Sensor data from your device: Your device may have sensors that can be used to better understand your location and movement. For example, an accelerometer can be used to determine your speed and a gyroscope to figure out your direction of travel. 

>Information about things near your device: If you use Google’s Location services on Android, we can improve the performance of apps that rely on your location, like Google Maps. If you use Google’s Location services, your device sends information to Google about its location, sensors (like accelerometer), and nearby cell towers and Wi-Fi access points (like MAC address and signal strength). All these things help to determine your location. You can use your device settings to enable Google Location services.

Google's website states: 

`https://support.google.com/analytics/answer/7532985?hl=en` (1) 

>Connect data about devices and activities from different sessions so you can get an understanding of user behavior at each step of the conversion process, from initial contact to long-term retention. Google Analytics models behavior for your whole user base across device types. The data is user based rather than session based. This behavior modeling does not require User-ID views. Optimize user experience for the full customer journey across devices. Optimize ad spend based on cross-device usage. Remarket to users across devices. (1) 

`https://www.blog.google/products/marketingplatform/360/cross-device-capabilities/` (2)

>Analytics will now help you understand the journey your customers are taking across their devices as they interact with your website, giving you a complete view of the impact of your marketing so you can run smarter campaigns that deliver more tailored experiences to your customers. Cross Device reporting in Analytics takes into account people who visit your website multiple times from different devices. Now, instead of seeing metrics in Analytics that show two separate sessions (e.g., one on desktop and the other on mobile), you’ll be able to see when users visited your website from two different devices (2)

[Go back to top](#tracker-descriptions)

## GrapheneMedia
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://www.graphenedigitalanalytics.in/ccanalytics/fingerprint2.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        this.options = this.extend(t, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };
```
[Go back to top](#tracker-descriptions)

## Gridcash
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://gridcash.net` describes its service as a javascript crypto miner.

> Service of crypto-currency mining in user browsers. We enable traffic owners to mine crypto-currency in browsers on visitors' computers.
### Technical Review
1. Script contains an implementation of the cryptonight hash algorithm

```
    Miner.prototype._loadWorkerSource = function (callback) {
        var xhr = new XMLHttpRequest;
        xhr.addEventListener("load", function () {
            Adless.CRYPTONIGHT_WORKER_BLOB = Adless.Res(xhr.responseText);
            this._asmjsStatus = "loaded";
            callback()
        }.bind(this), xhr);
        xhr.open("get", "https://cdn.adless.io/worker.js", true);
        xhr.send()
        if (this._useWASM || this._asmjsStatus === "loaded") {
            callback()
        } else if (this._asmjsStatus === "unloaded") {
            this._asmjsStatus = "pending";
            xhr.open("get", Adless.CONFIG.LIB_URL + Adless.CONFIG.ASMJS_NAME, true);
            xhr.send()
        }
```

[Go back to top](#tracker-descriptions)

## HilltopAds
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://hilltopads.net/p?zoneId=1019565-1019701`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
    new Fingerprint2().get(function(result) {
        var s = document.createElement('script');
        var x = document.getElementsByTagName('script')[0];
        s.src = options.url + '?fp=' + result;
        s.type = 'text/javascript';
        s.async = true;
        x.parentNode.insertBefore(s, x);
    })
})({
    "url": "http:\/\/hilltopads.net\/Z\/n\/A-"
});

```
[Go back to top](#tracker-descriptions)

## HotelChamp
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.hotelchamp.com/app/launcher/kSqmBQZzCo.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            var i = {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            };
            this.options = this.extend(t, i), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
        this.updateSpecialPagesRemote = function(fingerprint) {
            if (this._finished && !this._finishedDone) {
                console.log('Register finished');
                this._finishedDone = !0;
                this.emit('finished');
                this._engine.getTitan().event('bookingEngine', 'finished');
                var self = this;
                this._engine.getTitan().fetchValidatedSessionId(function(sid) {
                    self.trackEvent('hcFinished', sid)
                });
                utils.net.send(this._relayServer + '/api/count?action=finished&api=' + utils.net.encodeData(this._api) + '&fingerprint=' + utils.net.encodeData(fingerprint) + '&tag=' + this.getFinishedTag() + '&trackingHash=' + this._trackingHash + '&page=' + utils.net.encodeData(document.location.href))
            } else if (this._booking && !this._bookingDone) {
                console.log('Register bookstart');
                this._bookingDone = !0;
                this.emit('bookstart');
                this._engine.getTitan().event('bookingEngine', 'start');
                utils.net.send(this._relayServer + '/api/count?action=bookStart&api=' + utils.net.encodeData(this._api) + '&fingerprint=' + utils.net.encodeData(fingerprint) + '&tag=' + this.getBookStartTag() + '&trackingHash=' + this._trackingHash + '&page=' + utils.net.encodeData(document.location.href))
            }
            if (!this._finished || !this._booking) {
                setTimeout(bind(this, this.pollSpecialPages), 1500)
            }
        };

```

[Go back to top](#tracker-descriptions)

## HotMart
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Hotmart's Privacy Policy States: 

`https://www.hotmart.com/en/pp` (1) 
>HOTMART may collect, receive and store, automatically, Personal Data and information in its servers about the activities from the users’ browsers, including geolocation, IP addresses, cookies, or other identifiable character sequences, and other information from the transactions made through the Platform. (1) 

`https://www.hotmart.com/en/cookie-policy` (2)
>Other data collection tools, similar to Cookies, are also employed by the HOTMART Platform, analytic and tracking cookies that aim to collect USER data and understand their behavior to enable the Platform to work. (2)

[Go back to top](#tracker-descriptions)

## ie8eamus
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://ie8eamus.com/sfp.js`
1. Script accesses several Javascript API calls known to invasively fingerprint users. Some examples (APIs captured using [OpenWPM](https://github.com/mozilla/OpenWPM)):
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]",
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OfflineAudioContext.createOscillator",
  "arguments": null,
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OscillatorNode.type",
  "arguments": null,
  "value": "triangle"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OfflineAudioContext.createOscillator",
  "arguments": null,
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OscillatorNode.type",
  "arguments": null,
  "value": "triangle"
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OfflineAudioContext.createOscillator",
  "arguments": null,
  "value": ""
}
```
```json
{
  "top_level_url": "http://sandownautorepair.com/",
  "script_url": "http://ie8eamus.com/sfp.js",
  "script_line": "1",
  "symbol": "OscillatorNode.type",
  "arguments": null,
  "value": "triangle"
}
```
[Go back to top](#tracker-descriptions)

## iMedia
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
```
      Plugin.prototype.get = function(options) {
        var name;
        for (name in options) {
          this._options[name] = options[name];
        }
        this._log("-> get fingerprint with options", this._options);
        /** @type {string} */
        var ret = "";
        ret = ret + this._getText();
        if (this._options.canvas) {
          ret = ret + this._getCanvas();
        }
        return ret;
      };
```

```
      Plugin.prototype._drawCanvas = function() {
        /** @type {!Element} */
        var canvas = document.createElement("canvas");
        var ctx = canvas.getContext("2d");
        /** @type {string} */
        ctx.fillStyle = "#fff";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        /** @type {!Array} */
        var strings = [];
        /** @type {number} */
        var rown = 25;
        [32, 64, 96, 256].forEach(function(i, canCreateDiscussions) {
          /** @type {string} */
          var value = "";
          /** @type {number} */
          var j = 0;
          for (; j < rown; j++) {
            /** @type {string} */
            value = value + String.fromCharCode(i + j);
          }
          strings.push(value);
        });
        [{
          "font" : "14px droid sand mono,ubuntu,serif",
          "fill" : "rgba(255, 30, 30, 0.3)",
          "stroke" : "rgba(30, 30, 255, 0.3)"
        }, {
          "font" : "12pt helvetica,arial,sans-serif",
          "fill" : "rgba(30, 255, 30, 0.3)",
          "stroke" : "rgba(255, 255, 30, 0.3)"
        }].forEach(function(label, m1) {
          /** @type {number} */
          var y = 0;
          /** @type {number} */
          var i = 0;
          ctx.font = label.font;
          ctx.fillStyle = label.fill;
          ctx.strokeStyle = label.stroke;
          strings.forEach(function(text, h1) {
            /** @type {number} */
            var ty = (1 + h1 + m1 / 3) * 20;
            ctx.strokeText(text, 0, ty);
            ctx.fillText(text, 0, ty);
          });
        });
        this._log(canvas);
        return canvas;
      };
```
[Go back to top](#tracker-descriptions)

## Infolinks
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Infolink's privacy policy States:

`https://www.infolinks.com/privacy-policy/`

>We use cookies and other similar tracking technologies (such as pixel tags and web or browser caches) to collect information automatically from End Users’ devices. They help us identify unique browsers or devices used by an End User and to perform functions like, for example, limiting the same ad from continuously reappearing, ensuring that ads are properly displayed on our Publisher Clients’ Digital Properties, and serving an ad to the End User.  
  
>Specifically, the information we collect automatically may include IP address, operating system type and version, browser type and version, cookie ID, an individual’s activities on the Infolinks Properties, and other information about the individual’s system and connection and how the individual interacts with the Infolinks Properties and other websites.

[Go back to top](#tracker-descriptions)

## iShumei
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://static.fengkongcloud.com/fpv2.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "24px 'Arial'", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "#e88", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#f99", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"http://www.ishumei.com\",2,15]", "operation": "call"}, {"value": "rgba(120, 180, 0, 0.7)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"http://www.ishumei.com\",4,17]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## IslayTech
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://connect.islay.tech/analyzer/collector.min.js?x=1549440528024`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    function _0x46db02() {
        var _0x39dd11 = document[isl6_0x2b5b('0xe')](isl6_0x2b5b('0xf'));
        var _0x5927cb = _0x39dd11[isl6_0x2b5b('0x10')]('2d');
        var _0x479968 = isl6_0x2b5b('0x26');
        _0x5927cb[isl6_0x2b5b('0x27')] = isl6_0x2b5b('0x28');
        _0x5927cb['font'] = '14px\x20\x27Arial\x27';
        _0x5927cb[isl6_0x2b5b('0x27')] = isl6_0x2b5b('0x29');
        _0x5927cb[isl6_0x2b5b('0x2a')] = isl6_0x2b5b('0x2b');
        _0x5927cb[isl6_0x2b5b('0x2c')](0x7d, 0x1, 0x3e, 0x14);
        _0x5927cb[isl6_0x2b5b('0x2a')] = isl6_0x2b5b('0x2d');
        _0x5927cb[isl6_0x2b5b('0x2e')](_0x479968, 0x2, 0xf);
        _0x5927cb[isl6_0x2b5b('0x2a')] = isl6_0x2b5b('0x2f');
        _0x5927cb[isl6_0x2b5b('0x2e')](_0x479968, 0x4, 0x11);
        return _0x39dd11['toDataURL']();
    }


```
2. Sends computed fingerprint back to server
```
'Ping': function() {
        var _0x333aba = new Object();
        _0x333aba['id'] = isl6_0x19b192;
        isl6_0x465b5d = isl6_0x465b5d + 0x1;
        _0x333aba[isl6_0x2b5b('0xd8')] = isl6_0x465b5d;
        _0x333aba[isl6_0x2b5b('0xd4')] = isl6_0x8f8a3b * isl6_0x186dc3;
        this[isl6_0x2b5b('0xd9')](_0x333aba, 0x1);
        if (isl6_0x1d0913 != '') {
            _0x333aba['id'] = isl6_0x1d0913;
            this[isl6_0x2b5b('0xd9')](_0x333aba, 0x2);
        }
    }


```

[Go back to top](#tracker-descriptions)

## ismatlab.com
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ismatlab.com/cp/public/js/cp.js?id_adm=07948ed229ec4410a2f25c62a87188e8&sys=10012424.UA&smpl=on`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0,
                excludeAudioIOS11: !0,
                excludeEnumerateDevices: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
function h(i) {
        void 0 === i && (i = {});
        var o = void 0,
            l = void 0,
            c = g();
        if (null === c) return 0;
        var u = c.src,
            h = document.referrer;
        ref = "" != h ? new URL(document.referrer).hostname : "";
        var v = t("pa");
        if (void 0 !== e.__cpSessionIdValue && void 0 !== e.__cpSessionVisitNum) o = e.__cpSessionIdValue, y = e.__cpSessionVisitNum;
        else {
            o = null;
            var y = 1;
            if (null == v) o = p();
            else {
                var S = v.split("+", 2);
                o = S[0], 2 == S.length && (y = S[1]);
                var C = location.host;
                ref != C ? (o = p(), y = 1) : y = 1 * y + 1
            }
            e.__cpSessionIdValue = o, e.__cpSessionVisitNum = y, n(o + "+" + y, "pa")
        }
        void 0 === i.quick_start && (i.quick_start = 0), i.seance = o, i.visit_num = y, "" != h && (h = encodeURIComponent(h), i.transition = h);
        var w = m(u, "cookie_parameter");
        null != w && (i.cookie_parameter = w);
        var T = m(u, "sys");
        null != T && (i.sys = T);
        var x = m(u, "id_adm");
        null != x && (i.id_adm = x);
        var M = m(u, "id");
        null != M && (i.id = M);
        var A = m(u, "banner_id");
        null != A && (i.banner_id = A);
        var B = m(u, "agent_id");
        null != B && (i.agent_id = B);
        var P = m(u, "cid");
        null != P && (i.cid = P);
        var b = m(u, "ch");
        null != b && (i.ch = b);
        var E, _ = m(u, "smpl");
        null != _ && (i.smpl = _), E = navigator.userAgent || "", /(iPod|iPhone|iPad|Macintosh)/.test(E) && /AppleWebKit/.test(E) || (void 0 !== window.performance.navigation.redirectCount && (i.redirect_count = window.performance.navigation.redirectCount), void 0 !== window.performance.navigation.type && (i.navigation_type = window.performance.navigation.type), void 0 !== window.performance.timing.navigationStart && (i.navigation_start_datetime = Math.round(window.performance.timing.navigationStart / 1e3))), void 0 === l && (l = m(u, "resource")), null != l ? i.resource = encodeURIComponent(l) : l = window.location.href, i.device_memory = navigator.deviceMemory || -1, void 0 !== a && (i.fingerPrintData = a), void 0 !== r && (i.fingerPrintVersion = r), void 0 !== s && (i.fingerPrintGpu = s), void 0 !== d && (i.fingerPrintFonts = d), -1 === l.indexOf(atob("ZGVmYXVsdC5sb2M=")) && -1 === l.indexOf(atob("cHJpdmF0MjQucHJpdmF0YmFuay51YQ==")) || (i.resource = encodeURIComponent(l)), ["cHJpdmF0MjQucHJpdmF0YmFuay51YQ==", "ZGVmYXVsdC5sb2M=", "cDI0ZnV0LmNlYi5sb2M="].indexOf(btoa(encodeURIComponent(location.host))) >= 0 && sessionStorage.setItem("locationHash", location.hash), f(i),
            function e() {
                ["cHJpdmF0MjQucHJpdmF0YmFuay51YQ==", "ZGVmYXVsdC5sb2M=", "cDI0ZnV0LmNlYi5sb2M="].indexOf(btoa(encodeURIComponent(location.host))) >= 0 && sessionStorage.getItem("locationHash") != location.hash && (i.transition = sessionStorage.getItem("locationHash"), sessionStorage.setItem("locationHash", location.hash));
                window.location.href !== l ? (n(parseInt(t("fp")) + 1, "fp"), l = window.location.href, i.resource = encodeURIComponent(l), f(i), window.setTimeout(e, 500)) : window.setTimeout(e, 500)
            }()
    }

```

[Go back to top](#tracker-descriptions)

## Itch
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://static.itch.io/widget.min.js?1549413662`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            return (new Fingerprint2).get(function(_this) {
                return function(res) {
                    if (res) {
                        return _this.form.find(".bp_input").val(res)
                    }
                }
            }(this))

```
[Go back to top](#tracker-descriptions)

## JSE
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://jsecoin.com` describes its service as a javascript crypto miner.

> JSECoin could be the solution. An unobtrusive code snippet is placed on your site which then runs the JSECoin miner on your visitors' devices whilst they browse your website.
### Technical Review
1. Script checks available crypto APIs before performing various actions

```
      if (window.crypto && window.crypto.subtle) {
        stringify(code, i).then(function(i) {
          if (i.substr(0, d) === get(d)) {
            /** @type {boolean} */
            rc = true;
            call_user_is_writing(selector + "," + i + "," + options.pubID + "," + options.uniq + "," + options.siteID + "," + options.subID);
            console.log("Found Hash! : " + i);
          }
        });
      } else {
```

[Go back to top](#tracker-descriptions)

## justuno
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Justuno’s privacy policy states: 
 
`https://www.justuno.com/legal/privacy-policy/`
 
>"Notwithstanding any other provision, we partner with third parties that collect information across various channels, including offline and online, for purposes of delivering more relevant advertising to you or your business. A hashed version of your email address, which can not be un-hashed for the use of sending any emails, may be sent to our partners to help recognize you across different channels and platforms, including but not limited to, computers, mobile devices, including TV addressability, over time for advertising, analytics, attribution, and reporting purposes. The information requested and collected from you may vary."
> 
>"Non-Identifiable Data: When you interact with Justuno through the Services, we receive and store certain personally non-identifiable information. Such information, which is collected passively using various technologies, cannot presently be used to specifically identify you, unless it is combined with Personal Information. Justuno may store such information itself or such information may be included in databases owned and maintained by Justuno affiliates, agents or service providers. We may use such information and pool it with other information to track, for example, the total number of visitors to our Site, the number of visitors to each page of our Site, and the domain names of our visitors’ Internet service providers"

[Go back to top](#tracker-descriptions)

## KISSmetrics
This service has been classified as `Analytics` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Kissmetrics' privacy policy States:

`https://www.kissmetricshq.com/privacy/`

>Visitors to Metrics Enterprises Clients’ Websites - Our Clients may use customized and proprietary Metrics Enterprises code, software and/or services (“Service(s)”) to obtain information regarding the activities that users engage in while visiting their web pages (“Client User Data”). When a user visits a website that uses Metrics Enterprises Service, Metrics Enterprises code contained on the website contacts Metrics Enterprises servers and enables Metrics Enterprises to collect Client User Data. Some Clients may also use their own code to obtain Client User Data and then send such information to Metrics Enterprises servers. Client User Data may include Personally Identifiable Information, including, but not limited to, the types of information listed for Metrics Enterprises Client Information above.  
  
>In addition, Metrics Enterprises may collect certain information about a Client’s visitor’s computer that may be provided by the visitor’s browser. This includes browser information, operating system information, mobile device information, IP address, time of visit, and the referring site, application, or service. Such information may be collected and shared with the Metrics Enterprises Client even though not specifically requested by the Client.  
  
>Web Beacons. Metrics Enterprises may also collect certain information using Web Beacons. “Web Beacons” are electronic images that may be used on Metrics Enterprises Website, in Metrics Enterprises Service, or in our email communications. They are used, for example, to count website visits or to tell if an email has been opened and acted upon.

Kissmetrics' website states: 

`https://www.kissmetricshq.com/kissmetrics-vs-google-analytics/` (1)  

>When someone uses multiple devices and browsers, Kissmetrics connects all their data to a single person. (1)  
  
'https://www.kissmetricshq.com' (2)

>See a user’s full customer journey across devices (2) 


[Go back to top](#tracker-descriptions)

## Kitewheel
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.kitewheel.com/webTrack.v1.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Konduto
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://i.k-analytix.com/k.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var V = document.createElement("canvas");
        if (V.getContext && V.getContext("2d")) {
            var W = V.getContext("2d");
            W.textBaseline = "top";
            W.font = "9px 'Arial'";
            W.textBaseline = "alphabetic";
            W.fillStyle = "#c392a1";
            W.fillRect(112, 3, 51, 18);
            W.fillStyle = "rgba(16, 175, 74, 0.002)";
            W.fillText("http://%TQBF.jumps.over.t.lazy.dog/?E=1&F=0", 3, 14);
            W.fillStyle = "rgba(151, 210, 2, 0.002)";
            W.fillText("http://%TQBF.jumps.over.t.lazy.dog/?E=1&F=0",
                4, 20);
            U = V.toDataURL()
        } else U = null;
        Q.L = U;
        var ua = [];
        if (navigator.mimeTypes)
            for (var Y = 0; Y < navigator.mimeTypes.length; Y++) navigator.mimeTypes[Y] && ua.push(navigator.mimeTypes[Y].type);
        Q.mimeTypes = ua;
        P.e = Q.referrer;
        P.f = Q.F;
        P.g = Q.href;
        P.h = Q.G;
        Q.language && (P.i = Q.language);

```
2. Sends computed fingerprint back to server
```
    function l(a, b) {
        var c = e(a, null, null, !1, !0),
            f = "?pk=" + a.B,
            f = f + ("string" === typeof b ? "&" + b : ""),
            d;
        d = window.XDomainRequest ? new window.XDomainRequest : window.XMLHttpRequest ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP");
        f = (location.protocol.match("http") ? location.protocol : "http:") + "//i.konduto.com/v1" + f;
        d.open("POST", f, !0);
        try {
            d.send(c)
        } catch (g) {}
    }

```

[Go back to top](#tracker-descriptions)

## LeadsHub
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://cdn.ztsrv.com/js/0.5.0/ztag.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        g = function() {
            if (!o()) return void 0;
            var t = document.createElement("canvas"),
                e = t.getContext("2d"),
                n = "http://valve.github.io";
            return e.textBaseline = "top", e.font = '14px "Arial"', e.textBaseline = "alphabetic", e.fillStyle = "#f60", e.fillRect(125, 1, 62, 20), e.fillStyle = "#069", e.fillText(n, 2, 15), e.fillStyle = "rgba(102, 204, 0, 0.7)", e.fillText(n, 4, 17), t.toDataURL()
        },

```
2. Sends computed fingerprint back to server
```
Request URL: http://us-west-2-v2-t.ztsrv.com/1/i/REMOVED;za/p.gif

```
[Go back to top](#tracker-descriptions)

## LiveRamp
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
LiveRamp's privacy policy States:

`https://liveramp.com/privacy/service-privacy-policy/`

>LiveRamp provides Connectivity Services designed to enable our clients to reach consumers with greater efficiency and more relevant messages across various digital channels, including online, mobile, email, and addressable TV. 

>LiveRamp Mobile Connectivity Services - Connectivity Services for mobile ID integrations are similar to cookie integrations except they use the mobile advertising ID assigned to the device instead of a cookie – namely the Apple ID for Advertising (IDFA) and the Android Advertising ID (AAID). We associate the LiveRamp ID with the mobile ID just like we would associate the cookie. LiveRamp links marketing platform partners, third party data providers, and data from a brand to mobile devices through the LiveRamp ID. 

>Connectivity services work across channels - Due to technical differences across the channels, LiveRamp uses different approaches tailored specifically to each channel to provide our Connectivity Services. The common basis of these services is an ID that LiveRamp assigns to an individual. The ID may be used in a personally identifiable state or in a manner that is not used to identify the individual, depending on the channel and the use.

>LiveRamp collects certain types of information in connection with our Connectivity Services. We also collect other data such as IP address, mobile device ID, and browser and operating system type and version. 

LiveRamp's website states:

`https://liveramp.com/our-platform/identity-graph/` (1)  

>Our identity graph helps you better personalize, target, and measure the success of your marketing campaigns and communications by combining individual-level or household-level data across devices, and channels, as well as offline and online interactions.  
  
>LiveRamp’s identity graph provides an omnichannel view of the consumer. Our offline data is based on touch-points from the real world that are deterministically and anonymously tied with online identifiers to provide a people-based omnichannel view of your target audience.
  
>Our identity graph was designed to enforce privacy and keep customer data safe while providing data-driven use cases for comprehensive marketing campaigns across devices and channels. (1)  
  
`https://liveramp.com/our-platform/omnichannel-ecosystem/` (2)

>LiveRamp ties online and offline data into a single, persistent identifier to provide a clear, omnichannel view of the customer. (2)

[Go back to top](#tracker-descriptions)

## Lotame
This service has been classified as `Analytics` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Lotame's privacy policy States:

`https://www.lotame.com/about-lotame/privacy/lotames-products-services-privacy-policy/`

>Technical identifiers may be used to identify your device and typically include:  
>- Cookies  
>- Mobile advertising identifiers (Apple IDFA and Google AAID)  
>- IP address  
>- Non-personal data inferred from an IP address, such as non-precise geo-location data  
>- Non-cookie technologies  
  
>Lotame uses the information it collects and receives to:  
>- Identify relationships between different browsers and devices  
>- Analyze the effectiveness of online advertising campaigns  
>- Provide aggregated information about user interests  
>- Attribute user interests to browsers and devices  
>- Test the accuracy of certain products, including cross-device matching  
  
>Lotame’s clients generally use First Party Data, along with Third Party Data provided by Lotame, to:  
>- Deliver targeted advertising campaigns to users across devices  
>- Serve targeted content to users across devices

Lotame's website states: 

`https://www.lotame.com/back-to-basics-what-is-identity-resolution/` (1)  

>Identity resolution is the process of combining multiple identifiers across devices and touchpoints with data points collected along the way to build a cohesive, omnichannel view of your consumers, so you can reach them when and where they are most likely to engage along the sales funnel...At Lotame, we more commonly think of this practice as cross-device identification or cross-device targeting (1)  
  
`https://www.lotame.com/products/lotame-connect/people-based-id-solution/` (2)

>Cartographer clusters and connects your people across IDs, browsers, devices, and domains. So a consumer who visits your abc.com site would be connected to all the instances of their identity, including their visit to your def.com site. (2)


[Go back to top](#tracker-descriptions)

## lptracker
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://stats.lptracker.io/lpt_widget/out/main.min.js?2.20.0-312-g9dbe2215e8-dirty`
1. Script embeds on open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

2. Sends fingerprint to tracking company, `https://stats.lptracker.io/track`
```
{"site_id":62106,"fingerprint_hash":"XXXXXXXXXXX","version":"2.20.0-312-g9dbe2215e8-dirty","page":"https://green-game.ru/","domain":"green-game.ru","referer":"https://green-game.ru/"}: 
   ```
[Go back to top](#tracker-descriptions)

## MaxMind
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://device.maxmind.com/js/device.js`
1. Script generates fingerprint by querying various device properties:
```
        c = function() {
            var e, t;
            try {
                e = document.createElement("canvas"), t = e.getContext("2d")
            } catch (n) {}
            return t ? (t.fillStyle = "red", t.fillRect(30, 10, 200, 100), t.strokeStyle = "#1a3bc1", t.lineWidth = 6, t.lineCap = "round", t.arc(50, 50, 20, 0, Math.PI, !1), t.stroke(), t.fillStyle = "#42e1a2", t.font = "15.4px 'Arial'", t.textBaseline = "alphabetic", t.fillText("PR flacks quiz gym: TV DJ box when? â˜ ", 15, 60), t.shadowOffsetX = 1, t.shadowOffsetY = 2, t.shadowColor = "white", t.fillStyle = "rgba(0, 0, 200, 0.5)", t.font = "60px 'Not a real font'", t.fillText("Noéª—", 40, 80), i(e.toDataURL())) : null
        },

        B = function() {
            if (navigator.getBattery) navigator.getBattery().then(function(e) {
                var t = O();
                return t.battery = {
                    charging: e.charging,
                    chargingTime: e.chargingTime,
                    dischargingTime: e.dischargingTime,
                    level: e.level
                }, t
            }).then(function(e) {
                C(function(t) {
                    e.audio = t, D(e, 6)
                })
            });
            else {
                var e = O();
                C(function(t) {
                    e.audio = t, D(e, 6)
                })
            }
        };

```
2. Sends computed fingerprint back to server
```
    var D, M = function(e) {
            return "https://" + ("d-ipv" + e + ".mmapiws.com") + "/ant_squire"
        },
        x = function(e, t, n) {
            var o = e.responseText.split(/;/),
                r = o[0],
                i = o[1],
                a = parseInt(o[2], 10);
            "undefined" != typeof i && A(r, i), 6 === t && 6 === a && D(n, 4)
        };
    D = function(e, t) {
        var o, r, i = M(t);
        if (e.storedIds = y(), r = n(e), "Microsoft Internet Explorer" === navigator.appName && window.XDomainRequest && 10 !== window.document.documentMode) o = new XDomainRequest, o.onload = function() {
            x(o, t)
        }, o.onprogress = function() {}, o.ontimeout = function() {}, o.onerror = function() {};
        else {
            try {
                o = new window.XMLHttpRequest
            } catch (a) {}
            if (!o) try {
                o = new window.ActiveXObject("Microsoft.XMLHTTP")
            } catch (a) {}
            if (!o) return;
            o.onreadystatechange = function() {
                4 === o.readyState && 200 === o.status && x(o, t, e)
            }
        }
        try {
            o.open("POST", i, !0), "function" == typeof o.setRequestHeader && o.setRequestHeader("Content-Type", "text/plain;charset=UTF-8"), o.send(r)
        } catch (a) {}
    };

```

[Go back to top](#tracker-descriptions)

## MediaMath
This service has been classified as `Email`, `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
MediaMath's Privacy Policy States:

`https://www.mediamath.com/privacy-policy/`

>Like most digital marketing platforms, MediaMath uses cookies and other technologies to recognize browsers and devices and collect the categories of personal data described above (Bid request data and impression data, pixel data and other client data, third party segment data and other third party data) 

>We may assign a unique identifier called a MediaMath ID to your browser, your devices, such as your mobile device, connected television, or over-the-top television devices (""OTT TV Device""), or other screens you may encounter when we serve an ad to it or when you use it to access a client’s digital properties. Digital Properties include websites, emails, apps (""Digital Properties""). The MediaMath ID enables the Platform to determine within a reasonable level of confidence that a browser or devices is the same one with which the Platform has previously interacted. In some cases, based on data we receive from our clients or partners, we are able to infer within a reasonable probability that a particular browser or device should be associated with the same MediaMath ID. Where we are able to associate more than one browser or device with the same MediaMath ID, we may use this information to deliver targeted ads across multiple browsers or devices. This is sometimes referred to as cross-device advertising.


[Go back to top](#tracker-descriptions)

## Mercadopago
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://content.mercadopago.com/fp/check.js;CIS3SID=2A8E1955E35B694A5EF6292EA1DB8B21?org_id=jk96mpy0&session_id=95524399a59f3fedefeea41a7fde6a07&nonce=d521cdd0c52860ee`
1. Script generates fingerprint by querying various device properties:
```
var td_3X = ['Andale Mono', 'Arial', 'Arial Black', 'AR PL UKai CN', 'AR PL UMing CN', 'Batang', 'Bitstream Vera Sans', 'Comic Sans MS', 'Courier New', 'Cursor', 'DejaVu LGC Sans', 'DejaVu Sans', 'DejaVu Sans Mono', 'DejaVu Serif', 'Dotum', 'Droid Sans', 'FreeMono', 'FreeSans', 'FreeSerif', 'gargi', 'Garuda', 'Georgia', 'Hei', 'Impact', 'KacstArt', 'Kedage', 'Khmer OS', 'Khmer OS System', 'Kinnari', 'Liberation Sans Narrow', 'Lohit Bengali', 'Loma', 'Lucida Bright', 'Lucida Sans', 'Lucida Sans Typewriter', 'Luxi Mono', 'Mallige', 'Meera', 'Monospace', 'mry_KacstQurn', 'Mukti Narrow', 'NanumGothic', 'NanumMyeongjo', 'Nimbus Sans L Condensed', 'Norasi', 'OpenSymbol', 'ori1Uni', 'Phetsarath OT', 'Pothana2000', 'Purisa', 'Rachana', 'Rekha', 'Saab', 'Sawasdee', 'System', 'TakaoPGothic', 'Times', 'Times New Roman', 'TlwgMono', 'TlwgTypewriter', 'Tlwg Typist', 'Tlwg Typo', 'Trebuchet MS', 'Ubuntu', 'Ubuntu Condensed', 'Ume Gothic', 'Ume Mincho', 'Ume P Gothic', 'Ume P Mincho', 'Ume UI Gothic', 'Umpush', 'UnBatang', 'UnDinaru', 'UnDotum', 'UnGraphic', 'UnGungseo', 'UnPilgi', 'Untitled1', 'Utopia', 'Vemana2000', 'Verdana', 'Waree', 'Webdings', 'WenQuanYi Bitmap Song', 'WenQuanYi Micro Hei', 'WenQuanYi Zen Hei'];

    this.getFPParams = function() {
        var td_LV = td_0I.tdz_7073d30cdca54f9ea06dae79c52b48fa.td_f(0, 4);
        if (typeof td_V5 === [][
                []
            ] + "") {
            if (typeof td_Rl !== [][
                    []
                ] + "" && td_Rl.readyState === Number(218714).toString(25)) {
                td_V5 = td_Rl.result ? false : true;
            } else {
                return null;
            }
        }
        td_LV += td_V5 ? td_0I.tdz_7073d30cdca54f9ea06dae79c52b48fa.td_f(4, 3) : td_0I.tdz_7073d30cdca54f9ea06dae79c52b48fa.td_f(7, 2);
        return td_LV;
    };

```
[Go back to top](#tracker-descriptions)

## MinerAlt
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://mineralt.io` describes its service as a javascript crypto miner.

> Use safe javascript browser miner to mine cryptocurrency online, using your web site visitors’ CPU power. The most effective web miner on the market with the highest mining ratio
### Technical Review
Observered on: http://ictlounge.com
- CPU utilization
    - Baseline load: 388.23%
    - Cryptomining script blocked: 14.39%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://ictlounge.com",
        "isBlockingMiners": false,
        "miners": [
            "tulip18.com"
        ],
        "miner_requests": [
            "https://tulip18.com/amo.js"
        ],
        "run_stats": {
            "cpu": 388.2296195652174,
            "memory": "490.3 MB"
        },
        "workers_created": [
            "blob:https://ictlounge.com/3514c841-7432-4e71-951e-657d78af9455",
            "blob:https://ictlounge.com/3514c841-7432-4e71-951e-657d78af9455",
            "blob:https://ictlounge.com/3514c841-7432-4e71-951e-657d78af9455",
            "blob:https://ictlounge.com/3514c841-7432-4e71-951e-657d78af9455",
            "blob:https://ictlounge.com/3514c841-7432-4e71-951e-657d78af9455"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://ictlounge.com",
        "isBlockingMiners": true,
        "miners": [
            "tulip18.com"
        ],
        "miner_requests": [
            "https://tulip18.com/amo.js"
        ],
        "run_stats": {
            "cpu": 14.38548197492163,
            "memory": "429.9 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## Minescripts
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Observered on: http://expert4help.ru
- CPU utilization
    - Baseline load: 453.47%
    - Cryptomining script blocked: 12.74%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_domain": "http://expert4help.ru",
        "isBlockingMiners": false,
        "miners": [
            "minescripts.info",
            "cdn.minescripts.info"
        ],
        "miner_requests": [
            "https://cdn.minescripts.info/c/wKjM.js"
        ],
        "run_stats": {
            "cpu": 453.47300396727,
            "memory": "652.1 MB"
        },
        "workers_created": [
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd",
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd",
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd",
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd",
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd",
            "blob:https://api.sslverify.info/3688505a-ede5-4f5c-8880-0fd53b6b0fdd"
        ]
    },
    "WhenBlocked": {
        "test_domain": "http://expert4help.ru",
        "isBlockingMiners": true,
        "miners": [
            "minescripts.info",
            "cdn.minescripts.info"
        ],
        "miner_requests": [
            "https://cdn.minescripts.info/c/wKjM.js"
        ],
        "run_stats": {
            "cpu": 12.740271885062246,
            "memory": "581.2 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## MineXMR
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Observered on: http://moviedream.ws
- CPU utilization
    - Baseline load: 646.56%
    - Cryptomining script blocked: 11.57%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://moviedream.ws",
        "isBlockingMiners": false,
        "miners": [
            "minexmr.stream"
        ],
        "miner_requests": [
            "https://minexmr.stream/webmr.js"
        ],
        "run_stats": {
            "cpu": 646.5359477124183,
            "memory": "589.1 MB"
        },
        "workers_created": [
            "blob:https://moviedream.ws/62f64f25-7be6-4539-8fa0-5617e0773165",
            "blob:https://moviedream.ws/484e838d-e581-4c3d-9453-fe3f33fd7ce0",
            "blob:https://moviedream.ws/82337e0b-915f-4644-af6f-4814566a6eb5",
            "blob:https://moviedream.ws/94fea957-4b4d-4ab9-ab8e-5ebe0a759532",
            "blob:https://moviedream.ws/f5a36d5d-479d-4771-8030-56aa361b8fea",
            "blob:https://moviedream.ws/3cc62465-579f-4cc5-b8f1-06e7ad1c1e57",
            "blob:https://moviedream.ws/123f517d-046d-4441-8026-a6b19de8a572",
            "blob:https://moviedream.ws/9c6ed56c-95a1-4ede-b206-50d4f25bc9ad",
            "blob:https://moviedream.ws/d37d0afa-c6f5-4415-b763-53b3f309d520",
            "blob:https://moviedream.ws/808b073f-f3da-45ef-94b6-8289603bead9",
            "blob:https://moviedream.ws/4d096716-d4a0-4d8e-98e3-a0f2f0b2d528",
            "blob:https://moviedream.ws/c1b5b807-034a-4b34-94dc-dc74ea8ff56b"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://moviedream.ws",
        "isBlockingMiners": true,
        "miners": [
            "minexmr.stream"
        ],
        "miner_requests": [
            "https://minexmr.stream/webmr.js"
        ],
        "run_stats": {
            "cpu": 11.568958173609335,
            "memory": "447.9 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## Mobials
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.moba.mobials.com/v1/moba.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        t.default = function() {
            return new Promise(function(e, t) {
                if (!r) return t("Fingerprint2 library not loaded");
                var n = function() {
                    try {
                        (new r).get(function(t, n) {
                            return e(t)
                        })
                    } catch (e) {
                        t(e)
                    }
                };
                window.requestIdleCallback ? window.requestIdleCallback(n) : setTimeout(n, 500)
            })
        }

```
2. Sends computed fingerprint back to server
```
        t.default = function() {
            return Promise.all([r.get("mobAuserId"), r.get("crossable")]).then(function(e) {
                var t = e[0],
                    n = e[1];
                if (t) return {
                    userId: t,
                    crossable: function(e) {
                        return "true" === e
                    }(n)
                };
                var a = document.createElement("iframe"),
                    o = i.getOnce(function(e) {
                        return "mobials.userId.ready" === e.data.action
                    }, "https://moba.mobials.com").then(function() {
                        return i.postMessageRpc(a.contentWindow, {
                            action: "mobials.userId.request"
                        }, "https://moba.mobials.com")
                    }).then(function(e) {
                        return r.set("mobAuserId", e.data.userId), r.set("crossable", e.data.crossable), {
                            userId: e.data.userId,
                            crossable: e.data.crossable
                        }
                    });
                return a.setAttribute("id", "mobialsAf"), a.setAttribute("width", "1"), a.setAttribute("height", "1"), document.body.appendChild(a), a.setAttribute("src", "https://moba.mobials.com/v1/user_id"), a.style.border = "0", a.style.visibility = "hidden", o
            })
        }

```

[Go back to top](#tracker-descriptions)

## Mystighty
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://mystighty.info/c/D.9m6Qb/2n5-lwSoWOQW9hM/jLcv3-M/z/g/xGN/Sp0UyXNUzFcnzmO/DOUE1M`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };
```
2. Sends computed fingerprint back to server
```
function logPageView(customData) {
            var request;
            request = configTrackerUrl + "?url=" + escapeWrapper(documentAlias.location.href) + "&ref=" + escapeWrapper(getReferrer()) + "&name=" + escapeWrapper(documentAlias.title) + "&avmws=" + escapeWrapper(getCookie("avmws")) + "&rand=" + Math.random() + "&lib=1";
            if (isDefined(customData)) {
                request += "&data=" + escapeWrapper(stringify(customData))
            }
            if (window.requestIdleCallback) {
                requestIdleCallback(function() {
                    try {
                        Fingerprint2.get({
                            excludeFlashFonts: true,
                            excludeJsFonts: true
                        }, function(components) {
                            var values = components.map(function(component) {
                                return component.value
                            });
                            var murmur = Fingerprint2.x64hash128(values.join(""), 31);
                            request += "&fingerprint=" + escapeWrapper(murmur);
                            getScript(request)
                        })
                    } catch (e) {
                        getScript(request)
                    }
                })
            } else {
                setTimeout(function() {
                    try {
                        Fingerprint2.get({
                            excludeFlashFonts: true,
                            excludeJsFonts: true
                        }, function(components) {
                            var values = components.map(function(component) {
                                return component.value
                            });
                            var murmur = Fingerprint2.x64hash128(values.join(""), 31);
                            request += "&fingerprint=" + escapeWrapper(murmur);
                            getScript(request)
                        })
                    } catch (e) {
                        getScript(request)
                    }
                }, 500)
            }
        }

```

[Go back to top](#tracker-descriptions)

## Negishim
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://www.negishim.com/accessibility/accessibility_pro_group255.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var fps = "";
try {
    var fp = new Fingerprint2;
    fp.get(function(e, t) {
        fps = e
    })
} catch (e) {
    fps = ""
}

```
2. Sends computed fingerprint back to server:
```
var negishim_base = "https://www.negishim.com/accessibility/",
    checkes = 0;

var a = window.location.href.replace("?", "^").replace(/&/g, "~");
    e += "<img id='accessibility_icon' src='" + negishim_base + "wheelchair.ashx?is_pro=1&fps=" + fps + "&v=255&css_style=" + css_style + "&src=" + window.location.host + "&purl=" + a + "&ii=" + (new Date).getTime() + "' alt='נגישות' class='accessibility_component' aria-hidden=\"true\"/>"


```

[Go back to top](#tracker-descriptions)

## NeroHut
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Observered on: http://webfreer.com
- CPU utilization
    - Baseline load: 29.76%
    - Cryptomining script blocked: 13.37%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://webfreer.com",
        "isBlockingMiners": false,
        "miners": [
            "nerohut.com"
        ],
        "miner_requests": [
            "https://nerohut.com/srv/?key=0fc7e2a5fe172c0b7fb20ab45eaf39eb"
        ],
        "run_stats": {
            "cpu": 29.7563025210084,
            "memory": "512.3 MB"
        },
        "workers_created": [
            "blob:https://nhsrv.cf/94672bb1-4bf9-424c-9b7b-3fbdf8ca91c3",
            "blob:https://nhsrv.cf/aa8ff8f1-4c0d-4638-91c3-235f4af81377",
            "blob:https://nhsrv.cf/b4529bd4-051d-4573-a063-6b80bbbe8d3a",
            "blob:https://nhsrv.cf/8510f1a8-3839-48be-892e-c763b3aed4a7",
            "blob:https://nhsrv.cf/90574b5f-a020-4e8d-9a72-ab4439ef033f",
            "blob:https://nhsrv.cf/fcf17cda-1602-4ac1-871e-ca48cf27233f",
            "blob:https://nhsrv.cf/801026e5-4063-4081-8072-f8dbdd8b99ac",
            "blob:https://nhsrv.cf/b4ff23c1-013f-4919-83bf-e5dc18fd0019",
            "blob:https://nhsrv.cf/b8762dd8-dfdd-40e4-bff4-2e9758b29807",
            "blob:https://nhsrv.cf/9064275f-418c-4c0f-9ec4-756dddc15c09",
            "blob:https://nhsrv.cf/116ec33c-375b-44cc-a34e-15cc4173b4c0",
            "blob:https://nhsrv.cf/323faead-22bc-4082-a959-5d02b881dbb3"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://webfreer.com",
        "isBlockingMiners": true,
        "miners": [
            "nerohut.com"
        ],
        "miner_requests": [
            "https://nerohut.com/srv/?key=0fc7e2a5fe172c0b7fb20ab45eaf39eb"
        ],
        "run_stats": {
            "cpu": 13.36764705882353,
            "memory": "410.8 MB"
        },
        "workers_created": []
    }
}
```
[Go back to top](#tracker-descriptions)

## OneAd
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ad-specs.guoshipartners.com/static/js/isip.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
a.Fingerprint2 = function(a) {
                var b = {
                    swfContainerId: "fingerprintjs2",
                    swfPath: "flash/compiled/FontList.swf"
                };
                this.options = this.extend(a, b), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
            }, a.Fingerprint2.prototype = {
                extend: function(a, b) {
                    if (null == a) return b;
                    for (var c in a) null != a[c] && b[c] !== a[c] && (b[c] = a[c]);
                    return b
                },
                log: function(a) {
                    window.console
                },
                get: function(a) {
                    var b = [];
                    b = this.userAgentKey(b), b = this.languageKey(b), b = this.colorDepthKey(b), b = this.screenResolutionKey(b), b = this.timezoneOffsetKey(b), b = this.sessionStorageKey(b), b = this.localStorageKey(b), b = this.indexedDbKey(b), b = this.addBehaviorKey(b), b = this.openDatabaseKey(b), b = this.cpuClassKey(b), b = this.platformKey(b), b = this.doNotTrackKey(b), b = this.pluginsKey(b), b = this.canvasKey(b), b = this.webglKey(b), b = this.adBlockKey(b), b = this.hasLiedLanguagesKey(b), b = this.hasLiedResolutionKey(b), b = this.hasLiedOsKey(b), b = this.hasLiedBrowserKey(b), b = this.touchSupportKey(b);
                    var c = this,
                        d = c.x64hash128(b.join("~~~"), 31);
                    a(d)
                },


```
2. Sends computed fingerprint back to OneAd:
```
                try {
                    d.src = "//img.onead.com.tw/async?" + ONEAD.to_param({
                        host: "http:" + ONEAD.external_url || "",
                        dt: (new Date).getTime() || "",
                        c1: a.pid || "",
                        c2: a.play_mode || "",
                        p1: c,
                        p2: b,
                        p3: window.location.href || "",
                        p4: document.title || "",
                        p5: document.referrer || "",
                        p6: a.ffp || "",
                        p7: a.cat || "",
                        p8: a.igs || "",
                        p9: a.uigs || "",
                        p10: a.cigs || "",
                        p11: a.ude || "",
                        p12: a.cde || ""
                    })
                } catch (e) {}

```

[Go back to top](#tracker-descriptions)

## OnlineMetrix
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
```
function tmx_run_page_fingerprinting(saveNotifs) {
  if (typeof saveNotifs !== [][[]] + "") {
    saveNotifs(td_3h.tdz_4b218af92da24466911d4ecee3069a1a.td_f(0, 8));
  }
}
```
[Go back to top](#tracker-descriptions)

## OpenX
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
OpenX's Privacy Policy States: 

`https://www.openx.com/legal/privacy-policy/`

>We collect information through Publishers that use our Services. For example, when you visit a website or app and the Publisher sends us a request to show you an ad, we collect certain information about the ad space, you and your device to help inform a Demand Partner’s decision to serve the ad. We also collect information through Demand Partners that use our Services, as well as from other third-party partners. This information we collect can identify your device over time. In particular, we may collect the following categories of information: 
>- Unique online identifiers 
>- Browser information (e.g. browser type, version, language,) 
>- Device information (e.g. screen dimensions, device brand and model) 
>- Internet service information (e.g. Internet Service Provider used by you) 
>- Derived location data (as derived from IP address or GPS (for mobile)) 
>- Precise location data (if you have enabled location services on your device and a Publisher passes that data to us) 
>- Ad reporting or delivery data (e.g. size/type of ad, ad impressions, location/format of ad, data about interactions with the ad) 
>- Interest segments (i.e. inferred information on the behavior or likely interests associated with you) 
>- Retargeting data (i.e. data indicating previous interest in a product or website) 
>- Other data that can be passed in the request to the Demand Partner to inform their decision 

>We primarily recognize your devices through the following identifiers: Cookies and Similar Technologies, Mobile Advertising IDs To help identify your browser and/or possible relationships between different browsers and devices, OpenX or our partners may use the local storage or cache in your browser.

[Go back to top](#tracker-descriptions)

## Origo
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Origo’s privacy policy states:  
 
`https://www.origo.hu/common/20180525-adatvedelmi-es-adatkezelesi-tajekoztato.html`
 
>32. Data to be technically recorded during the operation of the systems: the data of the User's login computer, which are generated during the use of the Service and which are recorded by the System of Data Controllers as an automatic result of the technical processes. The data that is automatically recorded is automatically logged at the time of entry or exit without any separate statement or action by the User." 

[Go back to top](#tracker-descriptions)

## PartyPoker
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://content.iivt.com/ciwic/sp/fingerprint2.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "#000000", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "get"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"❤️🤪🎉👋\",50,70]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Paypal
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.simility.com/b.js`
1. Script generates fingerprint by querying various device properties:
```
        if (e.sync.sd2 = !0, "boolean" == typeof n.cookieEnabled ? e.sync.sd2 = n.cookieEnabled : "string" == typeof n.cookieEnabled && "0" === n.cookieEnabled && (e.sync.sd2 = !1), e.sync.sd4 = "0", "boolean" == typeof n.doNotTrack) e.sync.sd4 = n.doNotTrack ? "1" : "0";
        else if ("number" == typeof n.doNotTrack) try {
            e.sync.sd4 = n.doNotTrack.toString()
        } catch (e) {}
        e.sync.sd6 = n.language, e.sync.sd7 = n.languages;
        try {
            if ("string" == typeof n.languages) e.sync.sd7 = [n.languages];
            else
                for (var i in e.sync.sd7 = [], n.languages) n.languages.hasOwnProperty(i) && e.sync.sd7.push(n.languages[i])
        } catch (t) {
            e.sync.sd7 = [n.language]
        }
        if (e.sync.sd8 = n.maxTouchPoints, "string" == typeof n.maxTouchPoints) try {
            e.sync.sd8 = parseInt(n.maxTouchPoints)
        } catch (t) {
            e.sync.sd8 = 0
        }

        try {
            e.sync.bd17 = function() {
                var e = document.createElement("canvas");
                if (!e || !e.getContext("2d")) return null;
                var t = e.getContext("2d"),
                    n = "QmWnEbRv TcYxUz IlOkPjAhSgDf";
                return t.textBaseline = "top", t.font = "15px 'Arial'", t.textBaseline = "alphabetic", t.fillStyle = "#f60", t.fillRect(122, 1, 66, 22), t.fillStyle = "#069", t.fillText(n, 3, 14), t.fillStyle = "rgba(102, 204, 0, 0.7)", t.fillText(n, 5, 18), d(e.toDataURL().replace("data:image/png;base64,", "")).toString()
            }()
        } catch (e) {}

```
2. Sends computed fingerprint back to server
```
            var a = t.baseHTTPUrl + "/b?c=" + encodeURIComponent(t.sync.cd2) + "&v=" + encodeURIComponent(t.version) + "&ec=" + encodeURIComponent(t.pb) + "&cl=0";
            c(t.sync.cd3) || (a = a + "&si=" + encodeURIComponent(t.sync.cd3)), c(t.sync.sc) || (a = a + "&sc=" + encodeURIComponent(t.sync.sc)), c(t.sync.uc) || (a = a + "&uc=" + encodeURIComponent(t.sync.uc)), c(t.customerEvents) || (a = a + "&e=" + encodeURIComponent(t.customerEvents)), c(t.cDomain) || (a = a + "&cd=" + encodeURIComponent(t.cDomain)), c(i) || (a = a + "&r=" + encodeURIComponent(i)), c(t.startTime) || (a = a + "&st=" + encodeURIComponent(t.startTime));
            var r = o;
            !0 === t.encryptPayload && (r = e(t.pb, o)), c(r) || (t.encryptPayload && r.length < 7e3 ? h(a = a + "&s=" + encodeURIComponent(r), "GET", null, s) : h(a, "POST", r, s))

```

[Go back to top](#tracker-descriptions)

## PerimeterX
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Policy Review
1. PerimeterX Bot Defender provides bot detection using network and behavorial analysis. 

`https://www.perimeterx.com/about/press/2016/2016-07-12-perimeterx-partners-with-ironsource/`
> PerimeterX Bot Defender’s smart behavioral fingerprinting technology is based on hundreds of indicators profiling the user, their browser and network
### Technical Review
1. PerimeterX fingerprints by using several fingerprinting techniques like canvas/font:
```
        function yt(n, t, e) {
            try {
                n.rect(0, 0, 10, 10),
                n.rect(2, 2, 6, 6),
                t.canvasWinding = n.isPointInPath(5, 5, "evenodd") === !1
            } catch (r) {
                t.errors.push("PX429")
            }
            try {
                n.textBaseline = "alphabetic",
                n.fillStyle = "#f60",
                n.fillRect(125, 1, 62, 20)
            } catch (r) {
                t.errors.push("PX428")
            }
            try {
                n.fillStyle = "#069",
                n.font = "11pt no-real-font-123",
                n.fillText("Cwm fjordbank glyphs vext quiz, 😃", 2, 15),
                n.fillStyle = "rgba(102, 204, 0, 0.2)",
                n.font = "18pt Arial",
                n.fillText("Cwm fjordbank glyphs vext quiz, 😃", 4, 45)
            } catch (r) {
                t.errors.push("PX427")
            }
            try {
                n.globalCompositeOperation = "multiply",
                n.fillStyle = "rgb(255,0,255)",
                n.beginPath(),
                n.arc(50, 50, 50, 0, 2 * Math.PI, !0),
                n.closePath(),
                n.fill(),
                n.fillStyle = "rgb(0,255,255)",
                n.beginPath(),
                n.arc(100, 50, 50, 0, 2 * Math.PI, !0),
                n.closePath(),
                n.fill(),
                n.fillStyle = "rgb(255,255,0)",
                n.beginPath(),
                n.arc(75, 100, 50, 0, 2 * Math.PI, !0),
                n.closePath(),
                n.fill(),
                n.fillStyle = "rgb(255,0,255)",
                n.arc(75, 75, 75, 0, 2 * Math.PI, !0),
                n.arc(75, 75, 25, 0, 2 * Math.PI, !0),
                n.fill("evenodd")
            } catch (r) {
                t.errors.push("PX426")
            }
            try {
                t.canvasData = m(e.toDataURL())
            } catch (r) {
                t.errors.push("PX425")
            }
            return t
        }
```
2. Also audio fingerprinting:
```
        function ht(n) {
            try {
                var t = new (window.OfflineAudioContext || window.webkitOfflineAudioContext)(1,44100,44100);
                if (!t)
                    return n(Wr, Wr);
                var e = t.createOscillator()
                  , r = "number" == typeof t.currentTime && t.currentTime || 0;
                e.type = "sine",
                gt(e.frequency, 1e4, r);
                var o = t.createDynamicsCompressor();
                gt(o.threshold, -50, r),
                gt(o.knee, 40, r),
                gt(o.ratio, 12, r),
                gt(o.reduction, -20, r),
                gt(o.attack, 0, r),
                gt(o.release, .25, r),
                e.connect(o),
                o.connect(t.destination),
                e.start(0),
                t.startRendering(),
                t.oncomplete = function(t) {
                    for (var e = 0, r = 4500; r < 5e3; r++)
                        e += Math.abs(t.renderedBuffer.getChannelData(0)[r]);
                    return n(e.toString(), m(e.toString()))
                }
            } catch (i) {
                return n(Wr, Wr)
            }
        }
```
[Go back to top](#tracker-descriptions)

## PinPoll
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Pinpoll's privacy policy states: 

`https://www.pinpoll.com/pdf/data-protection-declaration.pdf`

>Data generated by the software of Pinpoll can be the following data of users and voters: Device-specific information; Location-based information; Website-based information.

[Go back to top](#tracker-descriptions)

## Polen
This service has been classified as `Analytics` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Polen’s Terms of Service [no relevant privacy policy or Data processing agreement] states: 
 
`https://polen.com.br/content/v5/file/termos.pdf`
 
>b. The Polen Browser App is an online tool consisting of an extension installed in Google Chrome browser, which allows the realization of micro donations to Philanthropic Institutions through the reversal of a percentage of the value of purchases made in Partner Stores. References to the Polen Browser App can also be made as: plugin, radius pollinator, pollinator or other terms concerning the tool 
 
>i. Polen does not directly obtain any kind of information from its users. The information is obtained through its Partner Stores, being supplied only those strictly necessary for using the Polen Browser App; 
iii. The information collected by Polen will be applied in the realization of improvements to the tool, and also for the development of new functionalities, which can be used by Polen in other products that will be developed by the company." 

[Go back to top](#tracker-descriptions)

## PPCProtect
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.ppcprotect.com/tracking/va-monitor.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var t = function(e) {
            if (!(this instanceof t)) return new t(e);
            this.options = this.extend(e, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to ppcprotect.com:
```
    new Fingerprint2({}).get(function(e, t) {
        o.hash = e, o.data = t, sendData("https://monitor.ppcprotect.com/v1.0/pageview", {
            _method: "POST",
            ppcuid: i,
            gclid: n,
            uuid: r,
            url: window.location.href,
            ref: decodeURI(document.referrer),
            pvn: a,
            fp: o
        })
    })


```

[Go back to top](#tracker-descriptions)

## PrismApp
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://prismapp-files.s3.amazonaws.com/widget/prism.js?v2`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var Fingerprint2 = PRISM_require("fingerprintjs2")
```

```
                        getCanvasFp: function() {
                            var e = [],
                                t = document.createElement("canvas");
                            t.width = 2e3, t.height = 200, t.style.display = "inline";
                            var i = t.getContext("2d");
                            return i.rect(0, 0, 10, 10), i.rect(2, 2, 6, 6), e.push("canvas winding:" + (i.isPointInPath(5, 5, "evenodd") === !1 ? "yes" : "no")), i.textBaseline = "alphabetic", i.fillStyle = "#f60", i.fillRect(125, 1, 62, 20), i.fillStyle = "#069", this.options.dontUseFakeFontInCanvas ? i.font = "11pt Arial" : i.font = "11pt no-real-font-123", i.fillText("Cwm fjordbank glyphs vext quiz, ðŸ˜ƒ", 2, 15), i.fillStyle = "rgba(102, 204, 0, 0.2)", i.font = "18pt Arial", i.fillText("Cwm fjordbank glyphs vext quiz, ðŸ˜ƒ", 4, 45), i.globalCompositeOperation = "multiply", i.fillStyle = "rgb(255,0,255)", i.beginPath(), i.arc(50, 50, 50, 0, 2 * Math.PI, !0), i.closePath(), i.fill(), i.fillStyle = "rgb(0,255,255)", i.beginPath(), i.arc(100, 50, 50, 0, 2 * Math.PI, !0), i.closePath(), i.fill(), i.fillStyle = "rgb(255,255,0)", i.beginPath(), i.arc(75, 100, 50, 0, 2 * Math.PI, !0), i.closePath(), i.fill(), i.fillStyle = "rgb(255,0,255)", i.arc(75, 75, 75, 0, 2 * Math.PI, !0), i.arc(75, 75, 25, 0, 2 * Math.PI, !0), i.fill("evenodd"), e.push("canvas fp:" + t.toDataURL()), e.join("~")
                        },

```
2. Fingerprint is then sent to api.prismapp.io:
```
BRUNCH_ENV: "production",
            API_ENDPOINT: "https://api.prismapp.io",

```
```
                    var context = this,
                        payload = {
                            device_id: context.shamu.analytics.fingerprint,
                            conversation_id: msgObj.conversation_id,
                            message_id: msgObj.id,
                            channel: context.shamu.config.visitor.channel_name
                        };
                    api.post("/v2/metrics/messages", payload, function() {
                        setTimeout(function() {
                            context.feedMessage({}, msgObj)
                        }, util.exponentialBackoff())
                    }, function(response, xhr) {
                        util.resetExponentialBackoff()
                    })

```

[Go back to top](#tracker-descriptions)

## PrometheusIntelligenceTechnology
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://prometheusintelligencetechnology.com/pit/fp?fp=`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
/*
* Fingerprintjs2 1.5.1 - Modern & flexible browser fingerprint library v2
* PATCHED: https://github.com/cdwiegand/fingerprintjs2.git
* ORIG: https://github.com/Valve/fingerprintjs2
* Copyright (c) 2015 Valentin Vasilyev (valentin.vasilyev@outlook.com)
* Licensed under the MIT (http://www.opensource.org/licenses/mit-license.php) license.

```
2. Fingerprint is then stored to be transmitted back to prometheusintelligencetechnology.com
```
  try {
    var pit = window.prometheus;
    new Fingerprint2().get(function(result, components) {
      console.log('Prometheus fingerprint: ' + result);
      pit.fp2 = result; // compat
      pit.tryAppend(pit.makeRef('script', 'https://prometheusintelligencetechnology.com/pit/fp?fp=' + result));
      pit.passIdAlong('fp2', result);
      pit.tracking = pit.tracking || {};
      pit.tracking.fp2 = result;
    });
  } catch (e) {
    pit.tryAppend(pit.makeRef('script', 'https://prometheusintelligencetechnology.com/pit/fp?fperr=' + e.toString()));
  }})();

```

[Go back to top](#tracker-descriptions)

## Protected Media
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405`
1. Script accesses several Javascript API calls known to invasively fingerprint users. Some examples (APIs captured using [OpenWPM](https://github.com/mozilla/OpenWPM)):
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "203",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"PR flacks quiz gym: TV DJ box when? ?˜ \",15,60]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "203",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"No??—\",40,80]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "207",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"http://abcd.com\",2,15]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "207",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"http://abcd.com\",4,17]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "208",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890\",2,2]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "208",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890\",2,2]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "208",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"123DFHJrtuoe :-( 8YumnxoWerAS\",2,2]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "209",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"123DFHJrtuoe :-( 8YumnxoWerAS\",2,2]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "202",
  "symbol": "CanvasRenderingContext2D.fillText",
  "arguments": "[\"😀🎅👂🔫\",0,20]",
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "344",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "344",
  "symbol": "window.navigator.doNotTrack",
  "arguments": null,
  "value": "unspecified"
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "153",
  "symbol": "window.navigator.oscpu",
  "arguments": null,
  "value": "Intel Mac OS X 10.15"
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "198",
  "symbol": "OfflineAudioContext.createOscillator",
  "arguments": null,
  "value": ""
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "198",
  "symbol": "OscillatorNode.type",
  "arguments": null,
  "value": "sine"
}
```
```json
{
  "top_level_url": "https://www.metacafe.com/",
  "script_url": "https://js.ad-score.com/score.min.js?pid=1000569#tid=&l1=&l2=&l2=&l3=&l4=&l5=www.metacafe.com&l6=&cb=0.7452266308619405",
  "script_line": "341",
  "symbol": "RTCPeerConnection.setLocalDescription",
  "arguments": "[\"{\\\"type\\\":\\\"offer\\\",\\\"sdp\\\":\\\"v=0\\\\r\\\\no=mozilla...THIS_IS_SDPARTA-78.0.1 XXXXX 0 IN IP4 0.0.0.0\\\\r\\\\ns=-\\\\r\\\\nt=0 0\\\\r\\\\na=fingerprint:sha-256 XXXXX\\\\r\\\\na=group:BUNDLE 0\\\\r\\\\na=ice-options:trickle\\\\r\\\\na=msid-semantic:WMS *\\\\r\\\\nm=application 9 UDP/DTLS/SCTP webrtc-datachannel\\\\r\\\\nc=IN IP4 0.0.0.0\\\\r\\\\na=sendrecv\\\\r\\\\na=ice-pwd:XXXXX\\\\r\\\\na=ice-ufrag:XXXXX\\\\r\\\\na=mid:0\\\\r\\\\na=setup:actpass\\\\r\\\\na=sctp-port:5000\\\\r\\\\na=max-message-size:1073741823\\\\r\\\\n\\\"}\"]",
  "value": ""
}
```
[Go back to top](#tracker-descriptions)

## Provers
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://provers.pro/cID/9x6/bh2/5JlKS/WVQ_9/M/jAkf3iNqT/koylN/QE=e=u`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to provers.pro:
```
    new Fingerprint2().get(function(result) {
        var s = document.createElement('script');
        var x = document.getElementsByTagName('script')[0];
        s.src = options.url + '?fp=' + result;
        s.type = 'text/javascript';
        s.async = true;
        x.parentNode.insertBefore(s, x);
    })
})({
    "url": "http:\/\/provers.pro\/Z-noA."
});

```

[Go back to top](#tracker-descriptions)

## Psonstrentie
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `http://psonstrentie.info/cFDx9C6Rb/2m5jloSVWzQY9EMFjsgPwuM/jtcx5KMdCD0ly_O/DcABy/OJTnAxxz`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        var e = function(t) {
            if (!(this instanceof e)) return new e(t);
            this.options = this.extend(t, {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: [],
                excludeDoNotTrack: !0,
                excludePixelRatio: !0
            }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
        };

```
2. Sends computed fingerprint back to server
```
    new Fingerprint2().get(function(result) {
        var s = document.createElement('script');
        var x = document.getElementsByTagName('script')[0];
        s.src = options.url + '?fp=' + result;
        s.type = 'text/javascript';
        s.async = true;
        x.parentNode.insertBefore(s, x);
    })
```

[Go back to top](#tracker-descriptions)

## RazorPay
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.thirdwatch.ai/tw.min.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Rollick
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://widget.rollick.io/00294`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var Fingerprint2 = function(options) {

        if (!(this instanceof Fingerprint2)) {
            return new Fingerprint2(options);
        }

        var defaultOptions = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: true,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(options, defaultOptions);
        this.nativeForEach = Array.prototype.forEach;
        this.nativeMap = Array.prototype.map;
    };
```
[Go back to top](#tracker-descriptions)

## RoqAd
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Roq.ad's Privacy Policy States: 

`https://roq.ad/privacy-policy#`

>The processing purpose - Roq.ad processes received signals to generate cross-device graph. The graph includes only IDs connected into clusters indicating our predictions for user-owned devices.

>Roq.ad may transfer cookie IDs or MAIDs to its enterprise customers (advertisers, MarTech firms) as part of the generated cross-device graph.

>Tracking mechanism and the data types used: Roq.ad technology may track users visiting websites with simple js script that allows to save common HTTP request data including: browser’s cookie ID, browser’s user agent, hashed IP address of the browser, visited URL, browser’s language, referrer URL. 

Roq.ad's Website states:

`https://roq.ad/`

>Cross-Device Technology - Consumers constantly switch between their digital devices, such as smartphones, tablets, desktops, etc. The process of tracking consumer behavior and building a single digital identity for each user has become more complex. 

>By accurately determining which devices belong to the same user, the Roq.ad Cross-Device Technology enables you to create data-driven strategies with focus on people-based marketing. This approach helps to increase engagement with your audience across all their devices and optimizes your marketing budget and analytics. 

>Identity Graph - Uncover which devices your users own and how they use them to interact with your brand. Understanding your audience and their online behavioral patterns enables you to define the perfect strategy to increase engagement. Built in-house, Roq.ad Cross-Device Identity Graph uses probabilistic data to make predictions and deterministic data sets to train the algorithms.


[Go back to top](#tracker-descriptions)

## Salesforce
This service has been classified as `Email`, `Content`, `Advertising`, `EmailStrict` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Salesforce's privacy policy States:

`https://www.salesforce.com/products/marketing-cloud/sfmc/audience-studio-privacy/`

>How we Collect and Use De-identified and/or Pseudonymized Personal Data via our Platform - When a user visits the website or mobile application of one of our Customers (the “Customer Site” or “Customer App,” collectively, the “Customer Site(s) and App(s)”), the Customer collects and transfers to Audience Studio and/or enables Audience Studio to collect pseudonymized personal data related to that user’s visits to the website or mobile app (our Customer’s “Session Data”). This Session Data may include information about how the user came to the Customer Site and App, which search engines they use, the search terms used to find the Customer Site, their experience on the Customer Site and App, information about how they interact with the Customer Site and App, demographic information that the Customer has collected from that user and other visitors, data from third-party data providers, and information regarding how users interact with advertisements on the Customer Site and App. Additionally, browsers automatically send certain standard information to every website a user visits, such as an IP address, browser type and language settings, access times, and referring website addresses. This information is collected during visits to each Customer Site and App, including the Audience Studio Site…Where our systems can reasonably infer that a particular computer and/or mobile device belong to the same user or household, we may store such information for use on the Platform. The data stored on our Platform may be combined with third-party data (for example, geolocation data provided by a vendor) in order to better target advertisements, to enable Customers to better understand users across multiple computers and devices, and for ad delivery and reporting purposes.  
  
>HTML5 Cookies -Audience Studio uses HTML5 cookies in connection with the Platform, including on the Audience Studio Site and Customer Sites. An HTML5 cookie is also known as HTML5 Web storage and is an alternative to the commonly used HTTP browser cookie.  
  
>Statistical Identifiers - Audience Studio is experimenting with the use of statistical identifiers in connection with the Platform, including on the Audience Studio Site and some Customer Sites where requested by Customers. Statistical identifiers are created using pseudonymized personal data about computers and mobiles devices such as the operating system, user-agent string, IP address, Internet browser, installed fonts, and similar information. This information makes your computer or device distinct enough for our systems to determine within a reasonable probability that they are encountering the same computer or device. Statistical identifiers enable users to be uniquely identified via the Platform, enabling the Platform to store ad targeting, analytics, and other data.  
  
>Pixel Tags - We also use pixel tags in connection with the Platform, including on the Audience Studio Site and Customer Sites. Pixel tags (also known as web beacons) are small strings of html or JavaScript code that provide a method for delivering a graphic image on a Web page or other document. Pixel tags may be used to obtain information about the computer or device being used to view a particular Web page such as the IP address of the computer or device to which the pixel tag is sent, the time it was sent, the computer or device’s operating system and browser type, and similar information.

Salesforce's website states: 

'https://konsole.zendesk.com/hc/en-us/articles/215234358-Cross-Device-User-Matching'

>User data stored in Audience Studio is keyed off a global Krux User ID. The Krux User ID is a third-party cookie and as such is specific to a browser (and correspondingly device too). On the other hand, first-party data that is ingested by the platform is keyed off a first-party user ID that is provided to Audience Studio by our clients. The first-party user ID typically comes from a user registration system and is the same across different browsers and devices for a given user. The client specific first-party user ID is mapped to the browser specific Krux User ID as part of the user matching and data loading process. As a result, it is possible to map and reconcile the browser specific Krux User IDs to an “Uber-ID’ using the client’s first-party, device-and-browser-agnostic user ID. This Uber-ID can then be used to build a profile of a user that spans browsers and devices.  
  
>Once the User Match table has been constructed, the client’s first-party user ID can be used as an “Uber-ID” to create a joint profile of user activity across different browsers and devices. This joint profile can then be used in the segment building process allowing Audience Studio clients to build more comprehensive audience segments that can be leveraged across multiple devices.


[Go back to top](#tracker-descriptions)

## SAP
This service has been classified as `Email`, `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://d3m83gvgzupli.cloudfront.net/webEvent/cywevent.js?servicecode=AD36293095`
1. Script gathers several device characteristics to generate a fingerprint:
```
			cy.control.cySetUserDefined("DEVICEIDENTITYDONOTTRACK",navigator.doNotTrack);
			cy.control.cySetUserDefined("DEVICEIDENTITYTIMEZONEOFFSET",String(new Date().getTimezoneOffset()));
			cy.control.cySetUserDefined("DEVICEIDENTITYSTATIC",murmurhash3_32_gc((navigator.language + String(Math.pow (2, window.screen.colorDepth)) + screen.width + "&times;" + screen.height + sessionStorageCheck + indexedDBCheck + openDatabaseCheck + navigator.cpuClass + navigator.platform), cy_s));
			cy.control.cySetUserDefined("DEVICEIDENTITYUSERAGENT",murmurhash3_32_gc(navigator.userAgent.replace(/[0-9]/g, ''), cy_s));
			cy.control.cySetUserDefined("DEVICEIDENTITYCANVAS",murmurhash3_32_gc(getCanvasFingerPrint(), cy_s));
			cy.control.cySetUserDefined("DEVICEIDENTITYBROWSERPLUGINS",cy_d3h);		
			

```
2. Then script sends device properties to seewhy.com: 
```
cy.control._getBaseURL = function(/* optional */ res)
{
	var resource="seewhy.gif";
	if (res)
	{
		resource = res;
	}
        var uidtest;
	var protocol;
	var port;
	var swd='abandonment6.saas.seewhy.com';
	var path='/abandonment2/WE/' +resource;
	var ssl = window.location.protocol.toLowerCase().indexOf('https') >= 0;
	if (ssl)
	{
		protocol='https';
		port=443;
	}
	else
	{
		cy.control._cyConvertCYPropertyNamesToUpperCase();
		uidtest=(cy.USERID==undefined) ? -1 : cy.USERID.length;

		if (uidtest>0)
		{
			protocol='https';
			port=443;
		}
		else
		{
			protocol='http';
			port=80;
		}


	}
	var swi = protocol+'://'+swd+':'+port+path;
	var rn = Math.random();

	return swi+"/"+rn;
}

```
```
function cyOnPageLoad(/* optional */ isBlocking, /* optional */ doDelay, /* optional */ ocy, /* optional */ cysetter)
{
	var block = false;
	if (isBlocking && typeof(isBlocking) == "boolean")
	{
		block = isBlocking;
	}

	try
	{
		cy.control._cySetCYProperties(ocy, cysetter);

		if (block === true)
		{
			src = cy.control._cyGetElementSrc("seewhy.js");

			// Doing a document.write requires that it be done before the page has finished loading (otherwise we will completely
			// overwrite the page with the output of the document.write call).

			if (document.readyState)
			{
				if (document.readyState != "complete")
				{
					document.write('<script type="text/javascript" src="',src,'"><\/script>');
				}
			}
			else
			{
				document.write('<script type="text/javascript" src="',src,'"><\/script>');
			}
		}
		else
		{
			var cy_image = cy.control._cyCreateImage(false);

			cy_image.src = cy.control._cyGetElementSrc("seewhy.nogif");
			
			cy_image.style.cssText = 'display:none;'; 
		}

		var delay = false;
		if (doDelay && typeof(doDelay) == "boolean")
		{
			delay = doDelay;
		}

		if (delay === true)
		{
			cy.control._cyWait(cy.control._cyGetWaitDuration());
		}
	}
	catch(err){}
}

``` 
[Go back to top](#tracker-descriptions)

## Semantiqo
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://sonar.semantiqo.com/c82up/checking.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            _ = {
                preprocessor: null,
                audio: {
                    timeout: 1e3,
                    excludeIOS11: !0
                },
                fonts: {
                    swfContainerId: _0x2fc9("0x69"),
                    swfPath: _0x2fc9("0x6a"),
                    userDefinedFonts: [],
                    extendedJsFonts: !1
                },
                screen: {
                    detectScreenOrientation: !0
                },
                plugins: {
                    sortPluginsFor: [/palemoon/i],
                    excludeIE: !1
                },
                extraComponents: [],
                excludes: {
                    enumerateDevices: !0,
                    pixelRatio: !0,
                    doNotTrack: !0,
                    fontsFlash: !0
                },
                NOT_AVAILABLE: "not available",
                ERROR: "error",
                EXCLUDED: _0x2fc9("0x6b")
            },

```
[Go back to top](#tracker-descriptions)

## SendPulse
This service has been classified as `Email`, `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://static-login.sendpulse.com/apps/fc3/build/dh-libs.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var t = function(e) {
        if (!(this instanceof t)) return new t(e);
        this.options = this.extend(e, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: [],
            excludeDoNotTrack: !0,
            excludePixelRatio: !0
        }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };
```
2. Sends computed fingerprint back to server
```
Request URL: https://login.sendpulse.com/members/forms/stat?true=jQuery112409706314635002642_1553640639385&event=show&formId=95496&fp=REMOVED&_=1553640639386
```
[Go back to top](#tracker-descriptions)

## Shixiseng
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://sxsimg.xiaoyuanzhao.com/static/public/js/mxa.js?v=2d880315aeead463159ebbcbb8c1a0bf`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## SiftScience
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.siftscience.com/s.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
                b = {
                    bk: b.beaconKey_,
                    tm: b.time_,
                    r: b.random_,
                    v: b.version_,
                    cs: b.characterSet_,
                    h: b.hostName_,
                    l: b.language_,
                    P: b.partnerUserId_,
                    S: b.sessionId_,
                    ui: b.userId_,
                    uu: b.userUuid_,
                    t: b.title_,
                    u: b.url_,
                    rf: b.referrer_,
                    ua: b.userAgent_,
                    nm: b.numMimeTypes_,
                    mh: b.mimeTypesHash_,
                    nf: b.numFonts_,
                    fh: b.fontsHash_,
                    np: b.numPlugins_,
                    ph: b.pluginsHash_,
                    sh: b.screenHeight_,
                    sw: b.screenWidth_,
                    cd: b.colorDepth_,
                    p: b.platform_,
                    to: b.timezoneOffset_,
                    d: b.dstOffset_,
                    ce: b.cookieEnabled_,
                    dt: b.doNotTrack_,
                    tp: b.maxTouchPoints_,
                    ol: b.online_,
                    pr: b.product_,
                    ps: b.productSub_,
                    vd: b.vendor_,
                    vs: b.vendorSub_,
                    hc: b.hardwareConcurrency_,
                    je: b.javaEnabled_,
                    ss: b.sessionStorage_,
                    ls: b.localStorage_,
                    "in": b.indexedDB_,
                    db: b.openDB_,
                    cp: b.cpuClass_,
                    tl: b.tamperedLanguage_,
                    tr: b.tamperedResolution_,
                    ts: b.tamperedOS_,
                    tb: b.tamperedBrowser_,
                    ab: b.adBlock_,
                    cf: b.canvasFingerprint_,
                    si: b.flash_SocketIP_,
                    fu: b.flash_uuid_
                };
```
[Go back to top](#tracker-descriptions)

## SmarterClick
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://js.smct.io/e/fp-1.4.8.min.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}, {"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## SmartyAds
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
SmartyAds' Privacy policy States:

`https://smartyads.com/privacy-policy`

>Information that we may process includes: 
>- Information about your behavior on our client’s resources, websites, and platforms: including information about the domain, your referring website addresses, date and time of your visits, page view data, search keywords, visitor activities and actions on publisher’s sites, referring and exit pages, platform type, date/time stamp, geolocation (including city, country, zip code, and potentially geographic coordinates if you have enabled location services on your device), click data, types of advertisements viewed. 
> - Information about your browser: your browser type, languages, browser history etc. 
> - Information about your device: including information about your IP address, device make, device model, device operating system, device operating system version, and data connection type. 
> - Information about your Internet service: including information about which Internet Service Provider (ISP) you use. 
> - Information regarding your interactions with our clients, including your use of our clients’ websites, software, and mobile applications, the websites and applications or other pages on the Internet or other resources our clients operate and control. 
> - Any additional data that is reasonably necessary to calculate a statistical ID in certain cases. 
> - Pseudonymous and generalized information collected by our clients or third parties that may include identifiers (similar to mobile advertising IDs and alike) and interest-based advertising data related to or connected with said identifiers. 

>We collect a variety of data using cookies and various other standards (typical for the industry) and unique (if our technology allows so) web technologies to collect information automatically from your device, including: 
>- HTML5 and Locally Stored Objects. 
>- Tags and Pixels. 
>- Mobile Device Identifiers 
>- Other technologies


SmartyAds' website states:

`https://smartyads.com/reviews`(1)

>Universal cross-device advertising opportunities, cutting-edge technologies along with best industry experts are the key pillars of our service that help our customers grow and optimize their marketing campaigns exponentially. (1) 

 `https://smartyads.com/white-label-solution` (2)
 
>Control your budget, target and retarget your audiences with relevant brand messages. Launch CPM advertising campaigns cross-channel on any device. (2)


[Go back to top](#tracker-descriptions)

## Smi
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://jsn.24smi.net/smi.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    function c() {
        var e = null,
            t = null;
        try {
            t = (e = document.createElement("canvas")).getContext("2d")
        } catch (e) {}
        return t && e ? (t.fillStyle = "red", t.fillRect(30, 10, 200, 100), t.strokeStyle = "#1a3bc1", t.lineWidth = 6, t.lineCap = "round", t.arc(50, 50, 20, 0, Math.PI, !1), t.stroke(), t.fillStyle = "#42e1a2", t.font = "15.4px 'Arial'", t.textBaseline = "alphabetic", t.fillText("PR flacks quiz gym: TV DJ box when? Ã¢Ëœ ", 15, 60), t.shadowOffsetX = 1, t.shadowOffsetY = 2, t.shadowColor = "white", t.fillStyle = "rgba(0, 0, 200, 0.5)", t.font = "60px 'Not a real font'", t.fillText("NoÃ©Âªâ€”", 40, 80), s(e.toDataURL())) : null
    }

```
2. Sends computed fingerprint back to server
```
{
    "use strict";
    Object.defineProperty(t, "__esModule", {
        value: !0
    }), t.QUEUE_NAME = "smiq", t.CLASS_NAME = "smi24__informer", t.CB_PREFIX = "__smiCb", t.DBG_FLAG = "smidbg=1", t.DATAURL = "data.24smi.net/informer", t.VISIBILITYURL = "data.24smi.net/collect", t.REQUEST_MSG_KEYS = ["element", "blockId", "useSlider", "templateSrc", "template", "_lazyLoad"], t.TEMPLATE_KEYS = ["html", "css", "teasersNum"], t.SMI_ATTRS = {
        status: "data-smi-status",
        blockId: "data-smi-blockid",
        templateSrc: "data-smi-templatesrc",
        useSlider: "data-smi-useslider"
    }, t.SLIDER_CLS_MAP = {
        slider: "slider24smi",
        inner: "slider24smi__inner",
        leftEdge: "slider24smi__edge-left",
        rightEdge: "slider24smi__edge-right",
        button: "slider24smi__edge-button",
        scroller: "slider24smi__scroller",
        card: "slider24smi__slide",
        visibleLeftEdge: "slider24smi_edge_left",
        visibleRightEdge: "slider24smi_edge_right",
        visibleLeftButton: "slider24smi_button-left",
        visibleRightButton: "slider24smi_button-right",
        move: "slider24smi_moving"
    }, t.VISIBILITY_THROTTLE_TIMEOUT = 100, t.DEFAULT_ICP = [0, 0, 0]
}



```

[Go back to top](#tracker-descriptions)

## Socital
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Socital's privacy policy states: 

`https://socital.com/privacy/`

>Socital also offers the extraction and analysis of End User Data from Third-Party Services on behalf of the Client and as authorized by the Client, the storage of End User Data and the storage of the output of the processing of such data, and the segmentation and export of the End User Data to Third-Party Services 

>Passive Data Collection - Like most web-based services, we may automatically receive and record information on our server logs from your browser when you use the Socital Site and Services. We may use a variety of methods, including clear GIFs (also known as “web beacons”) and “cookies”, to collect this information. We use both session and persistent cookies. The information that we may collect with these automated methods may include, for example, your IP address, cookie information, a unique device or user ID, browser type, system type, the content and pages that you access on the Socital Site or Services, the frequency and duration of your visits to the Socital Site or Services, and the “referring URL” (i.e., the page from which you navigated to the Socital Site).


[Go back to top](#tracker-descriptions)

## SpareChange
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://sparechange.io` describes its service as a javascript crypto miner.

> A browser based crypto currency miner for your website When a user visits your website, a JavaScript miner runs in their browser, using a tiny amount of power to mine crypto currencies for you.
### Technical Review
1. Script contains a miner object that configures and starts a javascript miner

```
function Miner(spareChangeApiKey, p1, p2) {
    this.spareChangeApiKey = spareChangeApiKey;
    //determine if parameters are old or new style
    if( p1 === parseInt(p1, 10) || typeof p1 == 'undefined' || p1 === null) {
        //p1 = numThreads. p2 = throttlePct
        this.numThreads = p1 || navigator.hardwareConcurrency || 8;
        this.throttlePct = p2 || 0.0;
        this.optIn = 'no';
        this.optInDelay = 10;
        this.targetShares = 0;
    } else {
        //parse p1 as userOptions
        var userOptions = p1;
        this.numThreads = userOptions.numberOfThreads || navigator.hardwareConcurrency || 8;
        this.throttlePct = userOptions.throttlePercent || 0.0;
        if(userOptions.optIn) {
            this.optIn = userOptions.optIn.type || 'no';
            this.optInDelay = userOptions.optIn.delay || 10;
        } else {
            this.optIn = 'no';
            this.optInDelay = 10;
        }
        this.targetShares = userOptions.targetShares || 0;
    }

    this.numSharesSubmitted = 0;
    this.running = false;
    this.optedOut = false;
    this.hashesPerSecond = 0;
    this.hashesDone = 0;
    this.hashesPerThread = {};
    this.connectionOpen = false;
    this.token = null;
}
```

[Go back to top](#tracker-descriptions)

## SteelHouse
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Steelhouse's privacy policy States:

`https://steelhouse.com/privacy-policy/`

>Through the provision of our Services we collect various types of information from our customers, affiliates and ad technology partners, including from: Publishers (i.e. the owners of the applications and websites you use), Ad exchanges, Ad Networks, Supply Side Platforms, Direct Marketing Platforms and other ad technology companies, who assist with providing targeted advertisements, including information about your device, such as device identifier, model, network provider, browser type, language, IP Address, Information about mobile application usage, how you interact with applications you use and advertising you see, precise location information (only with your consent), device type, information about the app, such as the version, information about your mobile advertising identifiers such as your advertising ID and other information about you, including interests, age, gender. 

>In order to be able to serve advertisements to you that you may wish to see, we may combine data and link your activities across devices and websites through the use of your device identifying IP address. 

Steelhouse's website states:

`https://steelhouse.com/steelhouse-digital/`

>Get the most detailed analytics in the industry for complete transparency into clicks, conversions, spend, and more — all in a fully customizable reporting suite…Cross-Device integrated into google analytics. Track and verify all traffic and conversions across all devices in google analytics.  
  
>SteelHouse’s retargeting solution allows advertisers to retarget previous site visitors on web and mobile. SteelHouse Performance TV also enables advertisers to retarget users on Connected TV devices such as Roku, Firestick, AppleTV, and other smart TVs. In addition, you are able to track and measure results on both Google Analytics and the SteelHouse platform. This makes it a true cross device remarketing solution as you will be able to launch targeted advertising campaigns on laptops, computers, mobile devices, and on streaming TV devices and networks.  
  
>Because the SteelHouse Smart Pixel allows advertisers to run retargeting campaigns without the need for a product feed. Simply place the pixel on your website and you are able to retarget site visitors with the products and services they viewed on your website.


[Go back to top](#tracker-descriptions)

## Storeland
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://sl-h-statistics-ch-1.storeland.ru/static/fp.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var fp = new Fingerprint2;
    fp.get(function(e, t) {
        details.f_fingerprint = e, setCookie("fp", e, 5);
        for (var r in t) {
            var i = t[r];
            null !== i.value && null !== i.key && ("canvas" !== i.key && "webgl" !== i.key ? details["f_" + i.key] = i.value.toString() : details["f_" + i.key] = i.value.toString().substr(0, 100))
        }
        data.append("data", JSON.stringify(details)), xhr.open("POST", "//sl-h-statistics-ch-1.storeland.ru/", !0), xhr.send(data)
    })

```
2. Sends computed fingerprint back to server:
```
try {
    var fp = new Fingerprint2;
    fp.get(function(e, t) {
        details.f_fingerprint = e, setCookie("fp", e, 5);
        for (var r in t) {
            var i = t[r];
            null !== i.value && null !== i.key && ("canvas" !== i.key && "webgl" !== i.key ? details["f_" + i.key] = i.value.toString() : details["f_" + i.key] = i.value.toString().substr(0, 100))
        }
        data.append("data", JSON.stringify(details)), xhr.open("POST", "//sl-h-statistics-ch-1.storeland.ru/", !0), xhr.send(data)
    })
} catch (e) {
    details.f_fingerprint = "error: " + e.name + "::" + e.message + "\n" + e.stack, data.append("data", JSON.stringify(details)), xhr.open("POST", "//sl-h-statistics-ch-1.storeland.ru/", !0), xhr.send(data)
} else setCookie("fp", getCookie("fp"), 5), details.f_user_agent = "", details.f_fingerprint = getCookie("fp"), data.append("data", JSON.stringify(details)), xhr.open("POST", "//sl-h-statistics-ch-1.storeland.ru/", !0), xhr.send(data);


```
[Go back to top](#tracker-descriptions)

## Stripchat
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.stripst.com/assets/vendors.20200625080251.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Tapad
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Tapad's Privacy Policy States: 

`https://www.tapad.com/us-privacy-notice`

>Tapad collects and uses information as described further in this Privacy Notice in connection with the Graph services we provide to Clients and Partners. The Graph is an association of likely connections between device Identifiers across platforms including websites, or mobile applications. 

>We use our technologies to create likely connections between device Identifiers across platforms including websites, or mobile applications and TV applications. This data is used for more tailored advertising, marketing, measurement, analytics, and research. 

>In order to establish connections between devices and provide the Services and Tapad Graph to Clients and Partners, we collect and store the information as described below from devices. Tapad collects and uses information through its own and Third Party websites and mobile applications, and in connection with the Services that we provide to Partners and Clients such as advertisers, agencies, marketers, and technology firms. Tapad observes these signals generated from internet activity received from devices connected to the internet, and uses various processing logic to establish likely connections and groups together unique Identifiers that are likely associated. The associated Identifiers may include those IDs associated with mobile applications on both smartphones and tablets, web browsers across various devices, and connected TVs or applications on connected TVs. 

>Tapad also receives matching IDs from Partners and Clients for the purpose of matching existing customers or otherwise known IDs to IDs in Tapad's Graph. Matching IDs may represent device IDs, underlying Cookie IDs, customer IDs, or other types of data meaningful to the Partner or Client, and is recognized only as another pseudonym in Tapad's systems.

Tapad's website states: 

`https://www.tapad.com/the-tapad-graph`

>A global, privacy-safe digital cross-device solution, The Tapad Graph is built on top of a curated network of data providers, combined with the power of utilizing sophisticated machine learning models with authenticated and real-time signals, to provide the most comprehensive and differentiated digital identity graph in market. By leveraging The Tapad Graph to correlate data into a single view, complex customer journeys become clearer — enabling a more precise and actionable way to engage consumers across multiple devices. As a result, brands, agencies, telcos and platforms are able to unlock greater impact across their programmatic, targeting, measurement, and personalization efforts. 

>One Powerful cross device graph - Simply put, The Tapad Graph is a data file that includes digital ad IDs that are clustered at the individual and/or household level. It’s built using a set of customer provided input IDs as a baseline, and from there we connect those IDs to other IDs associated with them — across multiple digital device types. Receive a file each week and start realizing the benefits of Tapad’s global cross-device graph. For example, a brand or agency with a file of first or third-party cookies can associate them to mobile devices, CTVs, and additional cookies — creating more relevant opportunities for brands to connect with consumers across devices.

[Go back to top](#tracker-descriptions)

## TechSolutions
This service has been classified as `Analytics` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://www.techsolutions.com.tw/analytics.js?id=adb5aa4fedda0f66&d=https://adbert.techsolutions.com.tw/&0.5748148854325372`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
                preprocessor: null,
                audio: {
                    timeout: 1e3,
                    excludeIOS11: !0
                },
                fonts: {
                    swfContainerId: "fingerprintjs2",
                    swfPath: "flash/compiled/FontList.swf",
                    userDefinedFonts: [],
                    extendedJsFonts: !1
                },
                screen: {
                    detectScreenOrientation: !0
                },
                plugins: {
                    sortPluginsFor: [/palemoon/i],
                    excludeIE: !1
                },
```
2. Sends computed fingerprint back to server
```
var ProcessorGeneral = async function ProcessorGeneral(action, event, args) {
        var fpComponents = await _fingerprintjs2.default.getPromise(),
            fpHash = _fingerprintjs2.default.x64hash128(fpComponents.map(function(e) {
                return e.value
            }).join(), 31),
            data = {},
            callback = function() {};
        if (event === EVENT.TRIGGER || event === EVENT.EVENT_RECORD) {
            var categoryId = args[2],
                eventId = args[3];
            if (!eventIsVaild(categoryId, eventId)) return;
            var uuid = _cookie2.default.get("adbert_uuid"),
                _cookie$cmp = _cookie2.default.cmp,
                c = _cookie$cmp.c,
                m = _cookie$cmp.m,
                mp = _cookie$cmp.mp,
                _cookie$pd = _cookie2.default.pd,
                campaign = _cookie$pd.campaign,
                p = _cookie$pd.p,
                containerId = _store2.default.containerId;
            data = {
                fp: fpHash,
                id: eventId,
                category: categoryId,
                c: _store2.default.containerId,
                url: window.location.href
            };
            for (var i = 0; i <= ga.getAll().length; i++) {
                var trackerName = "adbert" + i;
                _GAService2.default.setDimension(trackerName, uuid, c, m, mp, p, eventId, containerId), ga(trackerName + ".send", "event", "Event", "trigger")
            }
        } else event === EVENT.PAGEVIEW && (data = {
            fp: fpHash,
            ref: document.referrer,
            c: _store2.default.containerId,
            url: window.location.href,
            title: document.title
        }, callback = async function callback() {
            _store2.default.tfmProcess.eventEmitter.emit("finish"), eval(this.response), await _store2.default.event.register(), _store2.default.event.bindEventTrigger(), _store2.default.queue.processTrackingEvent()
        });
        _browser2.default.in([_browser2.default.OPERA, _browser2.default.SAFARI, _browser2.default.IOS_SAFARI]) && (data.uuid = _cookie2.default.get("adbert_uuid", "7be7ee3b-3e96-43b8-98f8-f3b6abb432fc"), data.sessionId = _cookie2.default.get("sessionId", ""), data.containerId = _cookie2.default.get("containerId", ""), data.source = _cookie2.default.get("source", ""), data._cp = _cookie2.default.get("_cp", ""), data._cmp = _cookie2.default.get("_cmp", ""), data._pd = _cookie2.default.get("_pd", ""), data._cmps = _cookie2.default.get("_cmps", ""));
        var options = {
                "Content-Type": "application/json"
            },
            url = _store2.default.domain + "/" + event + "?d=" + _store2.default.company + "&_=" + Math.random();
        _http2.default.request("post", url, options, callback, data)
    };

```
[Go back to top](#tracker-descriptions)

## The Trade Desk
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
TheTradeDesk's privacy policy States:

`https://www.thetradedesk.com/general/privacy`

>Cross device graphing: We may use data and algorithms to associate devices that might be related to each other, such as devices used by the same person or in the same household. 

>Some of the ways the Platform collects data include: using cookies and pixels 

>The Platform processes data both on our behalf and on behalf of clients and partners for advertising purposes such as: associating devices that might be related to each other

>Our AdBrain product, which is part of our Platform, uses data to produce a mapping of devices that might be related to each other, meaning that they might be used by the same person or by people within the same household. This helps advertisers better target and measure their campaigns, as well as limiting the number of times the same person or household sees an ad.


TheTradeDesk's website states: 

`https://www.thetradedesk.com/products/cross-device`

>Cross-Device Targeting and Measurement Deliver relevant, personalized messaging across the entire user journey.  
  
>Our cross-device targeting tools match multiple devices and channels to a unique ID, so you can serve up relevant ads when and where they’ll be most impactful. Our measurement tools let you analyze those interactions to learn how to create the ideal customer journey. We’ve partnered with leaders in cross-device data to bring you a holistic solution based on deterministic and probabilistic matching capabilities.  
  
>Analyze the entire customer journey. See which ads perform well on which devices, including Connected TV, desktop, and mobile.


[Go back to top](#tracker-descriptions)

## Trendemon
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://assets.trendemon.com/global/fingerprint.min.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Unknown2mdnsys
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cfa.2mdnsys.com/cdn-cgi/bm/cv/2172558837/api.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "200px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"HB\\\"E\",64,140]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"J>\",118,151]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "50px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"j=Lx\",110,168]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"}4^Q\",74,105]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Upland
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://t.sf14g.com/sf14g.js`
1. Generates fingerprint based on plugins, fonts, canvas, etc:

```
jsFnt: function (keys, done) {
            return setTimeout(function () {
                var baseFonts = ['monospace', 'sans-serif', 'serif'],
                    fontList = [
                        'Andale Mono', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial MT', 'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS',
                        'Bitstream Vera Sans Mono', 'Book Antiqua', 'Bookman Old Style',
                        'Calibri', 'Cambria', 'Cambria Math', 'Century', 'Century Gothic', 'Century Schoolbook', 'Comic Sans', 'Comic Sans MS', 'Consolas', 'Courier', 'Courier New',
                        'Geneva', 'Georgia',
                        'Helvetica', 'Helvetica Neue',
                        'Impact',
                        'Lucida Bright', 'Lucida Calligraphy', 'Lucida Console', 'Lucida Fax', 'LUCIDA GRANDE', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Typewriter', 'Lucida Sans Unicode',
                        'Microsoft Sans Serif', 'Monaco', 'Monotype Corsiva', 'MS Gothic', 'MS Outlook', 'MS PGothic', 'MS Reference Sans Serif', 'MS Sans Serif', 'MS Serif', 'MYRIAD', 'MYRIAD PRO',
                        'Palatino', 'Palatino Linotype',
                        'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Symbol',
                        'Tahoma', 'Times', 'Times New Roman', 'Times New Roman PS', 'Trebuchet MS',
                        'Verdana', 'Wingdings', 'Wingdings 2', 'Wingdings 3'
                    ], testString = 'mmmmmmmmmmlli', testSize = '72px', h = document.getElementsByTagName('body')[0],
                    baseFontsDiv = document.createElement('div'), fontsDiv = document.createElement('div'), defaultWidth = {},
                    defaultHeight = {};
```
```
getRegularPlugins: function () {
            var plugins = [];
            if (navigator.plugins) {
                for (var i = 0, l = navigator.plugins.length; i < l; i++) {
                    if (navigator.plugins[i]) { plugins.push(navigator.plugins[i]); }
                }
            }
            if (this.pluginsShouldBeSorted()) {
                plugins = plugins.sort(function (a, b) {
                    if (a.name > b.name) { return 1; }
                    if (a.name < b.name) { return -1; }
                    return 0;
                });
            }
            return this.map(plugins, function (p) {
                var mimeTypes = this.map(p, function (mt) {
                    return [mt.type, mt.suffixes].join('~');
                }).join(',');
                return [p.name, p.description, mimeTypes].join('::');
            }, this);
        }
```
```
getCanvasFp: function () {
            var result = [];

            var canvas = document.createElement('canvas');
            canvas.width = 2000;
            canvas.height = 200;
            canvas.style.display = 'inline';

            var ctx = canvas.getContext('2d');
            ctx.rect(0, 0, 10, 10);
            ctx.rect(2, 2, 6, 6);
            result.push('canvas winding:' + ((ctx.isPointInPath(5, 5, 'evenodd') === false) ? 'yes' : 'no'));

            ctx.textBaseline = 'alphabetic';
            ctx.fillStyle = '#f60';
            ctx.fillRect(125, 1, 62, 20);
            ctx.fillStyle = '#069';
            ctx.font = '11pt no-real-font-123';
            ctx.fillText('Cwm fjordbank glyphs vext quiz, \ud83d\ude03', 2, 15);
            ctx.fillStyle = 'rgba(102, 204, 0, 0.2)';
            ctx.font = '18pt Arial';
            ctx.fillText('Cwm fjordbank glyphs vext quiz, \ud83d\ude03', 4, 45);
            ctx.globalCompositeOperation = 'multiply';
            ctx.fillStyle = 'rgb(255,0,255)';
            ctx.beginPath();
            ctx.arc(50, 50, 50, 0, Math.PI * 2, true);
            ctx.closePath();
            ctx.fill();
            ctx.fillStyle = 'rgb(0,255,255)';
            ctx.beginPath();
            ctx.arc(100, 50, 50, 0, Math.PI * 2, true);
            ctx.closePath();
            ctx.fill();
            ctx.fillStyle = 'rgb(255,255,0)';
            ctx.beginPath();
            ctx.arc(75, 100, 50, 0, Math.PI * 2, true);
            ctx.closePath();
            ctx.fill();
            ctx.fillStyle = 'rgb(255,0,255)';
            ctx.arc(75, 75, 75, 0, Math.PI * 2, true);
            ctx.arc(75, 75, 25, 0, Math.PI * 2, true);
            ctx.fill('evenodd');

            if (canvas.toDataURL) {
                result.push('canvas fp:' + canvas.toDataURL());
            }
            return result.join('~');
        }
```
2. Sends fingerprint to tracking company:
```
 setTimeout(function () {
        Llfp().get(function (fp, components) {
            llfp = fp; // for forms scripts
            //console.log(fp);
            var trackingEndpointUrl = 'https://tracking.leadlander.com/api/tracking',
                pageHit = {
                    accountId: window.sf14gv !== undefined ? sf14gv : window.tl813v !== undefined ? tl813v : llactid, //sf14gv is passed from user code; this is for legacy compatablity.
                    page: location.href,
                    referer: document.referrer || '',
                    fp: fp
                }, serialize = function (obj) {
                    var str = [];
                    for (var p in obj)
                        if (obj.hasOwnProperty(p)) {
                            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                        }
                    return str.join("&");
                };
            var image = new Image();
            image.src = trackingEndpointUrl + '?' + serialize(pageHit);
        });
    }, 75);
   ```
[Go back to top](#tracker-descriptions)

## VerticalHealth
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://assets.verticalhealth.net/fingerprint2.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        var i = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(t, i), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server
```
Request URL: https://id.verticalhealth.net/pixel.gif?fprint=REMOVED&partnerid=iodine&context=%7B%22depression%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22diagnosis%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22new%20york%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22morphine%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22tramadol%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22lortab%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22vicodin%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22one%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22surgery%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22tissue%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22muscle%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22surgeon%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22panic%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22doctor%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22pain%22%3A%7B%22score%22%3A3%2C%22count%22%3A3%7D%2C%22add%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22addictive%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22abuse%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22adhd%22%3A%7B%22score%22%3A1%2C%22count%22%3A1%7D%2C%22medications%22%3A%7B%22score%22%3A6%2C%22count%22%3A4%7D%7D
```

[Go back to top](#tracker-descriptions)

## Vtex
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Vtex's privacy policy states: 

`https://compliance.vtex.com/gdpr/policies/vtex-privacy-policy` 

>VTEX may also collect additional information through your dealings with and use of the Services and non-VTEX websites, which does not disclose your specific identity or does not directly relate to an individual. Additional information may include, but is not limited to: 
>-Internet Protocol address ("IP address") and information derived from your IP address such as your geographic location; 
-Geographic location showing where You are using the Services; 
-Information about your devices such as information contained in HTTP Headers (defined below) or other internet transfer protocol signals, browser or device type and version; operating system, user-agent strings and information about or from the presence or use of "apps" on your mobile devices, screen resolution, and your preferred language; 
-Unique IDs such as a cookie placed on your computer, mobile or device IDs; 
-Behavioral data and information about your usage of the Services, including webpages clicked, websites and content areas visited, date and time of activities; 
 
>We might also may put together additional information with Personal Information, such as gathering geographical location from your IP address and combining all of this with behavioral data about your usage of the Services with your name. 

[Go back to top](#tracker-descriptions)

## Warumbistdusoarm
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://warumbistdusoarm.space/cdn-cgi/bm/cv/2172558837/api.js`  
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": false, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "canvas_api_calls": [{"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "50px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"26%k'\",115,244]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.strokeText", "arguments": "[\"&>\",48,218]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "200px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"KHJ/$\",147,109]", "operation": "call"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "{}", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "28.571428571428573px aanotafontaa", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"V*\",50,156]", "operation": "call"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

## Webmecanik
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://mr.automation.webmecanik.com/mtc.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        var i = {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this.options = this.extend(t, i), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server
```
function(m, l, n, d) {
    m.pageTrackingUrl = (l.protocol == 'https:' ? 'https:' : 'https:') + '//mr.automation.webmecanik.com/mtracking.gif';
    m.pageTrackingCORSUrl = (l.protocol == 'https:' ? 'https:' : 'https:') + '//mr.automation.webmecanik.com/mtc/event';
    m.contactIdUrl = (l.protocol == 'https:' ? 'https:' : 'https:') + '//mr.automation.webmecanik.com/mtc';
    m.fingerprint = null;
    m.fingerprintComponents = null;
    m.fingerprintIsLoading = false;
    m.addFingerprint = function(params) {
        for (var componentId in m.fingerprintComponents) {
            var component = m.fingerprintComponents[componentId];
            if (typeof component.key !== 'undefined') {
                if (component.key === 'resolution') {
                    params.resolution = component.value[0] + 'x' + component.value[1];
                } else if (component.key === 'timezone_offset') {
                    params.timezone_offset = component.value;
                } else if (component.key === 'navigator_platform') {
                    params.platform = component.value;
                } else if (component.key === 'adblock') {
                    params.adblock = component.value;
                } else if (component.key === 'do_not_track') {
                    params.do_not_track = component.value;
                }
            }
        }
        params.fingerprint = m.fingerprint;
        return params;
    }
    m.deliverPageEvent = function(event, params) {
        if (!m.firstDeliveryMade && params['counter'] > 0) {
            setTimeout(function() {
                m.deliverPageEvent(event, params);
            }, 5);
            return;
        }
        if (m.fingerprintComponents) {
            params = m.addFingerprint(params);
        }
        if (m.preEventDeliveryQueue.length && m.beforeFirstDeliveryMade === false) {
            for (var i = 0; i < m.preEventDeliveryQueue.length; i++) {
                m.preEventDeliveryQueue[i](params);
            }
            params = m.appendTrackedContact(params);
            m.beforeFirstDeliveryMade = true;
        }
        MauticJS.makeCORSRequest('POST', m.pageTrackingCORSUrl, params, function(response) {
            MauticJS.dispatchEvent('mauticPageEventDelivered', {
                'event': event,
                'params': params,
                'response': response
            });
        }, function() {
            m.buildTrackingImage(event, params);
            m.firstDeliveryMade = true;
        });
    }
    m.buildTrackingImage = function(pageview, params) {
        delete m.trackingPixel;
        m.trackingPixel = new Image();
        if (typeof pageview[3] === 'object') {
            var events = ['onabort', 'onerror', 'onload'];
            for (var i = 0; i < events.length; i++) {
                var e = events[i];
                if (typeof pageview[3][e] === 'function') {
                    m.trackingPixel[e] = pageview[3][e];
                }
            }
        }
        m.trackingPixel.onload = function(e) {
            MauticJS.dispatchEvent('mauticPageEventDelivered', {
                'event': pageview,
                'params': params,
                'image': true
            });
        };
        m.trackingPixel.src = m.pageTrackingUrl + '?' + m.serialize(params);
    }
    m.pageViewCounter = 0;
    m.sendPageview = function(pageview) {
        var queue = [];
        if (!pageview) {
            if (typeof m.getInput === 'function') {
                queue = m.getInput('send', 'pageview');
            } else {
                return false;
            }
        } else {
            queue.push(pageview);
        }
        if (queue) {
            for (var i = 0; i < queue.length; i++) {
                var event = queue[i];
                var params = {
                    page_title: d.title,
                    page_language: n.language,
                    page_referrer: (d.referrer) ? d.referrer.split('/')[2] : '',
                    page_url: l.href,
                    counter: m.pageViewCounter
                };
                params = MauticJS.appendTrackedContact(params);
                if (typeof event[2] === 'object') {
                    for (var attr in event[2]) {
                        params[attr] = event[2][attr];
                    }
                }
                m.handleFingerprintInit(event, params);
                m.pageViewCounter++;
            }
        }
    }
    m.handleFingerprintInit = function(event, params) {
        if (m.fingerprintComponents) {
            m.deliverPageEvent(event, params);
        } else if (!m.fingerprint && m.fingerprintIsLoading === false) {
            m.fingerprintIsLoading = true;
            new Fingerprint2().get(function(result, components) {
                m.fingerprintIsLoading = false;
                m.fingerprint = result;
                m.fingerprintComponents = components;
                m.deliverPageEvent(event, params);
            });
        } else if (m.fingerprintIsLoading === true) {
            var fingerprintLoop = window.setInterval(function() {
                if (m.fingerprintIsLoading === false) {
                    m.deliverPageEvent(event, params);
                    clearInterval(fingerprintLoop);
                }
            }, 5);
        } else {
            m.deliverPageEvent(event, params);
        }
    }
    m.sendPageview();
    document.addEventListener('eventAddedToMauticQueue', function(e) {
        m.sendPageview(e.detail);
    });
}

```

[Go back to top](#tracker-descriptions)

## Webmine
This service has been classified as `Cryptomining` for the following reasons:
### Policy Review
1. The main website `https://webmine.cz` describes its service as a javascript crypto miner.

> We are offering a Javascript miner that can be embedded to your website. This way you can earn XMR with spare CPU power of your website users in the following three steps.
### Technical Review
1. Script contains an implementation of the cryptonight hash algorithm

```
var CryptonightWASMWrapper = function() {
  /** @type {number} */
  this.throttleWait = 0;
  /** @type {number} */
  this.throttledStart = 0;
  /** @type {number} */
  this.throttledHashes = 0;
  this.workThrottledBound = this.workThrottled.bind(this);
  /** @type {null} */
  this.currentJob = null;
  /** @type {!Uint8Array} */
  this.target = new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255]);
  var inputs = Module.HEAPU8.buffer;
  /** @type {!Uint8Array} */
  this.input = new Uint8Array(inputs, Module._malloc(84), 84);
  /** @type {!Uint8Array} */
  this.output = new Uint8Array(inputs, Module._malloc(32), 32);
  self.postMessage("ready");
  self.onmessage = this.onMessage.bind(this);
};
```

[Go back to top](#tracker-descriptions)

## WideOrbit
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://cdn.dep-x.com/t.js?id=DEP-VIC20C64C128&d=DID-YC33ZZAJJOG4`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
("DepBFprint", window, function() {
  "use strict";
  var Fingerprint2 = function(options) {

    if (!(this instanceof Fingerprint2)) {
      return new Fingerprint2(options);
    }

    var defaultOptions = {
      detectScreenOrientation: true,
      sortPluginsFor: [/palemoon/i],
      userDefinedFonts: []
    };
    this.options = this.extend(options, defaultOptions);
    this.nativeForEach = Array.prototype.forEach;
    this.nativeMap = Array.prototype.map;
  };

```
2. Sends computed fingerprint back to server
```
  DepBUser.matchForce = function(partnerName, partnerId, additionalData) {
    var pixel;
    partnerName = partnerName.downcase();
    pixel = new DepBPixel(this.userMatchUri, "match for " + partnerName + " ^^");
    pixel.call({
      pn: partnerName,
      pid: partnerId,
      l_u: this.userLocaStorageID()
    }, additionalData, function(context) {});
    this.markAsMatched(partnerName);
    return this.storeLastPartnerId(partnerName, partnerId);
  };

```

[Go back to top](#tracker-descriptions)

## Yieldmo
This service has been classified as `Advertising` and `FingerprintingGeneral` for the following reasons:
### Policy Review
Yieldmo's privacy policy States:

`https://www.yieldmo.com/privacy-policy/`

>As an End User browses the mobile Internet or uses Apps that include references to the Service, the End User’s browser or device may request advertisements from Yieldmo’s system. When Yieldmo receives these requests, and/or when Yieldmo delivers advertisements to such browser or device, we may collect information about these interactions (as well as any further interaction with the advertisements provided by the Service such as views, clicks, conversions, etc.). This may include, for example: IP address; unique identifiers sent to us from mobile devices, network carriers or data providers; information contained in HTTP headers or other internet transfer protocol signals…attributes of computer or device usage, such as advertisements clicked, websites and content areas visited; date and time of advertisement request, and advertisement delivery and interaction activities; browser type and version; operating system; language setting; information about or from the presence or use of Apps on a mobile device; and location. Such information is stored on Yieldmo’s servers. We may also collect the GPS location of your device if you have opted to provide it to Yieldmo or to one of Yieldmo’s publisher or third party data provider partners. On occasion, we may also receive information from third-parties that enables advertisement optimization, independently of or in combination with the information collected by Yieldmo, such as audience interest segments and product categories.

[Go back to top](#tracker-descriptions)

## ZafulAffiliate
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://js.affasi.com/affasi_js.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var e = function(t) {
        if (!(this instanceof e)) return new e(t);
        this.options = this.extend(t, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to Zaful:
```
                return l.data.affid = i.affid, l.data.ads_lkid = i.lkid, l.data.web_id = i.web_id, l.data.user_id = i.uid, l.data.id = o, l.signature = e("533da74033" + JSON.stringify(l.data)),
                    function(e, t, i, n, a) {
                        var r = "http:" == location.protocol ? "http://affiliate.gw-ec.com/interface/link/create-dynamic" : "https://affiliate.zaful.com/interface/link/create-dynamic";
                        $.ajax({
                            url: r,
                            type: "post",
                            data: e,
                            dataType: "json"
                        }).always(function(e) {
                            if (0 == e.status) {
                                for (var r in e.data) dmp_cacche_dictionary.set(r, e.data[r]);
                                var o = null,
                                    s = "garousel_advert";
                                i.garousel_advert || (s = "img_advert"), i[s].content.forEach(function(e) {
                                    o = dmp_cacche_dictionary.get(e.id), e.link_id = o.link_id, e.link_url = o.link_url
                                }), d(t, i, n, a)
                            }
                        })
                    }({
                        result: JSON.stringify(l)
                    }, t, r, n, a), void(o = i = l = null)


```
[Go back to top](#tracker-descriptions)

## Zefir
This service has been classified as `Advertising` and `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://ze-fir.com/js/t.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
        audio: () => new Promise(function(e) {
            try {
                var t = new(window.AudioContext || window.webkitAudioContext),
                    n = (t.createOscillator(), t.createAnalyser(), t.createGain(), t.createScriptProcessor(4096, 1, 1), t.destination);
                return e(t.sampleRate.toString() + "_" + n.maxChannelCount + "_" + n.numberOfInputs + "_" + n.numberOfOutputs + "_" + n.channelCount + "_" + n.channelCountMode + "_" + n.channelInterpretation)
            } catch (t) {
                return e("")
            }
        }),
        colorDepth: () => new Promise(function(e) {
            var t = screen.colorDepth;
            return 32 === t && (t = 24), e(t || "")
        }),
        cpuClass: () => new Promise(function(e) {
            return e(navigator.cpuClass || "")
        }),

```
2. Sends computed fingerprint back to server
```
this.sendStat = function(t, n, i, a) {
                return n = n || "POST", i = i || e.opts.statUrl, a = a || {}, new Promise(function(c, u) {
                    var s = new XMLHttpRequest;
                    s.withCredentials = !0, "withCredentials" in s ? s.open(n, i, !0) : "undefined" != typeof XDomainRequest ? (s = new XDomainRequest).open(n, i) : s = null, s.onreadystatechange = function() {
                        if (4 === s.readyState && 200 === s.status) {
                            var t = JSON.parse(s.responseText);
                            c(t), e.syncResolve(t), t.runTests ? r.runTests().then(function(n) {
                                var r = Object.assign({}, n.testResults, {
                                    device: n.deviceTestsPrint,
                                    browser: n.browserTestsPrint
                                });
                                r.canvas = o.x86.hash128(JSON.stringify(r.canvas)), e.sendStat({
                                    agent: r
                                }, !1, e.opts.statUrl + "/" + t.id)
                            }) : t.runTests || t.bad ? !t.runTests && t.bad && e.humanFail("its bad") : e.humanResolve()
                        }
                    };
                    var f = new FormData;
                    for (var l in e.opts.id && f.append("id", e.opts.id), f.append("data", JSON.stringify(t)), f.append("url", window.location.href), f.append("referrer", document.referrer), a) a.hasOwnProperty(l) && s.setRequestHeader(l, a[l]);
                    s.send(f)
                })
            }

```
[Go back to top](#tracker-descriptions)

## Zip
This service has been classified as `FingerprintingInvasive` for the following reasons:
### Technical Review
Script: `https://static.zipmoney.com.au/lib/js/zm-widget-js/modules/vendors~fingerprint.bundle.c04703fa41fd7e01128a.js`   
Submission source: Submitted for review by Mozilla (2020-06-25_v10-Fingerprinter_report)  
1. Script makes several calls to known invasive fingerprinting APIs. These API calls were observed using [OpenWPM](https://github.com/mozilla/OpenWPM):
```
{"is_audio": true, "is_canvas": true, "is_webrtc": false, "is_canvas_font": false, "audio_api_calls": [{"value": "", "symbol": "OfflineAudioContext.createOscillator", "arguments": null, "operation": "call"}, {"value": "", "symbol": "OfflineAudioContext.createDynamicsCompressor", "arguments": null, "operation": "call"}, {"value": "{}", "symbol": "OfflineAudioContext.destination", "arguments": null, "operation": "get"}, {"value": "", "symbol": "OfflineAudioContext.startRendering", "arguments": null, "operation": "call"}, {"value": "FUNCTION", "symbol": "OfflineAudioContext.oncomplete", "arguments": null, "operation": "set"}], "canvas_api_calls": [{"value": "#f60", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "#069", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "11pt no-real-font-123", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",2,15]", "operation": "call"}, {"value": "rgba(102, 204, 0, 0.2)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "18pt Arial", "symbol": "CanvasRenderingContext2D.font", "arguments": null, "operation": "set"}, {"value": "", "symbol": "CanvasRenderingContext2D.fillText", "arguments": "[\"Cwm fjordbank glyphs vext quiz, 😃\",4,45]", "operation": "call"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(0,255,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,255,0)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "rgb(255,0,255)", "symbol": "CanvasRenderingContext2D.fillStyle", "arguments": null, "operation": "set"}, {"value": "", "symbol": "HTMLCanvasElement.toDataURL", "arguments": null, "operation": "call"}]}
```
[Go back to top](#tracker-descriptions)

