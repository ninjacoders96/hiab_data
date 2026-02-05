def _c(arr):
    return "".join(chr(x) for x in arr)

def api_base():
    return _c(
        [104,116,116,112,115,58,47,47] +     
        [119,101,98,115,104,111,112] +         
        [46] +
        [104,105,97,98] +                        
        [46,99,111,109]                       
    )

def api_path(code):
    return api_base() + _c(
        [47,97,112,105,47,118,97,114,105,97,110,116,47]
    ) + str(code) + _c(
        [47,100,101,116,97,105,108,115]
    )

def headers():
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.8",
        "cache-control": "no-cache",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
