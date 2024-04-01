#!/usr/bin/env python
import requests
import pyfiglet
import subprocess
import os
import ssl
import socket
from urllib.parse import urlparse


def check_security_headers(url):
    try:
        # Send a HEAD request to get only the response header
        response = requests.head(url)
        # Get the response headers
        response_headers = response.headers

        # List of security headers to check for in the response headers
        security_headers = [
            "Strict-Transport-Security", 
            "Content-Security-Policy", 
            "X-Frame-Options", 
            "X-Content-Type-Options", 
            "Referrer-Policy", 
            "Permissions-Policy"
        ]

        # Check if each security header is present in the response headers
        present_headers = [header for header in security_headers if header in response_headers]
        missing_headers = [header for header in security_headers if header not in response_headers]
        print("\n"+"\033[1m" + "Checking Security Headers" + "\033[0m")
        if present_headers:
            print("\033[1m"+"\nThese headers are present:"+"\033[0m")
            for header in present_headers:
                print(header)
        else:
            print("\033[1m"+"\nNo security headers are present."+"\033[0m")

        if missing_headers:
            print("\033[1m"+"\nThese headers are not present:"+"\033[0m")
            for header in missing_headers:
                print(header)
        else:
            print("\033[1m"+"\nAll security headers are present."+"\033[0m")


        # Check if "Server" header is present
        print("\n"+"\033[1m" + "Checking Server Header disclosure" + "\033[0m")
        if "Server" in response_headers:
            print("\nServer header is disclosed:", response_headers["Server"])
        else:
            print("\nServer header is not present.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching headers:", e)
def check_options_method_allowed(url):
    try:
        print("\n"+"\033[1m" + "Checking for option methods" + "\033[0m")
        # Run curl command to send OPTIONS request
        curl_command = f'curl -X OPTIONS --head {url}'

        # Execute the curl command and capture the output
        output = subprocess.check_output(curl_command, shell=True, stderr=subprocess.STDOUT)
        # Decode the byte string output to a regular string
        decoded_output = output.decode('utf-8')
        # Check if the response includes "Allow" header
        if 'Access-Control-Allow-Methods:' in decoded_output:
            print("OPTIONS method is allowed.")
            # Extract allowed methods from the response
            allowed_methods = [method.strip() for method in decoded_output.split('Access-Control-Allow-Methods:')[1].split('\n')[0].split(',')]
            print("Allowed methods:", allowed_methods)
        elif 'Allow:' in decoded_output:
            print("OPTIONS method is allowed.")
            # Extract allowed methods from the response
            allowed_methods = [method.strip() for method in decoded_output.split('Allow:')[1].split('\n')[0].split(',')]
            print("Allowed methods:", allowed_methods)
        else:
            print("OPTIONS method is not allowed.")

    except subprocess.CalledProcessError as e:
        print("Error occurred while running curl command:", e.output.decode('utf-8'))
def check__cookie_without_secure_flag(url):
    try:
        print("\n"+"\033[1m" + "Checking Cookie is set without secure flag or not" + "\033[0m")

        # Run curl command to check cookie request
        curl_command = f'curl --head {url}'

        # Execute the curl command and capture the output
        output = subprocess.check_output(curl_command, shell=True, stderr=subprocess.STDOUT)
        # Decode the byte string output to a regular string
        decoded_output = output.decode('utf-8')
        if 'Set-Cookie' in decoded_output:
            if 'Secure'in decoded_output:
                print("\nSecure flag are set: Safe")
            else:
                print("\nCookies without secure flagset : Vulnerable")
        else:
            print("\nNo cookies are set.")

    except subprocess.CalledProcessError as e:
        print("Error occurred while running curl command:", e.output.decode('utf-8'))

def check_ssl_tls(url):
    # Parse the URL to extract the hostname
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            try:
                print("\n"+"\033[1m" + f"Checking SSL/TLS version for {hostname}" + "\033[0m")
                ssl_version = ssock.version()
                print(f"\nSSL/TLS version used: {ssl_version}")
            except Exception as e:
                print(f"\nSSL/TLS check failed: {e}")
def ensure_url_scheme(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:  # If the scheme is missing, default to https
        url = "https://" + url
    return url

if __name__ == "__main__":
    os.system('clear')
    # Print the banner
    ascii_banner = pyfiglet.figlet_format("Web-Tester")
    print(ascii_banner + "BY MIDHLAJ")
    # Prompt the user for the URL input
    input_url = input("\nEnter the URL: ")
    url = ensure_url_scheme(input_url)
    check_security_headers(url)
    check_options_method_allowed(url)
    check__cookie_without_secure_flag(url)
    check_ssl_tls(url)
    
