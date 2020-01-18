# Tracker Descriptions
- [Adabra](#Adabra)
- [Adbot](#Adbot)
- [AdGainerSolutions](#AdGainerSolutions)
- [AdMaven](#AdMaven)
- [Admicro](#Admicro)
- [Adnium](#Adnium)
- [AdScore](#AdScore)
- [AdYouLike](#AdYouLike)
- [AivaLabs](#AivaLabs)
- [a.js](#a.js)
- [Albacross](#Albacross)
- [AppCast](#AppCast)
- [AuditedMedia](#AuditedMedia)
- [Augur](#Augur)
- [AvantLink](#AvantLink)
- [Azet](#Azet)
- [BetssonPalantir](#BetssonPalantir)
- [BigClick](#BigClick)
- [BitMedia](#BitMedia)
- [BlueCava](#BlueCava)
- [BoostBox](#BoostBox)
- [Brandcrumb](#Brandcrumb)
- [BreakTime](#BreakTime)
- [BrightEdge](#BrightEdge)
- [C3-Metrics](#C3-Metrics)
- [CallSource](#CallSource)
- [CartsGuru](#CartsGuru)
- [CashBeet](#CashBeet)
- [ClearLink](#ClearLink)
- [Clickayab](#Clickayab)
- [ClickFrog](#ClickFrog)
- [ClickGuard](#ClickGuard)
- [Clixtell](#Clixtell)
- [CoinHive](#CoinHive)
- [CoinPot](#CoinPot)
- [CryptoLoot](#CryptoLoot)
- [DoubleVerify](#DoubleVerify)
- [ECSAnalytics](#ECSAnalytics)
- [EroAdvertising](#EroAdvertising)
- [EyeNewton](#EyeNewton)
- [eyeReturn-Marketing](#eyeReturn-Marketing)
- [Fanplayr](#Fanplayr)
- [Foresee](#Foresee)
- [Friends2Follow](#Friends2Follow)
- [FuelX](#FuelX)
- [Gleam](#Gleam)
- [GrapheneMedia](#GrapheneMedia)
- [Gridcash](#Gridcash)
- [HilltopAds](#HilltopAds)
- [HotelChamp](#HotelChamp)
- [HotMart](#HotMart)
- [iMedia](#iMedia)
- [IslayTech](#IslayTech)
- [ismatlab.com](#ismatlab.com)
- [Itch](#Itch)
- [JSE](#JSE)
- [Konduto](#Konduto)
- [LeadsHub](#LeadsHub)
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
- [Opolen](#Opolen)
- [Paypal](#Paypal)
- [PerimeterX](#PerimeterX)
- [PinPoll](#PinPoll)
- [Poool](#Poool)
- [PPCProtect](#PPCProtect)
- [PrismApp](#PrismApp)
- [PrometheusIntelligenceTechnology](#PrometheusIntelligenceTechnology)
- [Provers](#Provers)
- [Psonstrentie](#Psonstrentie)
- [Rollick](#Rollick)
- [SAP](#SAP)
- [Semantiqo](#Semantiqo)
- [SendPulse](#SendPulse)
- [SiftScience](#SiftScience)
- [Smi](#Smi)
- [Socital](#Socital)
- [SpareChange](#SpareChange)
- [StackTrack](#StackTrack)
- [Storeland](#Storeland)
- [TechSolutions](#TechSolutions)
- [Upland](#Upland)
- [USocial](#USocial)
- [Vendemore](#Vendemore)
- [VerticalHealth](#VerticalHealth)
- [ViralLoops](#ViralLoops)
- [Webmecanik](#Webmecanik)
- [Webmine](#Webmine)
- [WideOrbit](#WideOrbit)
- [ZafulAffiliate](#ZafulAffiliate)
- [Zefir](#Zefir)
## Adabra
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## AdGainerSolutions
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## AdMaven
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## AdScore
This service has been classified as `Fingerprinting` for the following reasons:
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

## AdYouLike
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://serve.albacross.com/track.js`
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
2. Sends computed fingerprint back to server:
```
NosivaCore.getCollectorUrl = function(env) {
            switch (env) {
                case "production":
                    return "https://collect.albacross.com";
                case "staging":
                    return "http://collect.albakaos.com";
                case "local":
                    return "http://localhost:8080"
            }
        }

NosivaCore.markers = {}, NosivaCore.params = ["first_name", "last_name", "email", "company_name", "company_number", "campaign_id", "ad_id", "adform_tag_id", "adform_advertiser_id", "adform_campaign_id", "adform_tracking_setup_id", "adform_creative_id", "adform_cookie_id", "adform_unique_impression_id", "adform_media_id", "adform_line_item_id", "adform_media_network_id", "adform_banner_domain", "adform_rtb_inventory_source_id", "adform_rtb_domain", "adform_rtb_deal_or_package_id", "adform_request_id", "adform_advertising_id", "adform_external_publisher_id"], NosivaCore.shortFormat = !1, NosivaCore.domReady = function(fn) {
            "loading" != document.readyState ? fn() : document.addEventListener ? document.addEventListener("DOMContentLoaded", fn) : document.attachEvent("onreadystatechange", function() {
                "loading" != document.readyState && fn()
            })
        }, NosivaCore.sendEvents = function(events, callback, retries) {
            if (document.body) {
                "undefined" == typeof retries && (retries = 0), "undefined" != typeof callback && null !== callback && callback();
                var url = "";
                url = NosivaCore.shortFormat ? NosivaCore.getCollectorUrl(Nosiva.environment) + "/e.gif?" + NosivaCore.stringifyEvents(events, !0) : NosivaCore.getCollectorUrl(Nosiva.environment) + "/d.gif?d=" + NosivaCore.stringifyEvents(events, !1);
                var img = new Image;
                img.height = 0, img.width = 0, img.style.height = "0", img.style.width = "0", img.style.border = "0", img.style.margin = "0", img.style.padding = "0", img.style.position = "fixed", img.style.bottom = "0", img.style.left = "0", img.src = url, document.body.appendChild(img), img.onload = function() {
                    null !== img.parentNode && document.body.removeChild(img)
                }, 2 > retries && (img.onerror = function() {
                    setTimeout(function() {
                        document.body.removeChild(img), NosivaCore.sendEvents(events, null, retries + 1)
                    }, 1e3)
                })
            }
        }



```

[Go back to top](#tracker-descriptions)

## AppCast
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://click.appcast.io/pixels/generic1-6607.js?ent=196`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    Fingerprint.prototype = {
        get: function() {
            var keys = [];
            keys.push(navigator.userAgent);
            keys.push(navigator.language);
            keys.push(screen.colorDepth);
            keys.push((new Date).getTimezoneOffset());
            keys.push(!!window.sessionStorage);
            keys.push(this.hasLocalStorage());
            keys.push(!!window.indexedDB);
            keys.push(typeof document.body.addBehavior);
            keys.push(typeof window.openDatabase);
            keys.push(navigator.cpuClass);
            keys.push(navigator.platform);
            keys.push(navigator.doNotTrack);

```
2. Sends computed fingerprint back to server
```
try {
            var img = document.createElement("img"),
                action = "generic-te8/a31";;;;;;;;;;;
            try {
                ''
            } catch (ex) {}
            saveReqNumToSessionStorage(reqNum);
            var url = "https://click.appcast.io/" +
                action + ".png?r=" + encodeURIComponent(document.referrer) + (reqNum ? "&jid=" + reqNum : "") + "&tn=" + now + "&rn=" + random + "&fp=" + fp + window.acEmployerId;
            if (jobSeekerId) url += "&jsid=" + jobSeekerId;
            if (pSrc) url += "&psrc=" + pSrc;
            if (misc) url += "&misc=" + misc;
            if (aid) url += "&aid=" + aid;
            if (fa) url += "&fa=" + fa;
            if (exchangeId) url += "&exch=" + exchangeId;
            if (ccid) url += "&ccid=" + ccid;
            if (pid) url += "&pid=" + pid;
            if (cid) url += "&cid=" + cid;
            if (jt) url += "&jt=" + jt;
            img.src = url;
            img.style.display = "none";
            document.body.appendChild(img);
            if (/te8\/a31/i.test(action)) window.acAction =
                0;
            else if (/ue8\/a7/i.test(action)) window.acAction = 1;
            else if (/9k\/a17/i.test(action)) window.acAction = 2
        } catch (e$3) {}


```

[Go back to top](#tracker-descriptions)

## AuditedMedia
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Policy Review
1. Augur claims that they track users via devices, not through cookies. - `https://www.mediapost.com/publications/article/166916/bluecava-touts-device-fingerprinting.html`

> A set of APIs and tools that instantly enables businesses to recognize devices, and consumers across devices. - `https://www.augur.io/#landingPage`

> Cookie-less tracking - Instead of cookies (which cause mis-attribution), Augur uses CAKE, a multi-layer recognition architecture.

2. Augur claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://www.augur.io/privacypolicy`

> To deliver the Augur Services, our software collects, organizes, and uses Non-PII. This information includes, the date and time of visits to a Client Property, browser information (e.g., browser type, font signature), operating system information (e.g. screen resolution), IP addresses, non-precise geographic information ( e.g. time zone, city, state, country), battery level, and user agent

## AvantLink
This service has been classified as `Analytics`, `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://cdn.avmws.com/1013737/`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var defaultOptions = {
        preprocessor: null,
        audio: {
            timeout: 1e3,
            excludeIOS11: true
        },
        fonts: {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            userDefinedFonts: [],
            extendedJsFonts: false
        },
        screen: {
            detectScreenOrientation: true
        },
        plugins: {
            sortPluginsFor: [/palemoon/i],
            excludeIE: false
        },
        extraComponents: [],
        excludes: {
            enumerateDevices: true,
            pixelRatio: true,
            doNotTrack: true,
            fontsFlash: true
        },
        NOT_AVAILABLE: "not available",
        ERROR: "error",
        EXCLUDED: "excluded"
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

## Azet
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## BitMedia
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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

## BoostBox
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## Brandcrumb
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## ClearLink
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `http://supplier.clickyab.com/api/multi.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

```
swfContainerId:"fingerprintjs2"
```
[Go back to top](#tracker-descriptions)

## ClickFrog
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
### Policy Review
1. Doubleverify states they attempt to identify particular devices - `https://www.doubleverify.com/privacy/`

> and other data including browser configuration parameters such as browser language and session storage and local storage settings, and characteristics of your device such as the CPU class and time zone setting.

> Device identification technology, which analyzes device parameters collected as described above, including IP address and browser header information, to probabilistically identify a particular device. 
### Technical Review
1. Script uses canvas/font fingerprinting to fingerprint users

```
var canvasDrawBG = c.g.createElement("canvas");
if (canvasDrawBG.getContext && canvasDrawBG.getContext("2d")) {
  var ctx = canvasDrawBG.getContext("2d");
  /** @type {string} */
  ctx.textBaseline = "top";
  /** @type {string} */
  ctx.font = "14px Arial";
  /** @type {string} */
  ctx.textBaseline = "alphabetic";
  /** @type {string} */
  ctx.fillStyle = "#f60";
  ctx.fillRect(0, 0, 62, 20);
  /** @type {string} */
  ctx.fillStyle = "#069";
  ctx.fillText("!image!", 2, 15);
  /** @type {string} */
  ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
  ctx.fillText("!image!", 4, 17);
  return canvasDrawBG.toDataURL();
}
```

2. Script probes device properties to attempt to fingerprint users

```
sortable.push(["lang", this.navigator.language || navigator.browserLanguage]);
sortable.push(["tz", d.i.getTimezoneOffset()]);
sortable.push(["hss", this.Yt() ? "1" : "0"]);
sortable.push(["hls", this.Xt() ? "1" : "0"]);
sortable.push(["odb", typeof this.o.openDatabase]);
sortable.push(["cpu", this.navigator.cpuClass || ""]);
sortable.push(["pf", this.navigator.platform || ""]);
sortable.push(["dnt", this.navigator.doNotTrack || ""]);
sortable.push(["canv", this.Ps()]);
```
[Go back to top](#tracker-descriptions)

## ECSAnalytics
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## EyeNewton
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://eyenewton.ru/scripts/callback.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
                var c = setTimeout(function() {
                    return console.warn('Audio fingerprint timed out. Please report bug at https://github.com/Valve/fingerprintjs2 with your user agent: "' + navigator.userAgent + '".'), i.oncomplete = function() {}, i = null, n("audioTimeout")
                }, t.timeout);


```
2. Sends computed fingerprint back to server
```
ajax.get(settings_url, e, function(t) {
                if (eyenewtonLoader.next(), !t) return clearInterval(init_interval), !1;
                try {
                    var e = JSON.parse(t)
                } catch (e) {
                    return remoteErrorLog(e, "getSettings", typeof t + " " + t.length + " " + t), !1
                }
                if (0 == e.length) return clearInterval(init_interval), !1;
                if ("undefined" != typeof newton_callback_id_internal && null != e.callback_id && newton_callback_id_internal != e.callback_id) return clearInterval(init_interval), !1;
                if ((default_settings = merge_options(default_settings, e)).callback) {
                    default_settings.appearance_disabled = parseInt(default_settings.appearance_disabled), disableAppearanceOnMainPageLot(), default_settings.appearance_init = parseInt(default_settings.appearance_init), default_settings.appearance_exit = parseInt(default_settings.appearance_exit), default_settings.appearance_time = parseInt(default_settings.appearance_time), default_settings.current_time = parseInt(default_settings.current_time), default_settings.show_once_day = parseInt(default_settings.show_once_day), default_settings.hide_after_hours = parseInt(default_settings.hide_after_hours), default_settings.show_on_mobile = parseInt(default_settings.show_on_mobile), default_settings.dialog_enabled = parseInt(default_settings.dialog_enabled), default_settings.disable_delayed_calls = parseInt(default_settings.disable_delayed_calls), default_settings.have_departments = parseInt(default_settings.have_departments), default_settings.silent_mode = 1 == default_settings.silent_mode, default_settings.is_multiwidget = parseInt(default_settings.is_multiwidget), default_settings.multiwidget_application = parseInt(default_settings.multiwidget_application), default_settings.multiwidget_consultant = parseInt(default_settings.multiwidget_consultant), default_settings.enable_mobile_direct_call = parseInt(default_settings.enable_mobile_direct_call), default_settings.enable_log = parseInt(default_settings.enable_log), default_settings.chat_enabled = parseInt(default_settings.chat_enabled), default_settings.chat_active = parseInt(default_settings.chat_active), default_settings.manager_photo_enabled = parseInt(default_settings.manager_photo_enabled), default_settings.banner_enabled = parseInt(default_settings.banner_enabled), default_settings.banner_bottom = parseInt(default_settings.banner_bottom), default_settings.mini_version_enabled = parseInt(default_settings.mini_version_enabled);
                    var n = getParam("show_phone_button");
                    void 0 !== n && (default_settings.show_phone_button = n), null == (init_time = getInitTime()) && setInitTime(init_time = default_settings.current_time)
                }
                settingsLoaded = !0
            })
```

[Go back to top](#tracker-descriptions)

## eyeReturn Marketing
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Policy Review
1. Eyereturn claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://eyereturnmarketing.com/privacy/`

> Statistical IDs are created via an algorithm using non-personally identifiable and pseudonymous information about a computer or device. The information used may include the operating system, user-agent string, Web browser, approximate location, installed fonts, and similar information. This information makes your computer or device distinct enough for our systems to determine within a reasonable probability that they are encountering the same computer or device. These IDs are not used to target advertisements, and are only used for campaign analytics and reporting purposes
## Fanplayr
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://d38nbbai6u794i.cloudfront.net/client/production/platform/releases/1.56.0/platform.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

```
                cpuClassKey: function(a) {
                    return this.options.excludeCpuClass || a.push(this.getNavigatorCpuClass()), a
                },
                platformKey: function(a) {
                    return this.options.excludePlatform || a.push(this.getNavigatorPlatform()), a
                },
                doNotTrackKey: function(a) {
                    return this.options.excludeDoNotTrack || a.push(this.getDoNotTrack()), a
                },
                canvasKey: function(a) {
                    return !this.options.excludeCanvas && this.isCanvasSupported() && a.push(this.getCanvasFp()), a
                },
                webglKey: function(a) {
                    return !this.options.excludeWebGL && this.isCanvasSupported() && a.push(this.getWebglFp()), a
                },
                pluginsKey: function(a) {
                    return this.isIE() ? a.push(this.getIEPluginsString()) : a.push(this.getRegularPluginsString()), a
                },

```
2. Script then sends fingerprint to Fanplayer server
[Go back to top](#tracker-descriptions)

## Foresee
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## GrapheneMedia
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://api-identification.hotmart.com/id.min.js?account=a7d0d5a7-b5f0-49a5-9627-ebe36b4c8e8f`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
webglKey: function(a) {
                    if (this.options.excludeWebGL) return "undefined" === typeof NODEBUG && this.log("Skipping WebGL fingerprinting per excludeWebGL configuration option"), a;
                    if (!this.isWebGlSupported()) return "undefined" === typeof NODEBUG && this.log("Skipping WebGL fingerprinting because it is not supported in this browser"), a;
                    a.push(this.getWebglFp());
                    return a
                }, adBlockKey: function(a) {
                    this.options.excludeAdBlock || a.push(this.getAdBlock());
                    return a
                }, hasLiedLanguagesKey: function(a) {
                    this.options.excludeHasLiedLanguages || a.push(this.getHasLiedLanguages());
                    return a
                }, hasLiedResolutionKey: function(a) {
                    this.options.excludeHasLiedResolution || a.push(this.getHasLiedResolution());
                    return a
                }
```
2. Sends computed fingerprint back to server
```
window.hotlobj.config = {
    CONSOLE_DEBUG: 0,
    VISUAL_DEBUG: 0,
    HOTID: 'hotid',
    COOKIE_AGE_MINUTES: 25920000,
    DOMAIN: '.hotmart.com',
    IDENTIFICATION_PIXEL_URL: 'https://api-identification.hotmart.com/id.gif',
    TRACKING_REST_URL: 'https://tracking-api.hotmart.com/rest/track'
};


```

[Go back to top](#tracker-descriptions)

## iMedia
This service has been classified as `Fingerprinting` for the following reasons:
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

## IslayTech
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Fingerprinting` for the following reasons:
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

## Konduto
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Fingerprinting` for the following reasons:
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

## lptracker
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://stats.lptracker.io/lpt_widget/out/main.min.js?2.20.0-312-g9dbe2215e8-dirty`
1. Script embeds on open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

2. Sends fingerprint to tracking company, `https://stats.lptracker.io/track`
```
{"site_id":62106,"fingerprint_hash":"XXXXXXXXXXX","version":"2.20.0-312-g9dbe2215e8-dirty","page":"https://green-game.ru/","domain":"green-game.ru","referer":"https://green-game.ru/"}: 
   ```
[Go back to top](#tracker-descriptions)

## MaxMind
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Policy Review
1. Mediamath purchased Tactads, a provider of "cookieless and cross-device targeting technologies" - `https://www.mediamath.com/news/press-release-mediamath-acquires-tactads-to-enable-cookieless-cross-device-targeting-and-measurement/`

> MediaMath, the creator of the TerminalOne Marketing Operating System™ for digital marketers, today announced its acquisition of Tactads, provider of cookieless and cross-device targeting technologies. Integrated into TerminalOne, these technologies will provide advertisers the ability to communicate with consumers and unify marketing efforts across smartphone, tablet, laptop, desktop, and other devices...

> Tactads, a France-based company, has developed proprietary software that uses sophisticated algorithms to identify and associate devices using statistical techniques...

2. MediaMath privacy policy states they use cookieless tracking and specifically states they profile installed fonts and "similar information" - https://www.mediamath.com/privacy-policy/#Section-2

> The MediaMath ID can be a cookie ID (a unique ID assigned randomly by MediaMath to an unrecognized browser), a mobile advertising ID (a unique ID assigned by the mobile operating system, e.g. Apple ID for Advertising or Android Advertising ID), an OTT TV Device Identifier for Advertising (a unique ID assigned by an OTT TV provider, e.g., Roku ID for Advertising), or a statistical ID (created by MediaMath). We use information about your computer or device to generate the statistical ID, including your operating system, user-agent string, Internet Protocol (“IP”) address, installed fonts, and similar information. This information makes your computer or device distinct enough for our systems to determine within a reasonable probability that they are encountering the same computer or device over time, including in environments where MediaMath cookies are not supported.
### Technical Review
1. Script uses canvas/font fingerprinting to fingerprint users

```
var render = function(type) {
  /**
    * @param {string} id
    * @return {?}
    */
  function init(id) {
    /** @type {boolean} */
    var result = false;
    /** @type {number} */
    var i = 0;
    for (; i < baseFonts.length; i++) {
      if (target == "dom") {
        /** @type {string} */
        s.style.fontFamily = id + "," + baseFonts[i];
        o.appendChild(s);
        /** @type {boolean} */
        var val = s.offsetWidth != defaultWidth[baseFonts[i]] || s.offsetHeight != defaultHeight[baseFonts[i]];
        o.removeChild(s);
      } else {
        if (target == "canvas") {
          /** @type {string} */
          ctx.font = part + " " + id + "," + baseFonts[i];
          /** @type {boolean} */
          val = ctx.measureText(testString).width != defaultWidth[baseFonts[i]];
        }
      }
      /** @type {(boolean|undefined)} */
      result = result || val;
    }
    return result;
  }
  /** @type {!Array} */
  var baseFonts = ["monospace", "sans-serif", "serif"];
  /** @type {string} */
  var testString = "mmmmmmmmmmlli";
  /** @type {string} */
  var part = "72px";
  if (type != "dom") {
    /** @type {string} */
    var target = "canvas";
    /** @type {!Element} */
    var result = document.createElement("canvas");
    /** @type {string} */
    result.width = "100";
    /** @type {string} */
    result.height = "100";
    globalContainer$jscomp$0.appendChild(result);
  }
  if (!result || typeof result.getContext != "function") {
    /** @type {string} */
    target = "dom";
    var o = globalContainer$jscomp$0;
    /** @type {!Element} */
    var s = document.createElement("span");
    /** @type {string} */
    s.style.fontSize = part;
    /** @type {string} */
    s.innerHTML = testString;
    var defaultWidth = {};
    var defaultHeight = {};
    /** @type {number} */
    var i = 0;
    for (; i < baseFonts.length; i++) {
      s.style.fontFamily = baseFonts[i];
      o.appendChild(s);
      defaultWidth[baseFonts[i]] = s.offsetWidth;
      defaultHeight[baseFonts[i]] = s.offsetHeight;
      o.removeChild(s);
    }
  } else {
    var ctx = result.getContext("2d");
    defaultWidth = {};
    /** @type {number} */
    i = 0;
    for (; i < baseFonts.length; i++) {
      /** @type {string} */
      ctx.font = part + " " + baseFonts[i];
      defaultWidth[baseFonts[i]] = ctx.measureText(testString).width;
    }
  }
  /** @type {function(string): ?} */
  this.detect = init;
  /** @type {(string|undefined)} */
  this.method = target;
};
```

2. Script probes device properties to attempt to fingerprint users

```
/** @type {string} */
resultsFromProbes$jscomp$0["bcap"] = [$mime_type, prKey, getWindowData$jscomp$0("navigator", "cookieEnabled")].join("|");
}();
!function() {
/** @type {string} */
resultsFromProbes$jscomp$0["lges"] = [getWindowData$jscomp$0("navigator", "browserLanguage"), getWindowData$jscomp$0("navigator", "language"), getWindowData$jscomp$0("navigator", "userLanguage")].join("|");
}();
!function() {
/** @type {string} */
resultsFromProbes$jscomp$0["ob"] = [getWindowData$jscomp$0("navigator", "appCodeName"), getWindowData$jscomp$0("navigator", "appName"), getWindowData$jscomp$0("navigator", "platform"), getWindowData$jscomp$0("navigator", "cpuClass")].join("|");
}();

var get_date_offset = function(date) {
  /** @type {number} */
  var t = -date.getTimezoneOffset();
  return t !== null ? t : 0;
};

!function() {
  /** @type {string} */
  resultsFromProbes$jscomp$0["sc"] = [getWindowData$jscomp$0("screen", "width"), getWindowData$jscomp$0("screen", "height"), getWindowData$jscomp$0("screen", "availWidth"), getWindowData$jscomp$0("screen", "availHeight"), getWindowData$jscomp$0("screen", "pixelDepth"), getWindowData$jscomp$0("screen", "deviceXDPI"), getWindowData$jscomp$0("screen", "deviceYDPI")].join("|");
}();

PluginDetect$jscomp$0.java = {
mimeType : "application/x-java-applet",
classID : "clsid:8AD9C840-044E-11D1-B3E9-00805F499D93",
DTKclassID : "clsid:CAFEEFAC-DEC7-0000-0000-ABCDEFFEDCBA",
DTKmimeType : "application/npruntime-scriptable-plugin;DeploymentToolkit",

PluginDetect$jscomp$0.quicktime = {
mimeType : ["video/quicktime", "application/x-quicktimeplayer", "image/x-macpaint", "image/x-quicktime"],
progID : "QuickTimeCheckObject.QuickTimeCheck.1",
progID0 : "QuickTime.QuickTime",
classID : "clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B",
minIEver : 7,

PluginDetect$jscomp$0.devalvr = {
mimeType : "application/x-devalvrx",
progID : "DevalVRXCtrl.DevalVRXCtrl.1",
classID : "clsid:5D2CF9D0-113A-476B-986F-288B54571614",

PluginDetect$jscomp$0.flash = {
mimeType : ["application/x-shockwave-flash", "application/futuresplash"],
progID : "ShockwaveFlash.ShockwaveFlash",
classID : "clsid:D27CDB6E-AE6D-11CF-96B8-444553540000",

```

[Go back to top](#tracker-descriptions)

## Mercadopago
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `http://u.openx.net/tq/pi?k=gateway&rid=ab18c828-8715-4b6b-973c-aef4be5b121b&rt=1549406488`
1. Script generates fingerprint by querying various device properties including audio and canvas:
```
            var Y = D.OfflineAudioContext || D.webkitOfflineAudioContext;
            var Z = "u_audio_context";
            if (!Y) {
                return T(Z, "n/a")
            }
            try {
                var X = new Y(1, 44100, 44100);
                var V = X.createDynamicsCompressor();
                var U = X.createOscillator();
                U.type = "triangle";
                U.frequency.value = 10000;
                X.oncomplete = function(ab) {
                    for (var ad = ab.renderedBuffer.getChannelData(0), aa = 0, ac = 4500; ac < 5000; ac++) {
                        U += Math.abs(ad[ac])
                    }
                    T(Z, j("" + aa));
                    V.disconnect()
                };
                U.connect(V);
                V.connect(X.destination);
                U.start(0);
                X.startRendering()
            } catch (W) {
                T(Z, "error")
            }

        var H;
        var I;
        var K = "1";
        try {
            I = E.createElement("div");
            I.style.position = "absolute";
            I.style.width = I.style.height = I.style.border = I.style.padding = I.style.margin = 0;
            I.style.overflow = "hidden";
            E.body.appendChild(I);
            H = E.createElement("canvas");
            H.width = H.height = 10;
            I.appendChild(H);
            H.getContext("2d").strokeText("true", 0, 0)
        } catch (J) {
            K = "0"
        } finally {
            H && I && I.removeChild(H)
        }
        return K

```
2. Sends computed fingerprint back to server
```
Request URL: http://delivery-us-west-1.openx.net/w/1.0/ri?ph=REMOVED&ts=REMOVED
```

[Go back to top](#tracker-descriptions)

## Opolen
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://static.opolen.com.br/polen-lojaintegrada-pollinator.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var n = function(t) {
        if (!(this instanceof n)) return new n(t);
        this.options = this.extend(t, {
            swfContainerId: "fingerprintjs2",
            swfPath: "flash/compiled/FontList.swf",
            detectScreenOrientation: !0,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: [],
            excludeDoNotTrack: !0,
            excludePixelRatio: !0
        });
        this.nativeForEach = Array.prototype.forEach;
        this.nativeMap = Array.prototype.map
    };

```
2. Sends computed fingerprint back to server:
```
loadPolenContainer: function() {
            try {
                if (polenFramework.polenKey == null) {
                    polenHelper.logList.push("Polen key not found");
                    return
                }
                var n = polenStorage.getPolenContainer(),
                    t = polenStorage.getPolenTransactionId(n);
                jPolen.when(polenHelper.generateFingerprint()).done(function(n) {
                    var r = polenHelper.getParameterByName("polen") == "ativo" ? !1 : null,
                        u = polenHelper.mobilecheck(),
                        i = {
                            key: polenFramework.polenKey,
                            domain: polenFramework.domain,
                            page: polenFramework.currentUrl,
                            transactionId: t,
                            abTestName: "",
                            ngoUrl: "",
                            fingerprint: n,
                            original: r,
                            isMobile: u
                        };
                    jPolen.when(polenHelper.post(polenHelper.apiUrl + "/Transaction/GetPolenContainer/", i)).done(function(n) {
                        n ? n.success ? (polenStorage.setPolenContainer(n), polenStorage.setIsOriginal(n.original), polenStorage.setPolenTransactionId(n.transactionId), polenFramework.polenHtmlLoaded == !1 && (polenFramework.loadHtml(), polenFramework.polenHtmlLoaded = !0), polenPlatform.Load(), polenFramework.triggerTracers()) : n.unauthorizedUrl ? polenStorage.setPolenContainer(n.data) : polenHelper.log({
                            message: "errorType: " + n.errorType,
                            stack: n.errorDescription + " / " + n.errorDescription2
                        }, "post transaction/loadPolenContainer success=false", JSON.stringify(i), n.logToDatabase) : polenHelper.log({
                            message: "errorType: Api returned null",
                            stack: "errorType: Api returned null"
                        }, "post transaction/loadPolenContainer null", JSON.stringify(i))
                    }).fail(function(n, t, r) {
                        polenHelper.checkUrlChange();
                        polenHelper.log({
                            message: r + " " + n.status,
                            stack: n.responseText
                        }, "post transaction/loadPolenContainer", JSON.stringify(i), n.responseJSON.logToDatabase)
                    })
                }).fail(function(n, t, i) {
                    polenHelper.log({
                        message: i + " " + n.status,
                        stack: n.responseText
                    }, "post GET FINGERPRINT", JSON.stringify(request))
                })
            } catch (i) {
                polenHelper.log(i, "LoadPolen", "cookieEnabled:" + navigator.cookieEnabled)
            }
        }


```

[Go back to top](#tracker-descriptions)

## Paypal
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://pinpoll.com/global.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
var Fingerprint2 = function e(t) {
    if (!(this instanceof e)) return new e(t);
    this.options = this.extend(t, {
        swfContainerId: "fingerprintjs2",
        swfPath: "flash/compiled/FontList.swf",
        detectScreenOrientation: !0,
        sortPluginsFor: [/palemoon/i],
        userDefinedFonts: [],
        excludeDoNotTrack: !0
    }), this.nativeForEach = Array.prototype.forEach, this.nativeMap = Array.prototype.map
};
```
2. Sends computed fingerprint back to pinpoll.com:
```
                    d.style.display = "none", d.src = "https://static.pinpoll.com/static/start.html";
                    var u = !1,
                        p = function() {
                            !u && a && l && (function() {
                                0 === s.offsetHeight && (r = !0), s.remove(), d.remove();
                                var a = {
                                    plugins: n(),
                                    timezone: (new Date).getTimezoneOffset(),
                                    adblock: r ? 1 : 0,
                                    dnt: window.navigator.doNotTrack,
                                    cookiesEnabled: o() ? 1 : 0,
                                    thirdPartyCookiesEnabled: c ? 1 : 0,
                                    referrer: document.referrer,
                                    title: document.title,
                                    location: {
                                        hash: document.location.hash,
                                        hostname: document.location.hostname,
                                        pathname: document.location.pathname,
                                        protocol: document.location.protocol,
                                        search: document.location.search
                                    },
                                    screen: {
                                        width: window.screen.width,
                                        height: window.screen.height,
                                        colorDepth: window.screen.colorDepth,
                                        orientation: window.screen.orientation ? window.screen.orientation.type : null
                                    },
                                    metaTags: i(),
                                    fingerprint: t.fingerprint
                                };
                                e.open("post", "https://pa.pinpoll.com/v1/"), e.withCredentials = !0, e.setRequestHeader("Content-Type", "application/json"), e.send(JSON.stringify(a))
                            }(), u = !0)
                        };

```

[Go back to top](#tracker-descriptions)

## Poool
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://assets.poool.fr/poool-identity.min.js`
1. Script generates fingerprint by querying various device properties:
```
{
                    key: "getScreenResolution",
                    value: function() {
                        return window.screen.width && window.screen.height ? window.screen.height > window.screen.width ? [window.screen.height, window.screen.width] : [window.screen.width, window.screen.height] : [0, 0]
                    }
                }, {
                    key: "getCanvasSignature",
                    value: function() {
                        var t = $.getContext("2d"),
                            e = "http://www.poool.fr";
                        return t.clearRect(0, 0, $.width, $.height), t.textBaseline = "top", t.font = "14px 'Arial'", t.textBaseline = "alphabetic", t.fillStyle = "#f60", t.fillRect(125, 1, 62, 20), t.fillStyle = "#069", t.fillText(e, 2, 15), t.fillStyle = "rgba(102, 204, 0, 0.7)", t.fillText(e, 4, 17), $.toDataURL()
                    }
                }


```
2. Sends computed fingerprint back to server
```
{
                    key: "headers",
                    value: function(t) {
                        var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
                            n = {
                                "Content-Type": "application/json"
                            };
                        if (!1 !== e.app && (n["Bundle-Identifier"] = G.a.get("app_id")), !1 !== e.fingerprint && (n.FTag = V.get()), !1 !== e.identity && (n.PTag = I.a.get("_poool") || G.a.get("$user_id") || ""), !1 !== e.additional && !0 === G.a.get("cookies_enabled")) {
                            var r = window.xprops,
                                o = r.windowWidth,
                                i = r.windowHeight;
                            n.Additional = "" + "screen=".concat(o, "x").concat(i, ";") + "locale=".concat(ot.a.getLocale(), ";") + "mobile=".concat(ot.a.isMobile())
                        }
                        if (!1 !== e.signature) try {
                            var a = G.a.get("app_id"),
                                s = z.a.jws.JWS.sign(null, {
                                    alg: "HS256",
                                    cty: "JWT"
                                }, t, window.btoa(a));
                            s && (n.Signature = window.btoa(s), n.Token = "v2")
                        } catch (t) {
                            N.a.error("Cannot sign request")
                        }
                        return n
                    }
                }


```

[Go back to top](#tracker-descriptions)

## PPCProtect
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## Provers
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## Rollick
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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

## SAP
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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

## SiftScience
This service has been classified as `Fingerprinting` for the following reasons:
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

## Smi
This service has been classified as `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://plugin.socital.com/static/v1/socital.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
            var o = {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                detectScreenOrientation: !0,
                sortPluginsFor: [/palemoon/i],
                userDefinedFonts: []
            };

```
2. Sends computed fingerprint back to server
```
                            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null,
                                o = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null,
                                t = {
                                    browserID: a.browser.browserID,
                                    fingerprint: o,
                                    fingerprintData: e,
                                    superCookieID: a._getSuperCookieID(),
                                    uri: window.location.href,
                                    userID: a.userID,
                                    envData: a.browser.envData,
                                    uuid: (0, s.default)()
                                };
                            a.browser.visit = {
                                uuid: t.uuid
                            }, fetch(k + "/api/v1/events/browserVisit", {
                                method: "PUT",
                                body: JSON.stringify(t),
                                headers: {
                                    "Content-Type": "application/json"
                                }
                            })

```

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

## StackTrack
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://cdn.stat-track.com/statics/moosend-tracking.min.js?ts=5179362`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
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
e.prototype.ping = function(e) {
            if (this._isInitialized()) {
                var t = {
                        BrowserComponents: e,
                        ContactId: this.storage.getUserId(),
                        actionType: n.PING,
                        sessionId: this.storage.getSessionId(),
                        siteId: this.siteId
                    },
                    r = this.storage.getEmail(),
                    i = this.storage.getCampaignId();
                r && (t.ContactEmailAddress = r), i && (t.CampaignId = i), this.agent.sendPing(t)
            }
        }
```

[Go back to top](#tracker-descriptions)

## Storeland
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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

## TechSolutions
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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

## Upland
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## USocial
This service has been classified as `Social` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://usocial.pro/usocial/fingerprint2.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
    var Fingerprint2 = function(options) {
    var defaultOptions = {
      swfContainerId : "fingerprintjs2",
      swfPath : "flash/compiled/FontList.swf",
      detectScreenOrientation : true,
      sortPluginsFor : [/palemoon/i],
      userDefinedFonts : []
    };
    this.options = this.extend(options, defaultOptions);
    /** @type {function(this:(IArrayLike<T>|string), (function(this:S, T, number, !Array<T>): ?|null), S=): undefined} */
    this.nativeForEach = Array.prototype.forEach;
    /** @type {function(this:(IArrayLike<T>|string), (function(this:S, T, number, !Array<T>): R|null), S=): !Array<R>} */
    this.nativeMap = Array.prototype.map;
  };
```
2. Sends computed fingerprint back to server as `usocialuser` parameter
```
Request URL: https://usocial.pro/logs/store-view?&c=REMOVED&pid=REMOVED&usocialUser=REMOVED&pType=share&url=REMOVED&barDisplayStatus=
```
[Go back to top](#tracker-descriptions)

## Vendemore
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://d2hya7iqhf5w3h.cloudfront.net/scripts/analytics.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):
```
('Fingerprint2', this, function() {
    'use strict';
    var _0x75b9x15 = function(options) {
        if (!(this instanceof _0x75b9x15)) {
            return new _0x75b9x15(options)
        };
        var _0x75b9x17 = {
            swfContainerId: 'fingerprintjs2',
            swfPath: 'flash/compiled/FontList.swf',
            detectScreenOrientation: true,
            sortPluginsFor: [/palemoon/i],
            userDefinedFonts: []
        };
        this['options'] = this['extend'](options, _0x75b9x17);
        this['nativeForEach'] = Array['prototype']['forEach'];
        this['nativeMap'] = Array['prototype']['map']
    };
```
2. Sends computed fingerprint back to server
```
new Fingerprint2(options)['get'](function(_0x75b9x48) {
    var _0x75b9x8a = 'https://analytics.vendemore.com/visits';
    _0x75b9x8a += '?vlmref=' + customerCookieValue;
    _0x75b9x8a += '&vaid=' + ourCookieValue;
    _0x75b9x8a += '&fingerprint=' + _0x75b9x48;
    _0x75b9x8a += '&url=' + requestUrl;
    _0x75b9x8a += '&title=' + title;
    _0x75b9x8a += '&path=' + path;
    _0x75b9x8a += '&domain=' + domain;
    _0x75b9x8a += '&referrer=' + referrer;
    httpGetAsync(_0x75b9x8a, interactionControllerResponse)
})
```

[Go back to top](#tracker-descriptions)

## VerticalHealth
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## ViralLoops
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Technical Review
Script: `https://app.viral-loops.com/popup_assets/js/vl_load_v2.min.js`
1. Script embeds or includes snippets of an open source fingerprinting library, [fingerprintjs2](https://github.com/Valve/fingerprintjs2):

```
swfContainerId:"fingerprintjs2"
```
[Go back to top](#tracker-descriptions)

## Webmecanik
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## ZafulAffiliate
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

