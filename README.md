# m5-101 Course Repo
[Course website](https://paulcccccch.github.io/m5-101/)

Built with [mkdocs](https://www.mkdocs.org/)

## File Structure
```
D:.
├─docs
│  └─content
│      ├─.ipynb_checkpoints
│      ├─code
│      └─images
└─m5-101
    ├─content
    │  ├─code
    │  ├─equation-solver
    │  ├─hello-world
    │  ├─images
    │  ├─introduction
    │  ├─python-basics-1
    │  ├─python-set-up
    │  └─schedule
    ├─css
    ├─fonts
    ├─img
    └─js
```

The `m5-101` is generated by running `mkdocs build` or `mkdocs serve`. You don't need to change anything in that folder.
You can place `.md` or `.ipynb` files in `docs/content`, and modify the related element in `schedule.md`. Whenever you are not sure what to do, please look at the code that is up and running for examples, or contact the owner of the repo directly.

## Dependencies
```
mkdocs==1.1.2
mkdocs-cinder==1.2.0
mkdocs-jupyter==0.13.0
python-markdown-math==0.8
nbconvert==5.5
```

## Installation
First make sure you have `python3` installed.  
Then, run 
```
pip install mkdocs mkdocs-cinder mkdocs-jupyter python-markdown-math

```

## Run the doc locally
```
mkdocs serve
```

## Deploy to GitHub Pages
```
mkdocs gh-deploy
```

