import socket


def get_ip_address(host):
    try:
        ip_add = socket.gethostbyname(host)
        print(f"🔍 Resolved {host} to: {ip_add}")
        return ip_add
    except socket.gaierror:
        print(f"❌ Error: Cannot resolve '{host}'.")
        return None


def check_single_port(ip, port):
    services = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS",
                3306: "MySQL", 8080: "HTTP-Proxy"}
    service_name = services.get(port, "Unknown Service")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.5)
            s.connect((ip, port))

            print(f"✅ Port {port} ({service_name}) is OPEN!")

            try:
                s.send(b'Hello\r\n')
                raw_banner = s.recv(1024)
                banner = raw_banner.decode(errors='ignore').strip()
                if banner:
                    print(f"   🚩 Banner: {banner}")
            except:
                pass

    except ConnectionRefusedError:
        print(f"❌ Port {port} ({service_name}) is CLOSED.")
    except socket.timeout:
        print(f"⚠️ Port {port} ({service_name}) is FILTERED (timeout).")
    except Exception as e:
        print(f"❓ Error on port {port}: {e}")


def dynamic_port_scanner(ip):
    print("\nEnter a port (e.g., 80) or range (e.g., 20-25)")
    print("Press 'q' to quit.\n")

    while True:
        user_input = input("Port> ").strip().lower()

        if user_input == 'q':
            print("Exiting scanner.")
            break
        if '-' in user_input:
            try:
                start, end = map(int, user_input.split('-'))

                if start < 0 or end > 65535 or start > end:
                    print("❌ Invalid port range.")
                    continue

                for port in range(start, end + 1):
                    check_single_port(ip, port)

            except ValueError:
                print("❌ Invalid range format. Use like 20-80.")

        # Handle single port
        else:
            if not user_input.isdigit():
                print("❌ Invalid port number.")
                continue

            port = int(user_input)

            if port < 0 or port > 65535:
                print("❌ Port must be between 0 and 65535.")
                continue

            check_single_port(ip, port)


# ===== MAIN =====
hostname = input("Enter hostname: ").strip()
ip_address = get_ip_address(hostname)

if ip_address:
    dynamic_port_scanner(ip_address)