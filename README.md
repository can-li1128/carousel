# Carousel Design for New Books #
*Content*
- files used for index.html to run:
    - index.html
    - 2026spring.xlsx -> 2026spring.json -> 2026spring_updated.json
- index.html is a self-contained .html file that has html, CSS, and script. It's all you need to run this carousel with your file. Replace filename '2026spring_updated.json' in line 178 with your own file that include the same elements.
- 2026spring.xlsx is an Alma report with five columns: Title, ISBN, Author, Publication Date, & MMS ID.
  -  Run excel_to_json.py with this Excel to retrieve same data in JSON format (in my repo, it generates 2026spring.json);
  -  Run json_data_enricher.html to add Syndetics img_url and Primo permalinks to each title in JSON (in my repo, it generates 2026spring_updated.json)
  -  2026spring_updated.json is used as input for the carousel, line 178

*Function*
- index.html reads book records in 2026spring_updated.json from the same directory, displays thumbnail cover image from img_url, titles, formats author names, and on clicking, links to Primo records. 
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
- This program takes an Excel with ISBNs on the browser and output an Excel populated image URLs in a new column, img_url..
     - page: https://can-li1128.github.io/display-designs/add-imagelinks
     - code: https://github.com/can-li1128/display-designs/blob/master/add-imagelinks.html
- excel_carousel.html reads new-arrivals.xlsx to generate carousel. To use this code, replace file name in line 179 with your own Excel file with the same columns.
