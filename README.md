# Carousel Design for New Books #
*Content*
- index.html is a self-contained .html file that has html, CSS, and script. It's all you need to run this carousel with your file. Replace filename in line 178 const JSON_FILE_PATH = '2026spring_updated.json' with your own file.
- 2026spring.xlsx is an Alma report with five columns: Title, ISBN, Author, Publication Date, & MMS ID. 
    a) Run excel_to_json.py with this Excel to retrieve same data in JSON format (in my repo, 2026spring.json); 
    b) Run json_data_enricher.html to add Syndetics img_url and Primo permalinks to each title in JSON (in my repo, 2026spring_updated.json)
  - 2026spring_updated.json is used as input for the carousel.

*Function*
- index.html automatically reads book records in new-arrivals.xlsx from the same directory, extracts cover image from URLs, titles, formats author names, and uses permalinks to open Primo records on clicking. 
- Smooth infinite auto-rotation & controls: auto starts at loading, rotates in a continuous loop at 2-second interval, supported by Prev, Pause/Play, and Next navigation buttons.
- Hover behaviors: pauses rotation, magnifies book covers by 1.15 times on mouse hover or keyboard focus, displaying the book title immediately on a card and author after a 1-second delay.
- Linking: Clicking any book cover opens Primo record in a new tab
- Responsive layout: dynamically adjusts the number of visible covers based on screen size (displaying 7 on desktops, 4 on tablets, and 2 to 3 on phones).

*Web Accessibility (WCAG) Features*
- Screen reader live announcements (aria-live): Features a hidden status region that announces state updates (e.g., pause/play status or active slide shifts) to screen reader users.
- Motion Sensitivity Compliance (prefers-reduced-motion): Automatically respects user operating system preferences by disabling auto-rotation and animations for users sensitive to motion.
- Keyboard Focus Indicators (:focus-visible): Ensures high-contrast focus outlines around all interactive links and buttons for keyboard-only navigation.
- Aria Labeling & Hidden Clones: Decorative looping duplicates are marked with aria-hidden="true" to prevent redundant screen reader announcements, and links include descriptive aria-label text combining titles and authors.

*Associated code*
-  A program to enter multiple ISBNs on a browser, retrieve the FIRST cover and exit. e.g. 0811238652; 9780811238656; 9780811239578; 0811239578
    - page: https://can-li1128.github.io/display-designs/fetch-image
    - code: https://github.com/can-li1128/display-designs/blob/master/fetch-image.html
-  The initial new books Excel from Alma analytics doesn't have image links. Without image URLs, the program searches for an cover images for every row every single time the page loads. Loading the page with 89 covers takes 1-2 minutes. Populating the Excel with image URLs in a new column, img_url, avoids this problem--the page loads instantly. This program takes an Excel with ISBNs on the browser and output an Excel with the new column.
     - page: https://can-li1128.github.io/display-designs/add-imagelinks
     - code: https://github.com/can-li1128/display-designs/blob/master/add-imagelinks.html
