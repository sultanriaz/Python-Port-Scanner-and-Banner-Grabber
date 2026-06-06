#Python Port Scanner and Banner Grabber

A beginner-friendly Python command-line tool for scanning ports on a target host and performing basic banner grabbing on open services.

This project demonstrates the fundamentals of socket programming, hostname resolution, TCP port scanning, timeout handling, and basic cybersecurity reconnaissance.

This tool allows the user to enter a hostname such as google.com, resolve it into an IP address, and scan a single port or a range of ports.  When an open port is found, the tool attempts to grab the service banner and display basic response information.
#Example:

Enter hostname: google.com
Resolved google.com to: 142.251.37.142

Enter a port or range:
Port> 60-99

Port 60 is FILTERED (timeout).
Port 61 is FILTERED (timeout).
Port 62 is FILTERED (timeout).
...
Port 80 (HTTP) is OPEN!

#Banner:
HTTP/1.0 400 Bad Request
Content-Type: text/html; charset=UTF-8
Content-Length: 1555
#Features
Hostname to IP address resolution
Single port scanning
Port range scanning
Open port detection
Filtered port detection using timeout
Basic banner grabbing
Interactive command-line interface
Simple and beginner-friendly code structure
No external Python libraries required
#Technologies Used
Python
Socket Programming
TCP Networking
Command-Line Interface

#Learning Outcomes

Through this project, I learned:

How DNS hostname resolution works
How TCP ports are scanned
How sockets work in Python
How timeout-based filtering is detected
How banner grabbing works
How cybersecurity tools perform basic reconnaissance
Why ethical permission is important in security testing

#Future Improvements

Possible improvements for this project include:

Add multithreading for faster scanning
Add command-line arguments
Save scan results to a file
Export results in JSON format
Add better service detection
Add UDP scanning support
Add colored terminal output
Add scan summary report
Improve error handling
Add logging support
