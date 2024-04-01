

# Web Security Testing Tool

This Python script is designed for security professionals and developers to conduct basic security assessments on web applications. It evaluates the security posture of web applications by checking for essential HTTP security headers, the allowance of the HTTP OPTIONS method, and cookie security configurations.
---

## Features

- **Security Headers Check**: Verifies the presence of crucial HTTP security headers such as `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, and `Permissions-Policy`.
- **OPTIONS Method Analysis**: Determines if the HTTP OPTIONS method is enabled on the target server and identifies which HTTP methods are allowed, providing insights into potential misconfigurations or overly permissive CORS policies.
- **Cookie Security**: Assesses cookies set by the server for security-enhancing flags, specifically the `Secure` flag, which ensures cookies are sent only over secure HTTPS connections, and the `HttpOnly` flag, which prevents access to cookie values via JavaScript, mitigating the risk of cross-site scripting (XSS) attacks.
- **SSL/TLS Version Check**: Evaluates the SSL/TLS configuration of the target server by establishing a connection and identifying the version of the SSL/TLS protocol in use. This check helps in identifying outdated or insecure SSL/TLS versions that could make the server vulnerable to attacks such as POODLE or BEAST.

---


## Installation

Clone the repository to your local machine:

```sh
git clone https://your-repository-url-here
```

Navigate to the cloned directory:

```sh
cd path-to-cloned-directory
```

## Usage

To use the Web Security Testing Tool, follow these steps:

1. Make sure you are in the project directory.
2. Run the script with Python:

    ```sh
    python webt.py
    ```

3. When prompted, enter the URL of the web application you want to test:

    ```plaintext
    Enter the URL: https://example.com
    ```

4. The script will then perform the security checks and display the results in the console.

## Contributing

Contributions to improve the Web Security Testing Tool are welcome. If you have a suggestion, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

[Website](https://www.midhlaj.me/)

Project Link: [https://github.com/your_username/your_project](https://github.com/your_username/your_project)
