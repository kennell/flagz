import string


_regional_indicator_symbols = '🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿'
_data = {}
for char, indicator in zip(string.ascii_uppercase, _regional_indicator_symbols):
    _data[char] = indicator


def by_code(code):
    code = code.upper()
    return _data[code[0]] + _data[code[1]]