"""Build the English companion report (report_en.pdf) from report_en.ipynb.

Steps:
  1. execute report_en.ipynb, which re-runs the analysis notebooks;
  2. export it to HTML without code cells;
  3. print the HTML to an A4 PDF with headless Chromium (Playwright).

Requirements (in addition to requirements.txt):
    pip install -r requirements-report.txt
    playwright install chromium

Usage:
    python build_report.py
"""
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "report_en.ipynb"
HTML_OUT = ROOT / "temp" / "report_en.html"
PDF_OUT = ROOT / "report_en.pdf"

FOOTER = """
<div style="width:100%; font-family:Inter, Arial, sans-serif; font-size:7pt; color:#52514e;
            padding:0 18mm; display:flex; justify-content:space-between;">
  <span>Deforestation in the Cerrado of Maranhão · companion report</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>
"""


def main():
    (ROOT / "temp").mkdir(exist_ok=True)

    print(f"Executing {NOTEBOOK.name} ...")
    nb = nbformat.read(NOTEBOOK, as_version=4)
    ExecutePreprocessor(timeout=1200, kernel_name="python3").preprocess(nb, {"metadata": {"path": str(ROOT)}})
    nbformat.write(nb, NOTEBOOK)

    print("Exporting HTML ...")
    exporter = HTMLExporter(template_name="lab")
    exporter.exclude_input = True
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    html, _ = exporter.from_notebook_node(nb)
    HTML_OUT.write_text(html, encoding="utf-8")

    print(f"Printing {PDF_OUT.name} ...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML_OUT.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(PDF_OUT),
            format="A4",
            margin={"top": "18mm", "bottom": "18mm", "left": "18mm", "right": "18mm"},
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=FOOTER,
        )
        browser.close()
    print(f"Done: {PDF_OUT}")


if __name__ == "__main__":
    main()
