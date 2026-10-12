#!/usr/bin/env python3
"""Generate the static pages of the site.

Edit the data below (PUBLICATIONS, NEWS, ...) and run:

    python3 tools/build.py

It rewrites index.html, publications/index.html and cv/index.html.
No dependencies beyond the Python standard library.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ME = ("H. Kavianirad", "H. Kaviani Rad", "H. K. Rad")

SITE_URL = "https://kavianirad.github.io"
EMAIL = "hossein.kavianirad@tum.de"
SCHOLAR = "https://scholar.google.com/citations?user=DqDqY38AAAAJ&hl=en"
LINKEDIN = "https://www.linkedin.com/in/hossein-kavianirad-b23360139/"
GITHUB = "https://github.com/kavianirad"
TUM = "https://www.ce.cit.tum.de/itr/kavianirad/"
DBLP = "https://dblp.org/pid/360/8415"

# type: journal | conference | workshop | preprint
PUBLICATIONS = [
    dict(
        key="cazenave2026hybrid", year=2026, type="journal", badge="JRATE",
        title="Hybrid robot & FES rehabilitation after stroke: Short-term performance, fatigue, and patient experience",
        authors=["L. Cazenave", "C. Höhler", "S. Endo", "H. Kavianirad", "et al."],
        venue="Journal of Rehabilitation and Assistive Technologies Engineering, vol. 13, 2026",
        links={"DOI": "https://doi.org/10.1177/20556683261488467"},
        bib_type="article", bib_venue=("journal", "Journal of Rehabilitation and Assistive Technologies Engineering"),
        bib_extra={"volume": "13", "doi": "10.1177/20556683261488467"},
    ),
    dict(
        key="kavianirad2025dynamic", year=2025, type="preprint", badge="arXiv", selected=True,
        title="Cooperative Control of Hybrid FES-Exoskeleton: Dynamic Allocation",
        authors=["H. Kavianirad", "S. Endo", "D. Astarita", "L. Amato", "E. Trigili", "S. Hirche"],
        venue="arXiv preprint arXiv:2511.10117, 2025",
        links={"arXiv": "https://arxiv.org/abs/2511.10117", "PDF": "https://arxiv.org/pdf/2511.10117"},
        bib_type="article", bib_venue=("journal", "arXiv preprint arXiv:2511.10117"), bib_extra={},
    ),
    dict(
        key="hoehler2025repetitive", year=2025, type="journal", badge="Artif. Organs",
        title="Repetitive Grasping After Stroke Assisted by Functional Electrical Stimulation",
        authors=["C. Höhler", "S. Endo", "J. Hermsdörfer", "L. Cazenave", "H. Kavianirad", "K. Jahn", "C. Krewer"],
        venue="Artificial Organs, 2025",
        links={"DOI": "https://doi.org/10.1111/aor.15033"},
        bib_type="article", bib_venue=("journal", "Artificial Organs"), bib_extra={"doi": "10.1111/aor.15033"},
    ),
    dict(
        key="kavianirad2024dexterous", year=2024, type="conference", badge="BioRob", selected=True,
        title="Toward Dexterous Hand Functional Movement: Wearable Hybrid Soft Exoglove-FES Study",
        authors=["H. Kavianirad", "F. Missiroli", "S. Endo", "L. Masia", "S. Hirche"],
        venue="IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob), pp. 1346–1351, 2024",
        links={"DOI": "https://doi.org/10.1109/BioRob60516.2024.10719731", "IEEE": "https://ieeexplore.ieee.org/document/10719731"},
        bib_type="inproceedings", bib_venue=("booktitle", "2024 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob)"),
        bib_extra={"pages": "1346--1351", "doi": "10.1109/BioRob60516.2024.10719731"},
    ),
    dict(
        key="das2024framework", year=2024, type="conference", badge="BioRob", selected=True,
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
        links={"PDF": "https://sim2real.github.io/assets/papers/2022/sena.pdf"},
        bib_type="inproceedings", bib_venue=("booktitle", "3rd Workshop on Closing the Reality Gap in Sim2Real Transfer for Robotics"), bib_extra={},
    ),
    dict(
        key="rad2018boundary", year=2018, type="journal", badge="JSV",
        title="Boundary control of flexible satellite vibration in planar motion",
        authors=["H. K. Rad", "H. Salarieh", "A. Alasty", "R. Vatankhah"],
        venue="Journal of Sound and Vibration, vol. 432, pp. 549–568, 2018",
        links={"Publisher": "https://www.sciencedirect.com/science/article/abs/pii/S0022460X18304206"},
        bib_type="article", bib_venue=("journal", "Journal of Sound and Vibration"), bib_extra={"volume": "432", "pages": "549--568"},
    ),
    dict(
        key="rad2018antisymmetric", year=2018, type="journal", badge="Acta Astronaut.",
        title="Boundary control of anti-symmetric vibration of satellite with flexible appendages in planar motion with exponential stability",
        authors=["H. K. Rad", "H. Salarieh", "A. Alasty", "R. Vatankhah"],
        venue="Acta Astronautica, vol. 147, pp. 219–230, 2018",
        links={"Publisher": "https://www.sciencedirect.com/science/article/abs/pii/S0094576517318222"},
        bib_type="article", bib_venue=("journal", "Acta Astronautica"), bib_extra={"volume": "147", "pages": "219--230"},
    ),
    dict(
        key="kavianirad2018frictional", year=2018, type="journal", badge="Granular Matter",
        title="Frictional viscoelastic based model for spherical particles collision",
        authors=["H. Kaviani Rad", "H. Nejat Pishkenari"],
        venue="Granular Matter, vol. 20, pp. 1–10, 2018",
        links={"Publisher": "https://link.springer.com/article/10.1007/s10035-018-0835-9"},
        bib_type="article", bib_venue=("journal", "Granular Matter"), bib_extra={"volume": "20", "doi": "10.1007/s10035-018-0835-9"},
    ),
    dict(
        key="nejat2017transformation", year=2017, type="journal", badge="Granular Matter",
        title="Transformation of sliding motion to rolling during spheres collision",
        authors=["H. Nejat Pishkenari", "H. Kaviani Rad", "H. Jafari Shad"],
        venue="Granular Matter, vol. 19, pp. 1–13, 2017",
        links={"Publisher": "https://link.springer.com/article/10.1007/s10035-017-0755-0"},
        bib_type="article", bib_venue=("journal", "Granular Matter"), bib_extra={"volume": "19", "doi": "10.1007/s10035-017-0755-0"},
    ),
]

NEWS = [
    ("Jul 2026", 'Gave the ITR doctoral seminar talk <em>“Cooperative Shared Control of Hybrid FES-Exoskeleton”</em>. '
                 '<a href="https://www.ce.cit.tum.de/ics/news/article/the-next-doctoral-seminar-talk-will-take-place-next-monday-july-20th-and-will-be-given-by-hossein-kavianirad-the-title-of-the-talk-is-cooperative-shared-control-of-hybrid-fes-exoskeleton/">Announcement</a>'),
    ("2026", 'Journal paper on hybrid robot &amp; FES rehabilitation after stroke published in <em>JRATE</em>. '
             '<a href="https://doi.org/10.1177/20556683261488467">Paper</a>'),
    ("Nov 2025", 'New preprint: <em>Cooperative Control of Hybrid FES-Exoskeleton: Dynamic Allocation</em>. '
                 '<a href="https://arxiv.org/abs/2511.10117">arXiv</a>'),
    ("Mar 2025", 'Our EU project <strong>ReHyb</strong> on hybrid FES-exoskeleton stroke rehabilitation was featured in a TUM press release. '
                 '<a href="https://idw-online.de/de/news848815">Press release</a> · <a href="https://youtu.be/OboVMCkM9Yk">Video</a>'),
    ("2025", 'Paper on FES-assisted repetitive grasping after stroke published in <em>Artificial Organs</em>. '
             '<a href="https://doi.org/10.1111/aor.15033">Paper</a>'),
    ("2024", 'Two papers presented at <strong>IEEE BioRob 2024</strong>: a hybrid soft exoglove-FES study and sEMG-based hand intent recognition for FES.'),
    ("2023", 'Presented model-based shared control of a hybrid FES-exoskeleton at <strong>ICORR 2023</strong>.'),
    ("2022", 'Received the <strong>Best Paper Award</strong> at IEEE-EMBS IECBES 2022 for EMG-based volitional torque estimation in FES control.'),
]

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


def pub_html(p, prefix):
    links = "".join(f'<a href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in p["links"].items())
    bib_id = f"{prefix}-bib-{p['key']}"
    award = f'\n          <div class="pub-award"><i class="fa-solid fa-trophy"></i> {esc(p["award"])}</div>' if p.get("award") else ""
    return f"""      <li class="pub" data-type="{p['type']}">
        <div class="venue-badge {p['type']}" title="{TYPE_LABEL[p['type']]}">{esc(p['badge'])}</div>
        <div>
          <div class="pub-title">{esc(p['title'])}</div>
          <div class="pub-authors">{authors_html(p['authors'])}</div>
          <div class="pub-venue">{esc(p['venue'])}</div>{award}
          <div class="pub-links">{links}<button type="button" data-bib="{bib_id}">BibTeX</button></div>
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
        <a href="{DBLP}" aria-label="dblp"><i class="ai ai-dblp"></i></a>
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
   "sameAs":["{SCHOLAR}","{LINKEDIN}","{TUM}","{DBLP}","{GITHUB}"]}}
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
        <p>I am a PhD candidate at the <a href="https://www.ce.cit.tum.de/itr/">Chair of Information-oriented Control</a>, Technical University of Munich, supervised by <a href="https://www.ce.cit.tum.de/itr/hirche/">Prof. Sandra Hirche</a>. My research is on <strong>cooperative shared control of hybrid FES-exoskeletons</strong>: wearable systems that combine functional electrical stimulation of the user's own muscles with robotic actuation to restore arm and hand function after stroke and for activities of daily living.</p>
        <p>I work on <strong>EMG-based estimation of voluntary effort</strong> under stimulation, <strong>participant-specific neuromuscular modeling</strong>, and <strong>dynamic control allocation</strong> that shares assistance between FES and robot according to user participation, actuator limits, and rehabilitation goals. This work is part of the EU project <a href="https://idw-online.de/de/news848815">ReHyb</a> with clinical evaluation in stroke patients.</p>
        <p>My work on EMG-based torque estimation received the <strong>Best Paper Award at IEEE-EMBS IECBES 2022</strong>.</p>
        <p>Before TUM, I was a researcher at the Shiraz University Research Center working on dynamics, control, and system identification. I received my M.Sc. in Mechanical Engineering from Sharif University of Technology (ranked 2nd of 151) and my B.Sc. from Shiraz University (ranked 1st of 89), with work on boundary control of flexible structures and contact mechanics.</p>
        <div class="socials">
          <a href="mailto:{EMAIL}"><i class="fa-solid fa-envelope"></i>Email</a>
          <a href="{SCHOLAR}"><i class="ai ai-google-scholar"></i>Google Scholar</a>
          <a href="{LINKEDIN}"><i class="fa-brands fa-linkedin"></i>LinkedIn</a>
          <a href="{TUM}"><i class="fa-solid fa-building-columns"></i>TUM profile</a>
          <a href="{DBLP}"><i class="ai ai-dblp"></i>dblp</a>
          <a href="assets/Kavianirad_CV.pdf"><i class="fa-solid fa-file-pdf"></i>CV (PDF)</a>
        </div>
        <div class="callout"><i class="fa-solid fa-graduation-cap"></i>&nbsp; <strong>Students:</strong> I supervise Bachelor's and Master's theses in control, learning, dynamic modeling, and rehabilitation robotics. Feel free to email me with your CV and transcripts.</div>
      </div>
      <div class="hero-photo">
        <img src="assets/img/profile.jpg" alt="Portrait of Hossein Kavianirad" width="220" height="220">
        <div class="affil">Technical University of Munich<br>Munich, Germany</div>
      </div>
    </section>

    <section id="interests">
      <h2 class="section-title">Research interests</h2>
      <ul class="chips">
        <li>Shared &amp; cooperative control</li>
        <li>Hybrid FES-exoskeletons</li>
        <li>Functional electrical stimulation</li>
        <li>Rehabilitation robotics</li>
        <li>EMG &amp; biosignal processing</li>
        <li>Electrical impedance tomography</li>
        <li>Neuromuscular modeling</li>
        <li>System identification</li>
        <li>Dynamics &amp; nonlinear control</li>
      </ul>
    </section>

    <section id="news">
      <h2 class="section-title">News</h2>
      <ul class="news">
{news}
      </ul>
    </section>

    <section id="research">
      <h2 class="section-title">Research</h2>
      <div class="cards">
        <div class="card">
          <div class="card-icon"><i class="fa-solid fa-people-arrows"></i></div>
          <h3>Shared control of hybrid FES-exoskeletons</h3>
          <p>Model-based and cooperative controllers that combine muscle stimulation and robotic torque, with dynamic allocation that respects device limits, fatigue, and user preference.</p>
        </div>
        <div class="card">
          <div class="card-icon"><i class="fa-solid fa-wave-square"></i></div>
          <h3>EMG-based intent &amp; effort estimation</h3>
          <p>Estimating the user's volitional torque and hand intent from surface EMG despite stimulation artifacts, to keep the patient actively engaged in therapy.</p>
        </div>
        <div class="card">
          <div class="card-icon"><i class="fa-solid fa-hand"></i></div>
          <h3>Dexterous hand assistance</h3>
          <p>Wearable soft exogloves combined with FES for functional finger and wrist movements, evaluated with healthy participants and stroke patients.</p>
        </div>
        <div class="card">
          <div class="card-icon"><i class="fa-solid fa-satellite"></i></div>
          <h3>Dynamics &amp; control of flexible systems</h3>
          <p>Earlier work on boundary control of flexible satellite appendages with exponential stability, and contact models for granular particle collisions.</p>
        </div>
      </div>
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
      <p>Also on <a href="{SCHOLAR}">Google Scholar</a>, <a href="{DBLP}">dblp</a>, and the <a href="{TUM}">TUM ITR page</a>.</p>
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
    page = f"""{head("CV · Hossein Kavianirad", "Curriculum vitae of Hossein Kavianirad: education, research experience and skills.", "../", "/cv/")}
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
      <p class="bio">Hossein Kavianirad is a doctoral researcher at the Chair of Information-oriented Control (ITR), Technical University of Munich, advised by Prof. Sandra Hirche. His research develops cooperative shared control for hybrid FES-exoskeletons that combine functional electrical stimulation with robotic actuation to restore arm and hand function after stroke, within the EU Horizon project ReHyb. He holds an M.Sc. in Mechanical Engineering from Sharif University of Technology and a B.Sc. from Shiraz University. He received the IEEE-EMBS IECBES 2022 Best Paper Award.</p>
      <button type="button" class="copy-bio" id="copy-bio">Copy bio</button>
    </section>

    <section>
      <h2 class="section-title">Research experience</h2>
      <ul class="timeline">
        <li>
          <div class="when">04/2021 – present</div>
          <h3>Doctoral Researcher (PhD Candidate)</h3>
          <div class="where"><a href="https://www.ce.cit.tum.de/itr/">Chair of Information-oriented Control (ITR)</a>, Technical University of Munich, Germany</div>
          <p>Advisor: Prof. Sandra Hirche. Thesis topic: cooperative shared control of hybrid FES-exoskeletons. EMG-based volitional effort estimation, participant-specific neuromuscular modeling, dynamic control allocation between FES and robotic actuation, soft exoglove-FES hand assistance. Research assistant in the EU Horizon project ReHyb; design and experimental evaluation of human-centered control strategies in clinical settings; supervised more than 10 student projects.</p>
        </li>
        <li>
          <div class="when">2017 – 2021</div>
          <h3>Research Assistant, Control Engineer</h3>
          <div class="where">Shiraz University Research Center, Iran</div>
          <p>Practical control and system identification with actuator-, sensor/CPU- and human-in-the-loop testing; embedded sensing and actuation, INS, data fusion and Kalman filtering; C/C++, MATLAB and microcontroller programming.</p>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Education</h2>
      <ul class="timeline">
        <li>
          <div class="when">04/2021 – present</div>
          <h3>Ph.D. in Control</h3>
          <div class="where">Technical University of Munich, Germany</div>
          <p>Dissertation: <em>Cooperative Shared Control of Hybrid FES-Exoskeleton</em>. Advisor: Prof. Sandra Hirche.</p>
        </li>
        <li>
          <div class="when">2015 – 2017</div>
          <h3>M.Sc. in Mechanical Engineering</h3>
          <div class="where">Sharif University of Technology, Tehran, Iran</div>
          <p>GPA 19.27/20, ranked 2nd of 151. Thesis: <em>Boundary control of a flexible satellite (control design for hybrid PDE-ODE systems)</em>.</p>
        </li>
        <li>
          <div class="when">2011 – 2015</div>
          <h3>B.Sc. in Mechanical Engineering</h3>
          <div class="where">Shiraz University, Iran</div>
          <p>GPA 19.05/20, ranked 1st of 89. Thesis: <em>Energy harvesting in a piezoelastic beam excited by air flow</em>.</p>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Honors &amp; awards</h2>
      <ul class="timeline">
        <li><div class="when">2022</div><h3>Best Paper Award, IEEE-EMBS IECBES 2022</h3><div class="where">For “EMG-Based Volitional Torque Estimation in Functional Electrical Stimulation Control”</div></li>
        <li><div class="when">2015 – 2017</div><h3>Teaching assistantship funded by Iran's National Elites Foundation</h3></li>
        <li><div class="when">2015 – 2016</div><h3>Distinguished Student of Mechanical Engineering</h3><div class="where">Sharif University of Technology</div></li>
        <li><div class="when">2014 – 2015</div><h3>National Elites Foundation Fellowship &amp; Distinguished Student of Mechanical Engineering</h3><div class="where">Shiraz University</div></li>
        <li><div class="when">2011</div><h3>Top 0.3% of over 350,000 candidates</h3><div class="where">Iranian National University Entrance Exam</div></li>
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
        <li>
          <div class="when">2024</div>
          <h3>Toward Dexterous Hand Functional Movement: Wearable Hybrid Soft Exoglove-FES Study</h3>
          <div class="where">IEEE BioRob 2024</div>
        </li>
        <li>
          <div class="when">2023</div>
          <h3>Model-Based Shared Control of a Hybrid FES-Exoskeleton</h3>
          <div class="where">ICORR 2023</div>
        </li>
        <li>
          <div class="when">2022</div>
          <h3>EMG-Based Volitional Torque Estimation in FES Control</h3>
          <div class="where">IEEE-EMBS IECBES 2022</div>
        </li>
      </ul>
    </section>

    <section>
      <h2 class="section-title">Supervision</h2>
      <p>Supervised more than 10 Bachelor's and Master's theses and student research projects at ITR in control, learning, dynamic modeling, and rehabilitation robotics.</p>
    </section>

    <section>
      <h2 class="section-title">Skills</h2>
      <ul class="chips">
        <li>Nonlinear &amp; optimal control</li><li>Control allocation</li>
        <li>System identification</li><li>EMG signal processing</li><li>Functional electrical stimulation</li>
        <li>Exoskeletons &amp; soft wearables</li><li>Human-subject experiments</li>
        <li>Kalman filtering &amp; sensor fusion</li><li>Hardware-in-the-loop testing</li><li>MATLAB / Simulink</li><li>C / C++</li><li>Microcontroller programming</li>
      </ul>
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
