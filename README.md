# NFSMW2012 — Autolog Emu

Bring Autolog back to *Need for Speed: Most Wanted (2012)* — community-led, simple, and fun.

<img src="./img/nfs_most_wanted_2012.jpg" alt="Banner" style="width:100%; display:block; margin:0 auto; border-radius:5px;  " />

## 🎮 Try it

1. Add to your `hosts` file:  
   ```
   127.0.0.1  gsprodblapp-03.ea.com
   ```

2. Run the script:  
   ```
   python save_connections.py
   ```
   > Run as **Administrator** (or with sudo on Linux/Mac)

3. Launch the game → **Multiplayer** → **Sign in**

4. Check the `captures/` folder for `.bin` files

5. Share your captures and findings!

---

## ipconfig


```bash
Windows IP Configuration


Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter WiFi:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2402:3a80:1bbb:f9cb:a749:952e:91f6:bf25
   Temporary IPv6 Address. . . . . . : 2402:3a80:1bbb:f9cb:548e:27de:491f:2a05
   Link-local IPv6 Address . . . . . : fe80::f7ae:d3e5:23f2:c57b%18
   IPv4 Address. . . . . . . . . . . : 192.168.116.150
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::c8e0:95ff:fe93:67d6%18
                                       192.168.116.116
 ```

## ping 159.153.73.13

```bash
Pinging 159.153.73.13 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 159.153.73.13:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),

```


## tracert 159.153.73.13
```bash
Tracing route to gsprodblapp-03.ea.com [159.153.73.13]
over a maximum of 30 hops:

  1     3 ms     2 ms     1 ms  192.168.116.116
  2     *        *        *     Request timed out.
  3    40 ms    17 ms    27 ms  192.168.231.2
  4    55 ms    22 ms    29 ms  10.174.18.182
  5    40 ms    21 ms    31 ms  100.64.0.162
  6    61 ms    26 ms    37 ms  182.19.108.215
  7   306 ms    77 ms    69 ms  217.161.93.241
  8   254 ms   239 ms     *     ae34-xcr1.mrx.cw.net [195.2.2.57]
  9     *      318 ms   318 ms  ae6.edge1.mrs3.sp.lumen.tech [4.68.111.209]
 10     *        *        *     Request timed out.
 11     *      280 ms   322 ms  213.242.106.234
 12   427 ms   240 ms   279 ms  159.153.160.4
 13     *        *        *     Request timed out.
 14     *        *        *     Request timed out.
 15     *        *        *     Request timed out.
 16     *        *        *     Request timed out.
 17     *        *        *     Request timed out.
 18     *        *        *     Request timed out.
 19     *        *        *     Request timed out.
 20     *        *        *     Request timed out.
 21     *        *        *     Request timed out.
 22     *        *        *     Request timed out.
 23     *        *        *     Request timed out.
 24     *        *        *     Request timed out.
 25     *        *        *     Request timed out.
 26     *        *        *     Request timed out.
 27     *        *        *     Request timed out.
 28     *        *        *     Request timed out.
 29     *        *        *     Request timed out.
 30     *        *        *     Request timed out.

Trace complete 
```

## 🤝 Want to Help?

- Capture and share `.bin` traffic files  
- Help decode packet formats  
- Build fake replies to bring back multiplayer  
- Test once the reply server is ready

---

## 🌟 Fun Notes

Keep it friendly, share what you find, and have fun reviving this game together!  
We’re doing this for the love of the game 🎮✨
