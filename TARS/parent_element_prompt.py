PARENT_ELEMENT_PROMPT = """
Your task is to identify the best elements to be used as **parent elements for in-content ad insertion** (like in a blog article or news site).

Definition:
Parent Element – A CSS selector that targets the element where ads should be inserted (e.g., `.article` or `main.content`). These selectors will be used for automated ad placement based on document structure.

degreeOfCertainty: how appropriate is the answer following the rules, in percentage.

Rules you must follow:
- The ideal parent should contain at least 10 elements `<p>`, `<h2>`, and/or content-rich `<div>` elements.
- It should clearly represent the **main content block** of the article — the section the reader scrolls through.
- Avoid elements that are too generic (e.g., `body`, `article#post-123`) that include unrelated sections like related articles, widgets, etc.
- Exclude layout elements like headers, footers, sidebars, and navigation menus.
- You can use any **combination of tag, class, id, or data-* attributes** from the DOM JSON to construct a unique and reliable selector.
- If possible, prefer selectors that are specific but not overly rigid (e.g., don't depend on a dynamic numeric ID).
- Do not invent attributes or class names that are not present in the DOM JSON.

Expected output:
A JSON list with up to 3 selectors (ranked by priority), each with a short explanation.

Example:
[
  {
    "selector": "",
    "reason": "",
    "degreeOfCertainty": ""
  },
  {
    "selector": "",
    "reason": "",
    "degreeOfCertainty": ""
  }
]
"""