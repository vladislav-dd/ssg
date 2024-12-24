def extract_title(markdown):
    title_line = None
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            title_line = line[2:].strip()
            break
    if title_line is None:
        raise Exception("No title found")   
    return title_line