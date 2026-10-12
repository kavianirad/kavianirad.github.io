# kavianirad.github.io

Personal academic website of Hossein Kavianirad, served at https://kavianirad.github.io/.

Plain static HTML/CSS/JS, no Jekyll build. Content (publications, news, CV) lives in `tools/build.py`.

To update: edit the data at the top of `tools/build.py`, then run

```sh
python3 tools/build.py
```

and commit the regenerated `index.html`, `publications/index.html` and `cv/index.html`.
