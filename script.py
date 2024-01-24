import subprocess
import webbrowser


def build_html():
    # Run 'make html' command
    make_html_command = "make html"
    subprocess.run(make_html_command, shell=True, check=True)


def open_in_brave():
    # Specify Brave browser executable path
    brave_command = "brave _build/html/index.html"
    subprocess.run(brave_command, shell=True, check=True)


if __name__ == "__main__":
    # Build HTML
    build_html()

    # Open in Brave
    open_in_brave()
