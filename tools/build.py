# -*- coding: utf-8 -*-
"""Generic builder for bilingual paper guides.

Usage:
    python tools/build.py <paper_dir>

<paper_dir> must contain:
    meta.json   - title_en, title_zh, kicker, badge, subtitle, authors, venue, arxiv, note
    guide.html  - Chinese reading-guide HTML fragment
    body.txt    - tagged bilingual body (same tag set as the original Transformer build)
    tables.json - optional {key: html_fragment} for TABLE@@key
    img/        - figures referenced by FIG@@ / FIGROW@@
"""
import os, sys, json, subprocess, tempfile, pathlib
import pymupdf

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CSS = open(os.path.join(TOOLS, "style.css"), encoding="utf-8").read()


def render_body(lines, tables):
    out = []
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("@@")
        k = f[0]
        if k == "CH":
            label = "★" if f[1] == "abstract" else f[1]
            out.append(f'<section class="chapter" id="{f[1]}"><div class="ch-head"><span class="ch-num">{label}</span><h2>{f[2]}</h2><span class="ch-zh">{f[3]}</span></div>')
        elif k == "ENDCH":
            out.append("</section>")
        elif k == "LEAD":
            ps = "".join(f"<p>{p}</p>" for p in f[1].split("<P>"))
            out.append(f'<div class="lead"><div class="lead-label">本章导读 · READING NOTES</div>{ps}</div>')
        elif k == "SUB":
            out.append(f'<h3 class="sub">{f[1]} <span class="zh">{f[2]}</span></h3>')
        elif k == "H4":
            out.append(f'<h4 class="para">{f[1]} <span class="zh">{f[2]}</span></h4>')
        elif k == "P":
            out.append(f'<div class="pair"><div class="line en"><div class="tag">EN</div><div class="txt">{f[1]}</div></div>'
                       f'<div class="line zh"><div class="tag">译文</div><div class="txt">{f[2]}</div></div></div>')
        elif k == "NOTE":
            out.append(f'<div class="note"><b>解读 · </b>{f[1]}</div>')
        elif k == "EQ":
            num = f'<span class="eqn">{f[2]}</span>' if len(f) > 2 and f[2] else ""
            out.append(f'<div class="eqbox">{num}<div class="eq">{f[1]}</div><div class="eqnote"><b>公式解读 · </b>{f[3] if len(f)>3 else ""}</div></div>')
        elif k == "FIG":
            img, cap_en, cap_zh = f[1], f[2], f[3]
            extra = f'<div class="note" style="margin-top:2mm"><b>读图 · </b>{f[4]}</div>' if len(f) > 4 and f[4] else ""
            small = "small" if len(f) > 5 and f[5] == "small" else ""
            out.append(f'<figure class="{small} avoid"><img src="img/{img}" alt="">'
                       f'<figcaption><span class="en">{cap_en}</span><span class="zh">{cap_zh}</span></figcaption></figure>{extra}')
        elif k == "FIGROW":
            out.append('<div class="figrow avoid">'
                       f'<figure class="small"><img src="img/{f[1]}" alt=""></figure>'
                       f'<figure class="small"><img src="img/{f[2]}" alt=""></figure></div>'
                       f'<div style="margin-top:-1mm"><figcaption><span class="en">{f[3]}</span><span class="zh">{f[4]}</span></figcaption></div>')
        elif k == "TABLE":
            out.append(f'<div class="tblwrap avoid">{tables[f[1]]}</div>')
        elif k == "RAW":
            out.append(f[1])
        elif k == "PB":
            out.append('<div class="pagebreak"></div>')
        elif "@@" not in line:
            out.append(line)
        else:
            raise ValueError(f"unknown tag in {line[:90]}")
    return "\n".join(out)


def build(paper_dir):
    paper_dir = os.path.abspath(paper_dir)
    meta = json.load(open(os.path.join(paper_dir, "meta.json"), encoding="utf-8"))
    guide = open(os.path.join(paper_dir, "guide.html"), encoding="utf-8").read()
    body = open(os.path.join(paper_dir, "body.txt"), encoding="utf-8").read()
    tpath = os.path.join(paper_dir, "tables.json")
    tables = json.load(open(tpath, encoding="utf-8")) if os.path.exists(tpath) else {}

    title_en = meta["title_en"]
    fname = meta.get("filename") or title_en.replace("/", "-").replace(":", "-").replace("?", "") + ".pdf"
    out_pdf = os.path.join(ROOT, fname)
    html_path = os.path.join(paper_dir, "_book.html")

    cover = f"""
<div class="cover">
  <div class="cover-kicker">{meta['kicker']}</div>
  <h1>{title_en}</h1>
  <div class="cover-zh">{meta['title_zh']}</div>
  <div class="cover-rule"></div>
  <div class="cover-desc">{meta['subtitle']}</div>
  <div class="cover-authors" style="margin-top:9mm">{meta['authors']}<br><span style="font-size:9.5pt;color:#6b7b8b">{meta['venue']}</span></div>
  <div class="cover-meta"><span>{meta['note']}</span><span>{meta.get('series','CLASSIC PAPERS · BILINGUAL GUIDE')}</span></div>
</div>
<div class="pagebreak"></div>
<div class="guide">
{guide}
</div>
<div class="pagebreak"></div>
"""
    body_html = render_body(body.split("\n"), tables)
    doc = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>{title_en} · 中英对照导读</title><style>{CSS}</style></head><body>{cover}{body_html}</body></html>"""
    open(html_path, "w", encoding="utf-8").write(doc)

    raw_pdf = os.path.join(paper_dir, "_raw.pdf")
    url = pathlib.Path(html_path).as_uri()
    profile = os.path.join(tempfile.gettempdir(), "wb_chrome_pdf_profile_" + os.path.basename(paper_dir).replace(" ", "_"))
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
           "--allow-file-access-from-files", "--virtual-time-budget=12000",
           f"--user-data-dir={profile}", f"--print-to-pdf={raw_pdf}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not os.path.exists(raw_pdf):
        raise RuntimeError("Chrome failed: " + r.stderr[-800:])
    print("chrome:", r.returncode, os.path.getsize(raw_pdf), "bytes")

    pdf = pymupdf.open(raw_pdf)
    total = len(pdf)
    for i, page in enumerate(pdf):
        if i == 0:
            continue
        w, h = page.rect.width, page.rect.height
        page.draw_line((54, h-40), (w-54, h-40), color=(0.82,0.85,0.89), width=0.6)
        try:
            page.insert_text((54, h-26), f"{title_en}  ·  中英对照导读", fontname="china-s", fontsize=8, color=(0.42,0.48,0.55))
        except Exception:
            page.insert_text((54, h-26), title_en + " / Bilingual Reader", fontname="helv", fontsize=8, color=(0.42,0.48,0.55))
        label = f"{i+1} / {total}"
        tw = pymupdf.get_text_length(label, fontname="helv", fontsize=8)
        page.insert_text((w-54-tw, h-26), label, fontname="helv", fontsize=8, color=(0.42,0.48,0.55))
    pdf.set_metadata({"title": f"{title_en} · 中英对照导读", "author": "Classic Papers Bilingual Guide",
                      "subject": meta.get("arxiv", ""), "keywords": "论文导读, 中英对照, " + meta.get("kicker", "")})
    toc = []
    for i, page in enumerate(pdf):
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block: continue
            for ln in block["lines"]:
                for sp in ln["spans"]:
                    t = sp["text"].strip()
                    if sp["size"] > 15 and t and (not toc or toc[-1][1] != t) and len(t) < 90:
                        if t not in [title_en, meta["title_zh"]]:
                            toc.append([1, t, i+1])
    if toc:
        try:
            pdf.set_toc(sorted({(lvl,t,p) for lvl,t,p in toc}, key=lambda x:(x[2],x[1])))
        except Exception as e:
            print("toc skipped:", e)
    pdf.save(out_pdf, garbage=4, deflate=True)
    print(f"OK {out_pdf} | {total} pages | {os.path.getsize(out_pdf)} bytes")


if __name__ == "__main__":
    build(sys.argv[1])
