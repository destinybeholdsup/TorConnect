from stem import Signal
from stem.control import Controller

from rich.console import Console

import requests
import re
import subprocess
import time

TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051
COOKIE_AUTHENTICATION = 1
TOR_PASSWORD = 'password'

console = Console()

def is_tor_running():
    '''Don't need to call since called in start_tor()'''
    try:
        result = subprocess.run(
            ['tasklist', '/FI', 'IMAGENAME eq tor.exe'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return 'tor.exe' in result.stdout
    except Exception as e:
        console.print(f"[bold red]Error checking if Tor is running: {e}[/bold red]")
        return False

def kill_tor():
    '''Don't need to call since called in start_tor()'''
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'tor.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        console.print("[bold yellow]Existing Tor process terminated.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Failed to terminate Tor process: {e}[/bold red]")

def start_tor(tor_path='tor'):
    '''Checks if tor is running, starts tor using user's socks & control ports and cookie auth variable'''
    try:
        
        if is_tor_running:
            console.print("[bold yellow]Tor is already running, terminating the process...[/bold yellow]")
            kill_tor()
            time.sleep(1)
        
        process = subprocess.Popen([
            tor_path,
            f'--SocksPort', str(TOR_SOCKS_PORT),
            f'--ControlPort', str(TOR_CONTROL_PORT),
            '--CookieAuthentication', str(COOKIE_AUTHENTICATION)
        ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        console.print("[bold green]Starting Tor...[/bold green]")

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                raise Exception("Tor process exited unexpectedly.")

            console.print("Sevrer Status: " + output.strip())

            if re.search(r"Bootstrapped 100% \(done\): Done", output):
                break

        console.print("[bold green]Tor started successfully![/bold green]")
        return True

    except Exception as e:
        console.print(f"[bold red]Failed to start Tor: {e}[/bold red]")
        return False

def renew_tor_identity():
    """Requests a new identity from Tor server"""
    try:
        with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
            controller.authenticate(password=TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
            return True
    except Exception as e:
        console.print(f"[bold red]Failed to change Tor identity: {e}[/bold red]")
        return False

def get_tor_session():
    """Changes your web session to Tor's node"""
    session = requests.Session()
    session.proxies = {
        'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}'
    }

    return session
