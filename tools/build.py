#!/usr/bin/env python3
"""Generate the static pages of the site.

Edit the data below (PUBLICATIONS, NEWS, ...) and run:

    python3 tools/build.py

It rewrites index.html, publications/index.html and cv/index.html.
No dependencies beyond the Python standard library.
"""
import html
import os
import re
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ME = ("H. Kavianirad", "H. Kaviani Rad", "H. K. Rad")

SITE_URL = "https://kavianirad.github.io"
EMAIL = "hossein.kavianirad@tum.de"
SCHOLAR = "https://scholar.google.com/citations?user=DqDqY38AAAAJ&hl=en"
LINKEDIN = "https://www.linkedin.com/in/hossein-kaviani-rad-b23360139/"
GITHUB = "https://github.com/kavianirad"
TUM = "https://www.ce.cit.tum.de/itr/kavianirad/"
DBLP = "https://dblp.org/pid/360/8415"

# type: journal | conference | workshop | preprint
PUBLICATIONS = [
    dict(
        key="cazenave2026hybrid", year=2026, type="journal", badge="JRATE",
        highlights=["Clinical study with stroke patients"],
        title="Hybrid robot & FES rehabilitation after stroke: Short-term performance, fatigue, and patient experience",
        authors=["L. Cazenave", "C. Höhler", "S. Endo", "H. Kavianirad", "N. Peña-Pérez", "L.-M. Huber", "A. Yurkewich", "T. Keller", "S. Hirche", "K. Jahn", "et al."],
        venue="Journal of Rehabilitation and Assistive Technologies Engineering, vol. 13, 2026",
        links={"DOI": "https://doi.org/10.1177/20556683261488467"},
        bib_type="article", bib_venue=("journal", "Journal of Rehabilitation and Assistive Technologies Engineering"),
        bib_extra={"volume": "13", "doi": "10.1177/20556683261488467"},
    ),
    dict(
        key="kavianirad2025dynamic", year=2025, type="preprint", badge="arXiv", selected=True,
        highlights=["Under review at IEEE Transactions on Control Systems Technology"],
        title="Cooperative Control of Hybrid FES-Exoskeleton: Dynamic Allocation",
        authors=["H. Kavianirad", "S. Endo", "D. Astarita", "L. Amato", "E. Trigili", "S. Hirche"],
        venue="arXiv preprint arXiv:2511.10117, 2025 (under review at IEEE Transactions on Control Systems Technology)",
        links={"arXiv": "https://arxiv.org/abs/2511.10117", "PDF": "https://arxiv.org/pdf/2511.10117", "DOI": "https://doi.org/10.48550/arXiv.2511.10117"},
        bib_type="article", bib_venue=("journal", "arXiv preprint arXiv:2511.10117"), bib_extra={},
    ),
    dict(
        key="hoehler2025repetitive", year=2025, type="journal", badge="Artif. Organs",
        highlights=["Clinical study with stroke patients"],
        title="Repetitive Grasping After Stroke Assisted by Functional Electrical Stimulation",
        authors=["C. Höhler", "S. Endo", "J. Hermsdörfer", "L. Cazenave", "H. Kavianirad", "K. Jahn", "C. Krewer"],
        venue="Artificial Organs, vol. 49, no. 12, pp. 1733–1744, 2025",
        links={"DOI": "https://doi.org/10.1111/aor.15033"},
        bib_type="article", bib_venue=("journal", "Artificial Organs"), bib_extra={"volume": "49", "number": "12", "pages": "1733--1744", "doi": "10.1111/aor.15033"},
    ),
    dict(
        key="kavianirad2024dexterous", year=2024, type="conference", badge="BioRob", selected=True,
        highlights=["Featured in TUM press release (ReHyb)"],
        title="Toward Dexterous Hand Functional Movement: Wearable Hybrid Soft Exoglove-FES Study",
        authors=["H. Kavianirad", "F. Missiroli", "S. Endo", "L. Masia", "S. Hirche"],
        venue="IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob), pp. 1346–1351, 2024",
        links={"DOI": "https://doi.org/10.1109/BioRob60516.2024.10719731", "IEEE": "https://ieeexplore.ieee.org/document/10719731"},
        bib_type="inproceedings", bib_venue=("booktitle", "2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob)"),
        bib_extra={"pages": "1346--1351", "doi": "10.1109/BioRob60516.2024.10719731"},
    ),
    dict(
        key="das2024framework", year=2024, type="conference", badge="BioRob", selected=True,
        highlights=["Featured in TUM press release (ReHyb)"],
        title="Framework for Learning a Hand Intent Recognition Model from sEMG for FES-Based Control",
        authors=["N. Das", "S. Endo", "H. Kavianirad", "S. Hirche"],
        venue="IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob), pp. 1320–1327, 2024",
        links={"DOI": "https://doi.org/10.1109/BioRob60516.2024.10719910", "IEEE": "https://ieeexplore.ieee.org/abstract/document/10719910"},
        bib_type="inproceedings", bib_venue=("booktitle", "2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob)"),
        bib_extra={"pages": "1320--1327", "doi": "10.1109/BioRob60516.2024.10719910"},
    ),
    dict(
        key="kavianirad2023model", year=2023, type="conference", badge="ICORR", selected=True,
        title="Model-Based Shared Control of a Hybrid FES-Exoskeleton: An Application in Participant-Specific Robotic Rehabilitation",
        authors=["H. Kavianirad", "M. Forouhar", "H. Sadeghian", "S. Endo", "S. Haddadin", "S. Hirche"],
        venue="International Conference on Rehabilitation Robotics (ICORR), pp. 1–6, 2023",
        links={"DOI": "https://doi.org/10.1109/ICORR58425.2023.10304764", "IEEE": "https://ieeexplore.ieee.org/abstract/document/10304764"},
        bib_type="inproceedings", bib_venue=("booktitle", "2023 International Conference on Rehabilitation Robotics (ICORR)"),
        bib_extra={"pages": "1--6", "doi": "10.1109/ICORR58425.2023.10304764"},
    ),
    dict(
        key="kavianirad2022emg", year=2022, type="conference", badge="IECBES", selected=True,
        award="Best Paper Award",
        title="EMG-Based Volitional Torque Estimation in Functional Electrical Stimulation Control",
        authors=["H. Kavianirad", "S. Endo", "T. Keller", "S. Hirche"],
        venue="IEEE-EMBS Conference on Biomedical Engineering and Sciences (IECBES), pp. 171–176, 2022",
        links={"DOI": "https://doi.org/10.1109/IECBES54088.2022.10079376", "IEEE": "https://ieeexplore.ieee.org/abstract/document/10079376"},
        bib_type="inproceedings", bib_venue=("booktitle", "2022 IEEE-EMBS Conference on Biomedical Engineering and Sciences (IECBES)"),
        bib_extra={"pages": "171--176", "doi": "10.1109/IECBES54088.2022.10079376"},
    ),
    dict(
        key="sena2022gap", year=2022, type="workshop", badge="Sim2Real WS",
        title="The Gap in Functional Electrical Stimulation Simulation",
        authors=["A. Sena", "H. Kavianirad", "S. Endo", "E. Burdet", "S. Hirche"],
        venue="3rd Workshop on Closing the Reality Gap in Sim2Real Transfer for Robotics (RSS), 2022",
        links={"PDF": "https://sim2real.github.io/assets/papers/2022/sena.pdf", "mediaTUM": "https://mediatum.ub.tum.de/node?id=1692363"},
        bib_type="inproceedings", bib_venue=("booktitle", "3rd Workshop on Closing the Reality Gap in Sim2Real Transfer for Robotics"), bib_extra={},
    ),
    dict(
        key="rad2018boundary", year=2018, type="journal", badge="JSV",
        title="Boundary control of flexible satellite vibration in planar motion",
        authors=["H. K. Rad", "H. Salarieh", "A. Alasty", "R. Vatankhah"],
        venue="Journal of Sound and Vibration, vol. 432, pp. 549–568, 2018",
        links={"DOI": "https://doi.org/10.1016/j.jsv.2018.06.052"},
        bib_type="article", bib_venue=("journal", "Journal of Sound and Vibration"), bib_extra={"volume": "432", "pages": "549--568", "doi": "10.1016/j.jsv.2018.06.052"},
    ),
    dict(
        key="rad2018antisymmetric", year=2018, type="journal", badge="Acta Astronaut.",
        title="Boundary control of anti-symmetric vibration of satellite with flexible appendages in planar motion with exponential stability",
        authors=["H. K. Rad", "H. Salarieh", "A. Alasty", "R. Vatankhah"],
        venue="Acta Astronautica, vol. 147, pp. 219–230, 2018",
        links={"DOI": "https://doi.org/10.1016/j.actaastro.2018.03.050"},
        bib_type="article", bib_venue=("journal", "Acta Astronautica"), bib_extra={"volume": "147", "pages": "219--230", "doi": "10.1016/j.actaastro.2018.03.050"},
    ),
    dict(
        key="kavianirad2018frictional", year=2018, type="journal", badge="Granular Matter",
        title="Frictional viscoelastic based model for spherical particles collision",
        authors=["H. Kaviani Rad", "H. Nejat Pishkenari"],
        venue="Granular Matter, vol. 20, no. 4, art. 62, 2018",
        links={"DOI": "https://doi.org/10.1007/s10035-018-0835-9"},
        bib_type="article", bib_venue=("journal", "Granular Matter"), bib_extra={"volume": "20", "doi": "10.1007/s10035-018-0835-9"},
    ),
    dict(
        key="nejat2017transformation", year=2017, type="journal", badge="Granular Matter",
        title="Transformation of sliding motion to rolling during spheres collision",
        authors=["H. Nejat Pishkenari", "H. Kaviani Rad", "H. Jafari Shad"],
        venue="Granular Matter, vol. 19, no. 4, art. 70, 2017",
        links={"DOI": "https://doi.org/10.1007/s10035-017-0755-0"},
        bib_type="article", bib_venue=("journal", "Granular Matter"), bib_extra={"volume": "19", "doi": "10.1007/s10035-017-0755-0"},
    ),
]

NEWS = [
    ("Jul 2026", 'Gave the ITR doctoral seminar talk <em>“Cooperative Shared Control of Hybrid FES-Exoskeleton”</em>. '
                 '<a href="https://www.ce.cit.tum.de/ics/news/article/the-next-doctoral-seminar-talk-will-take-place-next-monday-july-20th-and-will-be-given-by-hossein-kavianirad-the-title-of-the-talk-is-cooperative-shared-control-of-hybrid-fes-exoskeleton/">Announcement</a>'),
    ("2026", 'Journal paper on hybrid robot &amp; FES rehabilitation after stroke published in <em>JRATE</em>. '
             '<a href="https://doi.org/10.1177/20556683261488467">Paper</a>'),
    ("Nov 2025", 'New preprint, under review at <em>IEEE Transactions on Control Systems Technology</em>: <em>Cooperative Control of Hybrid FES-Exoskeleton: Dynamic Allocation</em>. '
                 '<a href="https://arxiv.org/abs/2511.10117">arXiv</a>'),
    ("Mar 2025", 'Our EU project <strong>ReHyb</strong> on hybrid FES-exoskeleton stroke rehabilitation was featured in a TUM press release. '
                 '<a href="https://idw-online.de/de/news848815">Press release</a> · <a href="https://youtu.be/OboVMCkM9Yk">Video</a>'),
    ("2025", 'Paper on FES-assisted repetitive grasping after stroke published in <em>Artificial Organs</em>. '
             '<a href="https://doi.org/10.1111/aor.15033">Paper</a>'),
    ("2024", 'Two papers presented at <strong>IEEE BioRob 2024</strong>: a hybrid soft exoglove-FES study and sEMG-based hand intent recognition for FES.'),
    ("2023", 'Presented model-based shared control of a hybrid FES-exoskeleton at <strong>ICORR 2023</strong>.'),
    ("2022", 'Received the <strong>Best Paper Award</strong> at IEEE-EMBS IECBES 2022 for EMG-based volitional torque estimation in FES control.'),
]

# Google Scholar totals shown before the page loads the live data (profile, 15 Oct 2026).
STATS = {"citations": 144, "h_index": 7, "i10_index": 5}

TYPE_LABEL = {"journal": "Journal", "conference": "Conference", "workshop": "Workshop", "preprint": "Preprint"}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,600&display=swap" rel="stylesheet">\n'
         '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n'
         '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.4/css/academicons.min.css">')


def esc(s):
    return html.escape(s, quote=True)


def authors_html(authors):
    out = []
    for a in authors:
        out.append(f'<span class="me">{esc(a)}</span>' if a in ME else esc(a))
    return ", ".join(out)


def bibtex(p):
    names = " and ".join(a for a in p["authors"] if a != "et al.")
    if "et al." in p["authors"]:
        names += " and others"
    fields = [("title", p["title"]), ("author", names), p["bib_venue"], ("year", str(p["year"]))]
    fields += list(p["bib_extra"].items())
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields)
    return f"@{p['bib_type']}{{{p['key']},\n{body}\n}}"


def plain_citation(p):
    names = [a for a in p["authors"] if a != "et al."]
    who = ", ".join(names[:-1]) + (", and " + names[-1] if len(names) > 1 else names[0])
    if "et al." in p["authors"]:
        who += ", et al."
    return f'{who}, "{p["title"]}," {p["venue"]}.'


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def pub_html(p, prefix):
    links = "".join(f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in p["links"].items())
    bib_id = f"{prefix}-bib-{p['key']}"
    notes = []
    if p.get("award"):
        notes.append(f'<span class="pub-award"><i class="fa-solid fa-trophy"></i> {esc(p["award"])}</span>')
    for h in p.get("highlights", []):
        notes.append(f'<span class="pub-note">{esc(h)}</span>')
    if p["authors"][0] in ME:
        notes.append('<span class="pub-note first">First author</span>')
    notes_html = f'\n          <div class="pub-notes">{"".join(notes)}</div>' if notes else ""
    scholar_q = "https://scholar.google.com/scholar?q=" + urllib.parse.quote(f'"{p["title"]}"')
    badge = (f'<a class="scholar-badge" data-title="{norm_title(p["title"])}" href="{scholar_q}" target="_blank" rel="noopener" '
             f'title="Google Scholar citations"><span class="sb-l"><i class="ai ai-google-scholar"></i> scholar</span>'
             f'<span class="sb-n" hidden></span></a>')
    return f"""      <li class="pub" id="{p['key'] if prefix == 'all' else prefix + '-' + p['key']}" data-type="{p['type']}">
        <div class="venue-badge {p['type']}" title="{TYPE_LABEL[p['type']]}">{esc(p['badge'])}</div>
        <div>
          <div class="pub-title">{esc(p['title'])}</div>
          <div class="pub-authors">{authors_html(p['authors'])}</div>
          <div class="pub-venue">{esc(p['venue'])}</div>{notes_html}
          <div class="pub-links">{links}<button type="button" data-bib="{bib_id}">BibTeX</button><button type="button" class="cite-btn" data-cite="{esc(plain_citation(p))}">Cite</button>{badge}</div>
          <pre class="bibtex" id="{bib_id}">{esc(bibtex(p))}</pre>
        </div>
      </li>"""


def nav(active, base):
    items = [("About", f"{base}"), ("Publications", f"{base}publications/"), ("CV", f"{base}cv/")]
    lis = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if name == active else ""}>{name}</a></li>'
        for name, href in items)
    return f"""  <nav class="nav" aria-label="Main">
    <div class="container">
      <a class="brand" href="{base}">Hossein Kavianirad</a>
      <button class="icon-btn menu-toggle" id="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><i class="fa-solid fa-bars"></i></button>
      <ul class="nav-links" id="nav-links">
{lis}
        <li class="theme-item"><button class="icon-btn" id="theme-toggle" type="button" aria-label="Toggle theme"><i class="fa-solid fa-moon"></i></button></li>
      </ul>
    </div>
  </nav>"""


def head(title, description, base, path):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="author" content="Hossein Kavianirad">
  <link rel="canonical" href="{SITE_URL}{path}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{SITE_URL}{path}">
  <meta property="og:image" content="{SITE_URL}/assets/img/profile.jpg">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
  <script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
  {FONTS}
  <link rel="stylesheet" href="{base}assets/css/style.css">
  <script src="{base}assets/js/main.js" defer></script>
</head>"""


def footer(base):
    return f"""  <footer>
    <div class="container">
      <div>© <span id="year">2026</span> Hossein Kavianirad · Technical University of Munich</div>
      <div class="foot-links">
        <a href="mailto:{EMAIL}" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        <a href="{SCHOLAR}" aria-label="Google Scholar"><i class="ai ai-google-scholar"></i></a>
        <a href="{LINKEDIN}" aria-label="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
        <a href="{GITHUB}" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
      </div>
    </div>
  </footer>"""


def person_jsonld():
    return f"""  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Person","name":"Hossein Kavianirad",
   "jobTitle":"Doctoral Researcher","email":"mailto:{EMAIL}","url":"{SITE_URL}/",
   "image":"{SITE_URL}/assets/img/profile.jpg",
   "affiliation":{{"@type":"Organization","name":"Chair of Information-oriented Control, Technical University of Munich"}},
   "alumniOf":["Sharif University of Technology","Shiraz University"],
   "sameAs":["{SCHOLAR}","{LINKEDIN}","{TUM}","{GITHUB}"]}}
  </script>"""


def build_index():
    selected = [p for p in PUBLICATIONS if p.get("selected")]
    news = "\n".join(f'      <li><time>{d}</time><div>{t}</div></li>' for d, t in NEWS[:7])
    pubs = "\n".join(pub_html(p, "sel") for p in selected)
    page = f"""{head("Hossein Kavianirad · TUM", "Hossein Kavianirad is a doctoral researcher at the Chair of Information-oriented Control, TUM, working on shared control of hybrid FES-exoskeletons for neurorehabilitation.", "", "/")}
<body>
{nav("About", "")}
  <main class="container">
    <section class="hero" id="about">
      <div>
        <h1>Hossein Kavianirad</h1>
        <div class="role"><strong>Doctoral Researcher</strong> · Chair of Information-oriented Control (ITR) · Technical University of Munich</div>
        <p>I am a PhD candidate at the <a href="https://www.ce.cit.tum.de/itr/">Chair of Information-oriented Control</a>, Technical University of Munich, advised by <a href="https://www.ce.cit.tum.de/itr/hirche/">Prof. Sandra Hirche</a>. I develop <strong>cooperative shared control for hybrid FES-exoskeletons</strong>, wearable systems that combine electrical stimulation of a person's own muscles with robotic assistance to restore arm and hand function after stroke.</p>
        <p>My work spans participant-specific neuromuscular modeling, EMG-based estimation of voluntary effort under stimulation, and dynamic allocation of effort between muscles and motors, validated in human studies and with stroke patients in the EU Horizon project <a href="https://idw-online.de/de/news848815">ReHyb</a>. I trained in mechanical engineering and control at Sharif University of Technology and Shiraz University, and expect to complete my PhD in early 2027.</p>
        <p class="status"><span class="dot" aria-hidden="true"></span>Open to postdoctoral and research positions in control, rehabilitation robotics and human-robot interaction.</p>
        <div class="socials">
          <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i>Email</a>
          <a href="{SCHOLAR}"><i class="ai ai-google-scholar"></i>Google Scholar</a>
          <a href="{LINKEDIN}"><i class="fa-brands fa-linkedin"></i>LinkedIn</a>
          <a href="{TUM}"><i class="fa-solid fa-building-columns"></i>TUM profile</a>
          <a href="assets/Kavianirad_CV.pdf"><i class="fa-solid fa-file-pdf"></i>CV (PDF)</a>
        </div>
        <div class="callout"><i class="fa-solid fa-graduation-cap"></i>&nbsp; <strong>Students:</strong> I have supervised 16 students so far and offer Bachelor's and Master's theses in control, learning, dynamic modeling, and rehabilitation robotics. Feel free to email me with your CV and transcripts.</div>
      </div>
      <div class="hero-photo">
        <img src="assets/img/profile.jpg" alt="Portrait of Hossein Kavianirad" width="220" height="220">
        <div class="affil">Technical University of Munich<br>Munich, Germany</div>
      </div>
    </section>

    <section class="highlights" aria-label="Highlights">
      <div class="hl"><span class="hl-k">Best Paper Award</span><span class="hl-v">IEEE-EMBS IECBES 2022</span></div>
      <div class="hl"><span class="hl-k">{len(PUBLICATIONS)} publications</span><span class="hl-v">ICORR, BioRob, JSV, Acta Astronautica</span></div>
      <div class="hl"><span class="hl-k">EU Horizon ReHyb</span><span class="hl-v">clinical studies with stroke patients</span></div>
      <div class="hl"><span class="hl-k">16 students</span><span class="hl-v">theses and projects supervised</span></div>
    </section>

    <section id="research">
      <h2 class="section-title">Research</h2>
      <p class="lede">Hybrid FES-exoskeletons are redundant: the same joint torque can come from stimulated muscles, from motors, or from the user's own effort. My thesis, <em>Cooperative Shared Control of Hybrid FES-Exoskeleton</em>, asks how to model each source, estimate the user's contribution, and share the work between them safely and comfortably.</p>
      <div class="projects">
        <article class="project">
          <figure><img src="assets/img/research/modeling.jpg" alt="Diagram of the stimulation-to-torque pathway from FES electrodes through muscle activation to joint torque" loading="lazy"></figure>
          <div>
            <h3>Neuromuscular modeling for FES</h3>
            <p>Participant-specific, control-oriented models of the stimulation-to-torque pathway that capture inter-individual variability, fatigue and the attainable torque of each muscle group.</p>
            <div class="project-links"><a href="publications/#sena2022gap">Sim2Real 2022</a><a href="publications/#kavianirad2023model">ICORR 2023</a></div>
          </div>
        </article>
        <article class="project">
          <figure><img src="assets/img/research/emg.jpg" alt="Rendering of the forearm EMG and stimulation setup with the upper-limb musculoskeletal model" loading="lazy"></figure>
          <div>
            <h3>Volitional effort from EMG during stimulation</h3>
            <p>An adaptive filter removes stimulation artifacts from surface EMG so the user's voluntary torque and hand intent can be estimated in real time and kept in the loop.</p>
            <div class="project-links"><a href="publications/#kavianirad2022emg">IECBES 2022 · Best Paper</a><a href="publications/#das2024framework">BioRob 2024</a></div>
          </div>
        </article>
        <article class="project">
          <figure><img src="assets/img/research/allocation.jpg" alt="Hybrid FES-exoskeleton on a wheelchair with stimulation module, electrodes and force-torque sensor" loading="lazy"></figure>
          <div>
            <h3>Shared control and dynamic allocation</h3>
            <p>Model-based shared control and a dynamic control allocator that distributes torque between FES and exoskeleton in real time, respecting device limits, fatigue and user preference, with stability guarantees.</p>
            <div class="project-links"><a href="publications/#kavianirad2023model">ICORR 2023</a><a href="publications/#kavianirad2025dynamic">arXiv 2025</a><a href="publications/#cazenave2026hybrid">JRATE 2026</a></div>
          </div>
        </article>
        <article class="project">
          <figure><img src="assets/img/research/hand.jpg" alt="Hand with motion-capture markers and the matching inverse-kinematics hand model during exoglove and FES grasping" loading="lazy"></figure>
          <div>
            <h3>Dexterous hand function</h3>
            <p>A wearable soft exoglove combined with multi-array FES for functional finger and thumb movements, at least doubling finger mobility compared with stimulation alone. Ongoing: a hand prosthesis driven by high-density EMG for dexterous movements.</p>
            <div class="project-links"><a href="publications/#kavianirad2024dexterous">BioRob 2024</a><a href="publications/#hoehler2025repetitive">Artif. Organs 2025</a></div>
          </div>
        </article>
      </div>
      <p class="fig-credit">Figures from my dissertation, CC BY 4.0.</p>
    </section>

    <section id="news">
      <h2 class="section-title">News</h2>
      <ul class="news">
{news}
      </ul>
    </section>

    <section id="publications">
      <h2 class="section-title">Selected publications <a class="more" href="publications/">All publications →</a></h2>
      <ul class="pubs">
{pubs}
      </ul>
    </section>

    <section id="media">
      <h2 class="section-title">In the media</h2>
      <div class="two-col">
        <div class="video">
          <iframe src="https://www.youtube-nocookie.com/embed/OboVMCkM9Yk" title="ReHyb: hybrid FES-exoskeleton rehabilitation at TUM" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div>
          <h3 style="font-size:1.05rem;margin-bottom:.4rem">ReHyb: muscle stimulation meets exoskeleton</h3>
          <p style="margin:0 0 .75rem;color:var(--text-muted)">TUM's hybrid system combines functional electrical stimulation of the forearm with an arm and shoulder exoskeleton and a patient-specific digital twin. It has been tested with stroke patients together with Schön Klinik Bad Aibling.</p>
          <a href="https://idw-online.de/de/news848815">Read the press release →</a>
        </div>
      </div>
    </section>

    <section id="contact">
      <h2 class="section-title">Contact</h2>
      <div class="two-col">
        <ul class="contact-list">
          <li><i class="fa-solid fa-envelope"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><i class="fa-solid fa-phone"></i><span>+49 (89) 289-25776</span></li>
          <li><i class="fa-solid fa-door-open"></i><span>Room S4519 (building 0305, 4th floor)</span></li>
        </ul>
        <ul class="contact-list">
          <li><i class="fa-solid fa-location-dot"></i><span>Chair of Information-oriented Control<br>Technical University of Munich<br>Barer Str. 21, 80333 München, Germany</span></li>
        </ul>
      </div>
    </section>
  </main>
{footer("")}
{person_jsonld()}
</body>
</html>
"""
    write("index.html", page)


def build_publications():
    years = sorted({p["year"] for p in PUBLICATIONS}, reverse=True)
    groups = []
    for y in years:
        items = "\n".join(pub_html(p, "all") for p in PUBLICATIONS if p["year"] == y)
        groups.append(f'    <div class="pub-group">\n      <h2 class="pub-year">{y}</h2>\n      <ul class="pubs">\n{items}\n      </ul>\n    </div>')
    counts = {t: sum(1 for p in PUBLICATIONS if p["type"] == t) for t in TYPE_LABEL}
    filters = '<button type="button" data-filter="all" aria-pressed="true">All (%d)</button>' % len(PUBLICATIONS)
    for t, label in TYPE_LABEL.items():
        if counts[t]:
            filters += f'<button type="button" data-filter="{t}" aria-pressed="false">{label} ({counts[t]})</button>'
    page = f"""{head("Publications · Hossein Kavianirad", "Publications of Hossein Kavianirad on hybrid FES-exoskeletons, EMG-based control, and rehabilitation robotics.", "../", "/publications/")}
<body>
{nav("Publications", "../")}
  <main class="container">
    <header class="page-head">
      <h1>Publications</h1>
      <p>Also on <a href="{SCHOLAR}">Google Scholar</a> and the <a href="{TUM}">TUM ITR page</a>.</p>
      <dl class="stats" id="scholar-stats">
        <div><dt>Publications</dt><dd>{len(PUBLICATIONS)}</dd></div>
        <div><dt>Citations</dt><dd data-stat="citations">{STATS["citations"]}</dd></div>
        <div><dt>h-index</dt><dd data-stat="h_index">{STATS["h_index"]}</dd></div>
        <div><dt>i10-index</dt><dd data-stat="i10_index">{STATS["i10_index"]}</dd></div>
      </dl>
      <p class="stats-note">Totals from <a href="{SCHOLAR}">Google Scholar</a><span id="scholar-updated"></span>.</p>
    </header>
    <section>
      <div class="filters" role="group" aria-label="Filter by type">{filters}</div>
{chr(10).join(groups)}
    </section>
  </main>
{footer("../")}
</body>
</html>
"""
    write("publications/index.html", page)


def build_cv():
    page = f"""{head("CV · Hossein Kavianirad", "Curriculum vitae of Hossein Kavianirad: education, research experience, teaching, awards and skills.", "../", "/cv/")}
<body>
{nav("CV", "../")}
  <main class="container">
    <header class="page-head">
      <h1>Curriculum Vitae</h1>
      <p>Doctoral researcher in control and rehabilitation robotics at the Technical University of Munich.</p>
      <div class="socials"><a href="../assets/Kavianirad_CV.pdf"><i class="fa-solid fa-file-pdf"></i>Download full CV (PDF)</a><a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i>{EMAIL}</a></div>
    </header>

    <section>
      <h2 class="section-title">Short bio</h2>
      <p class="bio">Hossein Kavianirad is a doctoral researcher at the Chair of Information-oriented Control (ITR), Technical University of Munich, advised by Prof. Sandra Hirche. His research covers control theory, learning-based and human-centric control, and shared and cooperative control of hybrid exoskeletons and wearable robots. He develops controllers for input-redundant systems that distribute effort between an exoskeleton and functional electrical stimulation while accounting for the user's intent, using dynamic allocation with stability guarantees, model predictive control and EMG-based intent estimation, tested with healthy participants and stroke patients in the EU Horizon 2020 project ReHyb. He holds an M.Sc. in Mechanical Engineering from Sharif University of Technology and a B.Sc. from Shiraz University, and received the IEEE-EMBS IECBES 2022 Best Paper Award.</p>
      <button type="button" class="copy-bio" id="copy-bio">Copy bio</button>
    </section>

    <section>
      <h2 class="section-title">Education</h2>
      <ul class="timeline">
        <li>
          <div class="when">04/2021 – 03/2027 (expected)</div>
          <h3>Doctoral candidate, Electrical Engineering</h3>
          <div class="where">Technical University of Munich, TUM School of Computation, Information and Technology</div>
          <p>Chair of Information-oriented Control (ITR). Supervisor: Prof. Dr.-Ing. Sandra Hirche. Dissertation: <em>Cooperative Shared Control of Hybrid FES-Exoskeleton</em>.</p>
        </li>
        <li>
          <div class="when">09/2015 – 09/2017</div>
          <h3>M.Sc. Mechanical Engineering (Applied Mechanics)</h3>
          <div class="where">Sharif University of Technology, Tehran</div>
          <p>GPA 19.27/20, ranked 2nd of 151. Thesis: <em>Boundary Control of Vibration in Satellite Flexible Solar Panels</em> (Lyapunov-based boundary control, asymptotic and exponential stability, disturbance observer). Supervisors: Prof. H. Salarieh, Prof. A. Alasty.</p>
        </li>
        <li>
          <div class="when">09/2011 – 09/2015</div>
          <h3>B.Sc. Mechanical Engineering</h3>
          <div class="where">Shiraz University</div>
          <p>GPA 19.05/20, ranked 1st of 89. Project: <em>Energy harvesting in a piezoelastic beam excited by air flow</em> (supervisor: Prof. M. Farid).</p>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Research experience</h2>
      <ul class="timeline">
        <li>
          <div class="when">04/2021 – present</div>
          <h3>Doctoral Researcher</h3>
          <div class="where"><a href="https://www.ce.cit.tum.de/itr/">Chair of Information-oriented Control (ITR)</a>, Technical University of Munich</div>
          <ul class="bullets">
            <li>Designed shared and cooperative control for hybrid FES-exoskeletons: impedance-based shared control, MPC-based FES control, and a real-time dynamic allocator that redistributes torque between FES and exoskeleton under heterogeneous actuator constraints, with a stability proof. Extended it to personalized allocation based on participant-specific attainable sets.</li>
            <li>Identified user-specific nonlinear, delayed and time-varying neuromuscular models from sparse data with learning-based methods, and estimated volitional torque from EMG with a novel adaptive filter (<a href="https://doi.org/10.1109/IECBES54088.2022.10079376">Best Paper Award</a>).</li>
            <li>Ran studies with healthy participants and stroke patients on the NESM-γ elbow exoskeleton (Scuola Superiore Sant'Anna), the HRX-1 wrist robot (HumanRobotiX) and FES/EMG hardware (Tecnalia) in the EU Horizon 2020 project ReHyb (GA 871767), with Imperial College London and Schön Klinik Bad Aibling.</li>
            <li>Developing a hand prosthesis driven by high-density EMG for dexterous hand movements (ongoing).</li>
          </ul>
        </li>
        <li>
          <div class="when">10/2017 – 03/2021</div>
          <h3>Researcher</h3>
          <div class="where">Shiraz University Research Center, Iran</div>
          <p>System identification and control; embedded ARM control systems (Keil) with sensors and actuators in C/C++.</p>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Teaching &amp; supervision</h2>
      <ul class="timeline">
        <li>
          <div class="when">2021 – present · 5 semesters</div>
          <h3>Advanced Nonlinear Control</h3>
          <div class="where">M.Sc. course, ITR, TUM</div>
          <p>Supervision of student tutorial reports on advanced nonlinear-control topics, reviews and presentations.</p>
        </li>
        <li>
          <div class="when">SS 2023 – SS 2026 · 4 semesters</div>
          <h3>Advanced Control and Robotics Lab</h3>
          <div class="where">M.Sc. lab, LSR and ITR, TUM</div>
          <p>Supervisor of the <em>Sliding Mode Control</em> experiment.</p>
        </li>
        <li>
          <div class="when">2021 – present</div>
          <h3>Thesis and project supervision: 16 students</h3>
          <div class="where">Technical University of Munich</div>
          <p>7 B.Sc. theses, 1 M.Sc. thesis, 2 research internships and 6 engineering internships.</p>
        </li>
        <li>
          <div class="when">2015 – 2016</div>
          <h3>Teaching assistant</h3>
          <div class="where">Sharif University of Technology</div>
          <p>Advanced Control (M.Sc., Fall 2016) and Dynamics (Fall 2015); laboratory assistant, Dynamics of Machinery and Vibrations Lab (three semesters).</p>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Honors &amp; awards</h2>
      <ul class="timeline">
        <li><div class="when">2022</div><h3>Best Paper Award, IEEE-EMBS IECBES 2022</h3><div class="where">For “EMG-Based Volitional Torque Estimation in Functional Electrical Stimulation Control”</div></li>
        <li><div class="when">2015 – 2017</div><h3>Teaching assistantship funded by Iran's National Elites Foundation</h3></li>
        <li><div class="when">2015 – 2016</div><h3>Distinguished student of mechanical engineering</h3><div class="where">Sharif University of Technology</div></li>
        <li><div class="when">2014 – 2015</div><h3>National Elites Foundation fellowship; distinguished student of mechanical engineering</h3><div class="where">Shiraz University</div></li>
        <li><div class="when">2011 – 2017</div><h3>Ranked 2nd of 151 (M.Sc.) and 1st of 89 (B.Sc.)</h3><div class="where">Sharif University of Technology; Shiraz University</div></li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Talks</h2>
      <ul class="timeline">
        <li>
          <div class="when">07/2026</div>
          <h3>Cooperative Shared Control of Hybrid FES-Exoskeleton</h3>
          <div class="where">Doctoral seminar, TUM School of Computation, Information and Technology, Munich</div>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Skills</h2>
      <dl class="skills">
        <dt>Methods</dt><dd>Nonlinear, Lyapunov-based and boundary control · MPC · control allocation · shared control · system identification · learning-based modeling · EMG signal processing</dd>
        <dt>Programming</dt><dd>MATLAB/Simulink · C/C++ · embedded ARM (Keil) · Python · Git/GitHub · Claude Code</dd>
        <dt>Simulation &amp; CAD</dt><dd>MuJoCo · Simulink · Abaqus · SolidWorks</dd>
        <dt>Hardware</dt><dd>Elbow and wrist exoskeletons · soft exoglove · prosthetic and dexterous robotic hands · multi-array FES · EMG and HD-EMG · force/torque sensors · IMUs · Qualisys motion capture · embedded real-time controllers</dd>
        <dt>Languages</dt><dd>English (fluent) · German (basic) · Persian (native)</dd>
      </dl>
    </section>
  </main>
{footer("../")}
</body>
</html>
"""
    write("cv/index.html", page)


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


if __name__ == "__main__":
    build_index()
    build_publications()
    build_cv()
