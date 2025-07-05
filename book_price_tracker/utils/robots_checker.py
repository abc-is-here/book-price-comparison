import urllib.robotparser

def is_allowed(url, user_agent='*'):

    try:
        from urllib.parse import urlparse
        parse_result = urlparse(url)
        robots_url = f"{parse_result.scheme}://{parse_result.netloc}/robots.txt"
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception as e:
        print(f"Error checking robots.txt: {e}")
        return False