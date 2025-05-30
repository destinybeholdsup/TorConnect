# TorConnect

**TorConnect** is a Python library that makes it easy to connect to the Tor network for anonymous browsing and web scraping. It offers simple methods to manage Tor sessions, rotate IPs, and send requests through Tor's SOCKS proxy, helping you keep your online activity private and secure. 

## How does this work?
I am simply utilizing Tor's expert bundle to use their data and servers so you can route your session easily through their nodes.

1. This will check if tor.exe is running, if so, kill, if not, start
2. Waits till the bootstrap is done
3. Once done, the program will start executing whatever you need without having to worry about putting condition checks

## Getting Started
You're going to want to make sure Tor Expert Bundle is installed *(https://www.torproject.org/download/tor/)*

Extract the folder to a place on computer

Install the dependencies `pip install stem rich requests`

## How to use
There's an example in the github on how to make a basic request with it. Here's an *[Example](https://github.com/destinybeholdsup/TorConnect/blob/main/Example%201_Basic_Get_Request.py)* of it doing a get request.

From there on, it's the exact same as you would do for any ordinary request.

## What do I use this for?
Anything you want to do that requires proxies and you just don't want to buy proxies, too lazy, or just need a simple and quick way to hide your requests from the server or IPS.

## Future features
Make it easy for user to individualize Tor session per thread if wanting without multiple servers running at once
___
**I am not responsible if you use it for malicious purposes. This is simply for educational purposes for myself and others.**
