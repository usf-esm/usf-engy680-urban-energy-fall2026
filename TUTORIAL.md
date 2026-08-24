# ENGY 680 Tutorial: Setting Up Your Python + GitHub Environment

This tutorial covers the steps needed to get your computer
ready for Urban Energy and Climate problem sets: installing Python (via conda / Anaconda), installing
GitHub Desktop, cloning your personal course repo, running a Jupyter notebook,
and committing + pushing your work back to GitHub.

**Who this is for:** students with no prior command-line, Python, or Git
experience. Every step works on both **Mac** and **PC (Windows)** — where the
steps diverge, look for the 🍎 **Mac** / 🪟 **PC** labels.

**We will practice these steps in class together.** Before the first class, just pay attention to Step 0, though if you have time, you may want to get a headstart on installations to save WiFi bandwidth in class.

Note that these steps are primarily tested on a Mac. Behavior on Windows is somewhat dependent on software versions and thus unpredictable. If you encounter persistent problems, reach out to the instructor, TA, or other students to see if there may be a platform-specific challenge or error in these instructions.

## Attribution
Claude Sonnet 5 (with reasoning) was used to draft this tutorial from a description of the context, links to the README and homework instructions, and an outline of the 7 major steps: see [conversation](https://assistant.kagi.com/share/5464ab93-65b3-454a-bc61-db662c6a7d7f) via Kagi.

## Table of Contents
0. [Before you start](#0-before-you-start)
1. [Install conda (Miniconda)](#1-install-conda-miniconda)
2. [Install GitHub Desktop and sign in](#2-install-github-desktop-and-sign-in)
3. [Clone your private course repo](#3-clone-your-private-course-repo)
4. [Create and activate the conda environment](#4-create-and-activate-the-conda-environment)
5. [Launch Jupyter Lab](#5-launch-jupyter-lab)
6. [Run the demo/homework notebook](#6-run-the-demohomework-notebook)
7. [Commit and push your changes](#7-commit-and-push-your-changes)
8. _[Troubleshooting](#8-troubleshooting)_
<!--
9. [Screenshot checklist](#9-screenshot-checklist-for-instructors)
-->

---

## 0. Before you start

- You have a [github.com](https://github.com) account.
- You've emailed the instructor your GitHub username (or accepted the
      emailed repo invite), so your private repo `[YOUR_USERNAME]/engy680`
      exists and you have access.
- You have ~2 GB of free disk space (if installing Miniconda) or ~10 GB (if installing the full Anaconda with graphical Navigator) and a decent internet connection.

---

## 1. Install conda (Miniconda) or Anaconda

**Conda** is a tool for managing isolated Python installations ("environments")
so that every student in the class runs the *same* package versions,
regardless of what's already on your computer. **Miniconda** (a minimal
installer) is preferred to the full Anaconda Distribution to minimize disk space and the chance of conflicting environment dependencies (libraries explicitly or implicitly required by our notebooks invoked using "import" commands), since we'll build our
own environment from `environment.yml` anyway. **Miniconda is designed to run entirely from the command line (Terminal).**

The full **Anaconda** distribution works fine too if you already have it, and it is recommended on Windows.

### 🍎 Mac — Option A: Miniconda installation (recommended)

You can install via Terminal or graphically.

#### Option A1. Install Miniconda from Terminal using brew:
Open the **Terminal** app (Spotlight search or Applications window → "Terminal"), 
![Step 1: open terminal](screenshots/OpenTerminal.jpg)

then run:

```bash
brew install --cask miniconda
```
![Step 1: install conda](screenshots/BrewInstallConda.jpg)

If you don't have Homebrew yet, install it first from
[brew.sh](https://brew.sh), or install graphically.

#### Option A2. Graphical installation for Miniconda:

Go to [anaconda.com/download](https://www.anaconda.com/download) and download the **Miniconda** installer. Run the installer and follow the prompts (accept defaults unless you have a reason not to; on the "Install for" screen choose **Just Me**, not **All Users**).
![Step 1: Download Miniconda](screenshots/DownloadMiniconda.jpg)

### 🍎 Mac / 🪟 PC — Option B: Graphical Anaconda installer with Navigator application

Go to [anaconda.com/download](https://www.anaconda.com/download) and download the **Anaconda** installer. Run the installer and follow the prompts (accept defaults unless you have a reason not to; on the "Install for" screen choose **Just Me**, not **All Users**).

<!--
![Step 1: Miniconda installer welcome/license screen](screenshots/01a_miniconda_installer_welcome.jpg)
![Step 1: Miniconda installer install-for-me and location screen](screenshots/01b_miniconda_installer_options.jpg)
![Step 1: Miniconda installer finish screen](screenshots/01c_miniconda_installer_finish.jpg)
-->


### 🪟 PC note

On Windows, the installer adds an **Anaconda Prompt** to your Start Menu —
use this instead of the regular Command Prompt / PowerShell for all
`conda` or `jupyter` commands below or just use Navigator in this case
(unless you checked the box during install
to add conda to your system PATH).

### Verify the install

Open Terminal (Mac) or Anaconda Prompt (PC) and run:

```bash
conda --version
```

You should see something like `conda 24.x.x`. If you get "command not found,"
see [Troubleshooting](#8-troubleshooting).

![Step 1: Terminal showing successful `conda --version` output](screenshots/SuccessfulInstall.jpg)

---

## 2. Install GitHub Desktop and sign in

We'll use **GitHub Desktop** — a graphical app — instead of raw git commands,
so you never have to memorize `git` syntax, and to simplify logging into github (you [can no longer](https://github.blog/security/application-security/token-authentication-requirements-for-git-operations/) log in to access private repos from a terminal simply with a username and password; you have to use an ssh-key or OAuth procedure which GitHub Desktop takes care of for you).

1. Download it from [desktop.github.com](https://desktop.github.com). (You can alternatively install this via brew using the "github" cask.)
2. Install it:
   - 🍎 **Mac**: open the `.zip`, drag **GitHub Desktop** into Applications.
   - 🪟 **PC**: run the installer `.exe`; it installs and launches
     automatically.
3. Open GitHub Desktop and click **Sign in to GitHub.com**. This opens your
   browser to authorize the app — log in with your GitHub account and click
   **Authorize GitHub Desktop**, then return to the app.
4. If prompted, confirm your name/email for git commits (your GitHub account
   name/email is fine).

<!--
![Step 2: GitHub Desktop sign-in screen](screenshots/02a_github_desktop_signin.jpg)
![Step 2: Browser authorization prompt for GitHub Desktop](screenshots/02b_github_desktop_authorize.jpg)
![Step 2: GitHub Desktop configure git name/email screen](screenshots/02c_github_desktop_configure_git.jpg)

*(Reference if your UI looks different: GitHub's own docs on installing and
signing into GitHub Desktop.)*
-->
---

## 3. Clone your private course repo

Each student has a private repo named `[INSTRUCTOR_USERNAME]/engy680-[YOUR_USERNAME]`
(a copy of the shared course repo). 🛑 **DO NOT** try to do homework in the
shared/instructor repo — only your private copy. (The GitHub permissions should be configured to prevent this, but just in case they are not, this will keep your homework private.)

1. In GitHub Desktop, go to **File → Clone Repository...**
2. Click the **GitHub.com** tab and find `[INSTRUCTOR_USERNAME]/engy680-[YOUR_USERNAME]` in the
   list (or paste the URL under the **URL** tab if it doesn't show up).
3. Choose a **Local Path** — somewhere easy to find, e.g. `Documents/engy680`.
4. Click **Clone** and wait for it to finish.

![Step 3: File menu with Clone Repository highlighted](screenshots/FileMenuClone.jpg)
![Step 3: Clone Repository dialog, GitHub.com tab, repo selected](screenshots/CloneMenu.jpg)
![Step 3: Clone progress / completed clone view](screenshots/SuccessfulClone.jpg)

*If your repo isn't listed:* your invite may not be accepted yet — check your
email (including spam) for a GitHub invite, or confirm with the instructor
that your GitHub username was received.

---

## 4. Create and activate the conda environment

Your repo includes an `environment.yml` file that lists every Python package
the class needs (pandas, jupyterlab, matplotlib, etc.), so everyone has
identical versions.

### Option A: Command line (Mac or PC)

Open Terminal / Anaconda Prompt, navigate into your cloned repo, and create
the environment:

```bash
cd path/to/engy680
conda env create -f environment.yml -n engy680
```
![Step 4: installing env](screenshots/InstallingEnv.jpg)

This can take a few minutes ("solving environment..."). When it finishes,
activate it:

```bash
conda activate engy680
```

Your terminal prompt should now show `(engy680)` at the start of the line.

Verify:

```bash
conda env list
```

You should see `engy680` in the list with an asterisk `*` next to it if
active.

![Step 4: successful env](screenshots/SuccessfulEnv.jpg)

### Option B: Anaconda Navigator (graphical, no terminal)

1. Open **Anaconda Navigator**.
2. Click the **Environments** tab on the left.
3. Click **Import** at the bottom of the environments list.
4. Enter a name (e.g. `engy680`), browse to your repo's `environment.yml`
   under **Specification File**, and click **Import**.
5. Wait for the solver — this can take several minutes.

![Step 4: Navigator Environments tab with Import button highlighted](screenshots/NavImport.jpg)
![Step 4: Navigator Import dialog with name and .yml file selected](screenshots/NavImportDialog.jpg)

<!--
*(Reference: Anaconda's own Navigator docs on importing environments, if your
version's menu layout differs.)*
-->


---

## 5. Launch Jupyter Lab

With the `engy680` environment **active**, launch the notebook interface:

### Command line

```bash
conda activate engy680   # if not already active
jupyter-lab
```

A browser tab should open automatically showing the Jupyter Lab file
browser. (If not, copy the `http://localhost:8888/...` URL printed in the
terminal into your browser.)

![Step 5: Terminal launching jupyter-lab](screenshots/LaunchJupyter.jpg)
![Step 5: Jupyter Lab landing page in browser](screenshots/JupyterLanding.jpg)

### Anaconda Navigator

1. Go to the **Home** tab.
2. Make sure the environment dropdown at top reads **engy680**.
3. Click **Launch** under the **JupyterLab** tile.

   If the JupyterLab tile shows an **Install** button instead of **Launch**
   after you select the `engy680` environment, that usually means
   `jupyterlab` didn't make it into the environment during Step 4 (e.g., the
   import was interrupted). Click **Install** on the tile and wait for it to
   finish, or re-run the command-line install: `conda activate engy680 && conda install jupyterlab`.

   🤔 This step may have problems on some configurations. Since we are using only very standard packages with common usages, you may be able to successfully run the homework using the Base environment that comes with the Navigator package. This may be less somewhat likely to work in subsequent homeworks when we make a map visualization using geopandas.


![Step 5: Navigator Home tab, environment dropdown set to engy680](screenshots/NavSelectEnv.jpg)
![Step 5: Navigator JupyterLab launch tile](screenshots/NavJupyter.jpg)

---

## 6. Run the demo/homework notebook

1. In the Jupyter Lab file browser (left sidebar), navigate to the homework
   folder and double-click the notebook file (e.g. `simple_stock_rollover_HW1.ipynb`).
2. Run the existing demo cells top to bottom: **Run → Run All Cells** (or
   click each cell and press `Shift+Enter`).
3. Scroll to the bottom, and add new cells for your homework answers:
   - Click the `+` icon in the toolbar, or press `Esc` then `b` ("insert cell
     Below"), to add a new cell.
   - Change a cell to Markdown (dropdown in toolbar) if you want to write
     text explanations, or leave it as Code.
4. **Save** frequently: `Cmd/Ctrl + S`, or **File → Save Notebook**. Jupyter
   autosaves periodically, but always do a manual save before stepping away.
5. When done, **shut down** cleanly:
   - **File → Shut Down** (stops the whole Jupyter Lab server), or
   - Close the browser tab and go back to the terminal, press `Ctrl+C` twice
     to stop the server, or click **Stop** in Navigator.

![Step 6: Notebook open, Run All Cells highlighted in menu](screenshots/JupyterRunAll.jpg)
![Step 6: New cell added at bottom with homework code](screenshots/JupyterRunCell.jpg)
![Step 6: File → Shut Down menu option](screenshots/JupyterShutDown.jpg)

---

## 7. Commit and push your changes

Now save your work back to GitHub using GitHub Desktop.

1. Open **GitHub Desktop**. At the top-left, confirm the **current repository**
   dropdown shows `[YOUR_USERNAME]/engy680` — **not** the shared class repo.
2. Click the **Changes** tab (left side) to see every file you've modified.
   Click a file to see its diff (added/removed lines) on the right.
   
   🤓 In contrast to conventional code, (e.g., .py scripts or modules), this diff comparison is not as helpful for Jupyter notebooks which have been saved in a run state because it tracks
   verbose runtime changes to package versions, binary graphic outputs, etc. Ask about ways to clean this to allow more clean tracking when using notebooks.
3. **Check carefully**: only your notebook (`.ipynb`) and any code files
   should be checked/staged, along with any appendix chatbot session markdown files or other small addenda. **Uncheck** (or right-click → **Ignore file**,
   which adds it to `.gitignore`) any large data files, output CSVs, or
   generated images — these shouldn't go into version control.
4. Write a short **Summary** (e.g. "Drafting HW1 question 1", "Add HW1 question 1-2 code", "fixed error in question 2 calculation") in the box at
   bottom left, and optionally a longer **Description**.
5. Click **Commit to main**.
6. Click **Push origin** at the top to upload your commit(s) to GitHub.com.
7. (Optional but reassuring) Open your repo on github.com in a browser and
   confirm your latest commit appears in the history.

![Step 7: Repository dropdown showing correct repo selected](screenshots/GHDRepo.jpg)
![Step 7: Changes tab with file list and diff view](screenshots/GHDDiff.jpg)
![Step 7: Right-click context menu showing "Ignore file"](screenshots/GHDIgnore.jpg)
![Step 7: Commit message box and Commit to main button](screenshots/GHDCommit.jpg)
![Step 7: Push origin button after committing](screenshots/GHDPush.jpg)
![Step 7: GitHub.com commit history confirming the push](screenshots/GithubPostCommit.jpg)
![Step 7: GitHub.com commit diff comparison](screenshots/GitHubCommitWindow.jpg)

> 💡 **Reminder:** You don't need to save copies like `HW1_v2.ipynb` or
> `HW1_final.ipynb` — that's what git/version history is for. Just keep
> committing to the same file as you make progress.

---

## 8. Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `conda: command not found` | Restart your terminal after installing, or (Mac) run `conda init zsh` (or `bash`) then restart terminal. On PC, use the **Anaconda Prompt**, not regular Command Prompt. |
| `conda env create` is very slow / hangs on "Solving environment" | Normal — can take 5–15 minutes on first run. If it truly hangs (30+ min), try `conda install -n base conda-libmamba-solver` then re-run with `--solver=libmamba`. |
| GitHub Desktop can't find your repo when cloning | Confirm you accepted the email invite / your GitHub username was sent to the instructor. Try refreshing (sign out/in) in GitHub Desktop. |
| Jupyter opens but can't find installed packages (`ModuleNotFoundError`) | You likely launched Jupyter from the wrong environment. Confirm the terminal prompt shows `(engy680)`, or in Navigator confirm the environment dropdown is set correctly before clicking Launch. |
| GitHub Desktop won't let you push (file too large) | GitHub has a ~100 MB per-file hard limit. Un-stage the large file, delete it from tracking, add it to `.gitignore`, and re-commit. |
| Mac: "cannot be opened because the developer cannot be verified" | Right-click the app → **Open** (instead of double-click) the first time, then confirm. |

---

<!--
## 9. Screenshot checklist (for instructors)

| Filename | Step | Description |
|---|---|---|
| `01a_miniconda_installer_welcome.jpg` | 1 | Installer welcome/license screen |
| `01b_miniconda_installer_options.jpg` | 1 | Install-for-me / location screen |
| `01c_miniconda_installer_finish.jpg` | 1 | Installer finish screen |
| `01d_conda_version_terminal.jpg` | 1 | Terminal, `conda --version` output |
| `02a_github_desktop_signin.jpg` | 2 | GitHub Desktop sign-in screen |
| `02b_github_desktop_authorize.jpg` | 2 | Browser OAuth authorize prompt |
| `02c_github_desktop_configure_git.jpg` | 2 | Configure git name/email screen |
| `03a_clone_menu.jpg` | 3 | File → Clone Repository menu |
| `03b_clone_dialog.jpg` | 3 | Clone dialog, repo selected |
| `03c_clone_complete.jpg` | 3 | Clone finished view |
| `04a_conda_env_create.jpg` | 4 | Terminal mid-`conda env create` |
| `04b_conda_activate.jpg` | 4 | Terminal showing `(engy680)` prompt |
| `04c_navigator_import_button.jpg` | 4 | Navigator Import button |
| `04d_navigator_import_dialog.jpg` | 4 | Navigator Import dialog |
| `05a_jupyter_lab_launch_terminal.jpg` | 5 | Terminal launching jupyter-lab |
| `05b_jupyter_lab_landing_page.jpg` | 5 | Jupyter Lab landing page |
| `05c_navigator_env_dropdown.jpg` | 5 | Navigator environment dropdown |
| `05d_navigator_launch_jupyterlab.jpg` | 5 | Navigator JupyterLab launch tile |
| `06a_notebook_run_all.jpg` | 6 | Run All Cells menu |
| `06b_notebook_new_cell.jpg` | 6 | New cell added at bottom |
| `06c_notebook_shutdown.jpg` | 6 | File → Shut Down menu |
| `07a_repo_dropdown.jpg` | 7 | Repository dropdown, correct repo |
| `07b_changes_diff.jpg` | 7 | Changes tab, diff view |
| `07c_ignore_file_menu.jpg` | 7 | Right-click "Ignore file" |
| `07d_commit_box.jpg` | 7 | Commit message box + button |
| `07e_push_origin.jpg` | 7 | Push origin button |
| `07f_github_commit_history.jpg` | 7 | GitHub.com commit history |
```
-->

