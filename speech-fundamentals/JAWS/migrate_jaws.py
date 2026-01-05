import subprocess
import os
import re

base_url = "https://srt.csb-cde.ca.gov/jaws/"

lessons = [
    {"id": "1", "url": "jaws-lesson-1.html", "title": "Intro to JAWS", "file": "Lesson 01.md"},
    {"id": "2", "url": "jaws-lesson-2.html", "title": "Headings", "file": "Lesson 02.md"},
    {"id": "3", "url": "jaws-lesson-3.html", "title": "Links", "file": "Lesson 03.md"},
    {"id": "4", "url": "jaws-lesson-4.html", "title": "Buttons", "file": "Lesson 04.md"},
    {"id": "5", "url": "jaws-lesson-5.html", "title": "Checkboxes and Radio Buttons", "file": "Lesson 05.md"},
    {"id": "6", "url": "jaws-lesson-6.html", "title": "Combo Boxes and List Boxes", "file": "Lesson 06.md"},
    {"id": "7", "url": "jaws-lesson-7.html", "title": "Proofreading and Editing Text", "file": "Lesson 07.md"},
    {"id": "7.1", "url": "jaws-lesson-7a.html", "title": "JAWS Lesson 7.1", "file": "Lesson 07.1.md"},
    {"id": "7.2", "url": "jaws-lesson-7b.html", "title": "JAWS Lesson 7.2", "file": "Lesson 07.2.md"},
    {"id": "7.3", "url": "jaws-lesson-7c.html", "title": "JAWS Lesson 7.3", "file": "Lesson 07.3.md"},
    {"id": "7.4", "url": "jaws-lesson-7d.html", "title": "JAWS Lesson 7.4", "file": "Lesson 07.4.md"},
    {"id": "7.5", "url": "jaws-lesson-7e.html", "title": "JAWS Lesson 7.5", "file": "Lesson 07.5.md"},
    {"id": "7.6", "url": "jaws-lesson-7f.html", "title": "JAWS Lesson 7.6", "file": "Lesson 07.6.md"},
    {"id": "7.7", "url": "jaws-lesson-7g.html", "title": "JAWS Lesson 7.7", "file": "Lesson 07.7.md"},
    {"id": "8", "url": "jaws-lesson-8.html", "title": "Tables", "file": "Lesson 08.md"},
    {"id": "9", "url": "jaws-lesson-9.html", "title": "Images", "file": "Lesson 09.md"},
    {"id": "10", "url": "jaws-lesson-10.html", "title": "The Virtual Cursor", "file": "Lesson 10.md"},
    {"id": "11", "url": "jaws-lesson-11.html", "title": "Exploration", "file": "Lesson 11.md"},
]

def clean_content(content):
    lines = content.split('\n')
    cleaned_lines = []
    # Heuristics to remove navigation
    # Remove lines containing links to other jaws-lesson-*.html files if they are short (likely nav)
    # Also remove "Start JAWS Lesson" type links.
    
    for line in lines:
        if 'jaws-lesson-' in line and 'html' in line:
            # Check if it's a list item or standalone link which usually indicates navigation
            # But be careful not to remove inline references if any (unlikely in these lessons to have inline cross-refs that aren't nav)
            # The navigation in these files seems to be at the bottom or top list.
            # We'll rely on the fact that we are rebuilding the footer.
            pass # Skip this line
        elif "Start JAWS Lesson" in line:
            pass
        elif "Next Lesson" in line or "Previous Lesson" in line:
             if len(line) < 200: # Heuristic: Nav lines are short
                 pass
             else:
                 cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
            
    return '\n'.join(cleaned_lines)

for i, lesson in enumerate(lessons):
    print(f"Processing {lesson['title']}...")
    url = base_url + lesson['url']
    file_path = lesson['file']
    
    # Download and convert
    cmd = ['pandoc', url, '-f', 'html', '-t', 'markdown', '-o', file_path]
    subprocess.run(cmd, check=True)
    
    # Read content
    with open(file_path, 'r') as f:
        content = f.read()
        
    content = clean_content(content)
    
    # Add Navigation
    nav_links = []
    if i > 0:
        prev_l = lessons[i-1]
        nav_links.append(f"[Previous Lesson: {prev_l['title']}]({prev_l['file']})")
    
    if i < len(lessons) - 1:
        next_l = lessons[i+1]
        nav_links.append(f"[Next Lesson: {next_l['title']}]({next_l['file']})")
        
    footer = "\n\n---\n\n" + " | ".join(nav_links) + "\n"
    
    with open(file_path, 'w') as f:
        f.write(content + footer)

print("Done!")
