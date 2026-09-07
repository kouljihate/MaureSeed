def to_arabic_numerals(num_str):
    """Convert Western numerals to Arabic-Indic numerals."""
    arabic_digits = {'0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'}
    return ''.join(arabic_digits.get(d, d) for d in str(num_str))


def format_number(value, lang="en"):
    """Format number: show Arabic-Indic in brackets when Arabic."""
    num_str = str(value)
    if lang == "ar":
        arabic = to_arabic_numerals(num_str)
        return f"{num_str} ({arabic})"
    return num_str
