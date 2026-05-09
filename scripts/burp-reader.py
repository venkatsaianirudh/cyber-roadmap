import sys
from urllib.parse import urlparse, parse_qs


def read_request_file(filename):
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()
    except FileNotFoundError:
        print(f"[!] File not found: {filename}")
        sys.exit(1)


def split_request(raw_request):
    parts = raw_request.split("\n\n", 1)

    headers_part = parts[0]
    body = parts[1] if len(parts) > 1 else ""

    lines = headers_part.splitlines()

    if not lines:
        print("[!] Empty request file.")
        sys.exit(1)

    request_line = lines[0]
    header_lines = lines[1:]

    return request_line, header_lines, body


def parse_request_line(request_line):
    parts = request_line.split()

    if len(parts) < 3:
        return None, None, None

    method = parts[0]
    path = parts[1]
    http_version = parts[2]

    return method, path, http_version


def parse_headers(header_lines):
    headers = {}

    for line in header_lines:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    return headers


def extract_cookies(headers):
    cookie_header = headers.get("Cookie", "")
    cookies = {}

    if cookie_header:
        cookie_pairs = cookie_header.split(";")
        for pair in cookie_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                cookies[key.strip()] = value.strip()

    return cookies


def extract_query_params(path):
    parsed = urlparse(path)
    query_params = parse_qs(parsed.query)

    clean_params = {}
    for key, values in query_params.items():
        clean_params[key] = values

    return parsed.path, clean_params


def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def analyze_request(raw_request):
    request_line, header_lines, body = split_request(raw_request)

    method, path, http_version = parse_request_line(request_line)
    headers = parse_headers(header_lines)

    host = headers.get("Host", "Not found")
    user_agent = headers.get("User-Agent", "Not found")
    content_type = headers.get("Content-Type", "Not found")
    referer = headers.get("Referer", "Not found")
    origin = headers.get("Origin", "Not found")
    authorization = headers.get("Authorization", "Not found")

    clean_path, query_params = extract_query_params(path)
    cookies = extract_cookies(headers)

    print_section("REQUEST SUMMARY")
    print(f"Method       : {method}")
    print(f"Host         : {host}")
    print(f"Path         : {clean_path}")
    print(f"HTTP Version : {http_version}")

    print_section("FULL TARGET")
    print(f"https://{host}{path}")

    print_section("IMPORTANT HEADERS")
    print(f"User-Agent    : {user_agent}")
    print(f"Content-Type  : {content_type}")
    print(f"Referer       : {referer}")
    print(f"Origin        : {origin}")
    print(f"Authorization : {authorization}")

    print_section("QUERY PARAMETERS")
    if query_params:
        for key, values in query_params.items():
            print(f"{key}: {values}")
    else:
        print("No query parameters found.")

    print_section("COOKIES")
    if cookies:
        for key, value in cookies.items():
            print(f"{key}: {value}")
    else:
        print("No cookies found.")

    print_section("REQUEST BODY")
    if body.strip():
        print(body.strip())
    else:
        print("No body found.")

    print_section("SECURITY NOTES")

    if authorization != "Not found":
        print("[!] Authorization header found. This may contain tokens or credentials.")

    if cookies:
        print("[!] Cookies found. These may contain session IDs.")

    if method in ["POST", "PUT", "PATCH"]:
        print("[i] This request sends data to the server.")

    if query_params:
        print("[i] Query parameters found. Check for user-controlled input.")

    if body.strip():
        print("[i] Request body found. Check for login data, forms, JSON, or API input.")

    if not cookies and authorization == "Not found":
        print("[i] No obvious session token found in Cookie or Authorization headers.")


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("python burp_request_reader.py request.txt")
        sys.exit(1)

    filename = sys.argv[1]
    raw_request = read_request_file(filename)
    analyze_request(raw_request)


if __name__ == "__main__":
    main()
