def build_xml(word, matched_lines):
    total = len(matched_lines) - 1  # Exclude the word header
    xml = f'<lines word="{word}" total="{total}">\n'

    for index, line in matched_lines[1:]:  # Skip the first entry (word)
        xml += f'    <line line_number="{index}">\n'
        xml += f'        {line.strip()}\n'
        xml += '    </line>\n'

    xml += '</lines>'
    return xml.encode('utf-8')