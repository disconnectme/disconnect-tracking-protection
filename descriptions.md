# Tracker Descriptions
- [Admicro](#Admicro)
- [AdScore](#AdScore)
- [aster18cdn.nl](#aster18cdn.nl)
- [AuditedMedia](#AuditedMedia)
- [Augur](#Augur)
- [BlueCava](#BlueCava)
- [BoostBox](#BoostBox)
- [C3-Metrics](#C3-Metrics)
- [CoinHive](#CoinHive)
- [CoinPot](#CoinPot)
- [CryptoLoot](#CryptoLoot)
- [DoubleVerify](#DoubleVerify)
- [eyeReturn-Marketing](#eyeReturn-Marketing)
- [flightzy.date](#flightzy.date)
- [Foresee](#Foresee)
- [Gridcash](#Gridcash)
- [iMedia](#iMedia)
- [JSE](#JSE)
- [MediaMath](#MediaMath)
- [MinerAlt](#MinerAlt)
- [Minescripts](#Minescripts)
- [MineXMR](#MineXMR)
- [NeroHut](#NeroHut)
- [OnlineMetrix](#OnlineMetrix)
- [PerimeterX](#PerimeterX)
- [SpareChange](#SpareChange)
- [Webmine](#Webmine)
- [zymerget.bid](#zymerget.bid)
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
## AdScore
This service has been classified as `Analytics` and `Fingerprinting` for the following reasons:
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
## aster18cdn.nl
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
aster18cdn.nl has been identified using the following domains:
- aster18cdn.nl

Observered on: http://jashanmalgroup.com
- CPU utilization
    - Baseline load: 208.31%
    - Cryptomining script blocked: 18.84%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://jashanmalgroup.com",
        "isBlockingMiners": false,
        "miners": [
            "aster18cdn.nl"
        ],
        "miner_requests": [
            "https://aster18cdn.nl/bootstrap.min.js"
        ],
        "run_stats": {
            "cpu": 208.30810351947872,
            "memory": "543.2 MB"
        },
        "workers_created": [
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63",
            "blob:https://www.jashanmalgroup.com/88ebc6d4-1004-4d9e-846a-fd4feac29b63"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://jashanmalgroup.com",
        "isBlockingMiners": true,
        "miners": [
            "aster18cdn.nl"
        ],
        "miner_requests": [
            "https://aster18cdn.nl/bootstrap.min.js"
        ],
        "run_stats": {
            "cpu": 18.836178861788618,
            "memory": "470.2 MB"
        },
        "workers_created": []
    }
}
```
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
## Augur
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Policy Review
1. Augur claims that they track users via devices, not through cookies. - `https://www.mediapost.com/publications/article/166916/bluecava-touts-device-fingerprinting.html`

> A set of APIs and tools that instantly enables businesses to recognize devices, and consumers across devices. - `https://www.augur.io/#landingPage`

> Cookie-less tracking - Instead of cookies (which cause mis-attribution), Augur uses CAKE, a multi-layer recognition architecture.

2. Augur claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://www.augur.io/privacypolicy`

> To deliver the Augur Services, our software collects, organizes, and uses Non-PII. This information includes, the date and time of visits to a Client Property, browser information (e.g., browser type, font signature), operating system information (e.g. screen resolution), IP addresses, non-precise geographic information ( e.g. time zone, city, state, country), battery level, and user agent

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
## eyeReturn Marketing
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
### Policy Review
1. Eyereturn claims that they collect a variety of device fingerprints for the purpose of identifying users - `https://eyereturnmarketing.com/privacy/`

> Statistical IDs are created via an algorithm using non-personally identifiable and pseudonymous information about a computer or device. The information used may include the operating system, user-agent string, Web browser, approximate location, installed fonts, and similar information. This information makes your computer or device distinct enough for our systems to determine within a reasonable probability that they are encountering the same computer or device. These IDs are not used to target advertisements, and are only used for campaign analytics and reporting purposes
## flightzy.date
This service has been classified as `Cryptomining` for the following reasons:
### Technical Review
Observered on: http://tartaria.sk
- CPU utilization
    - Baseline load: 399.89%
    - Cryptomining script blocked: 40.49%

Raw log:
```
{
    "WhenNotBlocked": {
        "test_webpage": "http://tartaria.sk",
        "isBlockingMiners": false,
        "miners": [
            "flightzy.date"
        ],
        "miner_requests": [
            "https://flightzy.date/00oti2/w.js"
        ],
        "run_stats": {
            "cpu": 399.89349206349203,
            "memory": "748 MB"
        },
        "workers_created": [
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492",
            "blob:https://www.tartaria.sk/7174ef5c-544c-4f17-8c4e-0a6908c1c492"
        ]
    },
    "WhenBlocked": {
        "test_webpage": "http://tartaria.sk",
        "isBlockingMiners": true,
        "miners": [
            "flightzy.date"
        ],
        "miner_requests": [
            "https://flightzy.date/00oti2/w.js"
        ],
        "run_stats": {
            "cpu": 40.48730972351661,
            "memory": "597.9 MB"
        },
        "workers_created": []
    }
}
```
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

## iMedia
This service has been classified as `Advertising` and `Fingerprinting` for the following reasons:
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

## zymerget.bid
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
