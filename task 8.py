def is_valid_url(url):
    # Check if the URL starts with http:// or https://
    if url.startswith('http://') or url.startswith('https://'):
        # Basic check for a dot, indicating a domain name might be present
        if '.' in url:
            return True
    return False

# Example usage
print(is_valid_url('http://example.com'))  # Should return True
print(is_valid_url('https://example'))     # Should return False
print(is_valid_url('ftp://example.com'))   # Should return False
